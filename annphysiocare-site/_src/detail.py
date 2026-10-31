from layout import *

SERVICES_NAV = [("Musculoskeletal Physiotherapy","/musculoskeletal-physiotherapy/"),("Neurological Physiotherapy","/neurological-physiotherapy/"),
 ("Occupational Health Physiotherapy","/occupational-health-physiotherapy/"),("Online Physiotherapy","/online-physiotherapy/"),("Home Physiotherapy","/home-physiotherapy/"),
 ("Functional Capacity Evaluation","/functional-capacity-evaluation/"),("DSE Assessments","/dse-assessments/")]
TREAT_NAV = [("Acupuncture","/acupuncture/"),("Soft Tissue Mobilisation","/soft-tissue-mobilisation-physiotherapy/"),("Exercise Programme","/exercise-programme-physiotherapy/"),
 ("Manipulation and Mobilisation","/manipulation-and-mobilization-physiotherapy/"),("Electrotherapy","/electrotherapy/"),("Massage Physiotherapy","/massage-physiotherapy/"),("Shockwave Therapy","/shockwave-therapy/")]

def ul(items, cls=""): return f"<ul class='{cls}'>"+"".join(f"<li>{i}</li>" for i in items)+"</ul>"
def checks(items): return ul(items,"checks")
def pills(items): return ul(items,"pills")

def detail_page(slug, title, h1, crumb, intro, body, nav, img, imglabel, icon, testimonials_on=False, extra_tail=""):
    layout = f"""<section class="section"><div class="wrap article"><article class="prose">{body}</article>{related(nav, slug)}</div></section>"""
    tail = (testimonials(6) if testimonials_on else "") + funding() + request_band() + extra_tail
    return page(slug, title, layout+tail, desc=intro[:155], active="/services/" if nav is SERVICES_NAV else "/treatments/",
                hero=(h1, intro), crumbs=[(crumb[0], crumb[1]), (h1, None)])

P = {}   # slug -> html

# ---------------- SERVICES ----------------
P["/musculoskeletal-physiotherapy/"] = detail_page("/musculoskeletal-physiotherapy/","Musculoskeletal Physiotherapy | Ann Physiocare","Musculoskeletal Physiotherapy",("Services","/services/"),
 "Treatment of disease or injury relating to the muscles, bones, tendons, ligaments and nerves.",
 f"""<h2>Musculoskeletal Physiotherapy</h2>
<p>Musculoskeletal physiotherapy is the treatment of disease or injury relating the muscles, bones, tendons, ligaments and nerves. Treatment involves reducing pain, increasing movement and restoring function, to get you back to your daily or sporting activities as quickly as possible. Musculoskeletal complaints can be acute or chronic, ranging from ankle sprains to back pain or osteoarthritis, and can also include long term conditions such as joint hypermobility and fibromyalgia.</p>
<p>Our skilled team of physiotherapists will thoroughly assess you, to diagnose the underlying cause for your pain. Next, they will provide treatment to help relieve pain and restore movement, which can be achieved through massage, joint mobilisation, acupuncture, electrotherapy, exercise rehabilitation and many more. Following treatment, you and your physiotherapist will discuss your goals and come up with a plan of how to achieve them together. You will be prescribed a personalised home exercise programme, alongside education and advice on management strategies and how to prevent future recurrences.</p>
{media('service-msk.webp','Hands-on assessment','bone')}
<h2>What Is Included In This Service?</h2>
{pills(["Biomechanical Assessment","Manual Techniques","Acupuncture","Balance Training","Exercise Prescription","Work Assessment","Braces","Splints","Therapeutic Training","Sports Massage","Gait Retraining"])}
<h2>Symptoms</h2><p><strong>Common symptoms of musculoskeletal injuries include:</strong></p>
{checks(["Pain or aching","Stiffness","Swelling","Bruising","Reduced range of movement","Difficulty to weight bear or walk normally","Sleep disturbance","Mild weakness"])}
<p><strong>Less common symptoms may include:</strong></p>
{checks(["Moderate to severe weakness","Pins and needles or tingling","Numbness","Radiating pain"])}
<h2>Common MSK Injuries</h2>
<h3>Neck:</h3><p>The neck, or cervical spine, consists of 7 stacked bones called vertebrae, supported by muscles, tendons, ligaments and nerves. It is strong and flexible, designed to support the head and its movements, protect the spinal cord, and to facilitate blood flow to the brain. Irritation of the cervical spine structures can cause neck pain and stiffness, which may radiate to the head or down the shoulder.<br>Causes of neck pain may include: poor sleeping posture, prolonged positions (such as long periods of desk work or slouching), overuse from repetitive motions, trauma (for example whiplash following a road traffic accident), and degeneration (wear and tear as we grow older.</p>
<h3>Lower back:</h3><p>Low back pain is very common, affecting 4 out of 5 people at some point throughout their lifetime. It is the leading cause of job-related disability, contributing to missed work days. It is usually categorised into 3 types: acute (less than 6 weeks), sub-acute (6-12 weeks) and chronic (12+ weeks). The spine is a strong, stable and flexible structure which is not easily damaged; most causes of pain are simple strains or sprains.<br>Many physical and psychological factors can cause back pain, often in combination, and can include: ‘protecting’ the back and avoiding movements, stress, poor quality sleep, being overweight, not getting enough physical activity.</p>
<h3>Shoulder:</h3><p>Shoulder pain is very common and will affect most people at some point in their lives. The shoulder complex is made up of three bones: the clavicle (collarbone), the humerus (upper arm bone) and the scapula (shoulder blade). Being a ball and socket joint, it is the most mobile joint in the body. Allowing this increased movement to occur is a complex network of muscles, tendons, ligaments and cartilage. Due to the increased mobility, these soft tissue structures are relied on to achieve stability, and are therefore more susceptible to injury and more commonly the cause of shoulder pain and dysfunction.</p>
<h3>Knee:</h3><p>The knee is one of the most commonly injured joints, affecting all age ranges. It is a hinge joint which allows for mostly flexion and extension (bending and straightening) with minimal rotational movement. Due to the load placed on the knees with everyday activities, such as walking and running, it is one of the first places people notice symptoms of wear and tear (osteoarthritis). Osteoarthritis is the degeneration of healthy articular cartilage, which allows smooth movement and acts as a shock absorber.<br>Ligaments are important to provide stability for the knee joint. Ligaments are strong bands of tissue that connect bone to bone. Injuries to these may cause feelings of instability, or even the knee giving way. These are more commonly injured during sports or physical activity, where increased forces are sustained on the knee.</p>""",
 SERVICES_NAV,"","","bone",testimonials_on=True)

