import html, json
SITE = "Ann Physiocare"
PHONE = "0330 124 2392"; TEL = "03301242392"
EMAIL = "rehab@annphysiocare.com"
BOOK = "https://ann.jellypx.com/"
CMPNO = "07958438"
ADDR = "Ann Physiocare Ltd, 37A, Clase Road, Morriston, Swansea, SA6 8DS"
TP = "https://uk.trustpilot.com/review/annphysiocare.com"
SOC = [("Facebook","https://www.facebook.com/AnnPhysiocareUK/","M14 8h3V4h-3c-2.8 0-5 2.2-5 5v2H6v4h3v8h4v-8h3l1-4h-4V9c0-.6.4-1 1-1z"),
       ("X / Twitter","https://twitter.com/ANN_Physiocare?s=03","M18.2 2H21l-6.5 7.4L22 22h-6l-4.7-6.2L5.9 22H3l7-8L2.5 2h6.1l4.2 5.6L18.2 2zm-1 18h1.7L7.9 3.8H6.1L17.2 20z"),
       ("LinkedIn","https://www.linkedin.com/company/ann-physiocare-limited/","M4.5 9h4v12h-4V9zM6.5 3a2.3 2.3 0 110 4.6 2.3 2.3 0 010-4.6zM10.5 9h3.8v1.7c.6-1 1.9-2 3.900-2 4 0 4.800 2.600 4.800 6V21h-4v-5.400c0-1.300 0-3-1.900-3s-2.100 1.400-2.100 2.900V21h-4V9z"),
       ("Instagram","https://www.instagram.com/ann.physiocare/","M7 2h10a5 5 0 015 5v10a5 5 0 01-5 5H7a5 5 0 01-5-5V7a5 5 0 015-5zm0 2a3 3 0 00-3 3v10a3 3 0 003 3h10a3 3 0 003-3V7a3 3 0 00-3-3H7zm5 3.500a4.500 4.500 0 110 9 4.500 4.500 0 010-9zm0 2a2.500 2.500 0 100 5 2.500 2.500 0 000-5zM17.500 5.500a1 1 0 110 2 1 1 0 010-2z")]
