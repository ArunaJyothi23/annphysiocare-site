from layout import *
from detail import SERVICES_NAV, TREAT_NAV, checks, pills, ul
from locdata import LOCS

P = {}

# ====================== HOME ======================
svc_cards = [
 ("bone","Musculoskeletal Physiotherapy","/musculoskeletal-physiotherapy/","Musculoskeletal physiotherapy is the treatment of disease or injury relating the muscles, bones, tendons, ligaments and nerves. Treatment involves reducing pain, increasing movement and restoring function, to get you back to your daily or sporting activities as quick as possible."),
 ("brain","Neurological Physiotherapy","/neurological-physiotherapy/","Neurological physiotherapy is the treatment of injury or disease relating to the central nervous system, which involves the brain, spinal cord and nerves. Examples of neurological disorders include stroke, Parkinson’s disease and MS (multiple sclerosis)."),
 ("briefcase","Occupational Health Physiotherapy","/occupational-health-physiotherapy/","When working at a computer, or carrying out any kind of manual labour, there is always a way to do it that is the least physically damaging. Our physiotherapists can show you how to work smarter and prevent work related headache or injury. Repeated stress injuries “Our philosophy is that RSI is primarily a structural problem that can be completely treated, even in advanced stages.”"),
 ("video","Online Physiotherapy","/online-physiotherapy/","We are expert online physiotherapy consultants for the diagnosis, treatment and rehabilitation of back pain, knee pain, sports injury, post-op rehab & women's health."),
 ("home","Home physiotherapy","/home-physiotherapy/","Our Physiotherapists can visit you at your home and you will receive exactly the same high quality treatment that you would have if you were to come into the clinic!"),
]
home_tabs = [
 ("t-acu","Acupuncture","needle","/acupuncture/","treat-acupuncture.webp",
  ["Acupuncture is very effective for reducing pain and inflammation, and is an excellent way to ease discomfort. Acupuncture treatment involves using very fine needles in specific points on the body. This gentle needling triggers signals in the nervous system, causing increases in the brain’s production of natural painkillers called endorphins. These substances are morphine-like chemicals that influence the body’s perception of pain.",
   "The combination of modalities can accelerate a return to normal movement. In addition Acupuncture is a holistic treatment method and may improve mood, energy and sleep patterns. The benefits of Acupuncture for stress, insomnia, smoking cessation and reduction of pain are suitable for men or women."]),
 ("t-ele","Electrotherapy","bolt","/electrotherapy/","treat-electro.webp",
  ["Electrotherapy or electro-physical agents are uses in the musculoskeletal clinics to deal with an underlying pathology and to change the patient’s perception of their pain and other disabling symptoms.",
   "Our experienced Physiotherapists at Annphysicoare use different types of electrotherapy including Interferential, Ultrasound, TENS Pilates, Massage, Pain Management, Orthotics."]),
 ("t-mas","Massage","hand","/massage-physiotherapy/","treat-massage.webp",
  ["We offer individualized massages that are customized to fit your specific needs. Our experienced professional massage therapist may use one or more of the following massage techniques based on your personal needs and preferences: Deep tissue massage to loosen knots, release chronic muscle tension, reduce inflammation, and help eliminate scar tissue.",
   "Sports-specific massage for athletes of every discipline and level, to promote flexibility, reduce fatigue, improve endurance, maximize performance, and prevent injuries. Therapeutic massage sessions offer many benefits."]),
 ("t-exe","Exercise Programme","run","/exercise-programme-physiotherapy/","treat-exercise.webp",
  ["Exercise is essential to recovery from sports injuries, following surgery, after an acute trauma, in the management of acute and chronic low back pain, neck pain and headaches and in the treatment of arthritis and osteoporosis.",
   "Exercise prescription forms an integral part of most physiotherapy rehabilitation programmes. Exercise is essential to recovery from sports injuries, following surgery, after an acute trauma such as from a fall or fracture, in the management of acute and chronic low back pain, neck pain and headaches and in the treatment of long term conditions such as arthritis and osteoporosis."]),
]
def tabs_block(items, wrap_title=None):
    t="".join(f"<button class='tab{' on' if i==0 else ''}' data-t='{id}' role='tab'>{name}</button>" for i,(id,name,*_) in enumerate(items))
    pn=""
    for i,(id,name,icon,href,img,paras) in enumerate(items):
        ps="".join(f"<p>{p}</p>" for p in paras)
        pn+=(f"<div class='panel split{' on' if i==0 else ''}' id='{id}' role='tabpanel'><div><span class='eyebrow'>{name}</span><h3 style='font-size:1.9rem;margin-bottom:1rem'>{name}</h3>{ps}"
             f"<div class='btn-row'><a class='btn btn-primary' href='{href}'>Read More</a></div></div>"
             f"<div class='media' style=\"--img:url('/assets/img/{img}')\" role='img' aria-label='{name}'><div class='art'>{ic(icon)}</div></div></div>")
    return f"<div data-tabs><div class='tabs' role='tablist'>{t}</div>{pn}</div>"

HOME = f"""
<section class="hero">
 <video autoplay muted loop playsinline preload="metadata" poster="/assets/img/hero-poster.webp" aria-hidden="true"><source src="/assets/video/hero.mp4" type="video/mp4"></video>
 <div class="wrap"><div>
  <span class="eyebrow">Trusted Physiotherapy Provider</span>
  <h1>Physiotherapy <em>near you</em>, built around your recovery.</h1>
  <p class="lead">Ann Physiocare provides a range of physiotherapy services for individuals, businesses and insurers. Our emphasis is to provide our clients with the skills and motivation to self-manage their problems and to rapidly become independent from therapy.</p>
  <div class="btn-row"><a class="btn btn-accent" href="/locations/">Find a Local Clinic {ic('arrow')}</a><a class="btn btn-ghost" href="/services/">Services</a><a class="btn btn-ghost" href="{BOOK}" target="_blank" rel="noopener">Book Online</a></div>
  <div class="trust"><span>{ic('check')} HCPC &amp; CSP registered</span><span>{ic('check')} 60+ clinics</span><span>{ic('check')} NHS, insurance &amp; self-pay</span></div>
 </div>
 <div class="hero-card rv"><h3>How would you like to be seen?</h3><p>Choose the route that suits you — we’ll take it from here.</p>
  <a class="opt" href="{BOOK}" target="_blank" rel="noopener"><i>{ic('clip')}</i><div><b>Referred by GP?</b><span>Book online or ring us to arrange the appointment</span></div></a>
  <a class="opt" href="#" data-open="refModal" onclick="return false"><i>{ic('users')}</i><div><b>Looking for self referral?</b><span>Berkshire · Kent and Medway self-referral forms</span></div></a>
  <a class="opt" href="/in-work-support/"><i>{ic('briefcase')}</i><div><b>RCS In-Work Support</b><span>Swansea, Llanelli, Carmarthenshire</span></div></a>
  <a class="opt" href="tel:{TEL}"><i>{ic('phone')}</i><div><b>Call {PHONE}</b><span>Mon–Fri 8am–6pm · Sat 8am–4pm</span></div></a>
 </div></div>
</section>

<section class="stats"><div class="wrap"><div class="grid">
 <div class="stat"><b data-count="12" data-suffix="+">12+</b><span>Years Experience</span></div>
 <div class="stat"><b data-count="6000" data-suffix="+">6,000+</b><span>Patients Treated Monthly</span></div>
 <div class="stat"><b data-count="60" data-suffix="+">60+</b><span>Clinics</span></div>
 <div class="stat"><b>ISO 9001</b><span>Certified Quality</span></div></div></div></section>

<div class="marquee" aria-hidden="true"><div class="mq">
 {''.join(f"<span>{ic('check')} {t}</span>" for t in ["Musculoskeletal","Neurological","Occupational Health","Online Physiotherapy","Home Visits","Acupuncture","Shockwave Therapy","Electrotherapy","Massage","DSE Assessments","Functional Capacity Evaluation","Exercise Programmes"]*2)}
</div></div>

{funding()}

<section class="section alt"><div class="wrap split">
 {media('about-clinic.webp','Expert, friendly clinicians','users',minh='460px')}
 <div class="rv"><span class="eyebrow">About us</span><h2>Know About Ann Physiocare</h2>
 <p style="margin-top:1rem">Ann Physiocare provides a range of physiotherapy services for individuals, businesses and insurers. Our emphasis is to provide our clients with the skills and motivation to self-manage their problems and to rapidly become independent from therapy.</p>
 <p>We follow a holistic approach to assessment, comprehensive treatment, functional rehabilitation and advice and education on injury prevention. Get the best physiotherapy near you in multiple locations.</p>
 <p>Our Physiotherapy clinics have a highly skilled and experienced team of physiotherapists with a proven record of success in the prevention and treatment of musculo-skeletal injuries. As the leading physiotherapy clinics in UK, we strongly believe that working together as a multi-disciplinary team in co-operation with our clients produces sustainable results for our long-term goals of minimizing injury and the associated costs as well as enhancing well-being. All our physio clinics are committed to a quality approach of continuous improvement.</p>
 <div class="btn-row"><a class="btn btn-primary" href="/about/">More About Us</a></div></div></div></section>

<section class="section"><div class="wrap"><div class="sec-head center rv"><span class="eyebrow">What we do</span><h2>Services That We Offer</h2></div>
<div class="grid g3">
{''.join(f"<a class='card rv d{i%3}' href='{h}'><div class='ic'>{ic(i_)}</div><h3>{t}</h3><p>{d}</p><span class='more'>Read More</span></a>" for i,(i_,t,h,d) in enumerate(svc_cards))}
<a class="card rv d2" href="/services/" style="background:var(--grad-dark);color:#cfe3ea"><div class="ic" style="background:rgba(255,255,255,.15)">{ic('arrow')}</div><h3 style="color:#fff">Discover All Services</h3><p style="color:#cfe3ea">Including Functional Capacity Evaluation and DSE Assessments for employers.</p><span class="more" style="color:#fff">Discover All Services</span></a>
</div></div></section>

<section class="section alt"><div class="wrap"><div class="sec-head rv"><span class="eyebrow">Treatments</span><h2>What Treatments We Provide</h2>
<p class="lead">Our highly skilled and experienced physiotherapists have helped many reach their full potential through Exercise, Acupuncture, Electrotherapy and Massage.</p></div>
{tabs_block(home_tabs)}
<div class="btn-row"><a class="btn btn-outline" href="/treatments/">All treatments</a></div></div></section>

<section class="section" style="padding-bottom:0"><div class="wrap"><a class="card rv" href="/in-work-support/" style="display:grid;grid-template-columns:auto 1fr auto;gap:1.6rem;align-items:center;background:linear-gradient(120deg,#fff,#eaf6fd)"><div class="ic" style="margin:0">{ic('briefcase')}</div><div><h3 style="margin-bottom:.3rem">RCS In-Work Support</h3><p style="margin:0">Supporting you to manage musculoskeletal conditions, stay well at work and return to work safely — Swansea, Llanelli, Carmarthenshire.</p></div><span class="btn btn-primary">Find out more</span></a></div></section>

{locations_band()}
{testimonials(3)}
{questions_band()}
"""
P["/"] = page("/","Physiotherapy Near You | Ann Physiocare",HOME,desc="Ann Physiocare provides physiotherapy services for individuals, businesses and insurers across England, Wales and Scotland. HCPC & CSP registered physiotherapists.",active="/")

