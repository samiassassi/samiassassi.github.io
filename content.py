"""All site content, in English / French / Arabic.

Source of truth: Sami's CVs (source/CV_EN.docx, source/CV_FR.docx).
Edit text HERE, then rebuild:   python build.py
L(en, fr, ar) holds one string per language. Bibliographic titles (publications,
theses, talk titles) stay in their original language, as is standard.
"""


def L(en, fr, ar):
    return {"en": en, "fr": fr, "ar": ar}


# --------------------------------------------------------------------------- person
PERSON = {
    "name": L("Sami Assassi", "Sami Assassi", "سامي عساسي"),
    "display": L("Dr. Sami Assassi", "Dr Sami Assassi", "د. سامي عساسي"),
    "email": "assassisami@hotmail.com",
    "orcid": "0000-0002-1325-0207",
    "scholar": "",      # Google Scholar URL, e.g. "https://scholar.google.com/citations?user=XXXX"; empty = hidden
    "linkedin": "",     # LinkedIn URL; empty = hidden
    "researchgate": "", # ResearchGate URL; empty = hidden
    "city": L("Ottawa, Ontario, Canada", "Ottawa (Ontario), Canada", "أوتاوا، أونتاريو، كندا"),
    "degrees": L("Ph.D., HDR", "Ph.D., HDR", "دكتوراه، تأهيل جامعي"),
    "role": L("Agricultural economist", "Économiste agricole", "باحث في الاقتصاد الزراعي"),
    "position": L("Adjunct Professor, Saint Paul University, Ottawa",
                  "Professeur auxiliaire, Université Saint-Paul, Ottawa",
                  "أستاذ منتسب، جامعة سانت بول، أوتاوا"),
    "former": L("Teacher-researcher, ENSA Algiers, 2018–2026",
                "Enseignant-chercheur, ENSA d'Alger, 2018–2026",
                "أستاذ باحث، المدرسة الوطنية العليا للفلاحة، الجزائر، 2018–2026"),
    "headline": L("Contract farming, land and water markets, and who captures value in Algeria's tomato, citrus, dairy and cereal chains.",
                  "Agriculture contractuelle, marchés fonciers et de l'eau, et partage de la valeur dans les filières tomate, agrumes, lait et céréales en Algérie.",
                  "الزراعة التعاقدية، وأسواق الأراضي والمياه، وتقاسم القيمة في شعب الطماطم والحمضيات والحليب والحبوب في الجزائر."),
    "now": L("Adjunct Professor, Saint Paul University, Ottawa · Work-package lead, School Meal Systems and Supply Chains (IDRC) · NATAE project (Horizon Europe)",
             "Professeur auxiliaire, Université Saint-Paul, Ottawa · Responsable de lot, Systèmes de restauration scolaire (CRDI) · Projet NATAE (Horizon Europe)",
             "أستاذ منتسب، جامعة سانت بول، أوتاوا · مسؤول حزمة عمل، مشروع أنظمة الإطعام المدرسي (CRDI) · مشروع NATAE (أفق أوروبا)"),
    "lead": L("", "", ""),
    "bio": L(
        ["Dr. Sami Assassi is an agricultural economist specialising in agribusiness management, value chains, "
         "agricultural finance and marketing. He is Adjunct Professor at the Faculty of Humanities and Philosophy of "
         "Saint Paul University in Ottawa. From 2018 to 2026 he was a teacher-researcher at the National Higher "
         "School of Agronomy (ENSA) in Algiers, where he taught from undergraduate to doctoral level, supervised "
         "theses and directed the Laboratory of Agricultural, Agrifood, Rural and Environmental Economics.",
         "His research centres on contract farming between agro-industry and smallholders, land and water markets, "
         "the distribution of margins in fresh-produce chains, and farm performance. It appears in Development "
         "Policy Review, the Canadian Journal of Development Studies, Cahiers Agricultures and New Medit, with "
         "forthcoming articles in the Journal of Development Studies and Agribusiness.",
         "Since 2017 he has advised international development programmes for the World Bank, the European Union, "
         "FAO, UNDP and GIZ on value-chain analysis, climate-risk financing, multi-stakeholder platforms and "
         "monitoring, evaluation, accountability and learning (MEAL). He holds a Ph.D. in agrifood and rural "
         "economics and a Habilitation to Supervise Research (HDR), both WES-validated for Canada."],
        ["Le Dr Sami Assassi est économiste agricole, spécialiste du management des entreprises agricoles, des filières, "
         "de la finance agricole et du marketing. Il est professeur auxiliaire à la Faculté des sciences humaines "
         "et de philosophie de l'Université Saint-Paul, à Ottawa. De 2018 à 2026, il a été enseignant-chercheur "
         "à l'École nationale supérieure agronomique (ENSA) d'Alger, où il a enseigné du premier cycle au doctorat, "
         "encadré des mémoires et des thèses et dirigé le Laboratoire d'économie agricole, agroalimentaire, rurale "
         "et de l'environnement.",
         "Ses recherches portent sur l'agriculture contractuelle entre agro-industrie et petits producteurs, les "
         "marchés fonciers et de l'eau, la répartition des marges dans les filières de produits frais et la "
         "performance des exploitations. Elles sont publiées dans Development Policy Review, la Revue canadienne "
         "d'études du développement, Cahiers Agricultures et New Medit, avec des articles à paraître dans le "
         "Journal of Development Studies et Agribusiness.",
         "Depuis 2017, il conseille des programmes de coopération pour la Banque mondiale, l'Union européenne, la FAO, "
         "le PNUD et la GIZ : analyse de filières, financement des risques climatiques, plateformes multi-acteurs et "
         "suivi-évaluation (SEAR). Il est titulaire d'un doctorat en économie agroalimentaire et rurale et d'une "
         "habilitation universitaire (HDR), tous deux validés par WES pour le Canada."],
        ["الدكتور سامي عساسي باحث في الاقتصاد الزراعي، متخصص في تسيير المؤسسات الزراعية وسلاسل القيمة والتمويل الزراعي "
         "والتسويق. يشغل منصب أستاذ منتسب بكلية العلوم الإنسانية والفلسفة في جامعة سانت بول بأوتاوا. "
         "عمل من 2018 إلى 2026 أستاذاً باحثاً في المدرسة الوطنية العليا للفلاحة بالجزائر العاصمة، حيث درّس من "
         "مرحلة التدرج إلى الدكتوراه، وأشرف على المذكرات والأطروحات، وأدار مخبر الاقتصاد الزراعي والغذائي "
         "والريفي والبيئي.",
         "تتمحور أبحاثه حول الزراعة التعاقدية بين الصناعات الغذائية وصغار المنتجين، وأسواق الأراضي والمياه، "
         "وتوزيع الهوامش في سلاسل المنتجات الطازجة، وأداء المستثمرات الفلاحية. نُشرت أعماله في مجلات دولية "
         "منها ⁦Development Policy Review⁩ و⁦Canadian Journal of Development Studies⁩ و⁦Cahiers Agricultures⁩ "
         "و⁦New Medit⁩، ولديه مقالات قيد النشر في ⁦Journal of Development Studies⁩ و⁦Agribusiness⁩.",
         "منذ 2017 يقدّم خبرته لبرامج التعاون الدولي لصالح البنك الدولي والاتحاد الأوروبي ومنظمة الأغذية والزراعة "
         "وبرنامج الأمم المتحدة الإنمائي والوكالة الألمانية للتعاون الدولي، في مجالات تحليل سلاسل القيمة وتمويل "
         "المخاطر المناخية ومنصات الحوار متعددة الأطراف والمتابعة والتقييم. يحمل شهادة دكتوراه في الاقتصاد "
         "الغذائي والريفي وشهادة التأهيل الجامعي لإدارة البحوث، وكلتاهما معتمدتان من WES في كندا."]),
}

