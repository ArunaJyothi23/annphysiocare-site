# (display name, address, original slug on annphysiocare.com/physiotherapy/<slug>)
RAW = [
("Leicester","Leatherline House Business Centre - 24 71 Narrow Ln, Aylestone, Leicester, LE2 8NA","leicester"),
("Northampton","KB Therapy Clinic, 16-18 Stenson Street, Northampton, NN5 5ED","northampton"),
("Wellingborough","10B Strode Road, Wellingborough, NN8 1JE","wellingborough"),
("Gloucester","Acorn Dental Surgery, 146A Barnwood Road, Gloucester, GL4 3JT","gloucester"),
("Luton","Johnston's chiropodists & podiatrists, 23A Upper George St, Luton, LU1 2RD","luton"),
("Berkhamsted","H H Dickman Chemist, 224 High St, Berkhamsted, HP4 1BB","berkhamsted"),
("Swindon","Basepoint Westlea, Office 54, 2nd floor, Rivermead Dr, Westlea, Swindon, SN5 7EX","swindon"),
("St Albans","Riverside House, 1-5 High Street, London Colney, AL2 1RE","st-albens"),
("Watford","William Penn Leisure Centre, Shepherds Ln, Mill End, Rickmansworth, Watford, WD3 3HD","watford"),
("Reading - Chatham Place","Hotpod Yoga Reading, 2-4 Chatham Pl, Reading, RG1 7AR","reading-chatham-street"),
("Burnham","Chiltern House Business Centre, Eton Place, 64 High Street, Burnham, SL1 7JT","burnham"),
("Reading","Reading Health Centre, 61 Castle St, Reading, RG1 7SN","reading"),
("Chippenham","Regus, Room 5, Unit A1, Methuen Park, Corsham, Chippenham, SN14 0GT","chippenham"),
("Reading - Thatcham","Suite 8 Thatcham House, Turners Drive, Thatcham, Berkshire, RG19 4QD","reading-thatcham"),
("Yate - Bristol","Anytime Fitness, 17 East Walk, Yate Shopping Centre, Yate, Bristol, BS37 4AP","yate"),
("Reading - Woodley","Room 4, Synegis House Serviced Offices, Crockhamwell Rd, Woodley, Reading, RG5 3LE","reading-woodley"),
("Reading - Green Park","Regus, 200 Brook Drive, Green Park, Reading, RG2 6UB","reading-berkshire"),
("Newbury","2 Essex Street, Newbury, RG14 6QN","reading-newbury"),
("Harrow","Revital Dental Care, Shaftesbury Circle, South Harrow, Harrow, HA2 0AJ","harrow"),
("Bristol - Staple Hill","Christchurch Family Medical Practice, North St, Bristol, BS16 5SG","bristol-staplehill"),
("Finchley","Balfour House, 741 High Road, North Finchley, London, N12 0BP","finchley"),
("Enfield","Nicholas House, River Front, Enfield, EN1 3TF","enfield"),
("Bolton","The Consulting Rooms, 32-36 Chorley New Road, Bolton, BL1 4AP","bolton"),
("Hounslow","Bhogal Pharmacy, 48 Vicarage Farm Rd, London, TW5 0AB","hounslow"),
("Harlesden","Smart Aesthetic, 787-789 Harrow Rd, Harlesden, London, NW10 5PA","harlesden"),
("Wood Green","Havergal Surgery, 9-10 Havergal Villas, Green Lanes, Duckett's Green, London, N15 3DY","enfield-woodgreen"),
("Bristol - Southville","First Floor, Monarch House, Room 16, 1-7 Smyth Rd, Southville, Bristol, BS3 2BX","bristol-southville"),
("Primrose Hill","The Primrose Hill Business Centre, Room B15, 110 Gloucester Ave, London, NW1 8HX","primrose-hill"),
("Chingford","Chingford Mount Dental Practice, 35 Hall Lane, Chingford, London, E4 8HH","chingford"),
("Highbury","DW Fitness First, Unit A, Eaststand Apartments, Avenell Road, Highbury Square, London, N5 1FE","highbury"),
("Walton-on-Thames","Walton Business Centre, Unit 26, 44-46 Terrace Road, Walton-on-Thames, KT12 2SA","waltononthames"),
("Newport","Axis Chiropractic, 77 Caerau Road, Newport, NP20 4HJ","newport"),
("Farnborough","North Camp Pharmacy, 39-41 Camp Rd, North Camp, Farnborough, GU14 6EN","farnborough"),
("Fulham","Anytime Fitness Fulham (Hurlingham), Peterborough Rd, London, SW6 3EF","fulham"),
("Whitechapel","Qmotion Sport and Fitness Centre, 15 Bancroft Rd, Bethnal Green, London, E1 4FZ","whitechapel"),
("East Ham","East Ham Podiatry and Physiotherapy, 15 Burges Rd, London, E6 2BJ","eastham"),
("Ilford - Gants Hill","Rose Opticians, 583 Cranbrook Road, Gants Hill, Ilford, IG2 6JZ","ilford-gants-hill"),
("Streatham","Palace Road Surgery, 1 Palace Road, Streatham, SW2 3DY","streatham"),
("Morden","Peel House, Suite 101D6, 4-44 London Road, Morden, SM4 5BT","morden"),
("Lewisham","Vesta Road Surgery, 58 Vesta Road, London, SE4 2NH","lewisham"),
("Merthyr Tydfil","Merthyr Chiropractic Clinic, Pontmorlais West, Merthyr Tydfil, CF47 8UU","merthyr-tydfil"),
("Ewell","Everlast Fitness, Banstead Rd, Ewell, Epsom, KT17 3HG","ewell"),
("Cardiff","Hill Crest Dental Practice, 866 Newport Road, Rumney, Cardiff, CF3 4LJ","cardiff"),
("Croydon","Airport House Business Centre, Purley Way, Croydon, CR0 0XZ","croydon"),
("Halstead","Nature Wellness Hub, 75 High Street, Halstead, CO9 2JB","halstead"),
("Weston-super-Mare","Suite 25, Pure Offices, Pastures Avenue, St Georges, Weston-super-Mare, BS22 7SB","weston-super-mare"),
("Chelmsford","1 Tindal Square, Chelmsford, CM1 1EH","chelmsford"),
("Welling","27 Two 6 Beauty Ltd, 11 Upper Wickham Ln, Welling, DA16 3AA","welling"),
("Salisbury","65 New Street, The Parade, Salisbury, SP1 2PH","salisbury"),
("Thurrock","Everlast Fitness Club, Thurrock Shopping Park, Unit 12, The Junction, Weston Ave, RM20 3LP","thurrock"),
("Orpington","Anytime Fitness, 313 High St, Orpington, BR6 0NN","orpington"),
("Basildon","Essex Beauty & Aesthetics, 69 Southernhay, Basildon, SS14 1EU","basildon"),
("Barry","Barry Therapy Centre, 1st Floor, 44 Holton Road, Barry, CF63 4HD","barry"),
("Southampton","Arena Business Centre, Threefield Lane, Southampton, SO14 3LP","southampton"),
("Bridgend","7 Dunraven Place, Bridgend, CF31 1JF","bridgend"),
("Neath","Room 2, 1 Charlesville Place, Neath, SA11 1PY","neath"),
("Crawley","The Ark, Mount Ln, Turners Hill, Crawley, RH10 4RA","crawley"),
("Tonbridge","Hilden Park Golf and Leisure Club, Rings Hill, Hildenborough, Tonbridge, TN11 8LX","tonbridge"),
("Swansea","Swansea Tennis Centre, Brunel Way, Pentre-chwyth, Bon-y-maen, Swansea, SA1 7DS","swansea"),
("Royal Tunbridge Wells","iBeautify, 76 Calverley Rd, Royal Tunbridge Wells, TN1 2UJ","royaltunbridgewells"),
("Sheerness","Fusion 2 Health and Aesthetics, 202 High Street, Sheerness, ME12 1UQ","sheerness"),
("Burgess Hill","Sussex Osteopathy, 7A Mill Road, Burgess Hill, RH15 8DN","burgesshill"),
("Maidstone","Coxheath Chiropractic & Natural Therapy Centre, 43 Stockett Lane, Coxheath, Maidstone, ME17 4PT","maidstone"),
("Minster Medical Centre","Sheppey Community Hospital, Plover Rd, Minster on Sea, ME12 3LT","minsteronsea"),
("Taunton","Wellspring Leisure Centre, Cheddon Rd, Taunton, TA2 7QP","taunton"),
("Worthing","Freedom Works - Creative & Digital Hub, Stoke Abbott Rd, Worthing, BN11 1HJ","worthing"),
("Sittingbourne","RevitaliseU-Kent, 62 Bell Rd, Sittingbourne, ME10 4HE","sittingbourne"),
("Llanelli","Business Sense Training Building, 4 Queen Victoria Road, Llanelli, SA15 2TL","llanelli"),
("Carmarthen","Aardvark Alternatives, 6 Lammas Street, Carmarthen, SA31 3AD","carmarthen"),
("Hove","Hove Osteopathic Clinic, 233 New Church Road, Hove, BN3 4EE","hove"),
("Brighton","Citibase Brighton (Shaftesbury Court), Suite G10, 95 Ditchling Rd, Brighton, BN1 4ST","brighton"),
("Faversham","Abbey Place Clinic, 5 The Chapel, Abbey Place, Faversham, ME13 7BG","faversham"),
("Ashford","Ashford Back & Wellness Centre, Barrow Hill, Ashford, TN24 8RL","ashford"),
("Canterbury","KP GP Services, Lombard House, 12-17 Upper Bridge Street, Canterbury, CT1 2NF","canterbury"),
("Eastbourne","Podiamed, 1 Lushington Rd, Eastbourne, BN21 4LG","eastbourne"),
("Hastings","Falaise Gym, Cambridge Rd, Hastings, TN34 1EU","hastings"),
("Margate","HQ Margate, 35 Marine Terrace, Margate, CT9 1XJ","margate"),
("Exmouth","51 Imperial Road, Exmouth, EX8 1DQ","exmouth"),
("Newton Abbot","Contour Medical Aesthetics Academy, Bridge House, Newton Abbot, TQ12 2QS","newton-abbot"),
("Ivybridge","Nature's Larder, 10 Glanvilles Mill, Ivybridge, PL21 9PS","ivybridge"),
("Plymouth","Sound Chiropractic, 10 Abbotts Rd, Peverell, Plymouth, PL3 4PB","plymouth"),
("Edinburgh","10 B, Broughton Street Lane, Edinburgh, EH1 3LY","edinburgh"),
("Dundee","Level 1, 4 Panmure Street, Dundee, DD1 2BW","dundee"),
("Perth","Perth Yoga Studio, 7 Rose Terrace, Perth, PH1 5HA","perth"),
]