# ====================== ABOUT ======================
ABOUT=f"""
<section class="section"><div class="wrap split">
<div class="rv"><span class="eyebrow">Our story</span><h2>Know About Ann Physiocare</h2><blockquote style="margin:1.4rem 0;border-left:4px solid var(--accent);padding-left:1.2rem;font-family:var(--font-d);font-size:1.6rem;color:var(--navy)">“Great things never came from comfort zones”</blockquote>
<p>APC established - 2012 when Mani and friends decided to open a small, community-oriented physiotherapy clinic in his backyard. Now we’re a well-established service running clinics across England and Wales with over 85+ branches, centralized administration, with great prices, friendly service and lots of different treatment options.</p>
<p>Hundreds of patients have been treated in our clinics across the UK. We are proud members of the community that we serve. We are a community of Physiotherapist’s; Administrator’s and we’d like you to come and experience the service's we have. Whether you’re a private patient or referred through the NHS, we’re here to help and we’re different. Just like you.</p>
<div class="btn-row"><a class="btn btn-primary" href="/services/">Our Services</a><a class="btn btn-outline" href="/locations/">Find Location</a></div></div>
{media('about-story.webp','Established 2012','heart',minh='480px')}</div></section>

<section class="stats" style="margin-top:0"><div class="wrap"><div class="grid">
 <div class="stat"><b data-count="12" data-suffix="+">12+</b><span>Years Experience</span></div>
 <div class="stat"><b data-count="6000" data-suffix="+">6,000+</b><span>Patients Treated Monthly</span></div>
 <div class="stat"><b data-count="85" data-suffix="+">85+</b><span>Branches</span></div>
 <div class="stat"><b>ISO 9001</b><span>Certified Quality</span></div></div></div></section>

<section class="section"><div class="wrap"><div class="map-card rv"><div><span class="eyebrow">Find a clinic</span><h2>We have locations across the south of England and Wales</h2>
<p style="margin:1rem 0">With over 85+ locations, we are able to treat hundreds of patients on a daily basis. Each of our clinics have:</p>
<ul class="checks"><li>Highly skilled Physiotherapists who are HCPC &amp; CSP registered and vastly experienced.</li><li>A unique, forward thinking attitude that embodies all Ann Physiocare clinics.</li><li>A holistic approach to treatment.</li></ul>
<div class="btn-row"><a class="btn btn-primary" href="/locations/">Find Location</a></div></div>
<div><div class="media" style="--img:url('/assets/img/uk-map.webp');min-height:320px"><div class="art">{ic('pin')}</div></div></div></div></div></section>

<section class="section alt"><div class="wrap"><div class="sec-head center rv"><span class="eyebrow">Why us</span><h2>Some Reasons To Choose Us</h2></div>
<div class="grid g4">
<div class="card rv"><div class="ic">{ic('users')}</div><h3>Welcoming staff</h3><p>Welcoming and approachable staff.</p></div>
<div class="card rv d1"><div class="ic">{ic('clock')}</div><h3>Convenient times</h3><p>Convenient appointment times, most of clinics are open from 8am till 7pm, Monday to Saturday</p></div>
<div class="card rv d2"><div class="ic">{ic('pin')}</div><h3>Convenient locations</h3><p>Professional and friendly Physiotherapists with years of experience. Convenient Locations, most of our clinics are located close to local transport services and amenities.</p></div>
<div class="card rv d3"><div class="ic">{ic('heart')}</div><h3>Tailored treatment</h3><p>Treatment is tailored to the patient’s ailments; we try to resolve the cause and not just the pain.</p></div></div></div></section>
{funding()}
{testimonials(3)}
"""
P["/about/"]=page("/about/","About | Ann Physiocare",ABOUT,desc="Ann Physiocare was established in 2012 and now runs clinics across England and Wales.",hero=("About","Know About Ann Physiocare"),crumbs=[("About",None)],active="/about/")

# ====================== SERVICES ======================
more_svc=[("clip","Functional Capacity Evaluation","/functional-capacity-evaluation/","A Functional Capacity Evaluation (FCE) is a type of physical ability assessment that is used to evaluate an individual's ability to perform specific work-related tasks."),
 ("monitor","DSE Assessments","/dse-assessments/","The assessment involves a trained assessor who evaluates the workstation, including the desk, chair, monitor, keyboard, and mouse, to ensure that they are set up correctly to promote good posture and reduce the risk of musculoskeletal disorders.")]
svc_all = list(svc_cards)
svc_all[2]=("briefcase","Occupational Health Physiotherapy","/occupational-health-physiotherapy/","When working at a computer, or carrying out any kind of manual labour, there is always a way to do it without incurring futher physical injury. Our physiotherapists can show you how to work smarter and prevent work related headache or injury. “Our philosophy is that Repeated Strain Injury (RSI) is primarily a structural problem that can be completely treated, even in advanced stages.”")
svc_all[4]=("home","Home Physiotherapy","/home-physiotherapy/","Our Physiotherapists can visit you in your own home and you will receive exactly the same high quality treatment that you would have if you were to come into the clinic!")
svc_all += more_svc
SERV=f"""<section class="section"><div class="wrap"><div class="sec-head center rv"><span class="eyebrow">Services</span><h2>Our Services To Choose Us</h2>
<p class="lead">Experienced private physiotherapists providing physiotherapy services. We have 60+ Clinics locations across the south of England and Wales</p></div>
<div class="sec-head center rv"><h3 style="font-size:1.6rem">Services That We Offer</h3></div>
<div class="grid g3">{''.join(f"<a class='card rv d{i%3}' href='{h}'><div class='ic'>{ic(i_)}</div><h3>{t}</h3><p>{d}</p><span class='more'>Read More</span></a>" for i,(i_,t,h,d) in enumerate(svc_all))}
<a class="card rv" href="/in-work-support/"><div class="ic">{ic('briefcase')}</div><h3>RCS In-Work Support</h3><p>Physiotherapy support for eligible people accessing the RCS In-Work Support Service in Swansea, Llanelli and Carmarthenshire.</p><span class="more">Read More</span></a></div></div></section>
<section class="section alt"><div class="wrap"><div class="map-card rv"><div><span class="eyebrow">Nationwide</span><h2>We have locations nationwide across England and Wales</h2>
<p style="margin:1rem 0">With over 60+ locations, we treat 6,000 patients on a monthly basis. Each of our clinics have:</p>
<ul class="checks"><li>Highly skilled Physiotherapists who are HCPC &amp; CSP registered and post qualification experience.</li><li>A unique, forward thinking attitude that embodies all AnnPhysiocare clinics.</li><li>A holistic approach to treatment.</li></ul><div class="btn-row"><a class="btn btn-primary" href="/locations/">Find Location</a></div></div>
<div><div class="media" style="--img:url('/assets/img/uk-map.webp');min-height:320px"><div class="art">{ic('pin')}</div></div></div></div></div></section>
{funding()}{questions_band()}"""
P["/services/"]=page("/services/","Physiotherapy Services | Ann Physiocare",SERV,desc="Musculoskeletal, neurological, occupational health, online and home physiotherapy, plus FCE and DSE assessments.",hero=("Services","Experienced private physiotherapists providing physiotherapy services."),crumbs=[("Services",None)],active="/services/")