# --------------------------------------------------------------------------- research themes = value-chain stages
# "pubs" lists keys from PUBS; "projects" lists keys from PROJECTS.
THEMES = [
    {"id": "land", "icon": "land",
     "t": L("Land & water", "Foncier & eau", "الأرض والمياه"),
     "q": L("Who gets access to land and groundwater, and on what terms?",
            "Qui accède à la terre et à l'eau souterraine, et à quelles conditions ?",
            "من يصل إلى الأرض والمياه الجوفية، وبأي شروط؟"),
     "d": L("Tenancy markets, informal land transactions and the way they reallocate irrigation water; "
            "groundwater depletion and the sustainability of new irrigated agriculture in arid zones.",
            "Marchés du faire-valoir indirect, transactions foncières informelles et réallocation de l'eau d'irrigation ; "
            "épuisement des nappes et durabilité de la nouvelle agriculture irriguée en zones arides.",
            "أسواق الإيجار والمعاملات العقارية غير الرسمية ودورها في إعادة توزيع مياه السقي، واستنزاف المياه الجوفية "
            "واستدامة الزراعة المسقية الجديدة في المناطق الجافة."),
     "pubs": ["newmedit2023", "cagri2022"], "projects": ["gw2012"]},
    {"id": "farm", "icon": "farm",
     "t": L("Farms", "Exploitations", "المستثمرات الفلاحية"),
     "q": L("What makes farms perform, and does size matter?",
            "Qu'est-ce qui fait la performance des exploitations, et la taille compte-t-elle ?",
            "ما الذي يصنع أداء المستثمرات الفلاحية، وهل للحجم أهمية؟"),
     "d": L("Farm size and productivity, efficiency (DEA), social networks, innovation systems and the "
            "agroecological transition of family and entrepreneurial farms.",
            "Taille et productivité des exploitations, efficience (DEA), réseaux sociaux, systèmes d'innovation et "
            "transition agroécologique des exploitations familiales et entrepreneuriales.",
            "حجم المستثمرات وإنتاجيتها، والكفاءة (تحليل مغلف البيانات)، والشبكات الاجتماعية، ونظم الابتكار، "
            "والانتقال الإيكولوجي الزراعي للمستثمرات العائلية والمقاولاتية."),
     "pubs": ["newmedit2025", "jotaf2021", "rev_size"], "projects": ["natae", "ais2021"]},
    {"id": "contract", "icon": "contract",
     "t": L("Contracts", "Contrats", "العقود"),
     "q": L("Can contract farming include smallholders and raise their incomes?",
            "L'agriculture contractuelle peut-elle inclure les petits producteurs et améliorer leurs revenus ?",
            "هل تستطيع الزراعة التعاقدية إدماج صغار المنتجين وتحسين مداخيلهم؟"),
     "d": L("Contract farming between processors and growers in Algeria's industrial tomato chain: smallholder "
            "inclusion, income effects, opportunism, supplier portfolios and state subsidies as a hybrid "
            "enforcement mechanism.",
            "Agriculture contractuelle entre transformateurs et producteurs dans la filière tomate industrielle en "
            "Algérie : inclusion des petits exploitants, effets sur les revenus, opportunisme, portefeuilles "
            "fournisseurs et subventions publiques comme mécanisme hybride d'exécution des contrats.",
            "الزراعة التعاقدية بين المصنّعين والمنتجين في شعبة الطماطم الصناعية بالجزائر: إدماج صغار المنتجين، "
            "وأثرها على المداخيل، والسلوك الانتهازي، وتنويع الموردين، والدعم العمومي كآلية هجينة لتنفيذ العقود."),
     "pubs": ["jds_f", "agribiz_f", "dpr2024", "cjds2023", "cagri2020", "ulb2017"], "projects": ["cf2014"]},
    {"id": "market", "icon": "market",
     "t": L("Markets & margins", "Marchés & marges", "الأسواق والهوامش"),
     "q": L("Who captures value between the field and the consumer?",
            "Qui capte la valeur entre le champ et le consommateur ?",
            "من يستحوذ على القيمة بين الحقل والمستهلك؟"),
     "d": L("Price formation, trader margins and value distribution in fresh-produce chains, from Biskra's "
            "greenhouse tomatoes and wholesale markets to citrus, under environmental and economic crises.",
            "Formation des prix, marges des commerçants et répartition de la valeur dans les filières de produits "
            "frais, de la tomate sous serre et des marchés de gros de Biskra aux agrumes, en contexte de crises.",
            "تكوّن الأسعار وهوامش التجار وتوزيع القيمة في سلاسل المنتجات الطازجة، من طماطم البيوت البلاستيكية "
            "وأسواق الجملة في بسكرة إلى الحمضيات، في ظل الأزمات البيئية والاقتصادية."),
     "pubs": ["cagri_f", "cagri2017", "rev_citrus"], "projects": ["gis2012"]},
    {"id": "city", "icon": "city",
     "t": L("Food & cities", "Alimentation & villes", "الغذاء والمدن"),
     "q": L("How do cities feed themselves, and how should public buyers procure?",
            "Comment les villes se nourrissent-elles, et comment l'achat public doit-il s'organiser ?",
            "كيف تتغذى المدن، وكيف ينبغي أن تنظَّم المشتريات العمومية؟"),
     "d": L("Urban and agricultural concentration, peri-urban agriculture and food security, and procurement "
            "models for school-meal systems.",
            "Concentration urbaine et agricole, agriculture périurbaine et sécurité alimentaire, et modèles "
            "d'approvisionnement de la restauration scolaire.",
            "التمركز الحضري والزراعي، والزراعة شبه الحضرية والأمن الغذائي، ونماذج التموين في أنظمة الإطعام المدرسي."),
     "pubs": ["mmsh2026"], "projects": ["school2024"]},
]
CROSS = {
    "t": L("Across the chain: climate risk, public policy & insurance",
           "Transversal : risque climatique, politiques publiques & assurance",
           "على امتداد السلسلة: المخاطر المناخية والسياسات العمومية والتأمين"),
    "d": L("Economic impacts of climate events on cereal production, risk-financing models for inclusive "
           "agricultural insurance, and evaluation of cereal and land policies.",
           "Impacts économiques des événements climatiques sur la céréaliculture, modèles de financement des "
           "risques pour une assurance agricole inclusive, et évaluation des politiques céréalières et foncières.",
           "الآثار الاقتصادية للظواهر المناخية على إنتاج الحبوب، ونماذج تمويل المخاطر من أجل تأمين زراعي شامل، "
           "وتقييم سياسات الحبوب والعقار الفلاحي."),
}

# --------------------------------------------------------------------------- publications
# status: "pub" | "forth" (forthcoming / in press) | "review" (under review)
# kind: "article" | "chapter" | "paper"
PUBS = [
    {"k": "jds_f", "y": "", "status": "forth", "kind": "article", "lang": "en", "th": ["contract"],
     "a": "Assassi S.",
     "t": "Beyond individual opportunism: a review of the configurational global enforcement system in contract farming",
     "v": "Journal of Development Studies", "doi": ""},
    {"k": "agribiz_f", "y": "", "status": "forth", "kind": "article", "lang": "en", "th": ["contract"],
     "a": "Benmehaia A.M., Assassi S.",
     "t": "Many small growers or few large ones? Supplier portfolio design under contractual default in agro-industrial procurement",
     "v": "Agribusiness: An International Journal", "doi": ""},
    {"k": "cagri_f", "y": "", "status": "forth", "kind": "article", "lang": "en", "th": ["market", "land"],
     "a": "Assassi S., Lejars C., Ouaret W., Brown M.E., Amokrane A.",
     "t": "How are margins distributed within neo-agriculture supply chains during environmental and economic ‘crises’?",
     "v": "Cahiers Agricultures", "doi": ""},
    {"k": "mmsh2026", "y": "2026", "status": "pub", "kind": "chapter", "lang": "fr", "th": ["city"],
     "a": "Daoudi A., Assassi S., Bouzid A., Nechar M., Meribai A., Cherfaoui Z.",
     "t": "Concentration urbaine et agricole : une double polarisation qui interroge la sécurité alimentaire des villes",
     "v": "In: Les territoires urbains face au défi alimentaire. Perspectives croisées en région MENA. "
          "Maison méditerranéenne des sciences de l'homme", "doi": ""},
    {"k": "newmedit2025", "y": "2025", "status": "pub", "kind": "article", "lang": "en", "th": ["farm"],
     "a": "Assassi S., Zebbar N., Dib F.",
     "t": "Decoding farm size–performance relationship in Algerian agriculture: toward a unified analytical framework",
     "v": "New Medit", "doi": "10.30682/nm2505h"},
    {"k": "dpr2024", "y": "2024", "status": "pub", "kind": "article", "lang": "en", "th": ["contract"],
     "a": "Assassi S., Kleftodemos G., Benharrath O., Aybike B.",
     "t": "Enforcing contracts: the role of state subsidies as a hybrid enforcement mechanism in contracts between tomato processors and farmers in Algeria",
     "v": "Development Policy Review, e12827", "doi": "10.1111/dpr.12827"},
    {"k": "cjds2023", "y": "2023", "status": "pub", "kind": "article", "lang": "en", "th": ["contract"],
     "a": "Assassi S., Soullier G.",
     "t": "Do state-subsidised contractual arrangements improve farmers' income? Empirical evidence from Algeria",
     "v": "Canadian Journal of Development Studies 44(3)", "doi": "10.1080/02255189.2023.2212895"},
    {"k": "newmedit2023", "y": "2023", "status": "pub", "kind": "article", "lang": "en", "th": ["land"],
     "a": "Assassi S.",
     "t": "Are tenancy land markets equitable? A review of the “farmer selection” dynamics in Algeria",
     "v": "New Medit", "doi": "10.30682/nm2301g"},
    {"k": "cagri2022", "y": "2022", "status": "pub", "kind": "article", "lang": "fr", "th": ["land"],
     "a": "Assassi S., Daoudi A., Amokrane A.",
     "t": "Le marché foncier comme dispositif de réallocation de l'eau dans le périmètre irrigué de Guelma, Algérie",
     "v": "Cahiers Agricultures", "doi": "10.1051/cagri/2022028"},
    {"k": "jotaf2021", "y": "2021", "status": "pub", "kind": "article", "lang": "en", "th": ["farm"],
     "a": "Nechar M., Assassi S., Bendrissou M.",
     "t": "What impact of social networks on farmers' performances? Case of the milk sector in Ghardaïa, Algeria",
     "v": "Journal of Tekirdag Agricultural Faculty 18(4): 625–635", "doi": "10.33462/jotaf.825151"},
    {"k": "cagri2020", "y": "2020", "status": "pub", "kind": "article", "lang": "fr", "th": ["contract"],
     "a": "Assassi S., Daoudi A., Colin J.-Ph.",
     "t": "Quelle place pour les petits exploitants dans l'agriculture contractuelle ? Le cas de la tomate industrielle en Algérie",
     "v": "Cahiers Agricultures 29: 26", "doi": "10.1051/cagri/2020023"},
    {"k": "ulb2017", "y": "2017", "status": "pub", "kind": "paper", "lang": "fr", "th": ["contract"],
     "a": "Daoudi A., Colin J.-Ph., Terranti S., Assassi S.",
     "t": "L'agriculture contractuelle en Algérie : radiographie des arrangements public-privé",
     "v": "Université libre de Bruxelles, 33es Journées du développement de l'ATM, 17 p.", "doi": ""},
    {"k": "cagri2017", "y": "2017", "status": "pub", "kind": "article", "lang": "fr", "th": ["market"],
     "a": "Assassi S., Daoudi A., Lejars C.",
     "t": "Les profits « excessifs » des commerçants de fruits et légumes en Algérie : réalité ou préjugé infondé ? Le cas de la tomate primeur à Biskra",
     "v": "Cahiers Agricultures 26(2): 25002", "doi": "10.1051/cagri/2017009"},
    {"k": "rev_size", "y": "", "status": "review", "kind": "article", "lang": "en", "th": ["farm"],
     "a": "Benmehaia A.M., Assassi S.",
     "t": "Farm size–productivity beyond the mean: nonlinear and distributional evidence from Algeria",
     "v": "Journal of Agribusiness in Developing and Emerging Economies", "doi": ""},
    {"k": "rev_citrus", "y": "", "status": "review", "kind": "article", "lang": "en", "th": ["market"],
     "a": "Bouhaddou M.B., Assassi S.",
     "t": "When rational individual choices lead to a collective impasse: the drivers of circular lock-in in Algeria's citrus sector",
     "v": "", "doi": ""},
    {"k": "rev_climate", "y": "", "status": "review", "kind": "article", "lang": "en", "th": ["farm"],
     "a": "Assassi S.",
     "t": "How climate change is rewriting Algerian agriculture",
     "v": "", "doi": ""},
]