IC = {
 "phone":"<path d='M22 16.9v3a2 2 0 01-2.200 2 19.800 19.800 0 01-8.600-3.100 19.500 19.500 0 01-6-6A19.800 19.800 0 012.100 4.200 2 2 0 014.100 2h3a2 2 0 012 1.700c.1 1 .4 1.900.7 2.800a2 2 0 01-.5 2.100L8.100 9.900a16 16 0 006 6l1.300-1.300a2 2 0 012.100-.4c.9.300 1.800.6 2.800.7a2 2 0 011.700 2z'/>",
 "mail":"<rect x='2' y='4' width='20' height='16' rx='3'/><path d='M22 7l-10 6L2 7'/>",
 "pin":"<path d='M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 0116 0z'/><circle cx='12' cy='10' r='3'/>",
 "clock":"<circle cx='12' cy='12' r='10'/><path d='M12 6v6l4 2'/>",
 "bone":"<path d='M17 10c.7-.7 1.700-1 2.500-.7a2.500 2.500 0 10-3.300-3.300c.3.800 0 1.800-.7 2.500L9 15.500c-.7.700-1.700 1-2.500.7a2.500 2.500 0 103.300 3.300c-.3-.8 0-1.800.7-2.500z'/>",
 "brain":"<path d='M9.500 2A3.500 3.500 0 006 5.500v.3A3.500 3.500 0 004 9a3.500 3.500 0 001.500 2.900A3.500 3.500 0 006 17a3 3 0 003 3 3 3 0 003-3V5.500A3.500 3.500 0 009.500 2zM14.500 2A3.500 3.500 0 0118 5.500v.3A3.500 3.500 0 0120 9a3.500 3.500 0 01-1.500 2.900A3.500 3.500 0 0118 17a3 3 0 01-3 3 3 3 0 01-3-3'/>",
 "briefcase":"<rect x='2' y='7' width='20' height='14' rx='3'/><path d='M16 7V5a2 2 0 00-2-2h-4a2 2 0 00-2 2v2M2 13h20'/>",
 "video":"<rect x='2' y='5' width='14' height='14' rx='3'/><path d='M22 8l-6 4 6 4V8z'/>",
 "home":"<path d='M3 11l9-8 9 8M5 10v10h14V10M10 20v-6h4v6'/>",
 "clip":"<rect x='5' y='3' width='14' height='18' rx='2'/><path d='M9 3h6v3H9zM9 12h6M9 16h4'/>",
 "monitor":"<rect x='2' y='3' width='20' height='13' rx='2'/><path d='M8 21h8M12 16v5'/>",
 "needle":"<path d='M3 21l9-9M12 12l6-6 3 3-6 6zM15 3l6 6'/>",
 "bolt":"<path d='M13 2L4 14h7l-1 8 9-12h-7z'/>",
 "hand":"<path d='M18 11V6a2 2 0 00-4 0v4M14 10V4a2 2 0 00-4 0v6M10 10.500V6a2 2 0 00-4 0v8l-1.500-1.500a2 2 0 00-3 2.600L7 21h9a5 5 0 005-5v-5a2 2 0 00-3 0z'/>",
 "run":"<circle cx='13' cy='4' r='2'/><path d='M4 17l5-1 2-4 4 3v6M7 12l3-5 5 1 3 4'/>",
 "wave":"<path d='M2 12h3l2-7 4 14 3-10 2 3h6'/>",
 "check":"<path d='M5 12l5 5L20 7'/>",
 "shield":"<path d='M12 2l8 3v6c0 5-3.500 9-8 11-4.500-2-8-6-8-11V5z'/><path d='M9 12l2 2 4-4'/>",
 "heart":"<path d='M20.800 4.600a5.500 5.500 0 00-7.800 0L12 5.700l-1-1.100a5.500 5.500 0 00-7.800 7.800l1 1L12 21l7.800-7.600 1-1a5.500 5.500 0 000-7.800z'/>",
 "users":"<circle cx='9' cy='7' r='4'/><path d='M2 21v-2a5 5 0 015-5h4a5 5 0 015 5v2M16 3.100a4 4 0 010 7.800M22 21v-2a5 5 0 00-3.500-4.800'/>",
 "star":"<path d='M12 2l3.100 6.300 6.900 1-5 4.900 1.200 6.800L12 17.800 5.800 21l1.200-6.800-5-4.900 6.900-1z'/>",
 "file":"<path d='M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8zM14 2v6h6M8 13h8M8 17h5'/>",
 "arrow":"<path d='M5 12h14M13 5l7 7-7 7'/>",
 "up":"<path d='M12 19V5M5 12l7-7 7 7'/>",
 "search":"<circle cx='11' cy='11' r='7'/><path d='M21 21l-4.300-4.300'/>",
 "lock":"<rect x='4' y='11' width='16' height='10' rx='2'/><path d='M8 11V7a4 4 0 018 0v4'/>",
 "stetho":"<path d='M6 3v6a4 4 0 008 0V3M10 13v2a5 5 0 0010 0v-1'/><circle cx='20' cy='12' r='2'/>",
}
def ic(n, cls=""):
    return f"<svg viewBox='0 0 24 24' stroke-linecap='round' stroke-linejoin='round' aria-hidden='true' class='{cls}'>{IC[n]}</svg>"
def esc(s): return html.escape(s, quote=True)

NAV = [("Home","/",None),
 ("About Us","#",[("Who We Are","/about/"),("Privacy Policy","/privacy-policy/"),("Policies and Procedures","/policies-and-procedures/")]),
 ("Locations","/locations/",None),("Services","/services/",None),("Treatments","/treatments/",None),
 ("Pricing","/pricing/",None),("FAQ","/faq/",None)]

def nav_html(active):
    out=[]
    for label,href,sub in NAV:
        cls="l"+(" active" if (href==active or (sub and any(active==h for _,h in sub))) else "")
        if sub:
            items="".join(f"<a href='{h}'>{t}</a>" for t,h in sub)
            out.append(f"<li><a class='{cls}' href='#' aria-haspopup='true'>{label} ▾</a><div class='dd'>{items}</div></li>")
        else:
            out.append(f"<li><a class='{cls}' href='{href}'>{label}</a></li>")
    out.append(f"<li><a class='btn btn-accent' href='{BOOK}' target='_blank' rel='noopener'>Book Online</a></li>")
    return "<ul>"+"".join(out)+"</ul>"

WORDMARK = ("<span class='wordmark'><span class='mk'><svg viewBox='0 0 24 24'><circle cx='12' cy='5' r='2.500'/><path d='M12 8v6M6 11l6 2 6-2M9 21l3-7 3 7'/></svg></span>"
            "<span>Ann Physiocare<small>Physiotherapy</small></span></span>")
