import os, html, urllib.parse
from layout import *
from locdata import LOCS
HERE = os.path.dirname(os.path.abspath(__file__))
E_ = lambda s: html.escape(s or "", quote=True)

DATA = {}
for line in open(os.path.join(HERE, "clinicdata.tsv"), encoding="utf-8"):
    if not line.strip(): continue
    p = line.rstrip("\n").split("§")
    p += [""] * (7 - len(p))
    slug, lm, pk, da, fl, ai, tr = p[:7]
    th = ""
    if "Therapist Details" in tr:
        tr, th = tr.split("Therapist Details", 1); th = th.lstrip(" :").strip()
    DATA[slug] = dict(lm=lm.strip(), pk=pk.strip(), da=da.strip(), fl=fl.strip(), ai=ai.strip(), tr=tr.strip(), th=th)

STD_LM = "The practice is located in a busy and popular location and has good public transportation facilities. Well-lit treatment room, Reception and Waiting area and Toilet."
STD_TR = "Manual therapy, Soft tissue mobilisation, Exercise Therapy, Electrotherapy etc"

def row(k, v, ic_):
    if not v: return ""
    return f"<li><i>{ic(ic_)}</i><div><b>{k}</b><span>{E_(v)}</span></div></li>"

def clinic_page(l):
    n, slug = l["name"], l["slug"]
    d = DATA[slug]
    url = f"/physiotherapy/{slug}/"
    q = urllib.parse.quote("Ann Physiocare " + l["address"])
    tr = d["tr"] or STD_TR
    lm = d["lm"] or STD_LM
    info = (row("Landmark and Location", lm, "pin") + row("Parking", d["pk"], "pin")
            + row("Disabled Access", d["da"], "heart") + row("Ground / First Floor", d["fl"], "bone")
            + row("Additional Information", d["ai"] if d["ai"] != "TBD" else "", "clip")
            + row("Available Treatment Options", tr, "check") + row("Therapist Details", d["th"], "users"))
    intro = (f"<h2>{E_(n)} Physiotherapy</h2><p>Ann Physiocare offers top-quality physiotherapy in {E_(n)}, with over 12 years of experience and a commitment to client satisfaction. "
      f"Our {E_(n)} physiotherapy clinic features highly qualified, HCPC-registered physiotherapists who provide personalised treatments tailored to your needs. We specialise in conditions like neck pain, back pain, sports injuries, hip rehabilitation and post-operative recovery. "
      f"Whether you need private physiotherapy in {E_(n)} or prefer a female physiotherapist near you, our team is here to help. We offer flexible options, including {E_(n)} physiotherapy self-referral, ensuring quick and accessible care.</p>"
      f"<h2>Private Physiotherapy {E_(n)}</h2><p>Equipped with advanced facilities, our clinic uses modern techniques such as electrotherapy, massage, soft tissue mobilisation, and customised exercise programmes. We focus on addressing root causes to prevent recurrence, with treatments for sports injuries, musculoskeletal issues, and neurological conditions. For those seeking private physiotherapy near them, we also provide home-based sessions for added convenience.</p>"
      f"<p>At Ann Physiocare we are dedicated to delivering trusted care with a holistic approach that considers your overall health and well-being. Start your personalised recovery journey today by visiting our {E_(n)} physiotherapy clinic or calling <a href='tel:{TEL}'>{PHONE}</a>.</p>")
    near = [x for x in LOCS if x["region"] == l["region"] and x["slug"] != slug][:6]
    nearby = "".join(f"<a class='chip' href='/physiotherapy/{x['slug']}/'>{E_(x['name'])}</a>" for x in near)
    body = f"""
<section class="section"><div class="wrap split" style="align-items:start">
 <div class="prose rv">{intro}
  <div class="btn-row"><a class="btn btn-primary" href="{BOOK}" target="_blank" rel="noopener">Book Online</a><a class="btn btn-outline" href="tel:{TEL}">Call {PHONE}</a><a class="btn btn-outline" href="https://www.google.com/maps/search/?api=1&amp;query={q}" target="_blank" rel="noopener">View On Map</a></div></div>
 <aside class="card rv" style="padding:1.8rem"><h3 style="margin-bottom:1rem">{E_(n)} Physiotherapy</h3>
  <ul class="cinfo-list"><li><i>{ic('pin')}</i><div><b>Address</b><span>{E_(l['address'])}, United Kingdom</span></div></li>
  <li><i>{ic('phone')}</i><div><b>Phone</b><span><a href="tel:{TEL}">{PHONE}</a></span></div></li>
  <li><i>{ic('mail')}</i><div><b>Email</b><span><a href="mailto:{EMAIL}">{EMAIL}</a></span></div></li></ul></aside></div></section>
<section class="section alt"><div class="wrap"><div class="sec-head rv"><span class="eyebrow">Clinic information</span><h2>Visiting our {E_(n)} clinic</h2></div>
 <ul class="cinfo-list big rv">{info}</ul>
 <div class="map-embed rv"><iframe title="Map of Ann Physiocare {E_(n)}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q={q}&amp;output=embed"></iframe></div></div></section>
<section class="section"><div class="wrap"><div class="sec-head center rv"><span class="eyebrow">Pricing</span><h2>Choose Our Best Pricing</h2></div>
 <div class="pcards"><div class="pc rv"><h3>Physiotherapy Initial Consultation</h3><div class="amt">£50</div><small>Face to Face Initial Consultation and Examination</small><br><br><a class="btn btn-outline" href="https://buy.stripe.com/28oeYigEp0GlgI8aIQ" target="_blank" rel="noopener">Buy now</a></div>
 <div class="pc pop rv d1"><span class="badge">Save £30</span><h3>Buy 3 sessions for £110</h3><div class="amt">£110</div><small>Get an off-the-shelf package of 3 sessions for £110 and save £30 instantly!</small><br><br><a class="btn btn-accent" href="https://buy.stripe.com/cN2g2mbk5cp3eA07wD" target="_blank" rel="noopener">Buy now</a></div>
 <div class="pc rv d2"><h3>Physiotherapy Treatment</h3><div class="amt">£45</div><small>Face to Face Follow-up Treatment Session</small><br><br><a class="btn btn-outline" href="https://buy.stripe.com/cN24jE9bX1Kp8bC7wF" target="_blank" rel="noopener">Buy now</a></div></div>
 <p class="center" style="margin-top:1.6rem"><a href="/pricing/">See all prices</a> · <a href="/faq/">Frequently asked questions</a></p></div></section>
<section class="section alt"><div class="wrap"><h3>Other clinics nearby ({E_(l['region'])})</h3><div class="loc-tools">{nearby}<a class="chip" href="/locations/">All 84 clinics →</a></div></div></section>
{funding()}{testimonials(3)}{questions_band()}"""
    mt = META[slug]
    return page(url, mt["t"], body, desc=mt["d"], extra_head=f'<meta name="keywords" content="{E_(mt["k"])}">',
        hero=(f"Physiotherapy {n}", l["address"]), crumbs=[("Locations", "/locations/"), (n, None)], active="/locations/")

META = {}
for _l in open(os.path.join(HERE, "meta.tsv"), encoding="utf-8"):
    if _l.strip():
        _p = _l.rstrip("\n").split("§")
        META[_p[0]] = dict(t=_p[1].strip(), d=_p[2].strip(), k=_p[3].strip())

def all_clinic_pages():
    return {f"/physiotherapy/{l['slug']}/": clinic_page(l) for l in LOCS}