REVIEWING = [  # (year, journal)
    ("2026", "Discover Sustainability"),
    ("2026", "Frontiers in Sustainable Food Systems"),
    ("2026", "New Medit"),
    ("2024", "Cahiers Agricultures"),
    ("2023", "Cahiers Agricultures"),
]

# --------------------------------------------------------------------------- research projects
PROJECTS = [
    {"k": "school2024", "p": "2024 –", "f": "IDRC (Canada)",
     "t": L("School Meal Systems and Supply Chains", "Systèmes de restauration scolaire et chaînes d'approvisionnement",
            "أنظمة الإطعام المدرسي وسلاسل التموين"),
     "r": L("Leads the work package on implementing the new procurement model.",
            "Responsable du lot de travail sur la mise en œuvre du nouveau modèle d'approvisionnement.",
            "مسؤول عن حزمة العمل الخاصة بتطبيق نموذج التموين الجديد.")},
    {"k": "natae", "p": "2022 –", "f": "Horizon Europe · IAM Montpellier",
     "t": L("NATAE: Fostering agro-ecological transition in North Africa through multi-actor design, evaluation and networking",
            "NATAE : favoriser la transition agroécologique en Afrique du Nord par la conception, l'évaluation et la mise en réseau multi-acteurs",
            "NATAE: تعزيز الانتقال الإيكولوجي الزراعي في شمال إفريقيا عبر التصميم والتقييم والتشبيك متعدد الأطراف"),
     "r": L("Methodology for a cereal living lab in Sétif: cereal value chain, climate impacts and public policy for production and market risks.",
            "Méthodologie d'un living lab céréalier à Sétif : filière céréales, impacts climatiques et politiques publiques face aux risques productifs et commerciaux.",
            "منهجية مختبر حيّ للحبوب في سطيف: شعبة الحبوب، والآثار المناخية، والسياسات العمومية لمواجهة مخاطر الإنتاج والتسويق.")},
    {"k": "ais2021", "p": "2021 – 2026", "f": "DGRSDT (Algeria)",
     "t": L("Agricultural innovation systems for better food security",
            "Analyse des systèmes d'innovation agricole pour une meilleure sécurité alimentaire",
            "تحليل نظم الابتكار الزراعي من أجل أمن غذائي أفضل"),
     "r": L("Team member; led by Samia Akli (ENSA Algiers).", "Membre de l'équipe ; dirigé par Samia Akli (ENSA d'Alger).",
            "عضو في الفريق؛ بإدارة سامية عقلي (المدرسة الوطنية العليا للفلاحة).")},
    {"k": "cf2014", "p": "2014 – 2018", "f": "IDRC (Canada)",
     "t": L("Contract farming in Algeria and its effects on smallholder inclusion",
            "L'agriculture contractuelle en Algérie et ses effets sur l'inclusion des petits producteurs",
            "الزراعة التعاقدية في الجزائر وآثارها على إدماج صغار المنتجين"),
     "r": L("Associate researcher; co-led the socio-economic analysis, from field data collection to impact evaluation. Led by Ali Daoudi.",
            "Chercheur associé ; co-direction de l'analyse socio-économique, de la collecte de terrain à l'évaluation d'impact. Dirigé par Ali Daoudi.",
            "باحث مشارك؛ شارك في قيادة التحليل الاجتماعي والاقتصادي من جمع البيانات الميدانية إلى تقييم الأثر. بإدارة علي داودي.")},
    {"k": "gis2012", "p": "2012 – 2013", "f": "IDRC (Canada)",
     "t": L("Technical innovation systems in greenhouse vegetable production in Biskra",
            "Système d'innovation technique dans le maraîchage sous serre à Biskra",
            "نظام الابتكار التقني في زراعة الخضر تحت البيوت البلاستيكية في بسكرة"),
     "r": L("Junior researcher; led by Ali Daoudi (ENSA Algiers).", "Chercheur junior ; dirigé par Ali Daoudi (ENSA d'Alger).",
            "باحث مبتدئ؛ بإدارة علي داودي (المدرسة الوطنية العليا للفلاحة).")},
    {"k": "gw2012", "p": "2012 – 2013", "f": "ANR (France) · CIRAD G-EAU",
     "t": L("Vulnerability and adaptive capacity of new groundwater-irrigated agriculture in the Maghreb",
            "Vulnérabilité et capacité d'adaptation des nouvelles agricultures irriguées par les eaux souterraines au Maghreb",
            "هشاشة الزراعة المسقية الجديدة بالمياه الجوفية في المغرب العربي وقدرتها على التكيّف"),
     "r": L("Junior researcher; led by Marcel Kuper (CIRAD).", "Chercheur junior ; dirigé par Marcel Kuper (CIRAD).",
            "باحث مبتدئ؛ بإدارة مارسيل كوبر (CIRAD).")},
]