P["/neurological-physiotherapy/"] = detail_page("/neurological-physiotherapy/","Neurological Physiotherapy | Ann Physiocare","Neurological Physiotherapy",("Services","/services/"),
 "Treatment of injury or disease relating to the central nervous system — the brain, spinal cord and nerves.",
 f"""<h2>Neurological Physiotherapy</h2>
<p>When damage occurs to the central nervous system involving the brain, spinal cord and peripheral nerves, the injury or illness can manifest into a form of loss in coordination in movement, muscle spasms, tremors, and loss of sensation, balance, paralysis and various other physical conditions.</p>
<p>Neurological physiotherapy is used to address these physical conditions by helping train the movement, exercises that restore balance and recovery. This can also be used in fast recovery or rehabilitation following an injury or accident for children to achieve developmental milestones. When any damage happens to the brain or spinal cord, the nerves carrying the electrical signals become inactive, resulting in the various physical conditions. But the brain has a characteristic known as neuroplasticity by which the brain can create new connections, pathways through regular and repetitive physical activities and exercises.</p>
{media('service-neuro.webp','Neuro rehabilitation','brain')}
<p>Neurological physiotherapy takes advantage of the same principle and used to treat many disorders such as.</p>
{pills(["Cerebral palsy","Parkinson's","Dementia","Dyspraxia","Fibromyalgia","Head injuries","Spinal cord injuries","Multiple sclerosis","Muscular dystrophy","Myopathy","Peripheral nerve injury","Stroke","Developmental delays","Huntington's disease"])}
<p>And many more neuro physio conditions.</p>
<p>Treatment with this physiotherapy can improve your ability to perform daily tasks and support the functional behaviours you enjoy most. Driving, ascending stairs, shopping, gardening, or being able to turn over and change positions in bed, or transferring to your bed with assistance, are all examples of this. Several principles of neurological physiotherapy, such as the Bobath Concept, Carr and Shepherd Concept, Brunnstrom Approach, etc., are used depending on the client, their symptoms, and their goals.</p>
<h3>Benefits of neurological physiotherapy</h3>
{checks(["Make precise and goal-directed movements less difficult.","Enhance potential for everyday physical activity by retraining common motion patterns.","Muscle energy increases, allowing for a range of movement and the development of gross and fine motor skills.","Regain calm by improving the stance.","Lengthen tense muscle mass to aid in the reduction of spasticity and contractures","Boost your fitness levels","Assists problems with breathing","Lessens the hazard of chest infections","Reduces the risk of falling","Reduce stress and anxiety","Relieve pains"])}
<p>And many more indirect benefits are possible with neurological physiotherapy.</p>
<h4>What does it involve?</h4><p>Depending on the symptoms and patient's problem, any of the following may be prescribed:</p>
{ul(["Splinting or positioning to correct limb positioning or splint prescription to keep the joints from tightening.","Stretch and strengthen the muscles by doing exercises in bed.","Exercises for breathing and movement to prevent vascular problems such as chest infections and DVTs.","Mobilization aids in precise movement. Sit up straight, get up, and walk on mattresses.","Prescriptions for mobility aids, as well as recommendations and practice on how to use a strolling frame or other walking aids as required."])}
<p>An initial evaluation determines any issues caused by your neurological disorder, and a treatment plan tailored to your needs will be established.</p>
<p>Between you and your physiotherapist, a formal recovery programme with short and long-term treatment objectives will be established. Treatment for neurological physiotherapy may be done at home or in a clinic, whichever suits the needs.</p>""",
 SERVICES_NAV,"","","brain",testimonials_on=True)

P["/occupational-health-physiotherapy/"] = detail_page("/occupational-health-physiotherapy/","Occupational Health Physiotherapy | Ann Physiocare","Occupational Health Physiotherapy",("Services","/services/"),
 "Interventions aimed at minimising health and safety hazards for workers — prevention, evaluation, recovery and preparation.",
 f"""<h2>Occupational Health Physiotherapy</h2>
<p>Members of the Occupational Health (OH) community collaborate with various individuals, including employers, staff, other health practitioners and medical personnel, engineers and designers.</p>
<p>They include a range of interventions aimed at minimising health and safety hazards for workers. They do it by helping them prevent any injuries or managing to stay active, increase their work efficiency and eliminate occupation-related health issues where physiotherapist assistance can help.</p>
{media('service-occupational.webp','Healthy at work','briefcase')}
<h2>Is Occupational Health important?</h2>
<p>Employment is said to improve physical and mental well-being and a worker's sense of intent, trust, self-worth, freedom and fulfilment. Going back to work after an illness or accident can be seen as a significant outcome measure when considering recovery services and working-age people's help.</p>
<h2>What do we do?</h2>
<p>As Occupational Health specialists, we are trained to understand the intricate relationship between work efficiency and health. The main objectives of our OH support are</p>
{checks(["Workers' health and working capability should be maintained and improved.","Improvements to working conditions to make them more health and safety friendly","To ensure work cultures that support workplace health and safety, conducive social interactions, and increased productivity.","To help influence the employees' work output positively by assisting them to come out of their workplace health issues."])}
<p>Our Occupational Health Physiotherapists have extensive experience treating musculoskeletal conditions in the workplace, various psychological disturbances such as stress, depression and anxiety resulting from work. We address their chronic illness conditions and various other physiotherapy interventions to reduce absenteeism and promote their productivity.</p>
<h2>Annphysiocare expert tips for workplace fitness</h2>
{checks(["If you can, take some time off to get some fresh air.","Take a lunchtime stroll or join a fitness class to stay busy.","Maintain neck mobility by avoiding craning your phone between your ear and shoulder.","Don't overwork yourself for meeting deadlines at work; instead, distribute your workload and be punctual.","When the load is too heavy, seek assistance.","Have fun with your peers now and then in a day. Take breaks and hang out with them.","Plan weekend nature trips that release your stress."])}
<h3>Consult Us</h3>
<p>Here at Annphysiocare, our range of services offer essential aspects of occupational health and safety, such as prevention, evaluation, recovery, and preparation. You can assure to be served by a team of experienced physiotherapy experts, assisting you in the reduction of absenteeism and increasing occupational fulfilment in all types of workplaces and occupations.</p>
<div class="grid g2" style="margin-top:1.6rem"><a class="card" href="/functional-capacity-evaluation/"><div class="ic">{ic('clip')}</div><h3>Functional Capacity Evaluation</h3><span class="more">Learn more</span></a><a class="card" href="/dse-assessments/"><div class="ic">{ic('monitor')}</div><h3>DSE Assessments</h3><span class="more">Learn more</span></a></div>""",
 SERVICES_NAV,"","","briefcase")

