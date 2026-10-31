import os, re, json, html, sys
sys.path.insert(0, os.path.dirname(__file__))
from layout import *
import detail
from pages import P as MAIN
from locdata import LOCS
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\"'>=])(https?://[^\s<)]+[^\s<).,;])", r'<a href="\1" target="_blank" rel="noopener">\1</a>', s)
    s = re.sub(r"(rehab@annphysiocare\.com)", r'<a href="mailto:\1">\1</a>', s)
    return s

def md(text):
    out = []; lis = []
    def flush():
        nonlocal lis
        if lis: out.append("<ul>" + "".join(f"<li>{x}</li>" for x in lis) + "</ul>"); lis = []
    blocks = re.split(r"\n\s*\n", text.strip())
    for b in blocks:
        lines = [l.strip() for l in b.split("\n") if l.strip()]
        if not lines: continue
        first = lines[0]
        m = re.match(r"^(#{4,6})\s*(.+)$", first)
        if m:
            flush(); lvl = "h3" 
            out.append(f"<{lvl}>{inline(m.group(2).replace('**',''))}</{lvl}>")
            rest = lines[1:]
            if rest: out.append("<p>" + "<br>".join(inline(x) for x in rest) + "</p>")
            continue
        if all(re.match(r"^1\.", l) for l in lines if not l.startswith("in each case")) and len(lines) > 1 or first.startswith("1."):
            # numbered sub-items rendered as list
            for l in lines:
                if l.startswith("1."): lis.append(inline(l[2:].strip()))
                else:
                    if lis: lis[-1] += " " + inline(l)
                    else: out.append(f"<p>{inline(l)}</p>")
            flush(); continue
        flush()
        # paragraphs with embedded sub-items (e.g. "5.We may collect:" followed by 1.xx)
        buf = []
        for l in lines:
            if l.startswith("1."): lis.append(inline(l[2:].strip()))
            elif lis and not re.match(r"^\d+\.", l) and not l.startswith("**"):
                lis[-1] += " " + inline(l)
            else:
                if lis: pass
                buf.append(inline(l))
        if buf: out.append("<p>" + "<br>".join(buf) + "</p>")
        flush()
    return "\n".join(out)

def wrap(body, extra=""):
    return f"<section class='section'><div class='wrap'><article class='prose legal' style='max-width:900px;margin:auto'>{body}{extra}</article></div></section>"

pages = dict(MAIN); pages.update(detail.P)
from clinics import all_clinic_pages
pages.update(all_clinic_pages())

priv = open(os.path.join(ROOT, "_src/privacy.md"), encoding="utf-8").read()
pages["/privacy-policy/"] = page("/privacy-policy/", "Ann Physiocare | Privacy Policy", wrap(md(priv)),
    desc="Ann Physiocare Limited privacy policy.", hero=("Privacy Policy", None), crumbs=[("Privacy Policy", None)], active="/privacy-policy/")

terms = open(os.path.join(ROOT, "_src/terms.md"), encoding="utf-8").read()
terms_html = md(terms).replace("<h3>CONTACT INFORMATION", "<h3>CONTACT INFORMATION")
pages["/terms-of-use/"] = page("/terms-of-use/", "Ann Physiocare | Terms Of Use", wrap(terms_html),
    desc="Terms of use for www.annphysiocare.com.", hero=("Terms of Use", None), crumbs=[("Terms of Use", None)], active="/terms-of-use/")

POL = [("Consent and Chaperoning", "/upload/APC_Chaperone_Policy_Reviewed-August_2025.pdf"),
       ("Dealing with Complaints", "/upload/APC_Incident_Reporting_and_Complaints_Policy_-_Reviewed_-_August_2025.pdf"),
       ("GDPR Privacy Notice", "/upload/APC_Data_Protection_Policy_-_Reviewed_-_August_2025.pdf"),
       ("Patient Safety Incident Response Framework", "/upload/APC%20PSIRF%20final%20version.pdf")]
pol_body = ("<section class='section'><div class='wrap' style='max-width:980px'><div class='sec-head center'><span class='eyebrow'>Policies</span><h2>Policy Links</h2></div><div class='grid g2'>"
    + "".join(f"<a class='card' href='{u}' target='_blank' rel='noopener'><div class='ic'>{ic('clip')}</div><h3>{t}</h3><span class='more'>View PDF</span></a>" for t, u in POL)
    + "</div><div class='prose' style='margin-top:3rem'><h3>Monitoring Performance</h3><p>In addition to the policies above, we have several performance-monitoring systems to ensure that we continue to provide the highest level of service:</p>"
    "<p><strong>Patient Satisfaction</strong> An anonymous survey is carried out of patients every year. Results are analysed and published. Any changes are resourced and undertaken wherever appropriate. Click Patient Satisfaction Survey to see the results of the most recent survey.</p>"
    "<p><strong>Audit</strong> Therapists’ notes are audited yearly in accordance with CSP professional standards. Management systems are audited yearly in accordance with CSP service standards.</p></div></div></section>" + locations_band() + funding() + testimonials(3))
pages["/policies-and-procedures/"] = page("/policies-and-procedures/", "Policies and Procedures | Ann Physiocare", pol_body,
    desc="Ann Physiocare policies and procedures.", hero=("Policies and Procedures", None), crumbs=[("Policies and Procedures", None)], active="/policies-and-procedures/")

pages["/404.html"] = page("/404.html", "Page not found | Ann Physiocare",
    "<section class='section'><div class='wrap center'><h2>Page not found</h2><p class='lead'>The page you’re looking for has moved. Try one of the links in the menu or call "+PHONE+".</p><a class='btn btn-primary' href='/'>Back to home</a></div></section>",
    hero=("404", "Page not found"))

# write
urls = []
for slug, h in pages.items():
    if slug == "/": path = os.path.join(ROOT, "index.html")
    elif slug.endswith(".html"): path = os.path.join(ROOT, slug.lstrip("/"))
    else:
        path = os.path.join(ROOT, slug.strip("/"), "index.html")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w", encoding="utf-8").write(h)
    if not slug.endswith(".html") and slug != "/staff-login/": urls.append(slug)
json.dump(LOCS, open(os.path.join(ROOT, "assets/locations.json"), "w", encoding="utf-8"), ensure_ascii=False)
base = "https://www.annphysiocare.com"
open(os.path.join(ROOT, "sitemap.xml"), "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"<url><loc>{base}{u}</loc></url>\n" for u in urls) + "</urlset>\n")
open(os.path.join(ROOT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nDisallow: /staff-login/\nSitemap: {base}/sitemap.xml\n")
open(os.path.join(ROOT, "assets/img/favicon.svg"), "w").write("<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'><rect width='64' height='64' rx='16' fill='#0B93D6'/><path d='M32 48s-14-8.6-14-19a8 8 0 0 1 14-5 8 8 0 0 1 14 5c0 10.4-14 19-14 19z' fill='#fff'/><path d='M20 31h8l3-6 5 11 3-5h5' stroke='#C94B4B' stroke-width='3' fill='none' stroke-linecap='round' stroke-linejoin='round'/></svg>")
print(len(pages), "pages;", len(LOCS), "locations")