# --------------------------------------------------------------------------- field map (wilaya names as in assets/map.json)
# kind: "r" research, "c" consulting / advisory
SITES = {
    "Biskra": ("r", L("Greenhouse tomato economics, wholesale markets and trader margins; PASA chili-pepper value-chain platform (2021–22)",
                      "Économie de la tomate sous serre, marchés de gros et marges ; plateforme filière piment PASA (2021–22)",
                      "اقتصاد طماطم البيوت البلاستيكية وأسواق الجملة وهوامش التجار؛ منصة شعبة الفلفل الحار ضمن PASA (2021–22)"),
                L("Biskra", "Biskra", "بسكرة")),
    "Guelma": ("r", L("Contract farming in the industrial tomato chain (Ph.D.); land markets and irrigation water",
                      "Agriculture contractuelle dans la filière tomate industrielle (thèse) ; marché foncier et eau d'irrigation",
                      "الزراعة التعاقدية في شعبة الطماطم الصناعية (الدكتوراه)؛ سوق الأراضي ومياه السقي"),
               L("Guelma", "Guelma", "قالمة")),
    "Setif": ("r", L("World Bank value-chain mapping (2017); NATAE cereal living lab and policy review (2024–25)",
                     "Cartographie des filières pour la Banque mondiale (2017) ; living lab céréalier NATAE et revue des politiques (2024–25)",
                     "تشخيص سلاسل القيمة للبنك الدولي (2017)؛ المختبر الحيّ للحبوب NATAE ومراجعة السياسات (2024–25)"),
              L("Sétif", "Sétif", "سطيف")),
    "Ghardaia": ("r", L("Social networks and performance of dairy farmers", "Réseaux sociaux et performances des éleveurs laitiers",
                        "الشبكات الاجتماعية وأداء مربي الأبقار الحلوب"), L("Ghardaïa", "Ghardaïa", "غرداية")),
    "Alger": ("r", L("School-meal procurement, peri-urban agriculture; ENSA (2018–2026)",
                     "Approvisionnement des cantines scolaires, agriculture périurbaine ; ENSA (2018–2026)",
                     "تموين المطاعم المدرسية، الزراعة شبه الحضرية؛ المدرسة الوطنية العليا للفلاحة (2018–2026)"),
              L("Algiers", "Alger", "الجزائر")),
    "Blida": ("r", L("Citrus value chain and vertical coordination", "Filière agrumes et coordination verticale",
                     "شعبة الحمضيات والتنسيق العمودي"), L("Blida", "Blida", "البليدة")),
    "Laghouat": ("r", L("NATAE International Agroecology Research School, Aflou (2026)",
                        "École internationale de recherche en agroécologie NATAE, Aflou (2026)",
                        "المدرسة الدولية للبحث في الإيكولوجيا الزراعية NATAE، آفلو (2026)"), L("Laghouat", "Laghouat", "الأغواط")),
    "Tlemcen": ("c", L("EU territorial diagnosis of family farms, national park (2018); FAO non-timber forest products (2026)",
                       "Diagnostic territorial UE des exploitations familiales, parc national (2018) ; produits forestiers non ligneux FAO (2026)",
                       "تشخيص إقليمي للمستثمرات العائلية للاتحاد الأوروبي، الحظيرة الوطنية (2018)؛ المنتجات الغابية غير الخشبية للفاو (2026)"),
                L("Tlemcen", "Tlemcen", "تلمسان")),
    "Skikda": ("c", L("Inclusive value chains, EU DRI programme (2018–19)", "Chaînes de valeur inclusives, programme DRI UE (2018–19)",
                      "سلاسل القيمة الشاملة، برنامج DRI للاتحاد الأوروبي (2018–19)"), L("Skikda", "Skikda", "سكيكدة")),
    "Bouira": ("c", L("Inclusive value chains, EU DRI programme (2019)", "Chaînes de valeur inclusives, programme DRI UE (2019)",
                      "سلاسل القيمة الشاملة، برنامج DRI للاتحاد الأوروبي (2019)"), L("Bouira", "Bouira", "البويرة")),
    "Tissemsilt": ("c", L("Inclusive value chains, EU NIDID project (2019)", "Chaînes de valeur inclusives, projet NIDID UE (2019)",
                          "سلاسل القيمة الشاملة، مشروع NIDID للاتحاد الأوروبي (2019)"), L("Tissemsilt", "Tissemsilt", "تيسمسيلت")),
    "Saida": ("c", L("Inclusive value chains, EU NIDID project (2019)", "Chaînes de valeur inclusives, projet NIDID UE (2019)",
                     "سلاسل القيمة الشاملة، مشروع NIDID للاتحاد الأوروبي (2019)"), L("Saïda", "Saïda", "سعيدة")),
    "El Oued": ("c", L("Multi-stakeholder dialogue platforms, PASA (2022)", "Plateformes de dialogue multi-acteurs, PASA (2022)",
                       "منصات الحوار متعددة الأطراف، PASA (2022)"), L("El Oued", "El Oued", "الوادي")),
    "Bejaia": ("c", L("FAO training on non-timber forest products (2026)", "Formation FAO sur les produits forestiers non ligneux (2026)",
                      "تكوين الفاو حول المنتجات الغابية غير الخشبية (2026)"), L("Béjaïa", "Béjaïa", "بجاية")),
    "Jijel": ("c", L("FAO training on non-timber forest products (2026)", "Formation FAO sur les produits forestiers non ligneux (2026)",
                     "تكوين الفاو حول المنتجات الغابية غير الخشبية (2026)"), L("Jijel", "Jijel", "جيجل")),
}

STAYS = [  # (year, place, institution)
    ("2026", L("Ottawa, Canada", "Ottawa, Canada", "أوتاوا، كندا"), "Saint Paul University"),
    ("2025", L("College Park, USA", "College Park, États-Unis", "كوليدج بارك، الولايات المتحدة"), "University of Maryland, Dept. of Geographical Sciences"),
    ("2024", L("Montpellier, France", "Montpellier, France", "مونبلييه، فرنسا"), "IAM Montpellier (CIHEAM)"),
    ("2022–23", L("Montpellier, France", "Montpellier, France", "مونبلييه، فرنسا"), "CIRAD · UMR G-EAU"),
    ("2017", L("Montpellier, France", "Montpellier, France", "مونبلييه، فرنسا"), "UMR GRED"),
    ("2015–16", L("Paris, France", "Paris, France", "باريس، فرنسا"), "UMR DIAL"),
]

# --------------------------------------------------------------------------- teaching
COURSES = [
    {"t": L("Governance of agricultural and agrifood value chains", "Gouvernance des filières agricoles et agroalimentaires",
            "حوكمة السلاسل الزراعية والغذائية"),
     "lv": L("Ph.D.", "Doctorat", "دكتوراه"), "h": "", "since": "2022"},
    {"t": L("Agribusiness management", "Gestion des entreprises agricoles", "تسيير المؤسسات الزراعية"),
     "lv": L("Master's · Agricultural machinery", "Master · Machinisme agricole", "ماستر · الآلات الزراعية"), "h": "45", "since": "2018"},
    {"t": L("Management and marketing", "Gestion et marketing", "التسيير والتسويق"),
     "lv": L("Master's · Plant production", "Master · Productions végétales", "ماستر · الإنتاج النباتي"), "h": "36", "since": "2018"},
    {"t": L("Specialised agrifood project management", "Projets spécialisés agroalimentaires", "تسيير المشاريع الغذائية المتخصصة"),
     "lv": L("Master's · Rural economics", "Master · Économie rurale", "ماستر · الاقتصاد الريفي"), "h": "30", "since": "2018"},
    {"t": L("Agribusiness investment project analysis", "Analyse des projets d'investissement", "تحليل مشاريع الاستثمار الزراعي"),
     "lv": L("Master's · Food technology", "Master · Technologies alimentaires", "ماستر · التكنولوجيا الغذائية"), "h": "21", "since": "2019"},
    {"t": L("Introduction to agricultural economics", "Initiation à l'économie agricole", "مدخل إلى الاقتصاد الزراعي"),
     "lv": L("Undergraduate common core", "Tronc commun", "الجذع المشترك"), "h": "20", "since": "2022"},
]

PHD_SUPERVISION = L(
    "Vertical coordination in the citrus value chain in Algeria: towards a model for optimising farmer–agrifood business relationships (supervision project accepted and funded, 2024).",
    "Coordination verticale dans la filière agrumes en Algérie : vers un modèle d'optimisation des relations entre agriculteurs et entreprises agroalimentaires (projet d'encadrement accepté et financé, 2024).",
    "التنسيق العمودي في شعبة الحمضيات بالجزائر: نحو نموذج لتحسين العلاقات بين الفلاحين ومؤسسات الصناعات الغذائية (مشروع إشراف مقبول وممول، 2024).")

# (year, student, title_en, title_fr)
MASTERS = [
    ("2026", "Ikram Hafsaoui", "Agricultural product supply systems for school cafeterias in the wilaya of Algiers",
     "Analyse des systèmes d'approvisionnement en produits agricoles des cantines scolaires dans la wilaya d'Alger"),
    ("2025", "Nesrine Feniri", "Challenges and opportunities for developing the citrus value chain in Blida",
     "Défis et opportunités de développement de la filière agrumes : logiques de commercialisation des producteurs de Blida"),
    ("2025", "Meriem Bouchra Bouhaddou", "Citrus value chain: supply strategies of orange-juice producers",
     "Défis et opportunités de développement de la filière agrumes : logiques d'approvisionnement des producteurs de jus d'orange à Alger"),
    ("2024", "Feriel Dib", "The role of small peri-urban agriculture in food security: the case of Algiers",
     "Le rôle de la petite agriculture périurbaine dans la sécurité alimentaire, cas de la wilaya d'Alger"),
    ("2023", "Lyna Chemsi", "Strengths and weaknesses of entrepreneurial farms",
     "Les forces et les limites des exploitations agricoles entrepreneuriales"),
    ("2023", "Manel Benyoucef & Cherifa Amira Mohammedi", "A hibiscus-based dietary soft drink (start-up project)",
     "Élaboration d'une boisson gazeuse diététique à base d'extrait de roselle (projet de start-up)"),
    ("2022", "Lilia Kaddour", "Enforcement mechanisms of agricultural contracts: the case of a tomato processor",
     "Analyse des mécanismes d'exécution des contrats agricoles : le cas d'une conserverie de tomates"),
    ("2022", "Aicha Kaous", "The effect of biodiversity on farm sustainability",
     "L'effet de la biodiversité sur la durabilité des exploitations agricoles"),
    ("2022", "Nadjet Zebbar", "Farm size and productivity: evidence from the artichoke sector in Relizane",
     "Taille des exploitations et productivité : le secteur de l'artichaut à Relizane"),
    ("2022", "Toufik Bariziane", "Wholesale fruit and vegetable markets as vectors of agricultural innovation: El Ghrous, Biskra",
     "Les marchés de gros de fruits et légumes, vecteurs d'innovations : cas d'El Ghrous, Biskra"),
    ("2021", "Walid Hammouch", "Vertical coordination in the poultry value chain: the case of Poulet du Jour (Bellat)",
     "La coordination verticale au sein de la filière avicole : cas de la filiale Poulet du Jour (Bellat)"),
    ("2021", "Nesrine Guesmia", "Productive strategies of landowners under contract farming: industrial tomato in Guelma",
     "Les logiques productives des propriétaires fonciers face à l'agriculture contractuelle : tomate industrielle à Guelma"),
    ("2019", "Kenza Chibane", "Procurement strategies of the Soummam dairy, Béjaïa",
     "Stratégies d'approvisionnement de la laiterie Soummam, wilaya de Béjaïa"),
    ("2019", "Mohammed Bendrissou", "Social networks and farm practices: dairy cattle farming in Ghardaïa",
     "L'impact de l'intégration des réseaux sociaux sur les pratiques agricoles : élevage bovin laitier à Ghardaïa"),
]