P["/online-physiotherapy/"] = detail_page("/online-physiotherapy/","Online Physiotherapy | Ann Physiocare","Online Physiotherapy",("Services","/services/"),
 "Learn from highly qualified physiotherapists from the comfort of your home or office.",
 f"""<h2>Online Physiotherapy</h2>
<p>Don't worry if you're unable to physically reach our clinics with your busy working schedules. At AnnPhysiocare, we provide Online Physiotherapy allowing you to learn from some of our highly qualified physiotherapists right from the comfort of your home or office.It is ideal for people with mobility issues, childcare obligations, demanding work schedules, elderly and job-related.<br>Are you wondering how it works without hands-on treatment. Many fractures and musculoskeletal problems require sticking to regular exercises and clinical advice regarding lifestyle maintenance. All this can be quickly done through a simple online consultation.</p>
<p>For several years, both the NHS and the private sector have used online consultations in healthcare, including physiotherapy. It is an efficient form of physiotherapy delivery. We are here to help you achieve your goals whether you need an evaluation of a new injury, an analysis of how you are recovering with an old injury, or proceeding with your rehabilitation.</p>
{media('service-online.webp','Video consultation','video')}
<h3>Advantages of Online Physiotherapy</h3>
<p>Why make tiresome and inconvenient visits to physical clinics when at-home physiotherapy has several advantages and covers many physical interventions? Online Physiotherapy allows for the following:</p>
{checks(["Allows for comfort","Provides individualised services","Allows treatments to be carried out in familiar surroundings","There are no problems with mobility","Budget-friendly","Time management","Sessions conducted by expert, senior therapists","Standing/waiting in the queues eliminated"])}
<p>It is also known to increase the rate at which people recover.</p>
<h3>What if a condition can't be treated online?</h3>
<p>We recommend a more appropriate course of action if we discover during the initial assessment examination that your condition needs a different approach than online physiotherapy, we will make appropriate suggestions to plan your visits.</p>
<h3>What problems can be addressed through Online Physiotherapy?</h3>
<p>While some of the physiotherapy interventions require special attention, care and equipment, most common problems don't necessarily physically involve visiting our clinics. Some of the issues that can be addressed through Online Physiotherapy are:</p>
{pills(["Lower Back Pain","Knee Pain","Bell's Palsy","Hemiplegia","Shoulder Pain","Recovering from Bone Fractures","Any Musculoskeletal Injuries","Accident-Related Recoveries","Post-Surgery Rehabilitation and Many More."])}
<h3>Consult Us</h3>
<p>Here at Annphysiocare, one of our physiotherapists will conduct your consultation over a safe network using a private video call. To meet your needs, we use a range of online channels via Skype, Zoom and Whatsapp. We conduct 30-mins to 1-hour sessions at affordable prices. All you require is a smartphone, tablet, laptop or desktop computer that has a camera, microphone and speakers, headset or earphones.<br>Our systematic assessment, evaluation, and treatment plans give you the full experience of our physical clinic. We will provide you with tips and exercises to help you manage your injury to manage your pain and restore you to former lifestyle.</p>""",
 SERVICES_NAV,"","","video")

P["/home-physiotherapy/"] = detail_page("/home-physiotherapy/","Home Physiotherapy | Ann Physiocare","Home Visit Physiotherapy",("Services","/services/"),
 "Expert physiotherapy at your home — the same high quality treatment you would receive in the clinic.",
 f"""<h2>Home Physiotherapy</h2>
<p>If you're an elderly patient, have mobility problems, or if you're Housebound, Home Physiotherapy i.e. Physiotherapy conducted at your home is an ideal alternative for you. We at AnnPhysiocare offer Home Physiotherapy sessions guided by our expert physiotherapists, at your convenience and at affordable costs.</p>
<h2>What is Physiotherapy?</h2>
<p>Physiotherapy is an allied health speciality that uses biomechanics and anatomical structure of the body in applying manual and exercise therapy as well as various other techniques. These can be physically applied to the body for regaining, maintaining and improving its physical mobility, strength, and actvity.</p>
{media('service-home.webp','At your home','home')}
<p>Since they have a greater understanding of how the body functions, as they go through complete training and practice and are qualified in therapeutic skills to evaluate, diagnose and manage injuries, physiotherapists are better equipped to assist patients in regaining mobility.</p>
<h3>Physiotherapy helps relieve the patients from:</h3>
{checks(["Bone Fractures, Osteoporosis, and Osteoarthritis","Joint Issues","Injuries To The Spine","Sports-Related Accidents","Cerebral Palsy in Children","Helping Children Reach Their Developmental Milestones","Disorders Of The Nervous System","Soft Tissue Mobilization","Relieving Muscle Stiffness."])}
<h3>Home Physiotherapy</h3>
<p>Physiotherapy at home is very common these days and is sometimes more effective than clinical physiotherapy and has several advantages associated with it. With Home Physiotherapy, a physiotherapist will come to your home to diagnose and provide treatment. From discussing various topics surrounding the patient's wellbeing and recovery goals to the actual physiotherapy treatment methods.</p>
<p>There are many benefits to receving physiotherapy at your home.<br>It saves money associated with travelling. Some problems might require immediate attention and you may have to travel to the clinic. Having physiotherapy at home saves a lot of time and its management.<br>It enables personalized and comfortable treatment at your home. Home physiotherapy enables the therapist to spend more time with the patient to provide the one-to-one treatment and the benefits associated with it. Receiving physiotherapy at home means being in the safety and comfort of familiar surroundings. It boosts the morale of patients and speeds up the recovery process.</p>
<p>Except where certain physiotherapy treatments require necessary infrastructure and customized space, when commuting to clinics can not be avoided, Home physiotherapy is ideal for people who are housebound by illnesses, elderly people, people with mobility issues and for anyone in general who requires it.</p>
<h3>Consult Us</h3>
<p>At AnnPhysiocare, we have the best physiotherapists who have extensive experience in helping patients with chronic physical conditions come out of their situations and lead a happy and active life again. Book our physiotherapist for your home physiotherapy sessions today and we ensure your speedy recovery!</p>""",
 SERVICES_NAV,"","","home")