# ====================== TREATMENTS ======================
treat_items = home_tabs + [("t-sho","Shockwave Therapy","wave","/shockwave-therapy/","treat-shockwave.webp",
  ["Shockwave therapy device enables effective treatment of chronic pain associated with chronic inflammation and degeneration of tendons, joint capsules, ligaments, muscles and bones. It is also a great support in the therapy of trigger points, i.e. particularly sensitive places characterised by increased tension, which can generate radiating pain. The positive effects allow to stop taking painkillers, and often avoid having to undergo surgery.","<em>Please note Shockwave are available only in some locations.</em>"])]
treat_items[0]=("t-acu","Acupuncture","needle","/acupuncture/","treat-acupuncture.webp",
  ["<em>Please note Acupuncture are available only in some locations.</em>","Acupuncture is very effective for reducing pain and inflammation, and is an excellent way to ease discomfort. Acupuncture treatment involves using very fine needles in specific points on the body. This gentle needling triggers signals in the nervous system, causing increases in the brain’s production of natural painkillers called endorphins. These substances are morphine-like chemicals that influence the body’s perception of pain.",
   "The combination of modalities can accelerate a return to normal movement. In addition Acupuncture is a holistic treatment method and may improve mood, energy and sleep patterns. The benefits of Acupuncture is known to reduce pain for suitable for men and women."])
treat_items[1]=("t-ele","Electrotherapy","bolt","/electrotherapy/","treat-electro.webp",
  ["Electrotherapy or electro-physical agents are uses in the musculoskeletal clinics to deal with an underlying pathology and to change the patient’s perception of their pain and other disabling symptoms.","Our experienced Physiotherapists at Annphysicoare use different types of electrotherapy including Interferential, Ultrasound, TENS, Massage, Pain Management, Orthopaedic."])
more_t=[("hand","Soft Tissue Mobilisation","/soft-tissue-mobilisation-physiotherapy/","Hands-on techniques to break down adhesions and improve muscle function."),("bone","Manipulation and Mobilisation","/manipulation-and-mobilization-physiotherapy/","Manual interventions to alleviate joint stiffness and pain.")]
TREAT=f"""<section class="section"><div class="wrap"><div class="sec-head rv"><span class="eyebrow">Treatments</span><h2>What Treatments We Provide</h2>
<p class="lead">We are experts in diagnosis and pain management. Over 12+ years in physiotherapy industry. Find simple solutions to your injury and pain troubles.</p></div>
{tabs_block(treat_items)}
<h3 style="margin:3.5rem 0 1.4rem">More treatments</h3><div class="grid g2">{''.join(f"<a class='card' href='{h}'><div class='ic'>{ic(i_)}</div><h3>{t}</h3><p>{d}</p><span class='more'>Read More</span></a>" for i_,t,h,d in more_t)}</div></div></section>
{locations_band()}{funding()}{questions_band()}"""
P["/treatments/"]=page("/treatments/","Treatments | Ann Physiocare",TREAT,desc="Acupuncture, electrotherapy, massage, exercise programmes, shockwave therapy, soft tissue mobilisation and manipulation.",hero=("Treatments","What Treatments We Provide"),crumbs=[("Treatments",None)],active="/treatments/")

# ====================== LOCATIONS ======================
regs=["All","London","South East & East","South West","Wales","Midlands","North West","Scotland"]
LOC=f"""<section class="section"><div class="wrap"><div class="center rv" style="margin-bottom:2.4rem"><p class="lead">See our <a href="{TP}" target="_blank" rel="noopener"><strong>6,488 reviews</strong></a> on <strong>Trustpilot</strong></p>
<div class="btn-row" style="justify-content:center"><a class="btn btn-outline" href="{TP}" target="_blank" rel="noopener">★ Review us on Trustpilot</a></div></div>
<div class="loc-tools"><input id="locQ" type="search" placeholder="Search by town, postcode or clinic name…" aria-label="Search clinics"></div>
<div class="loc-tools" style="align-items:center">{''.join(f"<button class='chip{' on' if r=='All' else ''}' data-r='{r}'>{r}</button>" for r in regs)}<strong id="locCount" style="margin-left:auto;color:var(--muted)"></strong></div>
<div class="grid g3" id="locGrid"><p>Loading clinics…</p></div>
<noscript><ul>{''.join(f"<li><strong>{l['name']}</strong> — {l['address']}</li>" for l in LOCS)}</ul></noscript>
<div class="cta rv" style="margin-top:3rem"><div><h2>Can’t see your nearest clinic?</h2><p>Call our admin team on {PHONE} and we’ll help you find the right clinic, or book an online or home visit appointment.</p></div><div class="btn-row"><a class="btn btn-primary" href="tel:{TEL}">Call {PHONE}</a><a class="btn btn-ghost" href="{BOOK}" target="_blank" rel="noopener">Book Online</a></div></div>
</div></section>
<section class="section alt"><div class="wrap"><div class="grid g3"><div class="card"><div class="ic">{ic('phone')}</div><h3>Phone No</h3><p><a href="tel:{TEL}">{PHONE}</a></p></div><div class="card"><div class="ic">{ic('mail')}</div><h3>Email Address</h3><p><a href="mailto:{EMAIL}">{EMAIL}</a></p></div><div class="card"><div class="ic">{ic('pin')}</div><h3>Location</h3><p>{ADDR}</p></div></div></div></section>"""
P["/locations/"]=page("/locations/","Physiotherapy Locations | Ann Physiocare",LOC,desc="Find your nearest Ann Physiocare physiotherapy clinic.",hero=("Physiotherapy Locations","Over 60 clinics across England, Wales and Scotland."),crumbs=[("Locations",None)],active="/locations/")

# ====================== PRICING ======================
def tbl(title, rows):
    return f"<div class='tbl-wrap rv'><h4>{title}</h4><table>"+"".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a,b in rows)+"</table></div>"