# Doctoral juries (year, candidate, title_en, title_fr)
PHD_JURIES = [
    ("2026", "Gasmi Ben Salah", "The economic viability of agroforestry in Djelfa: the Senalba Chergui ‘Green Dam’ steppe forest",
     "La viabilité économique des opérations agroforestières à Djelfa : la forêt steppique du Barrage vert de Senalba Chergui"),
    ("2026", "Nadhir Laouar", "The technical innovation system of plasticulture in Biskra: the role of private actors",
     "Système d'innovation technique de la plasticulture à Biskra : le rôle des acteurs privés"),
    ("2026", "Khadidja Baroud", "Implementation and equity of redistributive land policies in Algeria",
     "La politique de mise en valeur foncière : mise en œuvre et équité"),
    ("2025", "Alaeddine Derderi", "Itinerant agricultural entrepreneurs and land and agrarian dynamics in arid Algeria: Rechaïga",
     "Les entrepreneurs agricoles itinérants et les dynamiques foncières et agraires en zones arides : le cas de Rechaïga"),
    ("2024", "Mohamed Amine Ouendeno", "Land markets and agricultural development in the Ziban (Biskra)",
     "Marchés fonciers et développement agricole au Ziban (Biskra)"),
    ("2023", "Wassila Hanafi", "Ex-post evaluation of the PNDAR programme: agricultural land development in Algeria",
     "Évaluation ex-post du programme PNDAR : mise en valeur des terres agricoles en Algérie"),
]
MASTER_JURIES_N = 28           # master's juries 2018–2025 (incl. 4 as president)

# --------------------------------------------------------------------------- consulting
CLIENTS = ["World Bank", "European Union", "FAO", "UNDP", "GIZ", "IDRC", "Horizon Europe", "Humanity & Inclusion"]

CONSULTING = [
    {"p": "2026", "c": "FADERCO · WellTech",
     "t": L("Training and support for start-ups in the green and circular economy.",
            "Formation et accompagnement de start-ups de l'économie verte et circulaire.",
            "تكوين ومرافقة المؤسسات الناشئة في مجال الاقتصاد الأخضر والدائري.")},
    {"p": "2026", "c": "FAO",
     "t": L("Training on market creation and commercialisation of non-timber forest products in Tlemcen, Béjaïa and Jijel.",
            "Formation sur la création de marchés et la commercialisation des produits forestiers non ligneux à Tlemcen, Béjaïa et Jijel.",
            "تكوين حول إنشاء الأسواق وتسويق المنتجات الغابية غير الخشبية في تلمسان وبجاية وجيجل.")},
    {"p": "2025", "c": "UNDP",
     "t": L("Review of risk-financing frameworks and proposal of a risk-financing model for Algeria (Inclusive Insurance project).",
            "Examen des cadres de financement des risques et proposition d'un modèle pour l'Algérie (projet Assurance inclusive).",
            "مراجعة أطر تمويل المخاطر واقتراح نموذج لتمويلها في الجزائر (مشروع التأمين الشامل).")},
    {"p": "2025", "c": "UNDP",
     "t": L("Study of the economic impacts of climate events on cereal production in Algeria.",
            "Étude des impacts économiques des événements climatiques sur la production céréalière en Algérie.",
            "دراسة الآثار الاقتصادية للظواهر المناخية على إنتاج الحبوب في الجزائر.")},
    {"p": "2024", "c": "Horizon Europe · NATAE",
     "t": L("Expert report on cereal public policies in Algeria, with a focus on Sétif.",
            "Rapport d'expertise sur les politiques publiques céréalières en Algérie, focus sur Sétif.",
            "تقرير خبرة حول السياسات العمومية للحبوب في الجزائر مع التركيز على سطيف.")},
    {"p": "2024", "c": "ANVREDET",
     "t": L("Training and coaching in project development and financial structuring for ENSA Incubator award-winners.",
            "Formation et coaching en montage et structuration financière de projets pour les lauréats de l'ENSA Incubator.",
            "تكوين ومرافقة في إعداد المشاريع وهيكلتها المالية لفائدة الفائزين في حاضنة المدرسة.")},
    {"p": "2021 – 2022", "c": "GIZ · EU · AFC",
     "t": L("National consultant for the Agricultural Sector Support Programme (PASA): three multi-stakeholder dialogue platforms in Biskra and El Oued, and a chili-pepper value-chain platform with capacity building in Biskra.",
            "Consultant national du Programme d'appui au secteur de l'agriculture (PASA) : trois plateformes de dialogue multi-acteurs à Biskra et El Oued, et plateforme de la filière piment avec renforcement des capacités à Biskra.",
            "خبير وطني لبرنامج دعم القطاع الفلاحي (PASA): إنشاء ثلاث منصات حوار متعددة الأطراف في بسكرة والوادي، ومنصة لشعبة الفلفل الحار مع تعزيز قدرات الفاعلين في بسكرة.")},
    {"p": "2019", "c": "EU · Humanity & Inclusion",
     "t": L("Identification and analysis of inclusive value chains in Tissemsilt and Saïda (NIDID, PADSEL-NOA).",
            "Identification et analyse des chaînes de valeur inclusives à Tissemsilt et Saïda (NIDID, PADSEL-NOA).",
            "تحديد وتحليل سلاسل القيمة الشاملة في تيسمسيلت وسعيدة (NIDID، PADSEL-NOA).")},
    {"p": "2018 – 2019", "c": "EU · Humanity & Inclusion",
     "t": L("Inclusive value-chain analysis in Skikda and Bouira, Rural Inclusive Development project (ENPARD Algeria).",
            "Analyse des chaînes de valeur inclusives à Skikda et Bouira, projet Développement rural inclusif (ENPARD Algérie).",
            "تحليل سلاسل القيمة الشاملة في سكيكدة والبويرة، مشروع التنمية الريفية الشاملة (ENPARD الجزائر).")},
    {"p": "2018", "c": "EU · AREA-ED",
     "t": L("Territorial diagnosis of vulnerable family farms in Tlemcen National Park: climate-change impacts, diversification and agroecological practices; trained the survey team (ACPP, ENPARD).",
            "Diagnostic territorial des exploitations familiales vulnérables du parc national de Tlemcen : impacts du changement climatique, diversification et pratiques agroécologiques ; formation de l'équipe d'enquêteurs (ACPP, ENPARD).",
            "تشخيص إقليمي للمستثمرات العائلية الهشة في الحظيرة الوطنية بتلمسان: آثار التغير المناخي والتنويع والممارسات الإيكولوجية الزراعية، مع تكوين فريق المحققين (ACPP، ENPARD).")},
    {"p": "2017", "c": "World Bank",
     "t": L("Identification and characterisation of the main agricultural value chains in Sétif (Reimbursable Advisory Services, integrated value chains).",
            "Identification et caractérisation des principales filières agricoles à Sétif (RAS, chaînes de valeur intégrées).",
            "تحديد وتوصيف أهم السلاسل الزراعية في سطيف (خدمات استشارية، سلاسل القيمة المتكاملة).")},
]