P["/functional-capacity-evaluation/"] = detail_page("/functional-capacity-evaluation/","Functional Capacity Evaluation | Occupational Health | Ann Physiocare","Functional Capacity Evaluation",("Services","/services/"),
 "A physical ability assessment that evaluates an individual's ability to perform specific work-related tasks.",
 f"""<h2>Functional Capacity Evaluation</h2>
<p>A Functional Capacity Evaluation (FCE) is a type of physical ability assessment that is used to evaluate an individual's ability to perform specific work-related tasks. The evaluation is typically performed by a trained healthcare professional, such as a physiotherapist, and can be used to assess an individual's ability to return to work after an injury or illness, or to determine their physical capabilities in the context of a job.</p>
<p>The FCE may also include an assessment of the individual's functional limitations, such as pain or reduced mobility, which may impact their ability to perform certain tasks. The results of the evaluation can be used to develop a plan for rehabilitation or to determine if the individual is fit to return to work. The information gathered from an FCE can also be used to help employers develop appropriate job descriptions and accommodations for employees with disabilities or other physical limitations.</p>
{media('service-fce.webp','Return-to-work assessment','clip')}
<h2>How a Functional Capacity Evaluation (FCE) works?</h2>
<ol class="steps">
<li><strong>Referral and Intake:</strong> The FCE is usually initiated by a healthcare provider, insurance company, or employer, who refers the individual to a qualified evaluator. The evaluator will conduct an intake assessment to gather information about the individual's medical history, injury or illness, job duties, and any other relevant information.</li>
<li><strong>Functional Limitations Assessment:</strong> The evaluator will also assess any functional limitations that may impact the individual's ability to perform certain tasks. This may include a pain assessment or an evaluation of the individual's mobility.</li>
<li><strong>Evaluation:</strong> The FCE typically consists of a series of physical tests and exercises designed to measure the individual's strength, range of motion, endurance, and other physical abilities. The tests will be specific to the individual's job requirements and may include tasks such as lifting, carrying, pushing, pulling, and repetitive movements, as well as balance and coordination exercises.</li>
<li><strong>Report and Recommendations:</strong> Following the evaluation, the evaluator will provide a report detailing the individual's physical abilities and any functional limitations that were identified. The report may also include recommendations for rehabilitation, job accommodations, or modifications to the individual's job duties to ensure their safety and ability to perform the required tasks.</li></ol>
<h2>Potential benefits of having a Functional Capacity Evaluation (FCE) Assessment:</h2>
{checks(["<strong>Accurate Assessment of Physical Abilities:</strong> An FCE is a comprehensive evaluation that assesses an individual's physical abilities in the context of their job requirements. This provides a detailed and accurate picture of the individual's capacity to perform specific tasks, which can help ensure that they are able to return to work safely and without risk of further injury or harm.","<strong>Tailored Rehabilitation Programs:</strong> The information gathered from an FCE can be used to develop a tailored rehabilitation program that is specific to the individual's physical capabilities and limitations. This can help ensure that the rehabilitation program is effective and targets the areas that need improvement.","<strong>Return-to-Work Planning:</strong> An FCE can be used to develop a plan for returning an individual to work, including identifying appropriate job duties and accommodations that will allow the individual to perform their job safely and effectively.","<strong>Objective Information for Employers:</strong> An FCE provides objective information about an individual's physical abilities and any functional limitations, which can assist employers in making informed decisions about job requirements and accommodations.","<strong>Reduced Risk of Injury:</strong> By ensuring that an individual is able to perform their job duties safely and without risk of further injury or harm, an FCE can help reduce the risk of workplace injuries and improve workplace safety."])}
<h3>Interested?</h3>
<p>We'd love to hear from you! If you're interested in discussing how our Functional Capacity Evaluations can benefit your business, get in touch with our friendly team.<br><strong>Call Us On {PHONE}. or start a Live Chat (9am-5pm)</strong>.</p>""",
 SERVICES_NAV,"","","clip",testimonials_on=True)

P["/dse-assessments/"] = detail_page("/dse-assessments/","DSE Assessments | Occupational Health | Ann Physiocare","Display Screen Equipment (DSE) Assessments",("Services","/services/"),
 "Identify and minimise health risks associated with the use of display screen equipment.",
 f"""<h2>DSE Assessments</h2>
<p>DSE (Display Screen Equipment) Assessment is a type of assessment that aims to identify and minimize potential health risks associated with the use of display screen equipment, such as computer screens, laptops, tablets, and smartphones.</p>
<p>The assessment involves a trained assessor who evaluates the workstation, including the desk, chair, monitor, keyboard, and mouse, to ensure that they are set up correctly to promote good posture and reduce the risk of musculoskeletal disorders. The assessor will also consider environmental factors such as lighting, noise, and temperature, which may affect the user's comfort and productivity.</p>
{media('service-dse.webp','Ergonomic workstation','monitor')}
<h2>How Display Screen Equipment (DSE) Assessment Works?</h2>
<ol class="steps">
<li><strong>Identify Employees in Need of Assessment:</strong> Employers can identify employees who regularly use DSE, such as computers, laptops, and other electronic devices, and determine who may be at risk for developing musculoskeletal disorders. These employees can then be scheduled for a DSE assessment.</li>
<li><strong>On-Site Assessment:</strong> A qualified assessor will visit the employee's workstation to conduct a thorough evaluation of the workstation and how it is being used. The assessor will typically use a checklist or questionnaire to assess the workstation and the employee's working posture.</li>
<li><strong>Evaluation of Risk Factors:</strong> The assessor will identify risk factors, such as awkward postures, excessive reaching, and poor workstation setup, that may contribute to musculoskeletal disorders. They will also evaluate the employee's posture, the position of the monitor, keyboard and mouse, and lighting, among other factors.</li>
<li><strong>Recommendations:</strong> The assessor will provide recommendations to address the identified risks and make the workstation more ergonomic. This may include changes to the workstation layout, such as adjusting the height of the desk or monitor, and providing ergonomic accessories, such as an ergonomic chair, keyboard or mouse. Recommendations may also include guidance on taking breaks and adjusting the workspace during the workday.</li>
<li><strong>Follow-Up:</strong> It is important to follow up with employees to ensure that the recommended changes are implemented and effective. The assessor may provide guidance on how to maintain good posture and proper use of the workstation to minimize the risk of developing musculoskeletal disorders.</li></ol>
<h2>Potential benefits of having a Display Screen Equipment (DSE) Assessment:</h2>
{checks(["<strong>Reduced Risk of Musculoskeletal Disorders:</strong> A DSE assessment can help identify ergonomic issues with workstations and recommend changes to reduce the risk of musculoskeletal disorders such as back pain, neck pain, and repetitive strain injuries.","<strong>Improved Productivity:</strong> An ergonomic workstation can help employees work more comfortably and efficiently, reducing fatigue and discomfort that can lead to decreased productivity.","<strong>Compliance with Health and Safety Regulations:</strong> Employers have a legal obligation to ensure that workstations meet health and safety regulations. A DSE assessment can help ensure compliance with these regulations and reduce the risk of liability for workplace injuries.","<strong>Employee Satisfaction and Retention:</strong> An FCE provides objective information about an individual's physical abilities and any functional limitations, which can assist employers in making informed decisions about job requirements and accommodations.","<strong>Cost Savings:</strong> Implementing ergonomic changes based on a DSE assessment can help reduce the risk of workplace injuries and associated costs, such as workers' compensation claims and lost productivity."])}
<h3>Interested?</h3>
<p>We'd love to hear from you! If you're interested in discussing how our DSE Assessments can benefit your business, get in touch with our friendly team.<br><strong>Call Us On {PHONE}. or start a Live Chat (9am-5pm)</strong>.</p>""",
 SERVICES_NAV,"","","monitor",testimonials_on=True)