def brand(dark=False):
    if dark: return f"<a class='brand' href='/' aria-label='Ann Physiocare home'>{WORDMARK}</a>"
    return ("<a class='brand' href='/' aria-label='Ann Physiocare home'>"
            "<img src='/assets/img/logo.png' alt='Ann Physiocare logo' width='200' height='52' "
            "onerror=\"this.style.display='none';this.nextElementSibling.style.display='flex'\">"+WORDMARK+"</a>")

def head(title, desc, slug, extra=""):
    canon = "https://annphysiocare.com"+slug
    return f"""<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title><meta name="description" content="{esc(desc)}"><link rel="canonical" href="{canon}">
{"" if "name='robots'" in extra else '<meta name="robots" content="index, follow">'}<meta name="theme-color" content="#0A2540"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}"><meta property="og:type" content="website">
<link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,500;0,9..144,600;1,9..144,500&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/style.css">{extra}</head>"""

def topbar():
    soc="".join(f"<a href='{u}' target='_blank' rel='noopener' aria-label='{n}'><svg viewBox='0 0 24 24'><path d='{p}'/></svg></a>" for n,u,p in SOC)
    return f"""<div class="topbar"><div class="wrap"><div class="links"><a class="phone" href="tel:{TEL}">{ic('phone','')}<span>{PHONE}</span></a>
<a href="/careers/">Careers</a><a href="/referral-form/">Referral Form</a><a href="/staff-login/">Staff</a><a href="/contact/">Contact</a></div>
<div class="soc">{soc}</div></div></div>"""

def header(active):
    return f"""<header class="site"><div class="wrap">{brand()}<button class="menu-btn" aria-label="Menu" aria-expanded="false"><span></span><span></span><span></span></button>
<nav class="main" aria-label="Main">{nav_html(active)}</nav></div></header>"""

def footer():
    soc="".join(f"<a href='{u}' target='_blank' rel='noopener' aria-label='{n}'><svg viewBox='0 0 24 24'><path d='{p}'/></svg></a>" for n,u,p in SOC)
    return f"""<footer class="site"><div class="wrap"><div class="fgrid">
<div>{brand(True)}<p>Ann Physiocare provides a range of physiotherapy services for individuals, businesses, and insurers.</p>
<p><strong style="color:#fff">Registered in England and Wales.</strong><br>Company Registration Number: {CMPNO}</p><div class="soc" style="display:flex;gap:.6rem">{soc}</div></div>
<div><h4>Company</h4><ul><li><a href="/about/">Who We Are</a></li><li><a href="/locations/">Locations</a></li><li><a href="/careers/">Careers</a></li><li><a href="/referral-form/">Referral Form</a></li><li><a href="/in-work-support/">RCS In-Work Support</a></li><li><a href="/contact/">Contact</a></li></ul></div>
<div><h4>Services &amp; Care</h4><ul><li><a href="/services/">Services</a></li><li><a href="/treatments/">Treatments</a></li><li><a href="/pricing/">Pricing</a></li><li><a href="/faq/">FAQ</a></li><li><a href="/privacy-policy/">Privacy Policy</a></li><li><a href="/policies-and-procedures/">Policies and Procedures</a></li><li><a href="/terms-of-use/">Terms of Use</a></li></ul></div>
<div><h4>Contact Us</h4><ul><li>{ic('phone','')} <a href="tel:{TEL}">{PHONE}</a></li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li>{ADDR}</li><li><a href="{TP}" target="_blank" rel="noopener">★ Read our Trustpilot reviews</a></li></ul></div>
</div><div class="fbot"><span>Copyright © <span data-year>2026</span> Ann Physiocare Ltd. All rights reserved.</span><span><a href="/privacy-policy/">Privacy</a> · <a href="/terms-of-use/">Terms</a> · <a href="/staff-login/">Staff Login</a></span></div></div></footer>"""