NETWORKS = [
    ("2017 –", L("NELGA, Network of Excellence on Land Governance in Africa (African Union, AfDB, UN; funded by GIZ and the World Bank), associate researcher",
                 "NELGA, Réseau d'excellence sur la gouvernance foncière en Afrique (UA, BAD, ONU ; financé par la GIZ et la Banque mondiale), chercheur associé",
                 "NELGA، شبكة التميز حول الحوكمة العقارية في إفريقيا (الاتحاد الإفريقي، البنك الإفريقي للتنمية، الأمم المتحدة)، باحث مشارك")),
    ("2016 –", L("National Cooperation Committee for the Advancement of Strategic Agricultural Sectors (Ministries of Agriculture and Higher Education), advisor",
                 "Comité national de coopération pour le perfectionnement des filières agricoles stratégiques (ministères de l'Agriculture et de l'Enseignement supérieur), conseiller",
                 "اللجنة الوطنية للتعاون من أجل تطوير الشعب الفلاحية الاستراتيجية (وزارتا الفلاحة والتعليم العالي)، مستشار")),
    ("2013 –", L("SIRMA, Irrigation Systems in the Maghreb network (CIRAD), member",
                 "SIRMA, réseau Systèmes irrigués au Maghreb (CIRAD), membre",
                 "SIRMA، شبكة أنظمة السقي في المغرب العربي (CIRAD)، عضو")),
]

# --------------------------------------------------------------------------- talks & media
MEDIA = [
    {"y": "2026", "o": "Radio Algérie · Chaîne 3",
     "t": "Agroecology, value chains and food system transition",
     "url": "https://podcast.radioalgerie.dz/fr/podcasts/Chaine3/1934519", "kind": "audio"},
    {"y": "2025", "o": "Radio Algérie Internationale",
     "t": "Agriculture and local development", "url": "https://www.youtube.com/watch?v=pdUFGNfOcdI", "kind": "video"},
    {"y": "2025", "o": "Radio Algérie Internationale",
     "t": "Innovation and digitalisation in agriculture", "url": "https://www.youtube.com/watch?v=2ZOlbRiivxg", "kind": "video"},
]

# (year, title, event_en, event_fr, event_ar, international?)
TALKS = [
    ("2026", "What is a value chain and why is it relevant for analysing agroecological trajectories?",
     "International Agroecology Research School, NATAE project, Aflou", "École internationale de recherche en agroécologie, projet NATAE, Aflou",
     "المدرسة الدولية للبحث في الإيكولوجيا الزراعية، مشروع NATAE، آفلو", True),
    ("2026", "Groundwater depletion, value chains evolution and neo-agriculture sustainability: lessons from greenhouse tomato farming in Algeria",
     "Knowledge Day, ENSA Algiers", "Journée du savoir, ENSA d'Alger", "يوم العلم، المدرسة الوطنية العليا للفلاحة", False),
    ("2025", "Distribution of margins in neo-agriculture production systems during ‘crisis’",
     "Geographical Sciences Seminar Series, University of Maryland, College Park", "Séminaire du Département des sciences géographiques, Université du Maryland, College Park",
     "سلسلة ندوات قسم العلوم الجغرافية، جامعة ماريلاند، كوليدج بارك", True),
    ("2025", "Enforcing contracts: the role of state subsidies as a hybrid enforcement mechanism in contracts between tomato processors and farmers in Algeria",
     "Knowledge Day, ENSA Algiers", "Journée du savoir, ENSA d'Alger", "يوم العلم، المدرسة الوطنية العليا للفلاحة", False),
    ("2024", "Distribution of margins in neo-agriculture supply chains: what impact of water, land and economic ‘crisis’?",
     "Knowledge Day, ENSA Algiers", "Journée du savoir, ENSA d'Alger", "يوم العلم، المدرسة الوطنية العليا للفلاحة", False),
    ("2024", "La faculté et les moyens d'inciter les agriculteurs à adopter des systèmes de production plus résilients",
     "Cayrovision, Club Agronova", "Cayrovision, Club Agronova", "كايروفيزيون، نادي أغرونوفا", False),
    ("2023", "State subsidies as a hybrid contract enforcement mechanism in Algerian tomato value chains: an alternative where public courts and private companies fail?",
     "5th National Seminar “Agricultural Sciences Day”, ENSA", "5e séminaire national « Journée des sciences agronomiques », ENSA",
     "الملتقى الوطني الخامس «يوم العلوم الفلاحية»، المدرسة الوطنية العليا للفلاحة", False),
    ("2023", "Les légumineuses en Algérie : rôle, forces et limites",
     "World Legume Day, EcoClub", "Journée mondiale des légumineuses, EcoClub", "اليوم العالمي للبقوليات، إيكوكلوب", False),
    ("2022", "La gouvernance des filières agricoles et agroalimentaires : cadre théorique et pratique",
     "Doctoral Days, Laboratory of Agricultural, Agrifood, Rural and Environmental Economics, ENSA",
     "Journées doctorales, Laboratoire d'économie agricole, agroalimentaire, rurale et de l'environnement, ENSA",
     "الأيام الدكتورالية، مخبر الاقتصاد الزراعي والغذائي والريفي والبيئي", False),
    ("2022", "Effets de la dynamique foncière sur l'utilisation des ressources naturelles",
     "National Seminar “Agricultural Sciences Day”, ENSA", "Séminaire national « Journée des sciences agronomiques », ENSA",
     "الملتقى الوطني «يوم العلوم الفلاحية»، المدرسة الوطنية العليا للفلاحة", False),
    ("2021", "L'impact mitigé d'un dispositif contractuel public-privé sur les revenus des agriculteurs : la filière tomate industrielle en Algérie",
     "3rd National Seminar “Agricultural Sciences Day”, ENSA", "3e séminaire national « Journée des sciences agronomiques », ENSA",
     "الملتقى الوطني الثالث «يوم العلوم الفلاحية»، المدرسة الوطنية العليا للفلاحة", False),
    ("2021–22", "Analyse financière des projets d'investissement",
     "Global Entrepreneurship Week, ENSA Incubator", "Semaine mondiale de l'entrepreneuriat, ENSA Incubator",
     "الأسبوع العالمي للمقاولاتية، حاضنة المدرسة", False),
    ("2021", "L'entrepreneuriat dans le secteur agricole : de vastes opportunités",
     "Webinar “Entrepreneurship ENSA-style”, ENSA Incubator", "Webinaire « L'entrepreneuriat en mode ENSA », ENSA Incubator",
     "ندوة رقمية «المقاولاتية على طريقة المدرسة»، حاضنة المدرسة", False),
    ("2018", "Research on land governance: the agricultural economics team at ENSA Algiers",
     "1st International Seminar of NELGA (AU, AfDB, GIZ, World Bank, UN), Rabat, Morocco",
     "1er séminaire international du réseau NELGA (UA, BAD, GIZ, Banque mondiale, ONU), Rabat, Maroc",
     "الملتقى الدولي الأول لشبكة NELGA (الاتحاد الإفريقي، البنك الإفريقي للتنمية، GIZ، البنك الدولي، الأمم المتحدة)، الرباط، المغرب", True),
    ("2017", "L'agriculture contractuelle en Algérie : radiographie de dispositifs public-privé",
     "33rd Development Days of the Third World Association, Université libre de Bruxelles, Belgium",
     "33es Journées du développement de l'Association tiers-monde, Université libre de Bruxelles, Belgique",
     "أيام التنمية الثالثة والثلاثون لجمعية العالم الثالث، جامعة بروكسل الحرة، بلجيكا", True),
    ("2017", "Quelles questions foncières en économie agricole ?",
     "1st North Africa Consultative Workshop of NELGA, Rabat, Morocco", "1er atelier consultatif Afrique du Nord du réseau NELGA, Rabat, Maroc",
     "الورشة التشاورية الأولى لشمال إفريقيا لشبكة NELGA، الرباط، المغرب", True),
    ("2015", "L'agriculture contractuelle en Algérie : un moyen d'intégration des petits exploitants ?",
     "Land course “Introduction to land issues”, ENSA & Montpellier Land Tenure Hub", "Cours foncier « Introduction à la problématique foncière », ENSA & Pôle foncier de Montpellier",
     "الدورة العقارية «مدخل إلى الإشكالية العقارية»، المدرسة الوطنية العليا للفلاحة وقطب العقار بمونبلييه", True),
    ("2015", "Les profits excessifs des commerçants de fruits et légumes en Algérie, une réalité ou un préjugé infondé ? Le cas de la tomate primeur de Biskra",
     "2nd International Seminar on Groundwater Governance in the Maghreb, Tunis, Tunisia", "2e séminaire international sur la gouvernance des eaux souterraines au Maghreb, Tunis, Tunisie",
     "الملتقى الدولي الثاني حول حوكمة المياه الجوفية في المغرب العربي، تونس", True),
    ("2013", "La plasticulture à El Ghrous : dynamique et facteurs d'évolution",
     "1st International Seminar on Groundwater Governance in the Maghreb, Biskra, Algeria", "1er séminaire international sur la gouvernance des eaux souterraines au Maghreb, Biskra, Algérie",
     "الملتقى الدولي الأول حول حوكمة المياه الجوفية في المغرب العربي، بسكرة، الجزائر", True),
]