# ---------------- TREATMENTS ----------------
P["/acupuncture/"] = detail_page("/acupuncture/","Acupuncture | Ann Physiocare","Acupuncture",("Treatments","/treatments/"),
 "A physiotherapy technique that originated in traditional Chinese medicine, using very thin needles at specific points.",
 f"""<h2>Acupuncture</h2>
<p>Acupuncture is a physiotherapy technique that originated in traditional Chinese medicine. It involves addressing various physical illnesses by releasing specific "pressure points" of the body using very thin needles applied through the skin to different depths, thereby alleviating the associated stress, chronic pains and related conditions.</p>
<p>These pressure points that have been identified are usually dense with nerve endings. Stimulating these pressure points triggers the nerves to release endorphins, stimulating muscles, tissues and organs linked to them. Different physical illnesses and conditions are associated with varying points of pressure to heal in Acupuncture.</p>
{media('treat-acupuncture.webp','Fine-needle acupuncture','needle')}
<p>This process helps to clear any blocks in the flow of energy, restoring the natural activeness and balance. The needles are gently applied to a sufficient depth that's enough to stimulate the nerves.</p>
<h2>There is an interesting philosophy behind it.</h2>
<p>There is an interesting philosophy behind how the Chinese discovered this technique! The Chinese believed that our body is driven by a seamless flow of invisible 'qi' (pronounced chee) which is responsible for creating health and well-being. Any restriction caused to or non-flow of 'qi' is why any disease or illness happens.</p>
<p>Acupuncture seeks to release such blockages and facilitate the free flow of 'qi'. The Chinese discovered Acupuncture to interfere with the 'qi' and restore its flow to eliminate the illness. That's why it's been in practice for around 2500 years.</p>
<p>An enormous amount of scientific and medical research today identifies Acupuncture as a potential method to relieve many chronic conditions</p>
<h3>How is it done?</h3>
<p>An acupuncturist will first enquire you about your health history. About your lifestyle, medications, sleep, diet and other relevant information. After a thorough examination of your present appearance, specific parameters such as pulse, tongue etc., the Acupuncturist will set out an appropriate method to apply.</p>
<p>The practice isn't the same for all. Instead, it's applied to the individuals symptoms and needs.</p>
<p>Acupuncture uses sharp, sterile and single-use needles to apply on the body. Depending on the illness, various physical points on the body are identified by practitioners to perforate them with needles as required.</p>
<p>The needles are kept for about 10-20 minutes and the entire session lasts for approximately 30 mins. Some people might feel some slight discomfort. But everyone feels a significant benefit to their lifestyle after going through a complete Acupuncture treatment.</p>
<h3>When is it used?</h3>
<p>It's used to treat several illnesses presently, backed up by current research and could be used in the following cases:</p>
{pills(["Chronic Pains","Stress and Anxiety","Allergies","Joint Pains","Headaches and Migraines","Hypertension","Insomnia or Sleep-Related Disorders","Sprains","Strokes","Osteoarthritis","Depression and Mood-Related Illnesses"])}
<p>Acupuncture is known to be an effective method in the above cases. As the results appear promising, more research is being done to use it in many other conditions.</p>
<h3>What are the after-effects of Acupuncture?</h3>
<p>People who went through Acupuncture would immediately see results and experience a new surge of energy and rejuvenation in them. Some may experience a calmness entering their lives.</p>
<p>On a positive note, those who have undergone Acupuncture might see changes in their food habits, sleep habits, bowel habits and activity levels.</p>
<h3>How to find an Acupuncturist?</h3>
<p>The best way to find an Acupuncturist is through referrals from reliable resources. Every Acupuncturist has a different approach. So go forward to ask as many questions and doubts as you feel the need for because it's essential that one feels comfortable with their respective Acupuncturist. A good Acupuncturist is certified by Acupuncture Association of Chartered Physiotherapist (AACP).</p>
<p><em>Please note Acupuncture is available only in some locations.</em></p>""",
 TREAT_NAV,"","","needle")

P["/electrotherapy/"] = detail_page("/electrotherapy/","Electrotherapy | AnnPhysiocare","Electrotherapy",("Treatments","/treatments/"),
 "Using electrical energy to stimulate the nervous system for pain relief, muscle activity and circulation.",
 f"""<h2>Electrotherapy Physiotherapy</h2>
<p>Using electrical energy in medical healing and treatment of our body has been known since ancient times. It has been observed that the human nervous system is sustained through electrical signals that are responsible for all bodily activities.<br>Electrotherapy simply involves external intervention in targeted areas of the body to stimulate the nervous system through the use of current towards achieving various muscle activities, tissue activities, pain relief, blood circulation etc.</p>
<p>Usually, Electrotherapy is performed by experienced practitioners in combination with other medications or exercises to achieve the best possible results. Electrotherapy is a minimally invasive method that uses battery-powered devices, wires and adhesive pads that are applied to the skin to deliver small signals of electrical energy. It involves no pain and the patient undergoes deep relaxation. Sometimes, a slight tingling and/or vibration may be experienced.</p>
{media('treat-electro.webp','Electrotherapy session','bolt')}
<p>There's not much scientific research and literature on what kind of problems can be treated using Electrotherapy but it is increasingly being used as an alternative to medicine in alleviating pains and causing relaxation.</p>
<h2>How does Electrotherapy work?</h2>
<p>Electrotherapy works by interfering with pain triggering nerve signals. It stimulates the release of endorphins that cause a soothing feeling, stimulates the muscle tissues to induce relaxation and increased blood circulation.</p>
<h2>When is it used?</h2>
<p>It's used in the following cases:</p>
{pills(["Nerve Pains","Muscle Pains and Spasms","People Going Through Exercise Therapies","Arthritis","Healing Wounds","Muscle Atrophy","Increase in Blood Circulation"])}
<h2>Types of Electrotherapy?</h2>
{checks(["Transcutaneous Electrical Nerve Stimulation (T.E.N.S.)","Percutaneous Electrical Nerve Stimulation (P.E.N.S.)","Electrical Muscle Stimulation (E.M.S.)","Low-Intensity Pulsed Ultrasound (L.I.P.U.S.)"])}
<p>The type of Electrotherapy prescribed is different for patients as it depends on their physical and medical conditions and the core problem they're facing.</p>
<h3>Transcutaneous Electrical Nerve Stimulation (TENS)</h3>
<p>Transcutaneous Electrical nerve stimulation is the most popular method used in case of alleviating pains. It's the best alternative to the use of medications and is simple in the method. It involves equipment that patients can carry in their hands that can be covered by regular clothing. The frequency and intensity can be modulated to create relaxation in the targeted area of the body.</p>
<p>It's mainly used to for</p>{ul(["Chronic Pains","Acute Pains Resulting from Severe Injuries","Lower Back Pain","Knee and Joint Pains","Arthritis etc."])}
<h3>Percutaneous Electrical Nerve Stimulation (P.E.N.S.)</h3>
<p>It's used as an alternative when T.E.N.S. doesn't work and involves similar equipment to generate current. But this method uses needles to penetrate deeper into the skin to reduce muscle spasms and reduce pain. Every patient's response is different, and it may involve multiple sessions for some before seeing a significant change.</p>
<h3>Electrical Muscular Stimulation (E.M.S.)</h3>
<p>It is mainly used for muscle contraction to strengthen the weak muscles and relieve intense pain by stimulating the surrounding nerves. Usually, it involves relatively high currents that are equal to the necessary nervous stimulation.</p>
<h3>Low-Intensity Pulsed Ultrasound (L.I.P.U.S.)</h3>
<p>It's used for bone repair and fracture healing. It involves using ultrasound waves to pass through the body tissues to trigger the natural healing process and thereby helping the speedy recovery of fractured bones.<br>Many other types of Electrotherapy are used in various problems, such as Pulsed Shortwave Diathermy (P.S.W.D.), Functional Electrical Stimulation (F.E.S.), Ultrasound Electrotherapy, Interferential electrotherapy, and Laser electrotherapy. Electrotherapy is gaining popularity as a zero-invasive method, and it can be used where medications may not help relieve patients of severe pain.</p>""",
 TREAT_NAV,"","","bolt")