PRICE=f"""<section class="section"><div class="wrap"><div class="sec-head center rv"><span class="eyebrow">Pricing</span><h2>Choose Our Best Pricing</h2>
<p class="lead">Clear and transparent pricing. Our best value treatment ... Our best value, most effective physiotherapy treatment programme.</p></div>
<div class="pcards">
<div class="pc rv"><h3>Physiotherapy Initial Consultation</h3><div class="amt">£50</div><small>Face to Face Initial Consultation and Examination</small><br><br><a class="btn btn-outline" href="https://buy.stripe.com/28oeYigEp0GlgI8aIQ" target="_blank" rel="noopener">Buy now</a></div>
<div class="pc pop rv d1"><span class="badge">Save £30</span><h3>Buy 3 sessions for £110</h3><div class="amt">£110</div><small>Get an off-the-shelf package of 3 sessions for £110 and save £30 instantly!</small><br><br><a class="btn btn-accent" href="https://buy.stripe.com/cN2g2mbk5cp3eA07wD" target="_blank" rel="noopener">Buy now</a></div>
<div class="pc rv d2"><h3>Physiotherapy Treatment</h3><div class="amt">£45</div><small>Face to Face Follow-up Treatment Session</small><br><br><a class="btn btn-outline" href="https://buy.stripe.com/cN24jE9bX1Kp8bC7wF" target="_blank" rel="noopener">Buy now</a></div></div></div></section>
<section class="section alt"><div class="wrap split" style="align-items:start"><div class="rv"><h2>Services</h2><p class="lead" style="margin:.8rem 0 1rem">Everything included in your physiotherapy programme.</p>
{checks(["Pain Management","Musculoskeletal &amp; Neurological Conditions","Acupuncture","Electrotherapy","Shockwave Therapy","Mobilisation &amp; Manipulation","Work &amp; Sports Injuries","Taping, Splinting &amp; Bracing","Fitness &amp; DSE Assessments","Weight Training","Spinal Problems","Peripheral Injuries","Premium admin support"])}</div>
<div><h2 style="margin-bottom:1.4rem" class="rv">Prices</h2>
{tbl("Physiotherapy &amp; Acupuncture",[("Face to Face Initial Consultation and Examination","£50"),("Face to Face Follow-up Treatment Session","£45"),("Online/Telephysio (video) Initial Consutation and Examination","£35"),("Online/Telephysio (video) Follow-up Treatment Session","£30")])}
{tbl("Home Visits",[("Initial Assessment and Treatment <small>[60 mins appointment]</small>","£130"),("Follow-up Treatment Session","£85")])}
{tbl("Additional Services",[("Postural Assessment","£45"),("Ergonomic Assessment &amp; Advice","£125"),("Remote DSE Workstation Assessment","£120"),("Face-to-Face DSE Workstation Assessment","£150")])}
{tbl("Shockwave Therapy",[("Initial Assessment","£85"),("Follow-up Treatment Session","£65")])}</div></div></section>
{funding()}{questions_band()}"""
P["/pricing/"]=page("/pricing/","Pricing | Ann Physiocare",PRICE,desc="Clear and transparent physiotherapy pricing from Ann Physiocare.",hero=("Pricing","Choose Our Best Pricing"),crumbs=[("Pricing",None)],active="/pricing/")

# ====================== FAQ ======================
def q(title, body, open_=False): return f"<details class='rv'{' open' if open_ else ''}><summary>{title}</summary><div class='dbody'>{body}</div></details>"
FAQ_TABLES = (tbl("Physiotherapy &amp; Acupuncture",[("Face to Face Initial Consultation and Examination","£50"),("Face to Face Follow-up Treatment Session","£45"),("Online/Telephysio (video) Initial Consutation and Examination","£35"),("Online/Telephysio (video) Follow-up Treatment Session","£30")])
 +"<p><strong>Get an off-the-shelf package of 3 sessions for £110 and save £30 instantly!</strong></p>"
 +f"<div class='btn-row' style='margin:0 0 1.4rem'><a class='btn btn-outline' href='https://buy.stripe.com/28oeYigEp0GlgI8aIQ' target='_blank' rel='noopener'>Physiotherapy Initial Consultation £50 — Buy now</a><a class='btn btn-outline' href='https://buy.stripe.com/cN24jE9bX1Kp8bC7wF' target='_blank' rel='noopener'>Physitherapy Treatment £45 — Buy now</a><a class='btn btn-primary' href='https://buy.stripe.com/cN24jE9bX1Kp8bC7wF' target='_blank' rel='noopener'>Buy 3 sessions for £110 (Save £30) — Buy now</a></div>"
 +tbl("Home Visits",[("Initial Assessment and Treatment <small>[60 mins appointment]</small>","£130"),("Follow-up Treatment Session","£85")])
 +tbl("Additional Services",[("Postural Assessment","£45"),("Ergonomic Assessment &amp; Advice","£125"),("Remote DSE Workstation Assessment","£120"),("Face-to-Face DSE Workstation Assessment","£150")])
 +tbl("Shockwave Therapy",[("Initial Assessment","£85"),("Follow-up Treatment Session","£65")]))
FAQ=f"""<section class="section"><div class="wrap" style="max-width:920px"><div class="sec-head center rv"><span class="eyebrow">FAQ</span><h2>Frequently Asked Questions</h2></div>
{q("How to manage appointments online?",f'''<p><strong>Demo video of Portal:</strong><br><a class="btn btn-outline" href="https://www.youtube.com/watch?v=9fI_8qiRYKw" target="_blank" rel="noopener">▶ Click here for demo video</a></p>
<p><strong>Online Appointment Guide:</strong><br>Please see instructions below to manage appointments, view exercises, sign consent forms, upload client documents (MRI, CTs, reports, etc)<br>Please do not contact the centre for any appointment related queries as they do not have your details. Please manage online or callus on {PHONE}.</p>
<p><strong>To login to the portal:</strong><br>If you are referred by your insurance provider or solicitor, your details will be registered on our system, even if you are a first time user, you do not have to sign up.<br>Please click the link- <a href="https://ann.jellypx.com" target="_blank" rel="noopener">https://ann.jellypx.com</a><br>Username – This is your email id or mobile number given to your insurance provider<br>Password – This is your date of birth in the following pattern – DDMMYYYY (You may change this after your first login), if you have problems with this, please click “forgotten?” button and you should be able to create a new password and log in.</p>
<p><strong>To Book An Appointment:</strong><br>Home page - Click Book Appointment button or Go to Menu - Appointments and click the ‘+’ sign at the bottom.</p>
<p><strong>To View Appointments:</strong><br>Go to Menu – Appointments. In mobile app, the menu icon appears as three lines on the top left hand side corner</p>
<p><strong>To Amend Or Cancel Appointment:</strong><br><strong>(Cannot amend or cancel an appointment within 24 hours of existing appointment)</strong><br>Go to Menu – Appointments<br>Click the Pencil icon to amend or ‘X’ icon to cancel appointment</p>
<p><strong>To View Exercises:</strong><br>Go to Menu - Documents. You should be able to view the exercises.</p>
<p><strong>To sign Consent Forms:</strong><br>Go to Menu – Forms – click pencil icon to enter signature</p>
<p><strong>To upload client documents:</strong><br>Click Upload items button on home page to upload Client’s MRI, CT, or GP reports, etc.</p>''',True)}
{q("What happens when I come for my first appointment?","<p>When entering the clinic, please introduce yourself to the receptionist at Reception and take a seat in our waiting room. Your first appointment may last 35 minutes and will involve an assessment as well as a physical examination. From this assessment, you and your physiotherapist will set treatment goals to restore or develop your potential. Your physiotherapist will then discuss the proposed treatment, likely outcomes and probable recovery time frame with you. You are welcome to ask questions so that you can make informed choices about your treatment. You may decline any treatment/s you do not wish to consent to and have the right to do so at any time.</p>")}
{q("Do I need to bring anything with me?","<p>If you have been given a referral, have X-rays or other test results please bring these with you.</p>")}
{q("Can I bring someone with me?","<p>Under normal circumstances, you are welcome to bring a family member/interpretor/or a friend with you, but due to the current COVID restrictions and social distancing, please attend the session on your own where practically possible.</p>")}
{q("What should I wear?","<p>Ideally wear loose, comfortable clothing. For neck and upper back problems your physiotherapist may ask you to remove your top. For lower back and hip complaints, you may be asked to remove your trousers. Appropriate clothing will help you to be comfortable during the assessment and help us to assess the problem and develop the very best treatment plan for you. If you have any specific queries regarding attending the clinic which we may have missed to mention, please contact us and we will try all our best to suit your needs.</p>")}
{q("What are your Prices?","<h4>Prices</h4>"+FAQ_TABLES)}
{q("Pets?","<img src='/assets/img/annpetspolicy.png' alt='Ann Physiocare pets policy' style='border-radius:16px;max-width:520px' onerror=\"this.style.display='none'\"><p>Please see our pets policy image above. If it does not display, contact us on "+PHONE+".</p>")}
{q("What are your payment terms?","<p>Payment is to be agreed prior to the consultation/treatment, either by cash or card. This can be made over the phone while booking your appointment or with the therapist at the treatment centre. Please do not make any payments at the reception desk.</p>")}
{q("Will my private health insurance cover my physiotherapy consultation fees?","<p>We are recognized by and work alongside many major health insurance companies, most health insurance policies do cover, or part-cover, physiotherapy fees. Please check with your insurance company.<br>We would be happy to help with any corporate or group enquiries, get in touch today for a tailored quote.</p>")}
{q("Do I need a referral?","<p>A referral is usually not necessary, although if you have one please bring it with you so that your physiotherapist can communicate with the referring practitioner if necessary.</p><p>A referral is sometimes required in order to claim for physiotherapy costs on your health insurance. Please check with your insurer.</p>")}
{q("Cancellation Policy","<p>If you need to cancel the appointment, please give us 24 hours notice to re-arrange your appointment. Cancellations made on the day of the appointment will be charged and so will non-attendance.</p>")}
{q("How can I make a formal complaint?",f'''<p><strong>Our Complaints Procedure:</strong></p><p>We are committed to providing a high quality physiotherapy service to all our patients but unfortunately if you are not happy with our service/location/therapist, etc you can make a formal complaint. We aim to constantly improve our services and standards of care and hence take our feedback and complaints very seriously.</p>
<p><strong>To make a complaint:</strong></p>{ul([f"You can either make a phone complaint by calling us on {PHONE} or","Email to <a href='mailto:complaints@annphysiocare.com'>complaints@annphysiocare.com</a>"])}
<p>One of the members of our Complaints Team with get in touch with you within 24 hours to discuss the issue and aim to resolve it as quickly as possible. In certain instances, we may request you to give written complaint if needed.</p>
<p><strong>What to include in a written complaint:</strong></p>{ul(["Your details (your name, our reference number, date of birth, and email ID) or","A brief background of the complaint","Who was involved (Therapist, Centre staff, Admin, etc)","What action you would like us to take to resolve it"])}
<p>On receiving this, we will then acknowledge receipt of your complaint either via phone or email for further information if needed for our investigation and report back to you with our findings and resolution.</p>
<p>If you are still not satisfied with the outcome of your complaint, you could request for this to be taken to our higher management or seek independent legal advice.</p>''')}
{q("How to find nearby clinics",'<p><a class="btn btn-outline" href="https://www.youtube.com/watch?v=N76Uz3dEs_8" target="_blank" rel="noopener">▶ Click here for demo video</a></p>')}
</div></section>{questions_band()}"""
P["/faq/"]=page("/faq/","FAQ | Ann Physiocare",FAQ,desc="Answers to common questions about booking, your first appointment, prices, insurance and complaints.",hero=("FAQ","Frequently Asked Questions"),crumbs=[("FAQ",None)],active="/faq/")