WORKSHOPS = [
    ("2025", L("Expert, thematic workshops on the Agricultural Sector Support Programme (PASA+), Ministry of Agriculture and Italian Agency for Development Cooperation (AICS)",
               "Expert, ateliers thématiques sur le Programme d'appui au secteur de l'agriculture (PASA+), ministère de l'Agriculture et AICS",
               "خبير، ورشات موضوعاتية حول برنامج دعم القطاع الفلاحي (PASA+)، وزارة الفلاحة والوكالة الإيطالية للتعاون الإنمائي")),
    ("2023", L("Expert, thematic reflection workshops on Algerian agriculture, Ministry of Agriculture",
               "Expert, ateliers de réflexion thématiques sur l'agriculture algérienne, ministère de l'Agriculture",
               "خبير، ورشات تفكير موضوعاتية حول الفلاحة الجزائرية، وزارة الفلاحة")),
    ("2021", L("ENSA representative, review of the statutes of agricultural technical bodies, Ministry of Agriculture and Rural Development",
               "Représentant de l'ENSA, examen du statut des corps techniques de l'administration de l'agriculture, MADR",
               "ممثل المدرسة، دراسة القانون الأساسي للأسلاك التقنية لإدارة الفلاحة، وزارة الفلاحة والتنمية الريفية")),
    ("2019", L("Research consultant, multi-stakeholder workshop on the professionalisation of palm climbers (AREA-ED, BEDE)",
               "Chercheur-consultant, atelier multi-acteurs « Professionnalisation des grimpeurs de palmiers » (AREA-ED, BEDE)",
               "باحث مستشار، ورشة متعددة الأطراف حول احترافية متسلقي النخيل (AREA-ED، BEDE)")),
    ("2018", L("Organiser, multi-stakeholder workshop on the new generation of public–private agricultural contracts, Algiers",
               "Organisateur, atelier multi-acteurs sur la nouvelle génération de contrats agricoles public-privé, Alger",
               "منظم، ورشة متعددة الأطراف حول الجيل الجديد من العقود الفلاحية بين القطاعين العام والخاص، الجزائر")),
    ("2016", L("Organiser, multi-stakeholder workshop on agricultural contracts with researchers, processors and farmers, Guelma",
               "Organisateur, atelier multi-acteurs sur les contrats agricoles avec chercheurs, industriels et agriculteurs, Guelma",
               "منظم، ورشة متعددة الأطراف حول العقود الفلاحية مع الباحثين والمصنّعين والفلاحين، قالمة")),
]

EVENTS = [
    ("2026", L("Organising committee, International Agroecology Research School, Aflou (NATAE)",
               "Comité d'organisation, École internationale de recherche en agroécologie, Aflou (NATAE)",
               "لجنة التنظيم، المدرسة الدولية للبحث في الإيكولوجيا الزراعية، آفلو (NATAE)")),
    ("2026", L("Scientific committee, national seminar “Animal production sectors in Algeria”, ENSA & INRA",
               "Comité scientifique, séminaire national « Filières de production animale en Algérie », ENSA & INRA",
               "اللجنة العلمية، الملتقى الوطني «شعب الإنتاج الحيواني في الجزائر»، المدرسة والمعهد الوطني للبحث الزراعي")),
    ("2025", L("Organising committee, NATAE field school, Sétif", "Comité d'organisation, école de terrain NATAE, Sétif",
               "لجنة التنظيم، المدرسة الميدانية NATAE، سطيف")),
    ("2021, 2025", L("Organising committee, international “Doctoral Days on Land Tenure”, ENSA & Montpellier Land Tenure Hub",
                     "Comité d'organisation, séminaire international « Journées doctorales foncier », ENSA & Pôle foncier de Montpellier",
                     "لجنة التنظيم، الملتقى الدولي «الأيام الدكتورالية حول العقار»، المدرسة وقطب العقار بمونبلييه")),
    ("2023", L("Chair, national seminar “Marketing of agricultural and agrifood products”", "Président, séminaire national « Le marketing des produits agricoles et agroalimentaires »",
               "رئيس لجنة التنظيم، الملتقى الوطني «تسويق المنتجات الزراعية والغذائية»")),
    ("2022", L("Chair, national seminar “Agricultural and agrifood development facing food-security challenges”",
               "Président, séminaire national « Le développement agricole et agroalimentaire face aux défis de la sécurité alimentaire »",
               "رئيس لجنة التنظيم، الملتقى الوطني «التنمية الزراعية والغذائية في مواجهة تحديات الأمن الغذائي»")),
    ("2023", L("Organising committee, international seminar, International Numidian Agriculture Fair, Constantine",
               "Comité d'organisation, séminaire international du Salon international de l'agriculture numide, Constantine",
               "لجنة التنظيم، الملتقى الدولي للمعرض الدولي للفلاحة النوميدية، قسنطينة")),
    ("2021 – 2023", L("Organising committee, 3rd–5th national seminars “Agricultural Sciences Day”, ENSA",
                      "Comité d'organisation, 3e–5e séminaires nationaux « Journée des sciences agronomiques », ENSA",
                      "لجنة التنظيم، الملتقيات الوطنية 3–5 «يوم العلوم الفلاحية»، المدرسة")),
    ("2021 – 2024", L("Organising committee, Global Entrepreneurship Week (1st–4th editions), ENSA Incubator",
                      "Comité d'organisation, Semaine mondiale de l'entrepreneuriat (1re–4e éditions), ENSA Incubator",
                      "لجنة التنظيم، الأسبوع العالمي للمقاولاتية (الطبعات 1–4)، حاضنة المدرسة")),
]

# --------------------------------------------------------------------------- CV
POSITIONS = [
    {"p": "2026 –", "t": L("Adjunct Professor", "Professeur auxiliaire", "أستاذ منتسب"),
     "o": L("Faculty of Humanities and Philosophy, Saint Paul University, Ottawa",
            "Faculté des sciences humaines et de philosophie, Université Saint-Paul, Ottawa",
            "كلية العلوم الإنسانية والفلسفة، جامعة سانت بول، أوتاوا"),
     "d": L("Lectures, applied research projects and expert panels in agribusiness.",
            "Conférences, projets de recherche appliquée et panels d'experts en agrobusiness.",
            "محاضرات ومشاريع بحث تطبيقي ولجان خبراء في مجال الأعمال الزراعية.")},
    {"p": "2018 – 2026", "t": L("Teacher-researcher", "Enseignant-chercheur", "أستاذ باحث"),
     "o": L("National Higher School of Agronomy (ENSA), Algiers", "École nationale supérieure agronomique (ENSA), Alger",
            "المدرسة الوطنية العليا للفلاحة، الجزائر العاصمة"),
     "d": L("Courses from undergraduate to Ph.D. level, thesis supervision, research and administration. "
            "Director of the Laboratory of Agricultural, Agrifood, Rural and Environmental Economics (2023–2025).",
            "Enseignement du premier cycle au doctorat, encadrement, recherche et administration. "
            "Directeur du Laboratoire d'économie agricole, agroalimentaire, rurale et de l'environnement (2023–2025).",
            "التدريس من التدرج إلى الدكتوراه، والإشراف على المذكرات، والبحث والإدارة. "
            "مدير مخبر الاقتصاد الزراعي والغذائي والريفي والبيئي (2023–2025).")},
    {"p": "2017 –", "t": L("Expert consultant", "Expert-consultant", "خبير استشاري"),
     "o": L("World Bank, European Union, FAO, UNDP, GIZ", "Banque mondiale, Union européenne, FAO, PNUD, GIZ",
            "البنك الدولي، الاتحاد الأوروبي، الفاو، برنامج الأمم المتحدة الإنمائي، GIZ"),
     "d": L("Technical and scientific advice, strategic planning, financial management, training and MEAL for international cooperation projects.",
            "Conseil technico-scientifique, planification stratégique, gestion financière, formation et suivi-évaluation (SEAR) de projets de coopération.",
            "استشارة تقنية وعلمية، وتخطيط استراتيجي، وتسيير مالي، وتكوين، ومتابعة وتقييم لمشاريع التعاون الدولي.")},
    {"p": "2014 – 2018", "t": L("Associate researcher", "Chercheur associé", "باحث مشارك"),
     "o": L("IDRC (Canada) / ENSA Algiers", "CRDI (Canada) / ENSA d'Alger", "المركز الكندي لبحوث التنمية الدولية / المدرسة الوطنية العليا للفلاحة"),
     "d": L("Co-led the socio-economic analysis of contract farming and its effect on smallholder inclusion.",
            "Co-direction de l'analyse socio-économique de l'agriculture contractuelle et de ses effets sur l'inclusion des petits producteurs.",
            "شارك في قيادة التحليل الاجتماعي والاقتصادي للزراعة التعاقدية وأثرها على إدماج صغار المنتجين.")},
]

