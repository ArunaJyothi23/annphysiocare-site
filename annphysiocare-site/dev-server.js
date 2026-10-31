const http = require('http');
const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const PORT = parseInt(process.env.PORT, 10) || 3000;
const ROOT = __dirname;
const SRC_DIR = path.join(ROOT, '_src');

const MIME_TYPES = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'application/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.webp': 'image/webp',
  '.gif': 'image/gif',
  '.svg': 'image/svg+xml',
  '.ico': 'image/x-icon',
  '.pdf': 'application/pdf',
  '.mp4': 'video/mp4',
  '.xml': 'application/xml; charset=utf-8',
  '.txt': 'text/plain; charset=utf-8',
  '.woff': 'font/woff',
  '.woff2': 'font/woff2',
  '.ttf': 'font/ttf',
};

// Live reload clients (Server-Sent Events)
const sseClients = new Set();

function broadcastReload() {
  for (const client of sseClients) {
    try {
      client.write('data: reload\n\n');
    } catch {
      sseClients.delete(client);
    }
  }
}

const LIVE_RELOAD_SCRIPT = `
<script>
(() => {
  let es = new EventSource('/__livereload');
  es.onmessage = (e) => {
    if (e.data === 'reload') {
      console.log('[LiveReload] Change detected, reloading page...');
      window.location.reload();
    }
  };
  es.onerror = () => {
    es.close();
    setTimeout(() => {
      new EventSource('/__livereload');
    }, 2000);
  };
})();
</script>
`;

let changeTimeout = null;
function handleFileChange(filename) {
  if (!filename) return;
  // Ignore temporary files, pycache, git, package files
  if (
    filename.includes('__pycache__') ||
    filename.endsWith('.pyc') ||
    filename.startsWith('.git') ||
    filename === 'dev-server.js' ||
    filename.endsWith('package-lock.json')
  ) {
    return;
  }

  if (changeTimeout) clearTimeout(changeTimeout);
  changeTimeout = setTimeout(() => {
    const isSrcChange = filename.startsWith('_src') || filename.includes(path.sep + '_src');
    if (isSrcChange) {
      console.log(`\n[Build] Change in _src (${filename}), rebuilding static pages...`);
      try {
        const out = execSync('python _src/build.py', { cwd: ROOT, encoding: 'utf-8' });
        console.log(`[Build] ${out.trim()}`);
      } catch (err) {
        console.error('[Build Error]', err.message);
      }
    } else {
      console.log(`\n[LiveReload] File changed: ${filename}`);
    }
    broadcastReload();
  }, 120);
}

// Watch directory for changes
try {
  fs.watch(ROOT, { recursive: true }, (eventType, filename) => {
    handleFileChange(filename);
  });
} catch (e) {
  console.warn('Recursive watch not supported, watching root and _src separately.');
  fs.watch(ROOT, (eventType, filename) => handleFileChange(filename));
  if (fs.existsSync(SRC_DIR)) {
    fs.watch(SRC_DIR, (eventType, filename) => handleFileChange(path.join('_src', filename)));
  }
}

const server = http.createServer((req, res) => {
  // SSE live reload endpoint
  if (req.url === '/__livereload') {
    res.writeHead(200, {
      'Content-Type': 'text/event-stream',
      'Cache-Control': 'no-cache, no-transform',
      'Connection': 'keep-alive',
      'Access-Control-Allow-Origin': '*'
    });
    res.write('\n');
    sseClients.add(res);
    req.on('close', () => sseClients.delete(res));
    return;
  }

  // Parse URL pathname
  let reqPath = '/';
  try {
    reqPath = decodeURI(new URL(req.url, `http://${req.headers.host || 'localhost'}`).pathname);
  } catch {
    res.writeHead(400, { 'Content-Type': 'text/plain' });
    return res.end('Bad Request');
  }

  // Prevent path traversal
  const safePath = path.normalize(path.join(ROOT, reqPath));
  if (!safePath.startsWith(ROOT)) {
    res.writeHead(403, { 'Content-Type': 'text/plain' });
    return res.end('403 Forbidden');
  }

  let filePath = safePath;

  // Resolve directory or clean URLs
  try {
    if (fs.existsSync(filePath)) {
      const stat = fs.statSync(filePath);
      if (stat.isDirectory()) {
        if (!reqPath.endsWith('/')) {
          res.writeHead(301, { Location: reqPath + '/' });
          return res.end();
        }
        filePath = path.join(filePath, 'index.html');
      }
    } else if (fs.existsSync(filePath + '.html')) {
      filePath = filePath + '.html';
    } else if (fs.existsSync(path.join(filePath, 'index.html'))) {
      res.writeHead(301, { Location: reqPath + '/' });
      return res.end();
    }
  } catch {
    // Continue to check existence below
  }

  // 404 handler
  if (!fs.existsSync(filePath) || fs.statSync(filePath).isDirectory()) {
    const notFoundPath = path.join(ROOT, '404.html');
    if (fs.existsSync(notFoundPath)) {
      res.writeHead(404, { 'Content-Type': 'text/html; charset=utf-8' });
      return res.end(fs.readFileSync(notFoundPath));
    }
    res.writeHead(404, { 'Content-Type': 'text/plain' });
    return res.end('404 Not Found');
  }

  const ext = path.extname(filePath).toLowerCase();
  const contentType = MIME_TYPES[ext] || 'application/octet-stream';

  if (ext === '.html') {
    let content = fs.readFileSync(filePath, 'utf-8');
    if (content.includes('</body>')) {
      content = content.replace('</body>', `${LIVE_RELOAD_SCRIPT}\n</body>`);
    } else {
      content += LIVE_RELOAD_SCRIPT;
    }
    res.writeHead(200, {
      'Content-Type': contentType,
      'Cache-Control': 'no-store, no-cache, must-revalidate',
    });
    return res.end(content);
  }

  // Static assets
  res.writeHead(200, {
    'Content-Type': contentType,
    'Cache-Control': 'no-cache'
  });
  const stream = fs.createReadStream(filePath);
  stream.on('error', () => {
    if (!res.headersSent) {
      res.writeHead(500, { 'Content-Type': 'text/plain' });
      res.end('Internal Server Error');
    }
  });
  stream.pipe(res);
});

server.listen(PORT, () => {
  console.log(`===============================================`);
  console.log(`  Ann Physiocare Dev Server`);
  console.log(`  Local URL:   http://localhost:${PORT}`);
  console.log(`  Live Reload: Active`);
  console.log(`  Auto Rebuild: Active (watching _src/)`);
  console.log(`===============================================`);
});