P["/massage-physiotherapy/"] = detail_page("/massage-physiotherapy/","Massage Physiotherapy | AnnPhysiocare","Massage Physiotherapy",("Treatments","/treatments/"),
 "Individualised massage for relaxation, pain relief and blood circulation.",
 f"""<h2>Massage Physiotherapy</h2>
<p>Massage is a technique that involves physical manipulation of various body parts, muscles, tissues, ligaments, tendons to achieve mainly relaxation, pain relief and blood circulation. It consists of physical hands and fingers to apply the right amount of pressure and speed in achieving the desired effect. Those who perform massages are professionally known as a masseur.</p>
{media('treat-massage.webp','Therapeutic massage','hand')}
<p>A massage is entirely harmless and anyone, medically ill or not, can choose to go through a regular massage session as it only involves positive outcomes. It involves various techniques and their combinations that masseurs are experts in and can be used in cases of:</p>
{checks(["Alleviating chronic and acute pain conditions","Eliminating stress resulting from occupational pressures","Insomnia","Depression and anxiety as Massage helps the release of serotonin and dopamine","Headaches and tension","Improving blood circulation and eliminate waste toxins","Muscular discomfort and pain","Loosening muscle stiffness","Skin toning","Release of oedema and swelling"])}
<p>And many more conditions.</p>
<p><strong>Effleurage:</strong> The word Effleurage is derived from a French word that means 'to skim'. This uses stroking and spreading the hands in the direction of the heart to improve circulation. It uses the palms and wide areas of the hands and fingers.</p>
<p>In <strong>stroking</strong>, relaxed hands and fingers are applied in the client's body in a rhythm and appropriate pressure.</p>
<p>In <strong>spreading</strong>, hands and fingers are extended and moved on the body with the right pressure and speed to achieve relaxation and lymph drainage.</p>
<h4>When is it used?</h4>{ul(["To prepare the client with the touch and make them feel easy","Relax muscles","To increase blood and lymph circulation to drain them"])}
<h4>Petrissage</h4>
<p>This involves kneading in which the targeted body areas compressed, picked up, squeezed and released alternatively. It is used for a more significant effect and generally improves circulation.<br>The techniques petrissage includes are</p>
<p><strong>Picking up:</strong> Deep body tissues are picked up, squeezed and released.</p>
<p><strong>Wringing:</strong> Picked up tissues and twisted to improve the effect.</p>
<p><strong>Shaking and Vibration:</strong> Gentle shakes and vibrations of the body.</p>
<h4>Other techniques are:</h4>
<p><strong>Hacking:</strong> It involves the use of the forearm to strike the body.</p>
<p><strong>Friction:</strong> Thumb and hand fingers are used in targeted areas with gentle to high pressure.</p>
<p><strong>Clapping:</strong> Cupped hands are used to give strokes on the body.</p>
<h4>Trigger point therapy</h4>
<p>Trigger points are in line with acupuncture points but are centres of intense muscular activity. Trigger point therapy involves applying appropriate pressure in these centres to relieve the pain of body parts connected to them.</p>
<p>We offer individualized massages that are customized to fit your specific needs. Our experienced professional massage therapist may use one or more of the following massage techniques based on your personal needs and preferences: Deep tissue massage to loosen knots, release chronic muscle tension, reduce inflammation, and help eliminate scar tissue.</p>
<p>Sports-specific massage for athletes of every discipline and level, to promote flexibility, reduce fatigue, improve endurance, maximize performance, and prevent injuries. Therapeutic massage sessions offer many benefits.</p>""",
 TREAT_NAV,"","","hand")