# ====================== CONTACT ======================
CONTACT=f"""<section class="section"><div class="wrap split" style="align-items:start"><div class="cinfo rv">
<div class="card"><div class="ic">{ic('clock')}</div><div><h3>Customer Service</h3><p>Mon - Fri: 8:00 AM-6:00 PM<br>Saturday: 8:00 AM-4:00 PM<br>(GMT)</p><p style="margin:0">Customer Service :- <a href="tel:{TEL}"><strong>{PHONE}</strong></a></p></div></div>
<div class="card"><div class="ic">{ic('mail')}</div><div><h3>Email Us</h3><p style="margin:0"><a href="mailto:{EMAIL}">{EMAIL}</a></p></div></div>
<div class="card"><div class="ic">{ic('pin')}</div><div><h3>Head Office</h3><p style="margin:0">Ann Physiocare Ltd,<br>37A, Clase Road,<br>Morriston, Swansea,<br>SA6 8DS</p></div></div></div>
<form class="form rv" data-form="Contact" novalidate><fieldset><legend>Get In Touch</legend><div class="fg">
<div><label for="n">Your Name <span class="req">*</span></label><input id="n" name="Name" required></div><div><label for="e">Your Email <span class="req">*</span></label><input id="e" type="email" name="Email" required></div>
<div><label for="p">Phone</label><input id="p" type="tel" name="Phone"></div><div><label for="s">Subject</label><input id="s" name="Subject"></div>
<div class="full"><label for="m">Message <span class="req">*</span></label><textarea id="m" name="Message" rows="6" required></textarea></div>
<div class="full"><label class="check"><input type="checkbox" required name="Terms accepted"> I Accept All <a href="/terms-of-use/" target="_blank">Terms &amp; Conditions</a></label></div></div></fieldset>
<button class="btn btn-primary" type="submit">Send Message {ic('arrow')}</button><div class="note" role="status"></div></form></div></section>{questions_band()}"""
P["/contact/"]=page("/contact/","Contact | Ann Physiocare",CONTACT,desc="Contact Ann Physiocare: phone, email and head office address.",hero=("Contact","We’re here to help."),crumbs=[("Contact",None)],active="/contact/")

# ====================== CAREERS ======================
ABOUT_CO = lambda y: f"Ann Physiocare Limited is a team of dedicated professionals providing specialised physical therapy for the various musculoskeletal and neurological conditions at various locations in UK. We have been offering Physiotherapy services for {y} years and rapidly expanding. At Ann Physiocare we are passionate about giving the highest level of care in treating current injury or complaint and emphasising the importance of giving preventative tools to keep injury free."
COMMON_LOOK=["Positive, constructive and approachable","Have a great work ethic and display a flexible, ‘can-do’ attitude","Able to manage a varied caseload of MSK patients"]
LOOK_PHYSIO=COMMON_LOOK+["Registered with HCPC, CSP and committed to ongoing CPD","Self-starters with excellent communication skills"]
LOOK_MGMT=COMMON_LOOK+["Relevant experience managing a clinic","Self-starters with excellent communication skills"]
BENEFITS=["Contributory pension","Employee assistance programme","28 days of annual leave including bank holidays","Comprehensive induction, on-going training and development to widen your career prospects."]
SUM_A=["To work as an autonomous MSK practitioner in accordance with the standards and codes of practice of the Chartered Society of Physiotherapy, the Health Professions Council.","To provide specialist physiotherapy services through a combination of assessment, diagnosis, formulation of MSK treatment programs, intervention and teaching that aim to improve, maximize and maintain the physical ability and minimize the dysfunction, disability of people.","To be responsible for a defined caseload as allocated, using evidence based practice and client centered principles to assess, plan, implement and evaluate interventions that aim to achieve best outcomes for the client.","To develop knowledge and skills that meets the competency framework through a range of study.","To undertake all necessary verbal and written documentation required for patient care.","To formulate goals/clinical objectives with patients / carers / relatives and other health professionals and continually re-assess patients to evaluate progress, and alter treatment programmes accordingly.","To be professionally and legally accountable for all aspects of their work including the management of patients in their care and to seek advice from senior staff as appropriate."]
SUM_B=["To provide high quality physiotherapy including assessment, treatment and advice to patients with MSK related problems.","To formulate and deliver an individual physiotherapy treatment programme based on a sound knowledge of evidence based practice including; manual and electrotherapy techniques, therapeutic handling, patient education, exercise classes, and other alternative options.","To assess and treat own caseload of patients, and maintain associated records as an autonomous practitioner with support from senior staff.","To be responsible for maintenance of accurate written and electronic records, involving comprehensive progress and discharge reports, in line with CSP and HCPC standards.","To undertake all necessary verbal and written documentation required for patient care.","To formulate goals/clinical objectives with patients / carers / relatives and other health professionals and continually re-assess patients to evaluate progress, and alter treatment programmes accordingly.","To be professionally and legally accountable for all aspects of their work including the management of patients in their care and to seek advice from senior staff as appropriate."]
APPLY="To apply, please forward your CV to <a href='mailto:hr@annphysiocare.com'>hr@annphysiocare.com</a> or use the form below."
def job(id, title, posted, role, jtype, loc, start, hours, salary, lic, years, summary, looks, extra="", apply=APPLY, intro=None, summary_title="JOB PURPOSE/SUMMARY", sum_intro=""):
    meta=[("Role",role),("Job Type",jtype),("Location",loc),("Start date",start),("Hours",hours),("Salary",salary)]+([("Licence/Certification",lic)] if lic else [])
    m="".join(f"<div><b>{k}:</b><span>{v}</span></div>" for k,v in meta)
    return (f"<details class='job rv' id='{id}'><summary><span>{title}<small>{loc} · {jtype} · {salary}"+(f" · Posted {posted}" if posted else "")+"</small></span></summary><div class='dbody'>"
      f"<p>{intro or ABOUT_CO(years)}</p><div class='jmeta'>{m}</div><h4>{summary_title}</h4>{sum_intro}{ul(summary)}{extra}"
      f"<h4>WE’RE LOOKING FOR PEOPLE WHO ARE</h4>{ul(looks)}<h4>WHAT’S IN IT FOR YOU?</h4><p>Ann Physiocare values its people, so you can expect a competitive salary and benefits that include:</p>{ul(BENEFITS)}"
      f"<p><strong>{apply}</strong></p><a class='btn btn-primary' href='#apply'>Apply with the form</a></div></details>")
def physio(id, title, loc, start="ASAP", jtype="Full-time, Permanent", salary="£26,000 to £32,000 (Pro-rata) dependent on experience", sums=SUM_B, posted=None, years=7):
    return job(id,title,posted,"Clinical Physiotherapist",jtype,loc,start,"Full time 37.5 hrs pw",salary,"HCPC (required)" if sums is SUM_A else None,years,sums,LOOK_PHYSIO)