WALES = {"Swansea","Llanelli","Carmarthen","Cardiff","Newport","Merthyr Tydfil","Barry","Bridgend","Neath"}
SCOT = {"Edinburgh","Dundee","Perth"}
LONDON = {"Finchley","Enfield","Hounslow","Harlesden","Wood Green","Primrose Hill","Chingford","Highbury","Fulham","Whitechapel","East Ham","Ilford - Gants Hill","Streatham","Morden","Lewisham","Croydon","Welling","Harrow","Orpington","Walton-on-Thames","Ewell"}
SOUTHEAST = {"Reading","Reading - Chatham Place","Reading - Thatcham","Reading - Woodley","Reading - Green Park","Newbury","Burnham","Farnborough","Southampton","Crawley","Brighton","Hove","Burgess Hill","Worthing","Eastbourne","Hastings","Tonbridge","Royal Tunbridge Wells","Sheerness","Minster Medical Centre","Maidstone","Sittingbourne","Faversham","Ashford","Canterbury","Margate","Luton","Berkhamsted","Watford","St Albans","Thurrock","Basildon","Chelmsford","Halstead"}
SOUTHWEST = {"Bristol - Staple Hill","Bristol - Southville","Yate - Bristol","Weston-super-Mare","Taunton","Salisbury","Swindon","Chippenham","Gloucester","Exmouth","Newton Abbot","Ivybridge","Plymouth"}
MIDLANDS = {"Leicester","Northampton","Wellingborough"}

def region(n):
    if n in WALES: return "Wales"
    if n in SCOT: return "Scotland"
    if n in LONDON: return "London"
    if n in SOUTHEAST: return "South East & East"
    if n in SOUTHWEST: return "South West"
    if n in MIDLANDS: return "Midlands"
    return "North West" if n=="Bolton" else "Other"

LOCS = [dict(name=n, address=a, slug=s, region=region(n)) for n,a,s in RAW]