P["/exercise-programme-physiotherapy/"] = detail_page("/exercise-programme-physiotherapy/","Home Exercise Programme Physiotherapy | Ann Physiocare","Exercise Programme (HEP) Physiotherapy",("Treatments","/treatments/"),
 "The most popular and effective method to correct body impairments and restore and maintain balance of the body.",
 f"""<h2>Exercise Programme (HEP) Physiotherapy</h2>
<p>Exercise in Physiotherapy is the most popular and effective method to correct body impairments, enhance muscular and skeletal functionality, reduce health risks, help restore and maintain the balance of the body in patients, elderly and adults with motor problems, to train the body to work at higher levels and for general well-being. Although they involve physical activity, exercises are different from physical activity as they're a systematic approach to improve physical fitness.</p>
{media('treat-exercise.webp','Guided rehabilitation','run')}
<p>According to WHO, adults between 18-64 age</p>
<blockquote>"should do at least 15-30 minutes of moderate-intensity aerobic physical activity per day or an equivalent combination of moderate to vigorous intensity activity throughout the week to maintain a healthy lifestyle. Moderate exercise is recommended for the elderly and people recovering from injuries and people with neurological conditions. There's ample scientific research about what a regular exercise regimen can do in maintaining good health.</blockquote>
<p>Exercise is essential to recovery from sports injuries, following surgery, after an acute trauma such as from a fall or fracture, in the management of acute and chronic low back pain, neck pain and headaches and in the treatment of long term conditions such as arthritis and osteoporosis.</p>
<h2>Where is it used?</h2>
<p>Therapeutic exercises are targeted exercises prescribed in different needs and achieving specific fitness goals for the patient. These may involve:</p>
{pills(["Stretching Exercises","Coordination Exercises","Strengthening Exercises","Musculoskeletal Exercises","Breathing Exercises","Balance Exercises","Endurance Conditioning and Reconditioning","Agility Exercises","Neuromuscular Training"])}
<h3>Types</h3>
<p>Therapeutic exercises are broadly categorised into many groups and each one uses external equipment to support them. Some of the popular ones are:</p>
{checks(["Strengthening Exercises","Range of Motion Exercises","Aerobic Exercises","Balance Exercises","Breathing Exercises","Aquatic Exercises","Relaxation Exercises"])}
<h3>Strengthening Exercises</h3><p>These are used for muscle strengthening. Muscles are loaded until fatigue. Resistance bands, weights and tubes are used.</p>
<h3>Range of Motion Exercises</h3><p>These are used to increase the range of joint movement and maintenance. Wand, pulley, t-bar, power board, skateboard etc.</p>
<h3>Aerobic Exercises</h3><p>These are used for the conditioning phase of the exercise program. Usually, the intensity of exercises is increased in this phase. Patients must inform their endurance levels here and discuss openly with the therapist.</p>
<h3>Balance Exercises</h3><p>Adults with motor issues, older adults with neurological problems need balance training to keep up their body's centre of gravity. It helps reduce falling. These involve standing on one leg with eyes closed or open, tiptoeing, standing on the heels etc.</p>
<h3>Breathing Exercises</h3><p>These involve assuming a comfortable posture, inhalation through the nose and exhalation through the mouth.</p>
<h3>Aquatic Exercises</h3><p>These are done in pools. There is a minimum risk of injury in aquatic exercises, and the water helps in increased relaxation. Various stretchings and movements are possible in the water and equipment like collars, rings, floating belts, swimming bars and hand paddles would be used.</p>
<h3>Relaxation Exercises</h3><p>Deep breathing techniques, pranayama, meditation and yoga techniques are used in this type of exercises.</p>
<h3>Safety and Cautions</h3><p>These exercises should always be done in the presence of an experienced therapist as patients who need exercise therapy are not used to intense physical exertion, which may lead to injuries. The equipment used should be checked whether they're in proper condition and safe to use. A therapist will always enquire about a patient's past, lifestyle, medical and health history and any present medications. Older adults, people with heart problems need special attention. People on certain medicines experience imbalance which also needs special care. In any case, patients should be aware of their tolerance limits and be open with their therapist for successful exercise physiotherapy and experience.</p>
<h3>Lack of Physical Exercise</h3><p>Risks of not exercising are obesity, fatigue, joint pains, cardiovascular risks, muscle and bone weakening, increased risk of various types of cancers and many health issues are possible. Maintaining a good exercise regimen is recommended for growing children and adults alike.</p>""",
 TREAT_NAV,"","","run")

P["/shockwave-therapy/"] = detail_page("/shockwave-therapy/","Shockwave Therapy | Ann Physiocare","Shockwave Therapy",("Treatments","/treatments/"),
 "Effective treatment of chronic pain associated with inflammation and degeneration of tendons, ligaments, muscles and bones.",
 f"""<h2>Shockwave Therapy</h2>
<p>Shockwave Therapy device enables effective treatment of chronic pain associated with chronic inflammation and degeneration of tendons, joint capsules, ligaments, muscles and bones. It is also a great support in the therapy of trigger points, i.e. particularly sensitive places characterised by increased tension, which can generate radiating pain. The positive effects allow to stop taking painkillers, and often avoid having to undergo surgery.</p>
<p>The therapy is being used to treat issues such as, but not limited to:</p>
{checks(["Muscle tension, trigger points","Plantar fasciitis","Patellar tendonitis – jumper’s knee","Inflammation of the lateral epicondyle of the humeral – tennis / golfer’s elbow","Painful shoulder syndrome","Inflammation and Achilles tendon pain","Calcaneal spur (lower and upper)","Anterior tibial syndrome","Iliotibial band syndrome","Overload and degenerative changes","Trochanteric bursitis","Tendinopathies and rotator cuff injury – tendon lesions","Chronic enthesopathies"])}
{media('treat-shockwave.webp','Shockwave device','wave')}
<h4>How does it work?</h4>
<p>During shockwave therapy, impulses are generated which frequency may affect the patient’s comfort during the treatment. The pulse frequency range from 1 to 25 Hz allows to increase patient comfort without losing the therapeutic properties of the treatment.</p>
<p>During the treatment, the device’s gun-shaped applicator transmits an average of 4,000 shocks, depending on the type of injury. The effectiveness of shockwave therapy has been clinically confirmed. Therapeutic treatments related to the penetration of tissues by the shockwave bring benefits in the form of:</p>
{checks(["better tissue blood supply","reduced muscle tone","anti-inflammatory and analgesic effect","tissue regeneration","disintegration of calcifications"])}
<h2>What to expect?</h2>
<p>Treatment can be uncomfortable but tolerable. Usually 3-4 treatments carried out at an interval of one week allow to achieve the desired effect of therapy. Importantly, the therapeutic results are long-lasting, and the treatment itself does not require anaesthesia. It is a quick therapy without side effects. The application of physiotherapy treatments using shockwaves often consents to avoid surgical intervention. Shockwave therapy is a completely safe, but extremely effective treatment used in orthopaedics, rehabilitation, sports and aesthetic medicine. The therapeutic session lasts about 15-20 minutes.</p>
<h2>Pricing</h2>
<div class="tbl-wrap"><table><tr><td>Initial Assessment</td><td>£80</td></tr><tr><td>Following treatment session</td><td>£60</td></tr></table></div>
<p><strong>Ann Physiocare’s “Astar Impactis M+” is leading edge machine in the world of Shockwave Therapy.</strong></p>
<p><em>Please note Shockwave is available only in some locations.</em></p>""",
 TREAT_NAV,"","","wave")