BDM_EXTRA="<h4>Responsibilities and Duties</h4>"+ul(["To undertake lead generation activity and support Operational Manager and Director with lead generation approach.","Develop new business proposals.","Lead and provide advice and technical support on business developments, tenders, funding bids and other defined commercial activities such as market assessments.","To lead on designated tenders and business cases.","To lead on the development of effective responses to opportunities to tender for services.","To actively participate in effective business case development.","To work with Operations Manager to ensure that the appropriate clinical, financial, activity, and performance information is in place to support development of proposals and tenders.","To scrutinise development proposals, tenders etc, ensuring that specific tender requirements are met and to submit them on behalf of the organisation.","Supply chain management at service providing locations."])+"<h4>Key Skills</h4><p>Team Management, ICT, Interviewing, Presenting, Health And Safety, Sales, Project Management, Training, Negotiation, Strong communication, Interpersonal skills.</p><h4>Required Experience and Qualifications</h4>"+ul(["Bachelor's degree or equivalent experience,","Industry related business development experience,","Proven knowledge and execution of successful development strategies,","Focused and goal-oriented."])+"<p>Preferred to have worked in the areas of Occupational Heath, medico-legal, Personal Injury, Insurance sector, rehabilitation services and solutions, NHS tenders, Commissioning.</p>"
jobs = [
 job("bdm-swansea","Business Development Manager (BDM)","5th July 2024","Business Development Manager","Full-time, Permanent","Swansea","ASAP","Full time 37.5 hrs pw","£40,000 per year",None,7,
   ["Identify partnership opportunities.","Develop new relationships in an effort to grow business and help company expand.","Maintain existing business.","Think critically when planning to assure project success .","To undertake all necessary verbal and written documentation required for patient care."],
   [], extra="", apply="To apply, <a href='https://uk.indeed.com/job/business-development-manager-bdm-f4831c4d69d7dbcc' target='_blank' rel='noopener'>click here [apply now]</a> or please forward your CV to <a href='mailto:hr@annphysiocare.com'>hr@annphysiocare.com</a> or use the form below.", sum_intro="<p>The ideal candidate will lead initiatives to generate and engage with business partners to build new business for the company.</p>"
 ).replace("<h4>WE’RE LOOKING FOR PEOPLE WHO ARE</h4><ul class=''></ul>","").replace(f"</ul><h4>WHAT’S IN IT",BDM_EXTRA+"<h4>WHAT’S IN IT",1) if False else None,
]
# BDM Swansea needs a custom body (no 'looking for' list) — build directly:
def bdm_swansea():
    meta=[("Role","Business Development Manager"),("Job Type","Full-time, Permanent"),("Location","Swansea"),("Start date","ASAP"),("Hours","Full time 37.5 hrs pw"),("Salary","£40,000 per year")]
    m="".join(f"<div><b>{k}:</b><span>{v}</span></div>" for k,v in meta)
    return (f"<details class='job rv' id='bdm-swansea'><summary><span>Business Development Manager (BDM)<small>Swansea · Full-time, Permanent · £40,000 per year · Posted 5th July 2024</small></span></summary><div class='dbody'><p>{ABOUT_CO(7)}</p><div class='jmeta'>{m}</div>"
      "<h4>JOB PURPOSE/SUMMARY</h4>"+ul(["Identify partnership opportunities.","Develop new relationships in an effort to grow business and help company expand.","Maintain existing business.","Think critically when planning to assure project success .","To undertake all necessary verbal and written documentation required for patient care."])
      +"<p>The ideal candidate will lead initiatives to generate and engage with business partners to build new business for the company.</p>"+BDM_EXTRA
      +"<p><strong>To apply, <a href='https://uk.indeed.com/job/business-development-manager-bdm-f4831c4d69d7dbcc' target='_blank' rel='noopener'>click here [apply now]</a> or please forward your CV to <a href='mailto:hr@annphysiocare.com'>hr@annphysiocare.com</a> or use the form below.</strong></p><a class='btn btn-primary' href='#apply'>Apply with the form</a></div></details>")
PM_SUM=["Practice manager will work with a variety of staff who work from or are based within Ann Physiocare practices. These staff will typically include Physiotherapists, Clinic coordinators, Regional managers."]
PM_DUTIES=["Recruit, train and supervise account managers and admin staff","Business planning","Handling financial systems for the practices","Selecting, training and supervising non-clinical staf","Developing and supervising appointment systems that work well for patients and clinicians","Ensuring accurate medical and financial records are kept and comply with GDPR","Developing strategies for the practices on issues such as computer systems and security, expanding or changing services, and long-term services","Control stocks of equipment, stationery, consumables and clinical suppies","Coordinating the buildings'(for all practices) cleaning, maintenance and security (records & GDPR)","To be a clinical receptionist around this role as practice manager so you can be in and around each of our clinics to get a feel for every aspect of the business"]
PM_QUAL=["The ability to manage a changing environment","Good communication skills and Organisational skills","Leadership and motivational skills","Confidence with information technology","Negotiating skills","The ability to challenge the way things are and find better alternatives","Honesty and fairness in dealing with other people","A commitment to the ideals of quality and fairness in delivering healthcare."]
pm = job("practice-manager","Health Care Practice Manager – Swansea",None,"Health Care Practice Manager","Full-time","Watford","8/1/2022","Full time 37.5 hrs pw","£26,000 to £28,000 dependent on experience",None,8,PM_SUM,LOOK_MGMT[:2]+["Able to manage a varied caseload of MSK patients","Relevant experience managing a clinic","Self-starters with excellent communication skills"],
  intro=ABOUT_CO(8), sum_intro="<p>We are a thriving and expanding organization operating within the health industry, with a specific focus on delivering cutting-edge solutions to our esteemed clientele. As a Practice Manager, your pivotal responsibility lies in communication and coordination of the staff and services. Your expertise will significantly contribute to effective service delivery. In the role of a Practice Manger, your contributions will be instrumental in the client management and satisfaction.</p>",
  extra="<p>You will be involved in a wide range of activities, including:</p>"+ul(PM_DUTIES)+"<h4>Key qualities:</h4>"+ul(PM_QUAL),
  apply="To apply, please forward your CV to <a href='mailto:hr@annphysiocare.com'>hr@annphysiocare.com</a> or <a href='mailto:mani.neel@annphysiocare.com'>mani.neel@annphysiocare.com</a> use the form below.")
ME_SUM=["The primary responsibility entails the development and continuous maintenance of the company's website. This involves designing and constructing an aesthetically pleasing, intuitive, and adaptable website for Ann Physiocare Ltd.","The key responsibility lies in implementing SEO best practices to optimize the website for search engines, thereby enhancing organic search rankings and driving relevant traffic. This involves conducting comprehensive keyword research, creating effective meta tags, optimizing page titles, and ensuring appropriate URL structures to improve search engine visibility. By diligently executing these strategies, the aim is to maximize the website's presence and visibility in search engine results pages","To be responsible for developing and executing robust digital marketing strategies that align with Ann Physiocare Ltd's business objectives. This will involve meticulously planning and implementing campaigns across diverse digital channels, including search engines, social media platforms, email marketing, and display advertising. By leveraging these channels effectively, you will aim to enhance brand visibility, engage target audiences, and drive desirable outcomes in line with Ann Physiocare Ltd's overarching goals.","To oversee and manage online advertising campaigns across platforms such as Google Ads and social media ads. This includes setting up campaigns, closely monitoring their performance, and continuously optimizing ad performance to drive targeted traffic and achieve conversions. By analyzing relevant metrics and making data-driven adjustments, you will strive to maximize return on investment (ROI) and ensure campaign success to establish and maintain a robust social media presence. This involves developing and curating compelling content, managing multiple social media accounts, actively engaging with followers, and harnessing the potential of various social media platforms to elevate brand awareness and foster meaningful engagement. By implementing effective social media strategies, your aim is to create a vibrant online community, enhance brand visibility, and cultivate positive interactions with the target audience."]
me = job("marketing-executive","Marketing Executive – Swansea",None,"Marketing Executive","Full-time","Swansea","4/1/2021","Full time 37.5 hrs pw","£24,400 to £28500 dependent on experience",None,8,ME_SUM,LOOK_MGMT,intro=ABOUT_CO(8),
  sum_intro="<p>We are a thriving and expanding organization operating within the health industry, with a specific focus on delivering cutting-edge solutions to our esteemed clientele. As a Marketing Executive, your pivotal responsibility lies in spearheading our marketing strategies and executing campaigns with utmost precision. Your expertise will significantly contribute to elevating our online visibility and effectively generating valuable leads. In the role of a Web Developer, your contributions will be instrumental in the creation of visually captivating and highly functional websites that align with our clients' objectives while ensuring an outstanding user experience. Your expertise in this domain will be vital in delivering exceptional results.</p>",
  apply="To apply, please forward your CV to <a href='mailto:hr@annphysiocare.com'>hr@annphysiocare.com</a> or <a href='mailto:mani.neel@annphysiocare.com'>mani.neel@annphysiocare.com</a> use the form below.")