def modal():
    return f"""<div class="modal" id="refModal" role="dialog" aria-modal="true" aria-labelledby="refT"><div class="mbox"><button class="x" aria-label="Close">×</button>
<span class="eyebrow">Referral options</span><div class="cols">
<div><h3 id="refT">Referred by GP?</h3><p>Please book via online or ring us to arrange the appointment.</p><div class="btn-row"><a class="btn btn-primary" href="{BOOK}" target="_blank" rel="noopener">Book Online</a><a class="btn btn-outline" href="tel:{TEL}">Call Admin team</a></div></div>
<div><h3>Looking for self referral?</h3><p>Self-referral is particularly suitable for individuals with relatively straightforward musculoskeletal issues like back pain, joint pain, or recent strains/sprains. If you have more complex needs, such as movement problems related to stroke or MS, you may still need a referral from your GP.</p>
<p>If you are based on the below mentioned areas use the self referral form.</p><div class="btn-row" style="margin-top:.4rem"><a class="btn btn-primary" href="https://physio-westberkshire.com/self-referral-form" target="_blank" rel="noopener">Berkshire</a><a class="btn btn-primary" href="https://physio-eastkent.com/self-referral-form" target="_blank" rel="noopener">Kent and Medway</a></div>
<p style="margin:1rem 0 0">If you have any query please call us on <a href="tel:{TEL}"><strong>{PHONE}</strong></a> so we can assist you promptly.</p></div></div></div></div>"""

def cookie():
    return """<div class="cookie" id="cookie" role="dialog" aria-label="Cookie consent"><h4>This website uses cookies</h4>
<p>We use cookies to personalise content and ads, to provide social media features and to analyse our traffic. We also share information about your use of our site with our social media, advertising and analytics partners who may combine it with other information that you've provided to them or that they've collected from your use of their services.</p>
<div class="sw"><label><input type="checkbox" checked disabled> Necessary</label><label><input type="checkbox" id="ck-pref"> Preferences</label><label><input type="checkbox" id="ck-stat"> Statistics</label><label><input type="checkbox" id="ck-mkt"> Marketing</label></div>
<div class="btn-row" style="margin:0"><button class="btn btn-primary" data-ck="all">Allow All</button><button class="btn btn-outline" data-ck="sel">Allow Selected</button><button class="btn btn-outline" data-ck="deny">Deny</button></div></div>"""

def fab():
    return f"<div class='fab'><button class='ref' data-open='refModal'>{ic('stetho','')} Referred by NHS? Book here</button><button class='top' aria-label='Back to top'>{ic('up','')}</button></div>"

def page(slug, title, body, desc="", active=None, hero=None, crumbs=None, extra_head="", scripts=""):
    """hero: (h1, lead) for inner pages; body already contains the sections."""
    h = head(title, desc or title, slug, extra_head)
    inner=""
    if hero:
        cr = "<div class='crumbs'><a href='/'>Home</a><span>/</span>" + "".join(
            (f"<a href='{u}'>{t}</a><span>/</span>" if u else f"<span>{t}</span>") for t,u in (crumbs or [])) + "</div>"
        lead = f"<p>{hero[1]}</p>" if len(hero)>1 and hero[1] else ""
        inner=f"<section class='page-hero'><div class='wrap'>{cr}<h1>{hero[0]}</h1>{lead}</div></section>"
    return (h+"<body>"+topbar()+header(active or slug)+"<main id='main'>"+inner+body+"</main>"+footer()+modal()+cookie()+fab()
            +"<script src='/assets/js/main.js'></script>"+scripts+"</body></html>")

# ---------- reusable blocks ----------
def funding():
    return f"""<section class="section"><div class="wrap"><div class="sec-head center rv"><span class="eyebrow">How you can pay</span><h2>Our Services For</h2></div>
<div class="fund">
<div class="card rv"><div class="ic">{ic('heart')}</div><h3>NHS</h3><p>We have a specialised body of knowledge and skills and can provide physiotherapy services across a range of settings, working either independently.</p></div>
<div class="card rv d1"><div class="ic">{ic('shield')}</div><h3>Insurance</h3><div class="logos"><span>BUPA</span><span>NUFFIELD HEALTH</span></div><p>Ann Physiocare is registered with all major Health Insurance providers, we always do our best to make your insurance process as smooth as possible.</p></div>
<div class="card rv d2"><div class="ic">{ic('users')}</div><h3>Pay As You Go Individuals</h3><p>We are able to assist individuals with a wide range of issues without the need for public or private funding.</p></div></div></div></section>"""

def request_band(book=BOOK):
    return f"""<section class="section" style="padding-top:0"><div class="wrap"><div class="cta rv"><div><h2>Request An Appointment</h2>
<p>Call Us On {PHONE} or Send us a direct message using the chat box in the bottom right hand corner of the screen and we will get back to you as quickly as possible!</p></div>
<div class="btn-row"><a class="btn btn-primary" href="/contact/">Request Appointment</a><a class="btn btn-ghost" href="{book}" target="_blank" rel="noopener">Book Online</a></div></div></div></section>"""