EDUCATION = [
    {"y": "2021", "t": L("Habilitation to Supervise Research (HDR), Agricultural Sciences – Agricultural Economics",
                         "Habilitation universitaire à diriger des recherches (HDR), sciences agronomiques – économie agricole",
                         "التأهيل الجامعي لإدارة البحوث، العلوم الفلاحية – الاقتصاد الزراعي"),
     "o": L("ENSA, Algiers", "ENSA d'Alger", "المدرسة الوطنية العليا للفلاحة، الجزائر"), "x": None, "h": None},
    {"y": "2017", "t": L("Ph.D., Agrifood and Rural Economics", "Doctorat en économie agroalimentaire et rurale", "دكتوراه في الاقتصاد الغذائي والريفي"),
     "o": L("ENSA, Algiers", "ENSA d'Alger", "المدرسة الوطنية العليا للفلاحة، الجزائر"),
     "x": L("Contract farming in the industrial tomato sector: actor logics and performance effects. The case of the Amor Benamor Cannery (CAB), Guelma, Algeria.",
            "L'agriculture contractuelle dans la filière tomate industrielle : logiques d'acteurs et effets sur leurs performances. Cas de la Conserverie Amor Benamor (CAB), wilaya de Guelma (Algérie).",
            "الزراعة التعاقدية في شعبة الطماطم الصناعية: منطق الفاعلين وآثارها على أدائهم. حالة مصبرة عمر بن عمر، ولاية قالمة، الجزائر."),
     "h": L("Highest honours with jury commendation", "Mention très honorable avec félicitations du jury", "بدرجة مشرف جداً مع تهنئة اللجنة")},
    {"y": "2013", "t": L("Master's, Agrifood Business Management", "Master en management des entreprises agroalimentaires", "ماستر في تسيير المؤسسات الغذائية"),
     "o": L("ENSA, Algiers", "ENSA d'Alger", "المدرسة الوطنية العليا للفلاحة، الجزائر"),
     "x": L("Price volatility of fresh agricultural products in Algeria: early tomatoes in El Ghrous, Biskra.",
            "La volatilité des prix des produits agricoles frais en Algérie : la tomate primeur d'El Ghrous, Biskra.",
            "تقلب أسعار المنتجات الزراعية الطازجة في الجزائر: الطماطم المبكرة في الغروس، بسكرة."),
     "h": L("Highest distinction", "Mention très bien", "بتقدير ممتاز")},
    {"y": "2013", "t": L("State Engineer, Agrifood Business Management", "Ingénieur d'État en gestion des entreprises agroalimentaires", "مهندس دولة في تسيير المؤسسات الغذائية"),
     "o": L("ENSA, Algiers", "ENSA d'Alger", "المدرسة الوطنية العليا للفلاحة، الجزائر"),
     "x": L("The functioning of the El Ghrous wholesale fruit and vegetable market, Biskra.",
            "Étude du fonctionnement du marché de gros de fruits et légumes d'El Ghrous, Biskra.",
            "دراسة سير سوق الجملة للخضر والفواكه بالغروس، بسكرة."),
     "h": L("Highest distinction", "Mention très bien", "بتقدير ممتاز")},
]

TRAINING = [
    ("2025", L("Remote sensing for agricultural and regional development", "Télédétection appliquée au développement agricole et régional", "الاستشعار عن بعد في خدمة التنمية الزراعية والجهوية"), "University of Maryland"),
    ("2023", L("Modelling for impact assessment", "Modélisation pour l'évaluation d'impact", "النمذجة لتقييم الأثر"), "UMR G-EAU & IAMM, Montpellier"),
    ("2018–19", L("University pedagogy and ICT in teaching", "Pédagogie universitaire et TIC", "البيداغوجيا الجامعية وتكنولوجيات الإعلام والاتصال"), "Univ. Algiers 1 · Univ. Constantine 1"),
    ("2017", L("Scientific writing in English (M. Kuper, D. Goodfellow)", "Rédaction scientifique en anglais (M. Kuper, D. Goodfellow)", "الكتابة العلمية بالإنجليزية (م. كوبر، د. غودفيلو)"), "CIRAD, Meknès"),
    ("2015", L("Research methodology in agricultural economics (J.-Ph. Colin)", "Méthodologie de recherche en économie agricole (J.-Ph. Colin)", "منهجية البحث في الاقتصاد الزراعي (ج.-ف. كولان)"), "ISTOM · IRD, Paris"),
    ("2015", L("Data Envelopment Analysis (C. Bignebat)", "Data Envelopment Analysis (C. Bignebat)", "تحليل مغلف البيانات (س. بينيبا)"), "UMR DIAL · INRAE"),
    ("2014", L("Land tenure issues", "Initiation à la question foncière", "مدخل إلى المسألة العقارية"), "ENSA & Montpellier Land Tenure Hub"),
]

ADMIN = [
    ("2023 – 2025", L("Director, Laboratory of Agricultural, Agrifood, Rural and Environmental Economics", "Directeur, Laboratoire d'économie agricole, agroalimentaire, rurale et de l'environnement", "مدير مخبر الاقتصاد الزراعي والغذائي والريفي والبيئي")),
    ("2023 – 2024", L("Interim Head, Department of Rural Economics (three terms)", "Chef du département d'économie rurale par intérim (trois fois)", "رئيس قسم الاقتصاد الريفي بالنيابة (ثلاث مرات)")),
    ("2021 – 2026", L("Member, Scientific Council of ENSA", "Membre du Conseil scientifique de l'ENSA", "عضو المجلس العلمي للمدرسة")),
    ("2018 – 2026", L("President, Pedagogical Committee, Department of Rural Economics", "Président du comité pédagogique du département d'économie rurale", "رئيس اللجنة البيداغوجية لقسم الاقتصاد الريفي")),
    ("2020 – 2026", L("Founding member and management team, ENSA Incubator", "Membre fondateur et équipe de direction, ENSA Incubator", "عضو مؤسس وعضو فريق إدارة حاضنة المدرسة")),
    ("2022 – 2026", L("Committee for the national programme “One thesis, one start-up”", "Comité ENSA du programme « Un mémoire, une startup »", "لجنة المدرسة لبرنامج «مذكرة تخرج – مؤسسة ناشئة»")),
    ("2025 – 2026", L("ENSA Erasmus unit", "Cellule Erasmus de l'ENSA", "خلية إيراسموس بالمدرسة")),
]

LANGS = [
    (L("Arabic", "Arabe", "العربية"), L("Native", "Langue maternelle", "اللغة الأم")),
    (L("Tamazight", "Tamazight", "الأمازيغية"), L("Native", "Langue maternelle", "اللغة الأم")),
    (L("French", "Français", "الفرنسية"), L("Advanced, certified", "Avancé, certifié", "متقدم، بشهادة")),
    (L("English", "Anglais", "الإنجليزية"), L("Advanced, certified", "Avancé, certifié", "متقدم، بشهادة")),
]

METHODS = L(
    ["Value-chain & margin analysis", "Contract & institutional economics", "Impact evaluation", "Econometrics",
     "Data Envelopment Analysis", "Investment project appraisal", "MEAL", "Multi-stakeholder platforms"],
    ["Analyse de filières & de marges", "Économie des contrats & institutions", "Évaluation d'impact", "Économétrie",
     "Data Envelopment Analysis", "Évaluation de projets d'investissement", "Suivi-évaluation (SEAR)", "Plateformes multi-acteurs"],
    ["تحليل سلاسل القيمة والهوامش", "اقتصاد العقود والمؤسسات", "تقييم الأثر", "الاقتصاد القياسي",
     "تحليل مغلف البيانات", "تقييم مشاريع الاستثمار", "المتابعة والتقييم", "منصات الحوار متعددة الأطراف"])
SOFTWARE = ["Stata", "SPSS", "EViews", "XLSTAT", "Power BI", "ENVI EX", "Generative AI"]

# --------------------------------------------------------------------------- news (home page)
NEWS = [
    ("2026", L("Appointed Adjunct Professor at Saint Paul University, Ottawa.",
               "Nommé professeur auxiliaire à l'Université Saint-Paul, Ottawa.",
               "تعيينه أستاذاً منتسباً في جامعة سانت بول بأوتاوا.")),
    ("2026", L("Two articles accepted: Journal of Development Studies and Agribusiness.",
               "Deux articles acceptés : Journal of Development Studies et Agribusiness.",
               "قبول مقالين للنشر في ⁦Journal of Development Studies⁩ و⁦Agribusiness⁩.")),
    ("2026", L("Lecturer and co-organiser, NATAE International Agroecology Research School, Aflou.",
               "Intervenant et co-organisateur, École internationale de recherche en agroécologie NATAE, Aflou.",
               "محاضر وعضو في تنظيم المدرسة الدولية للبحث في الإيكولوجيا الزراعية NATAE، آفلو.")),
    ("2026", L("Interview on Radio Algérie Chaîne 3: agroecology, value chains and food-system transition.",
               "Entretien sur la Chaîne 3 : agroécologie, filières et transition des systèmes alimentaires.",
               "حوار على القناة الإذاعية الثالثة: الإيكولوجيا الزراعية وسلاسل القيمة وتحول النظم الغذائية.")),
    ("2025", L("Research stay and seminar at the University of Maryland, College Park.",
               "Séjour de recherche et séminaire à l'Université du Maryland, College Park.",
               "إقامة بحثية وندوة في جامعة ماريلاند، كوليدج بارك.")),
]