BDML_SUM=["As an integral member of APC's Senior Management Team, you will actively contribute to the strategic and operational development of APC's business and commercial endeavors. Leveraging your expertise and insights, you will play a critical role in shaping the organization's growth strategies, identifying new opportunities, and enhancing revenue generation. Through your leadership and collaboration, you will drive the success and expansion of APC 's business operations in a dynamic and competitive market.","Assume the responsibility for overseeing and ensuring the effective execution of A's business and commercial activities. Utilize your strategic acumen and operational expertise to drive the successful implementation of key initiatives, optimize business processes, and enhance overall performance. Through effective leadership, resource management, and continuous evaluation, contribute to the achievement of organizational objectives, fostering sustainable growth and success in A's business endeavors.","To play a strategic and operational role in developing AnnPhysiocare’s (APC) business and commercial activities, as a member of APC’s Senior Management Team.","To market and sell all trading activities to an agreed annual target of invoiced revenue, to increase year on year.","To develop new business relationships, services and products; and generate and negotiate new contracts and income for APC to an agreed annual target of invoiced revenue, to increase year on year.","To oversee the effective delivery of APC’s business and commercial activities."]
bdml = job("bdm-london","Business Development Manager – London",None,"Business Development Manager","Full-time","London","10/10/2020","Full time 37.5 hrs pw","£26,500 to £30,500 dependent on experience",None,"over 7",BDML_SUM,LOOK_MGMT,intro=ABOUT_CO("over 7"),
  sum_intro="<p>We are a thriving and expanding organization operating within the health industry, with a specific focus on delivering cutting-edge solutions to our esteemed clientele. As a Business Development Manager, You will spearhead the identification of emerging business prospects, cultivate fruitful relationships with prospective clients, and propel growth and revenue generation for our organization. Leveraging your strategic acumen, exceptional communication proficiencies, and adeptness at recognizing market trends, you will play a crucial part in expanding our customer base and attaining our overarching business goals.</p>",
  apply="To apply, please forward your CV to <a href='mailto:hr@annphysiocare.com'>hr@annphysiocare.com</a> or <a href='mailto:mani.neel@annphysiocare.com'>mani.neel@annphysiocare.com</a> use the form below.")
S="£26,000 to £32,000 (Pro-rata) dependent on experience"
jobs_html = "".join([
 bdm_swansea(),
 physio("physio-london","Clinical Physiotherapist – London","Leicester",salary="£26,000 to £32,000 per year",sums=SUM_A,posted="5th July 2024"),
 physio("physio-leicester","Clinical Physiotherapist – Leicester","Leicester",salary="£26,000 to £32,000 per year",sums=SUM_A,posted="5th July 2024"),
 physio("physio-cardiff","Clinical Physiotherapist – Cardiff","Cardiff"),
 physio("physio-salisbury","Clinical Physiotherapist – Salisbury","Salisbury"),
 pm,
 physio("physio-weston","Clinical Physiotherapist – Weston","Weston"),
 physio("physio-beckenham","Clinical Physiotherapist – Beckenham","Beckenham"),
 physio("physio-finchley","Clinical Physiotherapist – Finchley","Finchley","3/15/2022",salary="£26,000 to £32,000 dependent on experience"),
 physio("physio-bristol","Clinical Physiotherapist – Bristol","Bristol","3/10/2022",years=9),
 physio("physio-bath","Clinical Physiotherapist – Bath","Bath"),
 physio("physio-tonbridge","Clinical Physiotherapist – Tonbridge","Tonbridge","1/15/2022"),
 physio("physio-maidstone","Clinical Physiotherapist – Maidstone","Maidstone"),
 physio("physio-newbury","Clinical Physiotherapist – Newbury","Newbury","11/15/2021",jtype="Part-time"),
 physio("physio-illford","Clinical Physiotherapist – Illford","Illford","10/25/2021"),
 physio("physio-brighton","Clinical Physiotherapist – Brighton","Brighton","9/25/2021"),
 physio("physio-southgate","Clinical Physiotherapist – Southgate","Southgate"),
 me,
 physio("physio-dollis-hill","Clinical Physiotherapist – Dollis Hill","Dollis Hill",salary="£26,000 to £32,000 dependent on experience"),
 bdml,
 physio("physio-welling","Clinical Physiotherapist – Welling","Welling","10/15/2019"),
 physio("physio-hove","Clinical Physiotherapist – Hove","Hove","9/15/2018"),
])
CAREERS=f"""<section class="section"><div class="wrap" style="max-width:960px"><div class="sec-head center rv"><span class="eyebrow">Join our team</span><h2>Current Opportunites</h2><p class="lead">Ann Physiocare values its people — competitive salary, contributory pension, 28 days annual leave and on-going training.</p></div>
{jobs_html}
<div class="cta rv" id="apply" style="margin-top:3rem;grid-template-columns:1fr"><div><h2>Are you interested in working with us for any other position, send us your CV now!</h2></div></div>
<form class="form rv" data-form="Careers application" data-to="hr@annphysiocare.com" style="margin-top:2rem" novalidate><fieldset><legend>Get In Touch</legend><div class="fg">
<div><label for="c1">Your Name <span class="req">*</span></label><input id="c1" name="Name" required></div><div><label for="c2">Your Email <span class="req">*</span></label><input id="c2" type="email" name="Email" required></div>
<div><label for="c3">Street Name <span class="req">*</span></label><input id="c3" name="Street" required></div><div><label for="c4">City <span class="req">*</span></label><input id="c4" name="City" required></div>
<div><label for="c5">Postcode <span class="req">*</span></label><input id="c5" name="Postcode" required></div><div><label for="c6">Telephone <span class="req">*</span></label><input id="c6" type="tel" name="Telephone" required></div>
<div><label for="c7">Reference</label><input id="c7" name="Reference"></div>
<div><label>Are you willing to relocate <span class="req">*</span></label><div class="radios"><label><input type="radio" name="Relocate" value="Yes" required> Yes</label><label><input type="radio" name="Relocate" value="No"> No</label></div></div>
<div class="full"><label for="c8">Cover Letter</label><textarea id="c8" name="Cover letter" rows="5"></textarea></div>
<div class="full"><label for="c9">CV <span class="req">*</span> <small style="font-weight:500;color:var(--muted)">(PDF or DOC format files preferably. This form does not accept DOCX format.)</small></label><input id="c9" type="file" name="CV" accept=".pdf,.doc" required></div></div></fieldset>
<button class="btn btn-primary" type="submit">Submit {ic('arrow')}</button><div class="note" role="status"></div></form></div></section>"""
P["/careers/"]=page("/careers/","Careers | Ann Physiocare",CAREERS,desc="Current job opportunities at Ann Physiocare: clinical physiotherapists, business development, marketing and practice management.",hero=("Careers","Current Opportunites"),crumbs=[("Careers",None)],active="/careers/")

# ====================== REFERRAL FORM ======================
def f(label,name,req=False,typ="text",full=False):
    return f"<div{' class=full' if full else ''}><label>{label}{' <span class=req>*</span>' if req else ''}</label><input type='{typ}' name='{name}'{' required' if req else ''}></div>"
def sel(label,name,opts,req=False):
    return f"<div><label>{label}{' <span class=req>*</span>' if req else ''}</label><select name='{name}'{' required' if req else ''}><option value=''>Select...</option>"+"".join(f"<option>{o}</option>" for o in opts)+"</select></div>"