def questions_band():
    return f"""<section class="section" style="padding-top:0"><div class="wrap"><div class="cta rv"><div><h2>Still Have Questions?</h2>
<p>Call Us On {PHONE} or Send us a direct message using the chat box in the bottom right hand corner of the screen and we will get back to you as quickly as possible!</p></div>
<div class="btn-row"><a class="btn btn-primary" href="/faq/">FAQ</a><a class="btn btn-ghost" href="{BOOK}" target="_blank" rel="noopener">Book Online</a></div></div></div></section>"""

TESTI = [
 ("I was referred to Ann Physiocare for neck and shoulder pain. I had the pleasure to be treated by Shyam. I can honestly say that he's amazing and gave great exercises to do at home which really helped. I would highly recommend and definitely choose Shyam at Ann Physiocare.","Sharon McGoey"),
 ("I came here with a personal injury & through the help of the caring team over a number of productive sessions I feel free from pain.Not only is the service great but the care and attention is superb. Amazing.","Talha Mallick"),
 ("My physio is excellent, provided me with good set of exercises which helped me with my pain. Very good handson skills. Highly recommeded.","Hussain Sofiean"),
 ("Very good experience with Sam who was very helpful and advised further exercises which were good for my recovery","Mehmet Gul"),
 ("I recommend. Ann Phisiocare Physiotherapy for every one . Very good","NMK"),
 ("Lipi Halder gave the most professional and thorough Physio. I would recommend her to anyone. She is amazing.","nabela aslam"),
]
def testimonials(n=6, title="Clients Testimonials"):
    cards=""
    for i,(q,w) in enumerate(TESTI[:n]):
        ini="".join(x[0] for x in w.split()[:2]).upper()
        cards+=f"<div class='tcard rv d{i%3}'><div class='stars'>★★★★★</div><p>“{q}”</p><div class='who'><span class='av'>{ini}</span><div><b>{w}</b><small>Ann Physiocare client</small></div></div></div>"
    return f"""<section class="section alt"><div class="wrap"><div class="sec-head center rv"><span class="eyebrow">Loved by patients</span><h2>{title}</h2>
<p class="lead">See our <a href="{TP}" target="_blank" rel="noopener"><strong>6,488 reviews</strong> on Trustpilot</a></p></div><div class="tgrid">{cards}</div>
<div class="center"><a class="btn btn-outline" href="{TP}" target="_blank" rel="noopener">Review us on Trustpilot</a></div></div></section>"""

def locations_band():
    return f"""<section class="section"><div class="wrap"><div class="map-card rv"><div><span class="eyebrow">Find a clinic</span><h2>We have locations across England, Wales and Scotland</h2>
<p style="margin:1rem 0">With over 60 locations, we are able to treat hundreds of patients on a daily basis. Each of our clinics have:</p>
<ul class="checks"><li>Highly skilled Physiotherapists who are HCPC &amp; CSP registered and vastly experienced.</li><li>A unique, forward thinking attitude that embodies all Ann Physiocare clinics.</li><li>A holistic approach to treatment.</li></ul>
<div class="btn-row"><a class="btn btn-primary" href="/locations/">Find Location</a></div></div>
<div><div class="media" style="--img:url('/assets/img/uk-map.webp');min-height:340px"><div class="art">{ic('pin')}</div><div class="tag"><i></i>84 clinics &amp; counting</div></div></div></div></div></section>"""

def media(img, label="", icon="heart", minh=None):
    st=f"--img:url('/assets/img/{img}')"+(f";min-height:{minh}" if minh else "")
    tag=f"<div class='tag'><i></i>{label}</div>" if label else ""
    return f"<div class='media rv' style=\"{st}\" role='img' aria-label='{esc(label or img)}'><div class='art'>{ic(icon)}</div>{tag}</div>"

def related(items, cur):
    li="".join(f"<li><a href='{h}'{' class=cur' if h==cur else ''}>{t}<span>→</span></a></li>" for t,h in items)
    return f"""<aside class="side"><div class="box"><h4>Explore</h4><ul>{li}</ul></div>
<div class="box call"><h4>Speak to our team</h4><span class="num">{PHONE}</span><a class="btn btn-primary" href="{BOOK}" target="_blank" rel="noopener">Book Online</a></div></aside>"""