P["/soft-tissue-mobilisation-physiotherapy/"] = detail_page("/soft-tissue-mobilisation-physiotherapy/","Soft Tissue Mobilisation Physiotherapy | AnnPhysiocare","Soft Tissue Mobilisation Physiotherapy",("Treatments","/treatments/"),
 "Hands-on techniques that break down adhesions and improve muscle function.",
 f"""<h2>Soft Tissue Mobilisation Physiotherapy</h2>
<p>Whenever there is an accident-related injury or muscular wound, muscles induce a long-term inflammatory response that results in long strands of collagenous scar tissue to heal the soft tissue injury. These new tissues pull against each other, creating centres for triggering pain. These are known as Adhesions. In Soft Tissue Mobilisation Therapy (STMT), an expert physiotherapist applies his hands in various pressures and speeds to your muscles, ligaments and fascial muscles to severe adhesions and improve muscle function.</p>
<p>Our physiotherapists are uniquely trained to use their hands to precisely manipulate soft tissues via muscles, tendons, ligaments and linked nerves to relieve pain and restore functionality. It also improves the mobility and stiffenes associated with muscles, blood circulation in less active areas. Soft tissue mobilisation methods requires extensive training for therapists in human anatomy and physiology and an understanding of how manipulating tissues changes physical function.</p>
{media('treat-stm.webp','Soft tissue technique','hand')}
<h3>Is it massage therapy?</h3>
<p>STM appears like massage therapy. But we offer massage therapy as part of Soft Tissue Mobilisation if required. Massage therapy doesn't serve any longer-term benefit in aiding the primary purpose. Instead, home workout and self-caring interventions are advised over massage therapy.</p>
<h3>What are the benefits?</h3><p>STM therapy seeks to bring the following benefits:</p>
{checks(["Adhesions must be broken down or reduced.","Increase your range of motion.","Muscles and tendons should be lengthened.","Reduce oedema and swelling.","Reduce pain and regain functionality","Release associated tension to increase the flexibility of muscles"])}
<h3>What conditions do we address?</h3>
<p>Through Soft Tissue Mobilisation (STM), we promise a solution to many health conditions involving muscles or other soft tissues. The following offers a glimpse:</p>
{pills(["Muscle Injuries Due To Accidents or Sports","Muscular Spasms","Muscles and Tendons Should Be Lengthened.","Muscular Sprains and Stiffness","Carpal Tunnel Syndrome","Contractures","Arthritis","Scar Tissue","Whiplash","Sciatica","Fibromyalgia","Joint Mobilisation","Neck pain","Plantar Fasciitis","Myofascial Pain and Restrictions","Chronic Ankle Sprains"])}
<h3>What techniques do we use?</h3>
<p>We have facilities and physiotherapists for both manual and instrument-based STM therapies. In manual therapy, we use unlocking spiral, direct oscillations, sustained pressure, perpendicular and parallel mobilisation and even friction massage to treat. We're experts in using instrument-based therapy as well. We have expert physiotherapists and infrastructure to support our patients in all possible conditions. It's generally used where manual intervention is complex. The ergonomic nature of these instruments, made up of stainless steel with unique contours in line with the body's anatomical shapes help the therapist to identify constraints and apply the required amount of pressure to the affected region.</p>
<h3>How to make the best use of STM?</h3>
<p>To get the most out of your STM therapy, we encourage you to maintain regular discipline by doing home exercises, physical activity, checking on body weight and diet. If you don't know whether to take up STM for your problem, we're here to help.</p>""",
 TREAT_NAV,"","","hand",testimonials_on=True)

P["/manipulation-and-mobilization-physiotherapy/"] = detail_page("/manipulation-and-mobilization-physiotherapy/","Manipulation and Mobilisation Physiotherapy | AnnPhysiocare","Manipulation and Mobilisation Physiotherapy",("Treatments","/treatments/"),
 "Manual interventions to alleviate joint stiffness and pain.",
 f"""<h2>Manipulation and Mobilisation Physiotherapy</h2>
<p>Are you feeling joint stiffness or pains? Then manipulation and Mobilisation could be the right option for your condition. We at AnnPhysiocare have the best and most experienced practitioners to take care of these issues in a simple way.</p>
<h2>What is Mobilisation and Manipulation?</h2>
<p>Both Manipulation and Mobilisation are manual interventions performed by a trained practitioner to alleviate pains and stiffness due to an injury or illness. It increases the range of movement of soft tissues via muscles, tendons, ligaments, nerves and bone joints - mainly in the neck region or upper and lower spinal region. However, it can be applied in case of any other joint pain.</p>
{media('treat-manipulation.webp','Joint mobilisation','bone')}
<p>The patient is made to lie in a relaxed posture and this allows the therapist to get hold of joints and perform any required movement. It's essentially achieving an activity that the patient cannot do themselves.</p>
<h2>What's the difference between the two techniques?</h2>
<p>Manipulation is swift, accurate and impulsive movement of a joint, going slightly beyond its range of motion, to relieve the reciprocal of its stiffness and lack of movement. It's characterized by a 'pop' sound known to be a result of cavitation of synovial fluids between the joints. Its also known as chiropractic adjustment.<br>It immediately results in pain relief due to the release of endorphins and increased flexibility.<br>Manipulation is a very speedy and sudden movement technique and requires great skill and experience from the therapists. Patients who choose to undergo manipulation must check thoroughly with their physicians and practitioners.</p>
<p>Mobilisation also involves affecting the joint movement, but it achieves the same with slow, smooth and repetitive movements. The movement covers the full range of the joint motion based on their grade and joints are fully stretched out.<br>The range of motion of each joint is graded on a five-point scale. Grades I and II are mostly used to alleviate discomfort and stiffness. Grades III–V are mainly used to improve mobility and joint flexibility.<br>Mobilisation is safer, and it allows the patient to ask for stopping it in the middle. It's ideal for elderly patients whose bones and joints are more fragile.</p>
<h3>Where do we use it?</h3>
<p>We use manipulation and Mobilisation as efficient techniques to relieve many joint pains. But we mainly use them in cases of:</p>
{checks(["Lower Back Pain","Upper Back Pain","Neck Pain","Joint Stiffness Involving","Shoulder, Spine, Elbow, Wrist, Hip, Ankle, Knee and Foot","Muscular Sprains"])}
<h2>Precautions</h2><p>These techniques are best avoided in the following cases:</p>
{checks(["Osteoporosis or Osteoarthritis","Bleeding joints","If there's is a total joint replacement","If the joint area has any malignant tumours.","Without the full diagnosis"])}
<h3>Consult Us</h3>
<p>AnnPhysiocare offers the best care and physiotherapy for your joint-related problems. We will provide you with after-treatment guidance for your successful recovery. Contact us for more details.</p>""",
 TREAT_NAV,"","","bone")