REF=f"""<section class="section"><div class="wrap" style="max-width:960px"><form class="form rv" data-form="Referral" novalidate>
<h2 style="margin-bottom:2rem">Referral Form</h2>
<fieldset><legend>Patient Details</legend><div class="fg">
{sel("Title","Title",["Mr","Mrs","Ms","Miss","Master","Dr"],True)}{f("First Name","First Name",True)}{f("Last Name","Last Name",True)}{f("Date of Birth","DOB",True,"date")}{f("Telephone","Telephone",True,"tel")}{f("Email","Email",False,"email")}
{f("Address Line 1","Address 1",True)}{f("Address Line 2","Address 2")}{f("City","City",True)}{f("Postcode","Postcode",True)}</div></fieldset>
<fieldset><legend>Referral Type <span class="req">*</span></legend><div class="fg">{sel("Referral Type","Referral Type",["GP","Self","Other"],True)}</div></fieldset>
<fieldset><legend>Referrer Details</legend><div class="fg">
{sel("Referrer Title","Referrer Title",["Dr","Mr","Mrs","Ms","Miss"],True)}{f("Referrer First Name","Referrer First Name",True)}{f("Referrer Last Name","Referrer Last Name",True)}{f("Organisation Name","Organisation",True)}{f("Referrer Telephone","Referrer Telephone",True,"tel")}{f("Referrer Email","Referrer Email",False,"email")}
{f("Referrer Address Line 1","Referrer Address 1",True)}{f("Referrer Address Line 2","Referrer Address 2")}{f("Referrer City","Referrer City",True)}{f("Referrer Postcode","Referrer Postcode",True)}</div></fieldset>
<fieldset><legend>Referral Details</legend><div class="fg">
<div class="full"><label>Current Symptoms</label><textarea name="Current Symptoms" rows="3"></textarea></div><div class="full"><label>Previous Treatment</label><textarea name="Previous Treatment" rows="3"></textarea></div><div class="full"><label>Other Medical Conditions</label><textarea name="Other Medical Conditions" rows="3"></textarea></div>
<div><label>Do you require a physiotherapist of the same gender?</label><div class="radios"><label><input type="radio" name="Gender preference" value="No Preference" checked> No Preference</label><label><input type="radio" name="Gender preference" value="Male"> Male</label><label><input type="radio" name="Gender preference" value="Female"> Female</label></div></div>
<div><label>Is the client aware of this referral and happy to be contacted by us?</label><div class="radios"><label><input type="radio" name="Client aware" value="Yes"> Yes</label><label><input type="radio" name="Client aware" value="No"> No</label></div></div>
<div class="full"><label>Please attach (If required)</label><input type="file" name="Attachment"></div></div></fieldset>
<button class="btn btn-primary" type="submit">Submit Referral {ic('arrow')}</button><div class="note" role="status"></div></form></div></section>"""
P["/referral-form/"]=page("/referral-form/","Referral Form | Ann Physiocare",REF,desc="Refer a patient to Ann Physiocare.",hero=("Refer to Us","Referral Form"),crumbs=[("Refer to Us",None)],active="/referral-form/")

# ====================== STAFF LOGIN ======================
STAFF=f"""<section class="section"><div class="wrap" style="max-width:520px"><form class="form rv" id="staffForm" novalidate><div class="ic">{ic('lock')}</div><h2 style="font-size:1.8rem;margin-bottom:1.2rem">Staff Login</h2>
<label for="sp">Enter the Password to Proceed</label><input id="sp" type="password" autocomplete="current-password" required><br><br><button class="btn btn-primary" type="submit">Enter</button><div class="note" role="status"></div></form></div></section>"""
P["/staff-login/"]=page("/staff-login/","Staff Login | Ann Physiocare",STAFF,hero=("Staff Login",None),crumbs=[("Staff Login",None)],active="/staff-login/",extra_head="<meta name='robots' content='noindex'>")

# ====================== IN-WORK SUPPORT ======================
RCS="https://rcs-wales.co.uk/helping-people/in-work-support-service/"
def steps(items): return "<ol class='steps'>"+"".join(f"<li><strong>{a}</strong><br>{b}</li>" for a,b in items)+"</ol>"
IWS=f"""<section class="section"><div class="wrap" style="max-width:980px"><div class="sec-head center rv"><span class="eyebrow">RCS In-Work Support</span><h2>Supporting You to Manage Musculoskeletal Conditions, Stay Well at Work and Return to Work Safely</h2>
<p class="lead">Referred to Ann Physiocare by RCS? Our physiotherapy team can assess your condition, provide appropriate treatment and help you manage physical problems that may be affecting your ability to work.</p>
<div class="btn-row" style="justify-content:center"><a class="btn btn-primary" href="#referred-pathway">I Have an RCS Referral</a><a class="btn btn-outline" href="{RCS}" target="_blank" rel="noopener">Apply Through RCS</a></div></div>
<h3 class="rv">How the Service Works</h3><p class="rv">RCS manages eligibility and referral. Ann Physiocare delivers the physiotherapy assessment and treatment once you've been referred.</p>
{steps([("Apply to RCS","Submit an application through the RCS In-Work Support Service."),("Eligibility Checked","RCS confirms whether you meet the criteria for the programme."),("Referred for Physiotherapy","Eligible applicants are referred to Ann Physiocare for treatment."),("Assessment &amp; Treatment","Our physiotherapy team assesses you and begins your care plan.")])}
<h3 style="margin-top:2.4rem">Eligibility</h3><p>Eligibility criteria apply. Please check the latest eligibility requirements directly with RCS.</p><a class="btn btn-outline" href="{RCS}" target="_blank" rel="noopener">Visit the RCS In-Work Support Service →</a>
<h3 style="margin-top:2.6rem">What Ann Physiocare Can Help With</h3><p>Physiotherapy support through this pathway may be suitable for:</p>
{checks(["Back and neck pain","Shoulder pain","Work-related musculoskeletal problems","Repetitive strain injuries (RSI)","Joint and muscle pain","Postural problems","Pain affecting work activities","Problems caused or aggravated by physical work","Difficulties returning to normal duties following injury","Advice on managing your condition while working"])}
<h3 id="referred-pathway" style="margin-top:2.6rem">Already Referred to Ann Physiocare?</h3><p>If RCS has referred you to Ann Physiocare for physiotherapy, our team will guide you through the next steps.</p>
{steps([("Assessment","Your physiotherapist assesses the problem and how it affects your work."),("Treatment","An individual treatment and rehabilitation programme is developed."),("Self-Management","Exercises and advice help you manage symptoms between appointments."),("Work-Focused Recovery","Where appropriate, treatment considers activities that are important for your job and your return to normal working activities.")])}
<h3 style="margin-top:2.6rem">Supporting Employees to Stay Well at Work</h3><p>Musculoskeletal problems can affect an employee's comfort, mobility, productivity and ability to remain at work. Through our work with the RCS In-Work Support Service, Ann Physiocare provides physiotherapy support focused on helping eligible employees and self-employed people manage physical health conditions affecting their work.</p>
<a class="btn btn-outline" href="{RCS}" target="_blank" rel="noopener">Find Out About RCS In-Work Support</a>
<h3 style="margin-top:2.6rem">Your Pathway at a Glance</h3><p>Not sure which route applies to you? Use this diagram to see where you fit.</p>
<div class="grid g2"><div class="card"><h3>Not Referred Yet</h3>{steps([("Apply to RCS",""),("Eligibility Assessment",""),("Referral","")])}</div><div class="card"><h3>RCS Referred</h3>{steps([("Ann Physiocare Physiotherapy",""),("Assessment",""),("Treatment / Rehabilitation","")])}</div>
<div class="card"><h3>I've Already Been Referred by RCS</h3><p>Continue to Ann Physiocare for appointment information.</p><a class="btn btn-primary" href="{BOOK}" target="_blank" rel="noopener">Continue to Booking</a></div>
<div class="card"><h3>I Haven't Been Referred Yet</h3><p>Check your eligibility and apply through RCS.</p><a class="btn btn-outline" href="{RCS}" target="_blank" rel="noopener">Apply Through RCS</a></div></div>
<h3 style="margin-top:2.6rem">Helping You Stay Active, Stay in Work and Return to Work with Confidence</h3>
<p>Ann Physiocare works with RCS to provide physiotherapy services for eligible people accessing the In-Work Support Service. If a musculoskeletal condition such as back pain, neck pain, joint pain or a work-related injury is affecting your ability to work, our physiotherapy team can provide assessment, treatment, rehabilitation and practical advice to support your recovery.</p>
<div class="grid g2"><div class="card"><h3>Already Referred by RCS?</h3><p>Find out what happens next and how to access your physiotherapy appointments.</p><a class="btn btn-primary" href="#referred-pathway">See Next Steps</a></div><div class="card"><h3>Not Yet Referred?</h3><p>Visit RCS to check your eligibility and apply for the In-Work Support Service.</p><a class="btn btn-outline" href="{RCS}" target="_blank" rel="noopener">Visit RCS</a></div></div></div></section>{questions_band()}"""
P["/in-work-support/"]=page("/in-work-support/","RCS In-Work Support Physiotherapy | Ann Physiocare",IWS,desc="Ann Physiocare provides physiotherapy treatment to eligible clients referred through the RCS In-Work Support Service. Find out how the referral pathway works and what to expect from assessment through to treatment.",extra_head='<meta name="keywords" content="RCS in-work support, physiotherapy Wales, work related musculoskeletal physiotherapy, RCS referral">',hero=("RCS In-Work Support Physiotherapy","RCS In-Work Support - Swansea, Llanelli, Carmarthenshire"),crumbs=[("RCS In-Work Support - Swansea, Llanelli, Carmarthenshire",None)],active="/in-work-support/")
