/* Ann Physiocare — site scripts (no dependencies) */
(function(){
  'use strict';
  // ---- CONFIG: set a form endpoint (Formspree, Getform, your PHP/Netlify handler) to submit forms by POST.
  // Left empty, forms open the visitor's email app (mailto) as a working fallback.
  var FORM_ENDPOINT = '';
  var FORM_TO = 'rehab@annphysiocare.com';

  var $ = function(s,c){return (c||document).querySelector(s)}, $$ = function(s,c){return Array.prototype.slice.call((c||document).querySelectorAll(s))};

  // year
  $$('[data-year]').forEach(function(e){e.textContent=new Date().getFullYear()});

  // mobile nav
  var mb=$('.menu-btn'), nav=$('nav.main');
  if(mb&&nav){
    mb.addEventListener('click',function(){var o=nav.classList.toggle('open');mb.setAttribute('aria-expanded',o)});
    $$('nav.main a').forEach(function(a){a.addEventListener('click',function(){ if(a.getAttribute('href')!=='#'){nav.classList.remove('open')} })});
  }

  // reveal on scroll
  if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.12});
    $$('.rv').forEach(function(e){io.observe(e)});
  } else {$$('.rv').forEach(function(e){e.classList.add('in')})}

  // counters
  function count(el){
    var end=parseFloat(el.dataset.count), suf=el.dataset.suffix||'', dur=1600, st=null, dec=(el.dataset.count.split('.')[1]||'').length;
    function step(t){st=st||t;var p=Math.min((t-st)/dur,1),v=end*(1-Math.pow(1-p,3));
      el.textContent=(dec?v.toFixed(dec):Math.round(v).toLocaleString('en-GB'))+suf; if(p<1)requestAnimationFrame(step)}
    requestAnimationFrame(step);
  }
  if('IntersectionObserver' in window){
    var co=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){count(e.target);co.unobserve(e.target)}})},{threshold:.5});
    $$('[data-count]').forEach(function(e){co.observe(e)});
  } else {$$('[data-count]').forEach(function(e){e.textContent=e.dataset.count+(e.dataset.suffix||'')})}

  // tabs
  $$('[data-tabs]').forEach(function(root){
    var tabs=$$('.tab',root), panels=$$('.panel',root);
    function go(id){tabs.forEach(function(t){t.classList.toggle('on',t.dataset.t===id);t.setAttribute('aria-selected',t.dataset.t===id)});
      panels.forEach(function(p){p.classList.toggle('on',p.id===id)})}
    tabs.forEach(function(t){t.addEventListener('click',function(){go(t.dataset.t)})});
  });

  // modal
  function openM(id){var m=document.getElementById(id);if(m){m.classList.add('open');document.body.style.overflow='hidden'}}
  function closeM(m){m.classList.remove('open');document.body.style.overflow=''}
  $$('[data-open]').forEach(function(b){b.addEventListener('click',function(){openM(b.dataset.open)})});
  $$('.modal').forEach(function(m){
    m.addEventListener('click',function(e){if(e.target===m||e.target.classList.contains('x'))closeM(m)});
    document.addEventListener('keydown',function(e){if(e.key==='Escape')closeM(m)});
  });

  // back to top
  var top=$('.fab .top');
  if(top){window.addEventListener('scroll',function(){top.classList.toggle('show',window.scrollY>600)},{passive:true});
    top.addEventListener('click',function(){window.scrollTo({top:0,behavior:'smooth'})})}

  // cookie consent
  var ck=$('#cookie'), KEY='apc-consent';
  function saveCk(v){try{localStorage.setItem(KEY,JSON.stringify(v))}catch(e){} ck.classList.remove('show');
    document.dispatchEvent(new CustomEvent('apc:consent',{detail:v}))}
  if(ck){
    var saved=null;try{saved=JSON.parse(localStorage.getItem(KEY))}catch(e){}
    if(!saved) setTimeout(function(){ck.classList.add('show')},1200); else document.dispatchEvent(new CustomEvent('apc:consent',{detail:saved}));
    $$('[data-ck]',ck).forEach(function(b){b.addEventListener('click',function(){
      var m=b.dataset.ck;
      if(m==='all')saveCk({necessary:1,preferences:1,statistics:1,marketing:1});
      else if(m==='deny')saveCk({necessary:1,preferences:0,statistics:0,marketing:0});
      else saveCk({necessary:1,preferences:+$('#ck-pref').checked,statistics:+$('#ck-stat').checked,marketing:+$('#ck-mkt').checked});
    })});
  }
  // TODO (hosting): load Google Analytics (G-EWQB7CDNMZ) only after consent.statistics === 1
  document.addEventListener('apc:consent',function(e){
    if(e.detail&&e.detail.statistics&&!window.__gaLoaded){window.__gaLoaded=1;
      var s=document.createElement('script');s.async=1;s.src='https://www.googletagmanager.com/gtag/js?id=G-EWQB7CDNMZ';document.head.appendChild(s);
      window.dataLayer=window.dataLayer||[];window.gtag=function(){dataLayer.push(arguments)};gtag('js',new Date());gtag('config','G-EWQB7CDNMZ');}
  });

  // forms
  $$('form[data-form]').forEach(function(f){
    var note=$('.note',f);
    function msg(t,err){if(!note)return;note.textContent=t;note.className='note'+(err?' err':'');note.style.display='block'}
    f.addEventListener('submit',function(e){
      e.preventDefault();
      if(!f.checkValidity()){f.reportValidity();return}
      var fd=new FormData(f), subject='Website enquiry: '+(f.dataset.form||'Contact');
      if(FORM_ENDPOINT){
        fetch(FORM_ENDPOINT,{method:'POST',body:fd,headers:{Accept:'application/json'}}).then(function(r){
          if(r.ok){f.reset();msg('Thank you — your message has been sent. We will be in touch shortly.')}else{msg('Sorry, something went wrong. Please call 0330 124 2392.',1)}
        }).catch(function(){msg('Sorry, something went wrong. Please call 0330 124 2392.',1)});
      } else {
        var body=[];fd.forEach(function(v,k){if(typeof v==='string'&&v)body.push(k+': '+v)});
        window.location.href='mailto:'+(f.dataset.to||FORM_TO)+'?subject='+encodeURIComponent(subject)+'&body='+encodeURIComponent(body.join('\n'));
        msg('Your email app should open with your details ready to send. If it does not, please email '+(f.dataset.to||FORM_TO)+' or call 0330 124 2392.');
      }
    });
  });

  // job accordions: open from hash
  if(location.hash){var d=document.querySelector(location.hash);if(d&&d.tagName==='DETAILS')d.open=true}

  // locations finder
  var grid=$('#locGrid');
  if(grid){
    fetch('/assets/locations.json').then(function(r){return r.json()}).then(function(L){
      var q=$('#locQ'), chips=$$('.chip[data-r]'), count=$('#locCount'), reg='All';
      function esc(s){return s.replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
      function render(){
        var t=(q.value||'').toLowerCase().trim();
        var r=L.filter(function(l){return (reg==='All'||l.region===reg)&&(!t||(l.name+' '+l.address).toLowerCase().indexOf(t)>-1)});
        count.textContent=r.length+' clinic'+(r.length===1?'':'s');
        grid.innerHTML=r.map(function(l){
          return '<article class="card lcard"><span class="rg">'+esc(l.region)+'</span><h3>'+esc(l.name)+'</h3><address>'+esc(l.address)+'</address>'+
          '<a class="btn btn-ghost-dark" style="padding:.6rem 1.1rem;font-size:.85rem" href="/physiotherapy/'+l.slug+'/">Clinic page</a> '+
          '<a class="btn btn-outline" style="padding:.6rem 1.1rem;font-size:.85rem" href="https://www.google.com/maps/search/?api=1&query='+encodeURIComponent('Ann Physiocare '+l.address)+'" target="_blank" rel="noopener">Directions</a> '+
          '<a class="btn btn-primary" style="padding:.6rem 1.1rem;font-size:.85rem" href="https://ann.jellypx.com/" target="_blank" rel="noopener">Book</a></article>';
        }).join('')||'<p>No clinics match your search. Please call 0330 124 2392 and we will help you find your nearest clinic.</p>';
      }
      q.addEventListener('input',render);
      chips.forEach(function(c){c.addEventListener('click',function(){chips.forEach(function(x){x.classList.remove('on')});c.classList.add('on');reg=c.dataset.r;render()})});
      render();
    });
  }

  // staff login (client-side placeholder; real auth must be server-side)
  var sl=$('#staffForm');
  if(sl){sl.addEventListener('submit',function(e){e.preventDefault();var n=$('.note',sl);n.textContent='Staff area access is handled by your administrator. Please contact '+FORM_TO+' if you need access.';n.className='note';n.style.display='block'})}
})();
