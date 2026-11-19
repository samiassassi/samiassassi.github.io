"""Build the static trilingual site into docs/ (GitHub Pages).

    python build.py

English pages at the root, French in fr/, Arabic (RTL) in ar/.
Text lives in content.py; layout and interface strings live here; styles in assets/style.css.
"""
import json
import re
import shutil
from html import escape
from pathlib import Path

import content as C

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "docs"
SITE_URL = "https://samiassassi.github.io"   # GitHub Pages address (org "samiassassi"); used for hreflang links
LANGS = ["en", "fr", "ar"]
PAGES = ["index", "research", "publications", "teaching", "advisory", "talks", "cv"]
YEAR = "2026"

# --------------------------------------------------------------------------- interface strings
T = {
 "en": {
  "nav": {"research": "Research", "publications": "Publications", "teaching": "Teaching", "advisory": "Advisory",
          "talks": "Talks & Media", "cv": "CV"},
  "title": {"index": "Agricultural economist", "research": "Research", "publications": "Publications",
            "teaching": "Teaching & supervision", "advisory": "Policy & development advisory",
            "talks": "Talks & media", "cv": "Curriculum vitae"},
  "contact": "Contact", "menu": "Menu", "theme": "Switch light / dark theme", "lang": "Language",
  "skip": "Skip to content",
  "btn_pubs": "Publications", "btn_cv": "Curriculum vitae", "btn_contact": "Get in touch",
  "now": "Now", "formerly": "Formerly", "based": "Based in",
  "stats": ["peer-reviewed journal articles", "advisory missions for international organisations",
            "master's theses supervised", "Algerian wilayas of fieldwork and advisory work"],
  "chain_k": "Research programme", "chain_h": "Research along the value chain",
  "chain_p": "Five links in the agrifood chain. Select one to see the related work.",
  "chain_more": "See the research", "chain_pubs": "Selected work",
  "sel_k": "Publications", "sel_h": "Recent and forthcoming", "all_pubs": "All publications",
  "clients_k": "Advisory work", "news_k": "Latest", "news_h": "News",
  "about_k": "About", "about_h": "Profile",
  "contact_h": "Get in touch",
  "contact_p": "Research collaboration, teaching, expert panels and advisory missions.",
  "email": "Email", "orcid": "ORCID", "scholar": "Google Scholar", "linkedin": "LinkedIn", "researchgate": "ResearchGate",
  "pages": "Pages", "rights": "All rights reserved.",
  # research
  "r_intro": "My work follows value along agricultural and agrifood chains in North Africa: who holds land and water, how farms perform, how contracts between farmers and agro-industry are designed and enforced, who captures margins in markets, and how cities and public buyers source food.",
  "r_themes": "Research themes", "r_q": "Question", "r_projects": "Research projects", "r_pubs": "Publications",
  "r_map_k": "Algeria", "r_map_h": "Fieldwork and missions",
  "r_map_p": "Wilayas covered by my research and advisory work. Hover or tap for details.",
  "r_map_r": "Research", "r_map_c": "Advisory missions",
  "r_map_src": "Boundaries: FEWS NET administrative units (48 wilayas, 2021). Northern Algeria shown.",
  "abs": "Abstract", "kw": "Keywords", "jel": "JEL",
  "kw_v": "contract farming; agrifood value chains; marketing margins; land and water markets; agricultural policy; North Africa",
  "eq_cap": "The farm-to-retail price spread: the consumer price equals the farm-gate price plus the margin taken at each link k of the chain. Who captures these margins, and why, runs through his research.",
  "fig": "Figure",
  "f_pos": "Position", "f_prev": "Previously",
  "f_prev_v": "Teacher-researcher, ENSA Algiers (2018–2026); Director, Laboratory of Agricultural, Agrifood, Rural and Environmental Economics (2023–2025)",
  "f_deg": "Degrees", "f_deg_v": "Ph.D., Agrifood and Rural Economics (2017) · HDR, Agricultural Economics (2021) · ENSA Algiers",
  "f_rec": "Record", "f_record": "{a} journal articles ({f} forthcoming) · {m} master's theses supervised · {j} doctoral juries · {s} advisory missions",
  "f_adv": "Advisory work for", "f_lang": "Languages",
  "map_cap": "Fieldwork and advisory missions in {n} wilayas, 2012–2026", "map_more": "Details by wilaya",
  "r_net_k": "International network", "r_net_h": "Research stays and collaborations",
  # publications
  "p_intro": "Peer-reviewed articles, book chapters and papers. Titles are given in their original language.",
  "p_filter": "Filter by theme", "p_all": "All", "p_forth": "Forthcoming", "p_review": "Under review",
  "p_count": "items", "p_doi": "DOI", "p_cite": "Copy citation", "p_copied": "Citation copied",
  "p_reviewer": "Peer review", "p_reviewer_p": "Reviewer for international journals:",
  "st_forth": "Forthcoming", "st_review": "Under review", "k_chapter": "Book chapter", "k_paper": "Conference paper",
  # teaching
  "t_intro": "Eight years of teaching at ENSA Algiers, from the undergraduate common core to the doctoral programme, with a focus on agribusiness management, project appraisal and value-chain governance.",
  "t_courses": "Courses taught", "t_hours": "h", "t_since": "since",
  "t_sup": "Supervision", "t_phd": "Doctoral supervision", "t_ma": "Master's theses supervised",
  "t_juries": "Thesis juries", "t_phd_j": "Doctoral juries",
  "t_ma_j": "master's thesis juries, 2018–2025, four of them as president.",
  "t_orig": "Thesis titles in English translation.", "t_orig_fr": "",
  # advisory
  "a_intro": "Since 2017 I have advised international cooperation programmes on value-chain development, climate-risk financing, multi-stakeholder dialogue and monitoring, evaluation, accountability and learning (MEAL).",
  "a_missions": "Selected missions", "a_clients": "Institutions", "a_workshops": "Policy workshops",
  "a_networks": "Networks & advisory committees", "a_coach": "Entrepreneurship coaching",
  "a_coach_p": "Since 2021: coaching student teams on entrepreneurship and financial analysis (Global Entrepreneurship Week, ENSA Incubator) and training start-ups in project development (national programme “One thesis, one start-up”).",
  # talks
  "m_intro": "Invited lectures, seminars and conference presentations, and interviews on agriculture, value chains and food systems.",
  "m_media": "Media", "m_listen": "Listen", "m_watch": "Watch", "m_talks": "Talks & lectures",
  "m_intl": "International", "m_events": "Scientific events organised",
  # cv
  "c_intro": "A summary of positions, degrees and service. A full CV is available on request.",
  "c_pos": "Positions", "c_edu": "Education", "c_thesis": "Thesis", "c_train": "Selected training",
  "c_admin": "Academic leadership & service", "c_lang": "Languages", "c_methods": "Methods", "c_soft": "Software",
  "c_print": "Print / save as PDF", "c_request": "Request full CV",
  "wes": "Ph.D. and HDR validated by WES for Canada.",
 },
 "fr": {
  "nav": {"research": "Recherche", "publications": "Publications", "teaching": "Enseignement", "advisory": "Expertise",
          "talks": "Conférences & médias", "cv": "CV"},
  "title": {"index": "Économiste agricole", "research": "Recherche", "publications": "Publications",
            "teaching": "Enseignement & encadrement", "advisory": "Expertise & conseil",
            "talks": "Conférences & médias", "cv": "Curriculum vitae"},
  "contact": "Contact", "menu": "Menu", "theme": "Basculer thème clair / sombre", "lang": "Langue",
  "skip": "Aller au contenu",
  "btn_pubs": "Publications", "btn_cv": "Curriculum vitae", "btn_contact": "Me contacter",
  "now": "Actuellement", "formerly": "Auparavant", "based": "Basé à",
  "stats": ["articles dans des revues à comité de lecture", "missions d'expertise pour des organisations internationales",
            "mémoires de master encadrés", "wilayas algériennes de terrain et d'expertise"],
  "chain_k": "Programme de recherche", "chain_h": "La recherche le long de la filière",
  "chain_p": "Cinq maillons de la filière. Sélectionnez-en un pour voir les travaux associés.",
  "chain_more": "Voir la recherche", "chain_pubs": "Travaux choisis",
  "sel_k": "Publications", "sel_h": "Récentes et à paraître", "all_pubs": "Toutes les publications",
  "clients_k": "Expertise", "news_k": "Actualités", "news_h": "Actualités",
  "about_k": "À propos", "about_h": "Profil",
  "contact_h": "Contact",
  "contact_p": "Collaboration de recherche, enseignement, panels d'experts ou missions de conseil.",
  "email": "E-mail", "orcid": "ORCID", "scholar": "Google Scholar", "linkedin": "LinkedIn", "researchgate": "ResearchGate",
  "pages": "Pages", "rights": "Tous droits réservés.",
  "r_intro": "Mes travaux suivent la valeur le long des filières agricoles et agroalimentaires en Afrique du Nord : qui détient la terre et l'eau, ce qui fait la performance des exploitations, comment les contrats entre agriculteurs et agro-industrie sont conçus et exécutés, qui capte les marges sur les marchés, et comment les villes et les acheteurs publics s'approvisionnent.",
  "r_themes": "Axes de recherche", "r_q": "Question", "r_projects": "Projets de recherche", "r_pubs": "Publications",
  "r_map_k": "Algérie", "r_map_h": "Terrains et missions",
  "r_map_p": "Wilayas couvertes par mes recherches et missions d'expertise. Survolez ou touchez pour le détail.",
  "r_map_r": "Recherche", "r_map_c": "Missions d'expertise",
  "r_map_src": "Limites : unités administratives FEWS NET (48 wilayas, 2021). Nord de l'Algérie.",
  "abs": "Résumé", "kw": "Mots-clés", "jel": "JEL",
  "kw_v": "agriculture contractuelle ; filières agroalimentaires ; marges de commercialisation ; marchés fonciers et de l'eau ; politique agricole ; Afrique du Nord",
  "eq_cap": "L'écart de prix du champ au détail : le prix au consommateur égale le prix à la production plus la marge prélevée à chaque maillon k de la filière. Qui capte ces marges, et pourquoi, traverse ses recherches.",
  "fig": "Figure",
  "f_pos": "Fonction", "f_prev": "Auparavant",
  "f_prev_v": "Enseignant-chercheur, ENSA d'Alger (2018–2026) ; directeur du Laboratoire d'économie agricole, agroalimentaire, rurale et de l'environnement (2023–2025)",
  "f_deg": "Diplômes", "f_deg_v": "Doctorat en économie agroalimentaire et rurale (2017) · HDR, économie agricole (2021) · ENSA d'Alger",
  "f_rec": "Bilan", "f_record": "{a} articles de revues ({f} à paraître) · {m} mémoires de master encadrés · {j} jurys de doctorat · {s} missions d'expertise",
  "f_adv": "Expertise pour", "f_lang": "Langues",
  "map_cap": "Terrains et missions d'expertise dans {n} wilayas, 2012–2026", "map_more": "Détail par wilaya",
  "r_net_k": "Réseau international", "r_net_h": "Séjours de recherche et collaborations",
  "p_intro": "Articles à comité de lecture, chapitres d'ouvrage et communications. Les titres sont donnés dans leur langue d'origine.",
  "p_filter": "Filtrer par axe", "p_all": "Tout", "p_forth": "À paraître", "p_review": "En évaluation",
  "p_count": "références", "p_doi": "DOI", "p_cite": "Copier la référence", "p_copied": "Référence copiée",
  "p_reviewer": "Évaluation par les pairs", "p_reviewer_p": "Évaluateur pour des revues internationales :",
  "st_forth": "À paraître", "st_review": "En évaluation", "k_chapter": "Chapitre d'ouvrage", "k_paper": "Communication",
  "t_intro": "Huit années d'enseignement à l'ENSA d'Alger, du tronc commun au doctorat, centrées sur la gestion des entreprises agricoles, l'évaluation de projets et la gouvernance des filières.",
  "t_courses": "Cours dispensés", "t_hours": "h", "t_since": "depuis",
  "t_sup": "Encadrement", "t_phd": "Encadrement doctoral", "t_ma": "Mémoires de master encadrés",
  "t_juries": "Jurys de thèse", "t_phd_j": "Jurys de doctorat",
  "t_ma_j": "jurys de mémoires de master, 2018–2025, dont quatre en qualité de président.",
  "t_orig": "", "t_orig_fr": "",
  "a_intro": "Depuis 2017, je conseille des programmes de coopération internationale en développement de filières, financement des risques climatiques, dialogue multi-acteurs et suivi-évaluation (SEAR).",
  "a_missions": "Missions choisies", "a_clients": "Institutions", "a_workshops": "Ateliers de politique publique",
  "a_networks": "Réseaux & comités consultatifs", "a_coach": "Accompagnement entrepreneurial",
  "a_coach_p": "Depuis 2021 : coaching d'équipes étudiantes en entrepreneuriat et analyse financière (Semaine mondiale de l'entrepreneuriat, ENSA Incubator) et formation de start-ups au montage de projets (programme « Un mémoire, une startup »).",
  "m_intro": "Conférences invitées, séminaires, communications et entretiens sur l'agriculture, les filières et les systèmes alimentaires.",
  "m_media": "Médias", "m_listen": "Écouter", "m_watch": "Regarder", "m_talks": "Conférences & communications",
  "m_intl": "International", "m_events": "Événements scientifiques organisés",
  "c_intro": "Synthèse des fonctions, diplômes et responsabilités. CV complet disponible sur demande.",
  "c_pos": "Fonctions", "c_edu": "Formation", "c_thesis": "Thèse", "c_train": "Formations complémentaires",
  "c_admin": "Responsabilités académiques", "c_lang": "Langues", "c_methods": "Méthodes", "c_soft": "Logiciels",
  "c_print": "Imprimer / PDF", "c_request": "Demander le CV complet",
  "wes": "Doctorat et HDR validés par WES pour le Canada.",
 },
 "ar": {
  "nav": {"research": "البحث", "publications": "المنشورات", "teaching": "التدريس", "advisory": "الخبرة",
          "talks": "المداخلات والإعلام", "cv": "السيرة الذاتية"},
  "title": {"index": "باحث في الاقتصاد الزراعي", "research": "البحث", "publications": "المنشورات",
            "teaching": "التدريس والإشراف", "advisory": "الخبرة والاستشارة",
            "talks": "المداخلات والإعلام", "cv": "السيرة الذاتية"},
  "contact": "تواصل", "menu": "القائمة", "theme": "تبديل الوضع الفاتح / الداكن", "lang": "اللغة",
  "skip": "انتقل إلى المحتوى",
  "btn_pubs": "المنشورات", "btn_cv": "السيرة الذاتية", "btn_contact": "تواصل معي",
  "now": "حالياً", "formerly": "سابقاً", "based": "مقيم في",
  "stats": ["مقالاً في مجلات محكّمة", "مهمة خبرة لمنظمات دولية", "مذكرة ماستر تحت إشرافه", "ولاية جزائرية شملها العمل الميداني والخبرة"],
  "chain_k": "البرنامج البحثي", "chain_h": "البحث على امتداد سلسلة القيمة",
  "chain_p": "خمس حلقات في السلسلة الغذائية. اختر واحدة للاطلاع على الأعمال المرتبطة بها.",
  "chain_more": "اكتشف البحث", "chain_pubs": "أعمال مختارة",
  "sel_k": "المنشورات", "sel_h": "الأحدث وقيد النشر", "all_pubs": "كل المنشورات",
  "clients_k": "الخبرة", "news_k": "المستجدات", "news_h": "المستجدات",
  "about_k": "نبذة", "about_h": "الملف الشخصي",
  "contact_h": "تواصل معي",
  "contact_p": "تعاون بحثي، تدريس، لجان خبراء أو مهام استشارية.",
  "email": "البريد الإلكتروني", "orcid": "ORCID", "scholar": "Google Scholar", "linkedin": "LinkedIn", "researchgate": "ResearchGate",
  "pages": "الصفحات", "rights": "جميع الحقوق محفوظة.",
  "r_intro": "تتبّع أعمالي القيمة على امتداد السلاسل الزراعية والغذائية في شمال إفريقيا: من يملك الأرض والمياه، وما الذي يصنع أداء المستثمرات، وكيف تُصاغ العقود بين الفلاحين والصناعات الغذائية وكيف تُنفَّذ، ومن يستحوذ على الهوامش في الأسواق، وكيف تتزود المدن والمشترون العموميون بالغذاء.",
  "r_themes": "محاور البحث", "r_q": "السؤال", "r_projects": "المشاريع البحثية", "r_pubs": "المنشورات",
  "r_map_k": "الجزائر", "r_map_h": "العمل الميداني والمهام",
  "r_map_p": "الولايات التي شملتها أبحاثي ومهام الخبرة. مرّر المؤشر أو المس الولاية للتفاصيل.",
  "r_map_r": "البحث", "r_map_c": "مهام الخبرة",
  "r_map_src": "الحدود: الوحدات الإدارية لـ FEWS NET (48 ولاية، 2021). شمال الجزائر.",
  "abs": "ملخص", "kw": "كلمات مفتاحية", "jel": "تصنيف JEL",
  "kw_v": "الزراعة التعاقدية؛ سلاسل القيمة الغذائية؛ هوامش التسويق؛ أسواق الأراضي والمياه؛ السياسة الزراعية؛ شمال إفريقيا",
  "eq_cap": "فارق السعر من الحقل إلى التجزئة: سعر المستهلك يساوي سعر المنتج مضافاً إليه الهامش المقتطع في كل حلقة k من السلسلة. من يستحوذ على هذه الهوامش، ولماذا، سؤال يتخلل أبحاثه.",
  "fig": "الشكل",
  "f_pos": "المنصب", "f_prev": "سابقاً",
  "f_prev_v": "أستاذ باحث، المدرسة الوطنية العليا للفلاحة (2018–2026)؛ مدير مخبر الاقتصاد الزراعي والغذائي والريفي والبيئي (2023–2025)",
  "f_deg": "الشهادات", "f_deg_v": "دكتوراه في الاقتصاد الغذائي والريفي (2017) · تأهيل جامعي في الاقتصاد الزراعي (2021) · المدرسة الوطنية العليا للفلاحة",
  "f_rec": "الحصيلة", "f_record": "{a} مقالاً في مجلات محكّمة ({f} قيد النشر) · {m} مذكرة ماستر تحت إشرافه · {j} لجان مناقشة دكتوراه · {s} مهمة خبرة",
  "f_adv": "خبرة لصالح", "f_lang": "اللغات",
  "map_cap": "أعمال ميدانية ومهام خبرة في {n} ولاية، 2012–2026", "map_more": "التفاصيل حسب الولاية",
  "r_net_k": "الشبكة الدولية", "r_net_h": "الإقامات البحثية والتعاون",
  "p_intro": "مقالات محكّمة وفصول في كتب ومداخلات. العناوين بلغتها الأصلية.",
  "p_filter": "التصفية حسب المحور", "p_all": "الكل", "p_forth": "قيد النشر", "p_review": "قيد التحكيم",
  "p_count": "مرجعاً", "p_doi": "DOI", "p_cite": "نسخ المرجع", "p_copied": "تم نسخ المرجع",
  "p_reviewer": "التحكيم العلمي", "p_reviewer_p": "محكّم لمجلات دولية:",
  "st_forth": "قيد النشر", "st_review": "قيد التحكيم", "k_chapter": "فصل في كتاب", "k_paper": "مداخلة",
  "t_intro": "ثماني سنوات من التدريس في المدرسة الوطنية العليا للفلاحة بالجزائر، من الجذع المشترك إلى الدكتوراه، مع التركيز على تسيير المؤسسات الزراعية وتقييم المشاريع وحوكمة السلاسل.",
  "t_courses": "المقاييس المدرَّسة", "t_hours": "سا", "t_since": "منذ",
  "t_sup": "الإشراف", "t_phd": "الإشراف على الدكتوراه", "t_ma": "مذكرات الماستر تحت إشرافه",
  "t_juries": "لجان المناقشة", "t_phd_j": "لجان مناقشة الدكتوراه",
  "t_ma_j": "لجنة مناقشة لمذكرات الماستر بين 2018 و2025، منها أربع بصفة رئيس.",
  "t_orig": "", "t_orig_fr": "عناوين المذكرات والأطروحات بلغتها الأصلية.",
  "a_intro": "منذ 2017 أقدّم الخبرة لبرامج التعاون الدولي في تطوير سلاسل القيمة وتمويل المخاطر المناخية والحوار متعدد الأطراف والمتابعة والتقييم.",
  "a_missions": "مهام مختارة", "a_clients": "المؤسسات", "a_workshops": "ورشات السياسات العمومية",
  "a_networks": "الشبكات واللجان الاستشارية", "a_coach": "المرافقة المقاولاتية",
  "a_coach_p": "منذ 2021: تأطير فرق الطلبة في المقاولاتية والتحليل المالي (الأسبوع العالمي للمقاولاتية، حاضنة المدرسة) وتكوين المؤسسات الناشئة في إعداد المشاريع (البرنامج الوطني «مذكرة تخرج – مؤسسة ناشئة»).",
  "m_intro": "محاضرات بدعوة وندوات ومداخلات علمية ولقاءات إعلامية حول الفلاحة وسلاسل القيمة والنظم الغذائية.",
  "m_media": "الإعلام", "m_listen": "استمع", "m_watch": "شاهد", "m_talks": "المحاضرات والمداخلات",
  "m_intl": "دولي", "m_events": "تظاهرات علمية من تنظيمه",
  "c_intro": "ملخص للمناصب والشهادات والمسؤوليات. السيرة الذاتية الكاملة متاحة عند الطلب.",
  "c_pos": "المناصب", "c_edu": "التكوين", "c_thesis": "الأطروحة", "c_train": "تكوينات مكمّلة",
  "c_admin": "المسؤوليات الأكاديمية", "c_lang": "اللغات", "c_methods": "المناهج", "c_soft": "البرمجيات",
  "c_print": "طباعة / PDF", "c_request": "طلب السيرة الكاملة",
  "wes": "الدكتوراه والتأهيل الجامعي معتمدان من WES في كندا.",
 },
}
LANG_NAME = {"en": "English", "fr": "Français", "ar": "العربية"}
LANG_SHORT = {"en": "EN", "fr": "FR", "ar": "ع"}

# --------------------------------------------------------------------------- icons
ICON = {
 "land": '<path d="M12 3s-4.2 4.7-4.2 7.6a4.2 4.2 0 0 0 8.4 0C16.2 7.7 12 3 12 3z"/><path d="M3 18h18M6 21h12"/>',
 "farm": '<path d="M12 21V7"/><path d="M12 7C9.8 7 8.5 5.4 8.5 3.2 10.7 3.2 12 4.8 12 7zm0 0c2.2 0 3.5-1.6 3.5-3.8C13.3 3.2 12 4.8 12 7z"/><path d="M12 12c-2.2 0-3.5-1.6-3.5-3.8 2.2 0 3.5 1.6 3.5 3.8zm0 0c2.2 0 3.5-1.6 3.5-3.8-2.2 0-3.5 1.6-3.5 3.8z"/><path d="M12 17c-2.2 0-3.5-1.6-3.5-3.8 2.2 0 3.5 1.6 3.5 3.8zm0 0c2.2 0 3.5-1.6 3.5-3.8-2.2 0-3.5 1.6-3.5 3.8z"/>',
 "contract": '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5"/><path d="M8.5 12.5h7"/><path d="M8.5 17c1-1.3 1.8-1.3 2.4 0s1.6 1.2 2.7-.5"/>',
 "market": '<path d="M12 3v17M8 21h8M4.5 7h15"/><path d="M4.5 7 2 13a2.6 2.6 0 0 0 5 0L4.5 7zM19.5 7 17 13a2.6 2.6 0 0 0 5 0l-2.5-6z"/><circle cx="12" cy="3.5" r=".6"/>',
 "city": '<path d="M3 21h18"/><path d="M5 21V10l5-3v14M10 21V4l9 4v13"/><path d="M13 10.5h3M13 14h3M13 17.5h3M7 13h1M7 16.5h1"/>',
 "mail": '<rect x="2.5" y="4.5" width="19" height="15" rx="2"/><path d="m3 6.5 9 6.5 9-6.5"/>',
 "pin": '<path d="M19.5 10c0 5.5-7.5 11-7.5 11s-7.5-5.5-7.5-11a7.5 7.5 0 0 1 15 0z"/><circle cx="12" cy="10" r="2.6"/>',
 "orcid": '<circle cx="12" cy="12" r="9.5"/><path d="M8.6 10v6.5M8.6 7.6v.1M11.4 16.5V10h2.2a3.2 3.2 0 0 1 0 6.5z"/>',
 "ext": '<path d="M14 4h6v6M20 4l-9 9"/><path d="M18 14v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h5"/>',
 "copy": '<rect x="9" y="9" width="11" height="11" rx="2"/><path d="M5 15H4.5A1.5 1.5 0 0 1 3 13.5v-9A1.5 1.5 0 0 1 4.5 3h9A1.5 1.5 0 0 1 15 4.5V5"/>',
 "play": '<circle cx="12" cy="12" r="9.5"/><path d="m10 8.5 5.5 3.5-5.5 3.5z"/>',
 "mic": '<rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5.5 11a6.5 6.5 0 0 0 13 0M12 17.5V21M8.5 21h7"/>',
 "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>',
 "moon": '<path d="M20.5 14.5A8.5 8.5 0 1 1 9.5 3.5a7 7 0 0 0 11 11z"/>',
 "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
 "close": '<path d="M6 6l12 12M18 6 6 18"/>',
 "print": '<path d="M7 9V3h10v6"/><rect x="3" y="9" width="18" height="8" rx="2"/><path d="M7 14h10v7H7z"/>',
 "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
 "cap": '<path d="m2 9 10-5 10 5-10 5z"/><path d="M6 11v5c3 2 9 2 12 0v-5M22 9v6"/>',
 "globe": '<circle cx="12" cy="12" r="9.5"/><path d="M2.5 12h19M12 2.5c2.6 2.8 3.9 6 3.9 9.5s-1.3 6.7-3.9 9.5c-2.6-2.8-3.9-6-3.9-9.5s1.3-6.7 3.9-9.5z"/>',
 "doc": '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5M9 13h6M9 17h6"/>',
 "link": '<path d="M10 14a4.5 4.5 0 0 0 6.4 0l3-3a4.5 4.5 0 0 0-6.4-6.4l-1 1"/><path d="M14 10a4.5 4.5 0 0 0-6.4 0l-3 3a4.5 4.5 0 0 0 6.4 6.4l1-1"/>',
}


def icon(name, cls="ic"):
    return (f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICON[name]}</svg>')


# The mark: a solid navy monogram block with a red base rule.
MARK = '<span class="mark" aria-hidden="true">SA</span>'  # navy monogram block with red base rule (CSS)


def furrows(n=15, w=1400, gap=34):
    """Decorative lines: disabled in the institutional design."""
    return ""
    paths = []
    for i in range(n):
        y = 18 + i * gap
        a = 22 + (i % 5) * 7
        paths.append(f'<path d="M-40 {y} C {w*0.22:.0f} {y-a}, {w*0.42:.0f} {y+a}, {w*0.62:.0f} {y} S {w*0.9:.0f} {y-a*0.8:.0f}, {w+40} {y+a*0.4:.0f}"/>')
    return (f'<svg class="furrows" viewBox="0 0 {w} {n*gap+30}" preserveAspectRatio="xMidYMid slice" aria-hidden="true">'
            f'<g fill="none" stroke="currentColor" stroke-width="1">{"".join(paths)}</g></svg>')


# --------------------------------------------------------------------------- helpers
CUR_PAGE = ' aria-current="page"'
CUR_TRUE = ' aria-current="true"'


def short_venue(pg, p):
    v = p["v"]
    if not v:
        return pg.t["st_review"] if p["status"] == "review" else ""
    if v.startswith("In:"):
        return pg.t["k_chapter"]
    return re.sub(r"\s*[\d(].*$", "", v.split(",")[0]).strip()


def e(s):
    return escape(str(s), quote=True)


class Page:
    def __init__(self, lang, slug):
        self.lang, self.slug = lang, slug
        self.root = "" if lang == "en" else "../"
        self.t = T[lang]

    def tr(self, d):
        return d[self.lang] if isinstance(d, dict) else d

    def href(self, slug, lang=None):
        lang = lang or self.lang
        pre = self.root + ("" if lang == "en" else f"{lang}/")
        return f"{pre}{slug}.html"

    def asset(self, p):
        return f"{self.root}assets/{p}"


CLIENT_TR = {  # institution names, per language
    "World Bank": {"fr": "Banque mondiale", "ar": "البنك الدولي"},
    "European Union": {"fr": "Union européenne", "ar": "الاتحاد الأوروبي"},
    "FAO": {"ar": "الفاو"},
    "UNDP": {"fr": "PNUD", "ar": "برنامج الأمم المتحدة الإنمائي"},
    "IDRC": {"fr": "CRDI", "ar": "المركز الكندي لبحوث التنمية الدولية"},
    "Horizon Europe": {"ar": "أفق أوروبا"},
    "Humanity & Inclusion": {"fr": "Humanité & Inclusion", "ar": "منظمة الإنسانية والإدماج"},
}


def client(pg, c):
    return CLIENT_TR.get(c, {}).get(pg.lang, c)


FUNDERS = {  # funder labels in projects, per language
    "IDRC (Canada)": {"fr": "CRDI (Canada)", "ar": "المركز الكندي لبحوث التنمية الدولية (كندا)"},
    "DGRSDT (Algeria)": {"fr": "DGRSDT (Algérie)", "ar": "المديرية العامة للبحث العلمي والتطوير التكنولوجي (الجزائر)"},
    "ANR (France) · CIRAD G-EAU": {"fr": "ANR (France) · CIRAD G-EAU", "ar": "الوكالة الوطنية للبحث (فرنسا) · CIRAD G-EAU"},
}


def funder(pg, f):
    return FUNDERS.get(f, {}).get(pg.lang, f)


PUB = {p["k"]: p for p in C.PUBS}
THEME = {t["id"]: t for t in C.THEMES}
PROJ = {p["k"]: p for p in C.PROJECTS}


def authors_html(a):
    return e(a).replace("Assassi S.", '<strong class="me">Assassi S.</strong>')


def status_label(pg, p):
    if p["status"] == "forth":
        return pg.t["st_forth"]
    if p["status"] == "review":
        return pg.t["st_review"]
    return p["y"]


def citation(p, pg):
    yr = p["y"] or status_label(pg, p)
    s = f'{p["a"]} ({yr}). {p["t"]}.'
    if p["v"]:
        s += f' {p["v"]}.'
    if p["doi"]:
        s += f' https://doi.org/{p["doi"]}'
    return s


def pub_item(pg, p, compact=False):
    tags = []
    if p["status"] == "forth":
        tags.append(f'<span class="tag tag-forth">{e(pg.t["st_forth"])}</span>')
    if p["status"] == "review":
        tags.append(f'<span class="tag tag-review">{e(pg.t["st_review"])}</span>')
    if p["kind"] == "chapter":
        tags.append(f'<span class="tag">{e(pg.t["k_chapter"])}</span>')
    if p["kind"] == "paper":
        tags.append(f'<span class="tag">{e(pg.t["k_paper"])}</span>')
    tags.append(f'<span class="tag tag-lang">{p["lang"].upper()}</span>')
    title = e(p["t"])
    if p["doi"]:
        title = f'<a href="https://doi.org/{e(p["doi"])}" target="_blank" rel="noopener">{title}</a>'
    venue = f'<span class="venue">{e(p["v"])}</span>' if p["v"] else ""
    actions = ""
    if not compact:
        acts = []
        if p["doi"]:
            acts.append(f'<a class="act" href="https://doi.org/{e(p["doi"])}" target="_blank" rel="noopener">{icon("link")}DOI {e(p["doi"])}</a>')
        acts.append(f'<button class="act copy" type="button" data-cite="{e(citation(p, pg))}">{icon("copy")}{e(pg.t["p_cite"])}</button>')
        actions = f'<div class="acts">{"".join(acts)}</div>'
    th = " ".join(p["th"])
    return (f'<li class="pub" id="{p["k"]}" data-th="{th}" lang="{p["lang"]}" dir="ltr">'
            f'<p class="pub-t">{title}</p><p class="pub-a">{authors_html(p["a"])}</p>'
            f'<p class="pub-v">{venue}<span class="tags">{"".join(tags)}</span></p>{actions}</li>')


# --------------------------------------------------------------------------- layout
def head(pg, title, desc):
    alts = "".join(f'<link rel="alternate" hreflang="{l}" href="{e((SITE_URL + "/" if SITE_URL else "") + ("" if l == "en" else l + "/") + pg.slug + ".html")}">' for l in LANGS) if SITE_URL else ""
    person = {
        "@context": "https://schema.org", "@type": "Person", "name": "Sami Assassi", "honorificPrefix": "Dr.",
        "jobTitle": "Agricultural economist", "email": f"mailto:{C.PERSON['email']}",
        "affiliation": {"@type": "CollegeOrUniversity", "name": "Saint Paul University"},
        "alumniOf": {"@type": "CollegeOrUniversity", "name": "École nationale supérieure agronomique (ENSA), Algiers"},
        "sameAs": [f"https://orcid.org/{C.PERSON['orcid']}"] + [u for u in (C.PERSON["scholar"], C.PERSON["linkedin"], C.PERSON["researchgate"]) if u],
        "knowsAbout": ["Agricultural economics", "Contract farming", "Agrifood value chains", "Agribusiness management", "Land markets"],
    }
    ld = f'<script type="application/ld+json">{json.dumps(person, ensure_ascii=False)}</script>' if pg.slug == "index" else ""
    return f"""<!doctype html>
<html lang="{pg.lang}" dir="{'rtl' if pg.lang == 'ar' else 'ltr'}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="author" content="Sami Assassi">
<meta property="og:type" content="profile">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:image" content="{pg.asset('portrait.jpg')}">
<meta name="theme-color" content="#0B2545">
{alts}
<link rel="icon" href="{pg.asset('favicon.svg')}" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Carlito:ital,wght@0,400;0,700;1,400&amp;family=IBM+Plex+Sans+Arabic:wght@300;400;600&amp;family=JetBrains+Mono:wght@400;500&amp;display=swap" rel="stylesheet">
<link rel="stylesheet" href="{pg.asset('style.css')}">
<script>(function(){{try{{var t=localStorage.getItem('sa-theme');if(t)document.documentElement.setAttribute('data-theme',t);}}catch(e){{}}document.documentElement.classList.add('js');}})();</script>
{ld}
</head>"""


def header(pg):
    t = pg.t
    links = "".join(
        f'<li><a href="{pg.href(s)}"{CUR_PAGE if s == pg.slug else ""}>{e(t["nav"][s])}</a></li>'
        for s in PAGES[1:])
    langs = "".join(
        f'<a href="{pg.href(pg.slug, l)}" hreflang="{l}" lang="{l}"{CUR_TRUE if l == pg.lang else ""} title="{LANG_NAME[l]}">{LANG_SHORT[l]}</a>'
        for l in LANGS)
    return f"""<body data-page="{pg.slug}">
<a class="skip" href="#main">{e(t['skip'])}</a>
<header class="site-head">
 <div class="wrap head-row">
  <a class="brand" href="{pg.href('index')}">{MARK}<span class="brand-txt"><span class="brand-name">{e(pg.tr(C.PERSON['display']))}</span><span class="brand-sub">{e(pg.tr(C.PERSON['role']))}</span></span></a>
  <nav class="nav" id="nav" aria-label="Main">
   <ul>{links}<li><a href="#contact">{e(t['contact'])}</a></li></ul>
  </nav>
  <div class="head-tools">
   <div class="langs" role="group" aria-label="{e(t['lang'])}">{langs}</div>
   <button class="icon-btn theme-btn" type="button" aria-label="{e(t['theme'])}" title="{e(t['theme'])}">{icon('sun', 'ic i-sun')}{icon('moon', 'ic i-moon')}</button>
   <button class="icon-btn menu-btn" type="button" aria-controls="nav" aria-expanded="false" aria-label="{e(t['menu'])}">{icon('menu', 'ic i-menu')}{icon('close', 'ic i-close')}</button>
  </div>
 </div>
</header>
<main id="main">"""


def contact_links(pg, cls="clinks"):
    P = C.PERSON
    items = [f'<a href="mailto:{P["email"]}">{icon("mail")}<span>{e(P["email"])}</span></a>',
             f'<a href="https://orcid.org/{P["orcid"]}" target="_blank" rel="noopener">{icon("orcid")}<span dir="ltr">ORCID {P["orcid"]}</span></a>']
    if P["scholar"]:
        items.append(f'<a href="{e(P["scholar"])}" target="_blank" rel="noopener">{icon("cap")}<span>Google Scholar</span></a>')
    if P["researchgate"]:
        items.append(f'<a href="{e(P["researchgate"])}" target="_blank" rel="noopener">{icon("globe")}<span>ResearchGate</span></a>')
    if P["linkedin"]:
        items.append(f'<a href="{e(P["linkedin"])}" target="_blank" rel="noopener">{icon("link")}<span>LinkedIn</span></a>')
    items.append(f'<span>{icon("pin")}<span>{e(pg.tr(P["city"]))}</span></span>')
    return f'<div class="{cls}">{"".join(items)}</div>'


def footer(pg):
    t = pg.t
    links = "".join(f'<li><a href="{pg.href(s)}">{e(t["nav"][s])}</a></li>' for s in PAGES[1:])
    langs = " · ".join(f'<a href="{pg.href(pg.slug, l)}" lang="{l}">{LANG_NAME[l]}</a>' for l in LANGS)
    return f"""</main>
<footer class="site-foot" id="contact">
 <div class="wrap">
  <div class="foot-cta">
   <div><p class="kicker">{e(t['contact'])}</p><h2>{e(t['contact_h'])}</h2><p class="muted">{e(t['contact_p'])}</p></div>
   <a class="btn btn-primary" href="mailto:{C.PERSON['email']}">{icon('mail')}{e(t['btn_contact'])}</a>
  </div>
  <div class="foot-grid">
   <div class="foot-brand">{MARK}<div><p class="foot-name">{e(pg.tr(C.PERSON['display']))}</p><p class="muted">{e(pg.tr(C.PERSON['role']))} · {e(pg.tr(C.PERSON['degrees']))}</p></div></div>
   <div><p class="foot-h">{e(t['contact'])}</p>{contact_links(pg)}</div>
   <div><p class="foot-h">{e(t['pages'])}</p><ul class="foot-links">{links}</ul></div>
  </div>
  <div class="foot-base"><span>© {YEAR} Sami Assassi. {e(t['rights'])}</span><span class="foot-langs">{langs}</span></div>
 </div>
</footer>
<div class="toast" role="status" aria-live="polite"></div>
<script src="{pg.asset('site.js')}" defer></script>
</body>
</html>"""


def page_hero(pg, kicker, title, intro):
    """Inner-page header: breadcrumb (functional, not decorative), title, one-line intro."""
    crumb = f'<p class="crumb"><a href="{pg.href("index")}">{e(pg.tr(C.PERSON["display"]))}</a><span aria-hidden="true">/</span>{e(title)}</p>'
    return f"""<section class="phero"><div class="wrap">{crumb}<h1>{e(title)}</h1><p class="lead">{e(intro)}</p></div></section>"""


def section(h, body, kicker="", cls="", sid=""):
    i = f' id="{sid}"' if sid else ""
    return f'<section class="sec {cls}"{i}><div class="wrap"><h2 class="sec-h">{e(h)}</h2>{body}</div></section>'


# --------------------------------------------------------------------------- pages
def record(pg):
    arts = sum(1 for p in C.PUBS if p["kind"] == "article" and p["status"] in ("pub", "forth"))
    forth = sum(1 for p in C.PUBS if p["status"] == "forth")
    return pg.t["f_record"].format(a=arts, f=forth, m=len(C.MASTERS), j=len(C.PHD_JURIES), s=len(C.CONSULTING))


def chain(pg, full_link=True):
    """Value-chain schematic: five linked stages, a cross-cutting base layer, and a detail panel."""
    t = pg.t
    nodes, panels = [], []
    for i, th in enumerate(C.THEMES):
        sel = "true" if i == 0 else "false"
        nodes.append(f'<button class="node" type="button" role="tab" id="tab-{th["id"]}" aria-controls="panel-{th["id"]}" aria-selected="{sel}" tabindex="{0 if i == 0 else -1}">'
                     f'<span class="node-t">{e(pg.tr(th["t"]))}</span></button>')
        pubs = "".join(
            f'<li dir="ltr" lang="{PUB[k]["lang"]}"><a href="{pg.href("publications")}#{k}">{e(PUB[k]["t"])}</a>'
            f'<span class="muted"> · <i>{e(short_venue(pg, PUB[k]))}</i>{(" " + PUB[k]["y"]) if PUB[k]["y"] else (" · " + pg.t["st_forth"] if PUB[k]["status"] == "forth" else "")}</span></li>'
            for k in th["pubs"][:3])
        panels.append(f'<div class="panel" role="tabpanel" id="panel-{th["id"]}" aria-labelledby="tab-{th["id"]}"{"" if i == 0 else " hidden"}>'
                      f'<div class="panel-l"><h3 class="panel-q">{e(pg.tr(th["t"]))}</h3><p>{e(pg.tr(th["d"]))}</p>'
                      + (f'<a class="more" href="{pg.href("research")}#{th["id"]}">{e(t["chain_more"])} {icon("arrow", "ic arr")}</a>' if full_link else "")
                      + f'</div><div class="panel-r"><p class="mini-h">{e(t["chain_pubs"])}</p><ul class="mini-pubs">{pubs}</ul></div></div>')
    return (f'<div class="chain"><div class="chain-track" role="tablist" aria-label="{e(t["chain_h"])}">{"".join(nodes)}</div>'
            f'<div class="cross"><span class="cross-t">{e(pg.tr(C.CROSS["t"]))}</span><span class="cross-d">{e(pg.tr(C.CROSS["d"]))}</span></div>'
            f'<div class="chain-panels">{"".join(panels)}</div></div>')


JEL = [("Q12", "Micro analysis of farm firms, farm households and farm input markets"),
       ("Q13", "Agricultural markets and marketing; cooperatives; agribusiness"),
       ("Q15", "Land ownership and tenure; land use; irrigation"),
       ("Q18", "Agricultural policy; food policy"),
       ("L14", "Transactional relationships; contracts and reputation; networks"),
       ("O13", "Agriculture; natural resources; environment")]



def page_index(pg):
    t, P = pg.t, C.PERSON
    hero = f"""<section class="hero">
<div class="wrap hero-grid">
 <figure class="portrait"><img src="{pg.asset('portrait.jpg')}" alt="{e(pg.tr(P['display']))}" width="480" height="600">
  <figcaption><a href="https://orcid.org/{P['orcid']}" target="_blank" rel="noopener" dir="ltr">{icon('orcid')}ORCID {P['orcid']}</a><span>{icon('pin')}{e(pg.tr(P['city']))}</span></figcaption></figure>
 <div class="hero-txt">
  <h1 class="hero-name">{e(pg.tr(P['display']))}</h1>
  <p class="hero-role">{e(pg.tr(P['role']))} · {e(pg.tr(P['degrees']))}<br>{e(pg.tr(P['position']))}</p>
  <div class="abstract">
   <p><span class="abs-k">{e(t['abs'])}.</span> {e(pg.tr(P['headline']))}</p>
   <p class="abs-row"><span class="abs-k">{e(t['kw'])}:</span> {e(t['kw_v'])}</p>
  </div>
  <div class="actions">
   <a class="btn btn-primary" href="{pg.href('publications')}">{e(t['btn_pubs'])}</a>
   <a class="btn btn-line" href="{pg.href('cv')}">{e(t['btn_cv'])}</a>
   <a class="txt-link" href="mailto:{P['email']}">{icon('mail')}{e(P['email'])}</a>
  </div>
 </div>
</div></section>"""

    facts = [(t["f_pos"], pg.tr(P["position"])), (t["f_prev"], t["f_prev_v"]), (t["f_deg"], t["f_deg_v"]),
             (t["f_rec"], record(pg)), (t["f_adv"], " · ".join(client(pg, c) for c in C.CLIENTS[:5])), (t["f_lang"], " · ".join(pg.tr(a) for a, _ in C.LANGS))]
    facts_html = "".join(f'<div><dt>{e(k)}</dt><dd>{e(v)}</dd></div>' for k, v in facts)
    facts_sec = f'<section class="facts-sec"><div class="wrap"><dl class="facts">{facts_html}</dl></div></section>'

    chain_sec = section(t["chain_h"], f'<p class="sec-p">{e(t["chain_p"])}</p>{chain(pg)}', "", "sec-chain")
    map_sec = section(t["r_map_h"], field_map(pg), "", "", "fieldwork")

    sel = [p for p in C.PUBS if p["status"] == "forth"] + [p for p in C.PUBS if p["status"] == "pub"][:3]
    pubs = f'<ul class="pubs pubs-sel">{"".join(pub_item(pg, p, compact=True) for p in sel)}</ul>' \
           f'<a class="more" href="{pg.href("publications")}">{e(t["all_pubs"])} {icon("arrow", "ic arr")}</a>'
    pubs_sec = section(t["sel_h"], pubs)

    bio = "".join(f"<p>{e(x)}</p>" for x in pg.tr(P["bio"]))
    news = "".join(f'<li><span class="yr">{y}</span><span>{e(pg.tr(x))}</span></li>' for y, x in C.NEWS)
    about = f"""<section class="sec"><div class="wrap about-grid">
<div><h2 class="sec-h">{e(t['about_h'])}</h2><div class="prose">{bio}</div><p class="note">{e(t['wes'])}</p></div>
<aside class="news"><h2 class="side-h">{e(t['news_h'])}</h2><ul class="news-list">{news}</ul></aside>
</div></section>"""
    return hero + map_sec + facts_sec + chain_sec + pubs_sec + about


SEA = {"en": "Mediterranean Sea", "fr": "Mer Méditerranée", "ar": "البحر الأبيض المتوسط"}


def field_map(pg, intro=True, compact=False):
    """Fieldwork map. Full version: numbered markers keyed to a legend. Compact (home hero): keys + link."""
    t = pg.t
    m = json.loads((ROOT / "assets" / "map.json").read_text(encoding="utf-8"))
    order = [k for k, v in C.SITES.items() if v[0] == "r"] + [k for k, v in C.SITES.items() if v[0] == "c"]
    num = {k: i + 1 for i, k in enumerate(order)}
    paths, marks = [], []
    for w in m["wilayas"]:
        s_ = C.SITES.get(w["n"])
        if s_:
            kind, desc, name = s_
            label = e(pg.tr(name)) if compact else f'{num[w["n"]]}. {e(pg.tr(name))}'
            paths.append(f'<path class="w on {kind}" d="{w["d"]}" data-w="{e(w["n"])}" data-name="{label}" data-desc="{e(pg.tr(desc))}" tabindex="0" role="img" aria-label="{e(pg.tr(name))}: {e(pg.tr(desc))}"/>')
            x, y = w["c"]
            if compact:
                marks.append(f'<circle class="mk-dot {kind}" data-w="{e(w["n"])}" cx="{x}" cy="{y}" r="3.2"/>')
            else:
                marks.append(f'<g class="mk {kind}" data-w="{e(w["n"])}" transform="translate({x} {y})"><circle r="9.5"/><text y="3.6">{num[w["n"]]}</text></g>')
        else:
            paths.append(f'<path class="w" d="{w["d"]}"/>')
    W, H = m["w"], m["h"]
    km = 100 * m["px_per_km"]
    mid = "mh" if compact else "mf"
    deco = (f'<text class="sea" x="{W*0.47:.0f}" y="34" text-anchor="middle">{e(SEA[pg.lang])}</text>'
            f'<g class="scale" transform="translate(22 30)"><path d="M0 0v6h{km:.1f}v-6M{km/2:.1f} 3v3"/><text x="0" y="20">0</text><text x="{km:.1f}" y="20" text-anchor="middle">100 km</text></g>'
            f'<g class="north" transform="translate({W-28} 26)"><path d="M0 -14 L6 6 L0 2 L-6 6 Z"/><text y="20" text-anchor="middle">N</text></g>')
    grat = ""
    if not compact and "proj" in m:
        pj = m["proj"]
        gx = lambda lon: (lon - pj["w_lon"]) * pj["kx"] * pj["scale"]
        gy = lambda lat: (pj["n_lat"] - lat) * pj["scale"]
        lines, labels = [], []
        for lon in range(0, 10, 2):
            x = gx(lon)
            lines.append(f'M{x:.1f} 0V{H}')
            labels.append(f'<text x="{x:.1f}" y="{H - 6}" text-anchor="middle">{abs(lon)}°{"E" if lon > 0 else ""}</text>')
        for lat in (32, 34, 36):
            y = gy(lat)
            lines.append(f'M0 {y:.1f}H{W}')
            labels.append(f'<text x="{W - 4}" y="{y - 4:.1f}" text-anchor="end">{lat}°N</text>')
        grat = f'<g class="grat"><path d="{" ".join(lines)}"/>{"".join(labels)}</g>'
    svg = (f'<svg class="dz-map" viewBox="0 0 {W} {H}" role="group" aria-label="{e(t["r_map_h"])}">'
           f'<defs><linearGradient id="fade-{mid}" x1="0" y1="0" x2="0" y2="1"><stop offset=".72" stop-color="#fff"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>'
           f'<mask id="{mid}"><rect width="100%" height="100%" fill="url(#fade-{mid})"/></mask></defs>'
           f'<g mask="url(#{mid})">{"".join(paths)}<path class="outline" d="{m["outline"]}"/></g>{grat}<g class="marks">{"".join(marks)}</g>{deco}</svg>')
    if compact:
        keys = (f'<div class="map-keys"><span><i class="sw r"></i>{e(t["r_map_r"])}</span><span><i class="sw c"></i>{e(t["r_map_c"])}</span>'
                f'<a class="more more-light" href="{pg.href("research")}#fieldwork">{e(t["map_more"])} {icon("arrow", "ic arr")}</a></div>')
        return (f'<figure class="map-box map-compact"><figcaption class="map-cap">{e(t["map_cap"].format(n=len(C.SITES)))}</figcaption>'
                f'{svg}<div class="map-tip" hidden></div>{keys}</figure>')
    rows = []
    for kind in ("r", "c"):
        items = "".join(f'<li data-w="{e(k)}"><span class="num {kind}">{num[k]}</span><strong>{e(pg.tr(C.SITES[k][2]))}</strong><span class="muted">{e(pg.tr(C.SITES[k][1]))}</span></li>'
                        for k in order if C.SITES[k][0] == kind)
        rows.append(f'<div><p class="mini-h"><span class="sw {kind}"></span>{e(t["r_map_" + kind])}</p><ul class="site-list">{items}</ul></div>')
    p_ = f'<p class="sec-p">{e(t["r_map_p"])}</p>' if intro else ""
    return (f'{p_}<div class="map-grid"><figure class="map-box">{svg}<div class="map-tip" hidden></div>'
            f'<figcaption class="map-src"><strong>{e(t["fig"])} 1.</strong> {e(t["map_cap"].format(n=len(C.SITES)))}. {e(t["r_map_src"])}</figcaption></figure>'
            f'<div class="map-legend">{"".join(rows)}</div></div>')



def page_research(pg):
    t = pg.t
    out = page_hero(pg, pg.tr(C.PERSON["role"]), t["title"]["research"], t["r_intro"])
    out += section(t["chain_h"], chain(pg, full_link=False), t["chain_k"], "sec-chain")
    cards = []
    for i, th in enumerate(C.THEMES):
        pubs = "".join(f'<li dir="ltr" lang="{PUB[k]["lang"]}"><a href="{pg.href("publications")}#{k}">{e(PUB[k]["t"])}</a></li>' for k in th["pubs"])
        projs = "".join(f'<li><span class="yr">{e(PROJ[k]["p"])}</span> {e(pg.tr(PROJ[k]["t"]))}</li>' for k in th["projects"])
        cards.append(f"""<article class="theme reveal" id="{th['id']}">
<div class="theme-head"><h3>{e(pg.tr(th['t']))}</h3></div>
<p>{e(pg.tr(th['d']))}</p>
<div class="theme-lists"><div><p class="mini-h">{e(t['r_pubs'])}</p><ul class="mini-pubs">{pubs}</ul></div>
{f'<div><p class="mini-h">{e(t["r_projects"])}</p><ul class="mini-proj">{projs}</ul></div>' if projs else ''}</div></article>""")
    out += section(t["r_themes"], f'<div class="themes">{"".join(cards)}</div>', "", "sec-alt")

    projects = "".join(f"""<li class="tl-item reveal"><span class="tl-p">{e(p['p'])}</span><div><h3>{e(pg.tr(p['t']))}</h3>
<p class="tl-f">{e(funder(pg, p['f']))}</p><p>{e(pg.tr(p['r']))}</p></div></li>""" for p in C.PROJECTS)
    out += section(t["r_projects"], f'<ol class="timeline">{projects}</ol>')

    out += section(t["r_map_h"], field_map(pg), t["r_map_k"], "sec-alt", "fieldwork")

    stays = "".join(f'<li class="reveal"><span class="yr">{y}</span><strong>{e(i)}</strong><span class="muted">{e(pg.tr(pl))}</span></li>' for y, pl, i in C.STAYS)
    nets = "".join(f'<li class="reveal"><span class="yr">{y}</span><span>{e(pg.tr(x))}</span></li>' for y, x in C.NETWORKS)
    out += section(t["r_net_h"], f'<ul class="cards3">{stays}</ul><h3 class="sub-h">{e(t["a_networks"])}</h3><ul class="rows">{nets}</ul>', t["r_net_k"])
    return out


def page_publications(pg):
    t = pg.t
    out = page_hero(pg, t["nav"]["publications"], t["title"]["publications"], t["p_intro"])
    chips = [f'<button class="chip" type="button" data-f="all" aria-pressed="true">{e(t["p_all"])}</button>']
    chips += [f'<button class="chip" type="button" data-f="{th["id"]}" aria-pressed="false">{icon(th["icon"])}{e(pg.tr(th["t"]))}</button>' for th in C.THEMES]
    groups = []

    def group(label, items, gid):
        if items:
            groups.append(f'<div class="pgroup" id="{gid}"><h3 class="pyear">{e(label)}</h3><ul class="pubs">{"".join(pub_item(pg, p) for p in items)}</ul></div>')

    group(t["p_forth"], [p for p in C.PUBS if p["status"] == "forth"], "forthcoming")
    for y in sorted({p["y"] for p in C.PUBS if p["status"] == "pub"}, reverse=True):
        group(y, [p for p in C.PUBS if p["status"] == "pub" and p["y"] == y], f"y{y}")
    group(t["p_review"], [p for p in C.PUBS if p["status"] == "review"], "review")
    rev = "".join(f'<li><span class="yr">{y}</span><em>{e(j)}</em></li>' for y, j in C.REVIEWING)
    body = (f'<div class="filters" role="group" aria-label="{e(t["p_filter"])}">{"".join(chips)}</div>'
            f'<p class="count" aria-live="polite"><span>{len(C.PUBS)}</span> {e(t["p_count"])}</p>'
            f'<div class="plist">{"".join(groups)}</div>'
            f'<div class="reviewer"><h3 class="sub-h">{e(t["p_reviewer"])}</h3><p class="muted">{e(t["p_reviewer_p"])}</p><ul class="rows">{rev}</ul></div>')
    out += f'<section class="sec"><div class="wrap">{body}</div></section>'
    return out


def page_teaching(pg):
    t = pg.t
    out = page_hero(pg, "ENSA · Saint Paul University", t["title"]["teaching"], t["t_intro"])
    courses = "".join(f"""<li class="course reveal"><p class="course-lv">{e(pg.tr(c['lv']))}</p><h3>{e(pg.tr(c['t']))}</h3>
<p class="course-m">{(c['h'] + ' ' + e(t['t_hours']) + ' · ') if c['h'] else ''}{e(t['t_since'])} {c['since']}</p></li>""" for c in C.COURSES)
    out += section(t["t_courses"], f'<ul class="courses">{courses}</ul>')
    ma_title = (lambda m: m[2]) if pg.lang == "en" else (lambda m: m[3])
    tl_lang = "en" if pg.lang == "en" else "fr"
    masters = "".join(f'<li><span class="yr">{m[0]}</span><div><strong>{e(m[1])}</strong><span lang="{tl_lang}" dir="ltr" class="th-t">{e(ma_title(m))}</span></div></li>' for m in C.MASTERS)
    note = t["t_orig_fr"] or t["t_orig"]
    sup = (f'<div class="callout">{icon("cap")}<div><p class="mini-h">{e(t["t_phd"])}</p><p>{e(pg.tr(C.PHD_SUPERVISION))}</p></div></div>'
           f'<h3 class="sub-h">{e(t["t_ma"])} <span class="cnt">{len(C.MASTERS)}</span></h3><ul class="rows theses">{masters}</ul>'
           + (f'<p class="note">{e(note)}</p>' if note else ""))
    out += section(t["t_sup"], sup, "", "sec-alt")
    phd = "".join(f'<li><span class="yr">{j[0]}</span><div><strong>{e(j[1])}</strong><span lang="{tl_lang}" dir="ltr" class="th-t">{e(j[2] if pg.lang == "en" else j[3])}</span></div></li>' for j in C.PHD_JURIES)
    juries = (f'<h3 class="sub-h">{e(t["t_phd_j"])} <span class="cnt">{len(C.PHD_JURIES)}</span></h3><ul class="rows theses">{phd}</ul>'
              f'<p class="big-note"><span class="stat-n">{C.MASTER_JURIES_N}</span> {e(t["t_ma_j"])}</p>')
    out += section(t["t_juries"], juries)
    return out


def page_advisory(pg):
    t = pg.t
    out = page_hero(pg, t["nav"]["advisory"], t["title"]["advisory"], t["a_intro"])
    clients = "".join(f'<li>{e(client(pg, c))}</li>' for c in C.CLIENTS)
    out += f'<section class="clients clients-top"><div class="wrap"><p class="kicker">{e(t["clients_k"])}</p><ul class="client-row">{clients}</ul></div></section>'
    missions = "".join(f"""<li class="tl-item reveal"><span class="tl-p">{e(m['p'])}</span><div><p class="tl-f">{e(m['c'])}</p><p>{e(pg.tr(m['t']))}</p></div></li>""" for m in C.CONSULTING)
    out += section(t["a_missions"], f'<ol class="timeline">{missions}</ol>')
    ws = "".join(f'<li><span class="yr">{y}</span><span>{e(pg.tr(x))}</span></li>' for y, x in C.WORKSHOPS)
    nets = "".join(f'<li><span class="yr">{y}</span><span>{e(pg.tr(x))}</span></li>' for y, x in C.NETWORKS)
    out += section(t["a_workshops"], f'<ul class="rows">{ws}</ul><h3 class="sub-h">{e(t["a_networks"])}</h3><ul class="rows">{nets}</ul>'
                   f'<div class="callout">{icon("farm")}<div><p class="mini-h">{e(t["a_coach"])}</p><p>{e(t["a_coach_p"])}</p></div></div>', "", "sec-alt")
    return out


def page_talks(pg):
    t = pg.t
    out = page_hero(pg, t["nav"]["talks"], t["title"]["talks"], t["m_intro"])
    media = "".join(f"""<li class="media reveal"><a href="{e(m['url'])}" target="_blank" rel="noopener">
<span class="media-ic">{icon('play' if m['kind'] == 'video' else 'mic')}</span>
<span class="media-o">{e(m['o'])} · {m['y']}</span><span class="media-t" lang="en" dir="ltr">{e(m['t'])}</span>
<span class="media-cta">{e(t['m_watch'] if m['kind'] == 'video' else t['m_listen'])} {icon('ext')}</span></a></li>""" for m in C.MEDIA)
    out += section(t["m_media"], f'<ul class="medias">{media}</ul>')
    ev_i = {"en": 2, "fr": 3, "ar": 4}[pg.lang]
    talks = "".join(f"""<li><span class="yr">{x[0]}</span><div><span class="talk-t" dir="auto">{e(x[1])}</span>
<span class="muted">{e(x[ev_i])}{f' <span class="tag">{e(t["m_intl"])}</span>' if x[5] else ''}</span></div></li>""" for x in C.TALKS)
    out += section(t["m_talks"], f'<ul class="rows talks">{talks}</ul>', "", "sec-alt")
    evs = "".join(f'<li><span class="yr">{y}</span><span>{e(pg.tr(x))}</span></li>' for y, x in C.EVENTS)
    out += section(t["m_events"], f'<ul class="rows">{evs}</ul>')
    return out


def page_cv(pg):
    t, P = pg.t, C.PERSON
    out = page_hero(pg, f"{pg.tr(P['display'])} · {pg.tr(P['degrees'])}", t["title"]["cv"], t["c_intro"])
    tools = (f'<div class="cv-tools"><button class="btn btn-line print-btn" type="button">{icon("print")}{e(t["c_print"])}</button>'
             f'<a class="btn btn-line" href="mailto:{P["email"]}?subject=CV">{icon("doc")}{e(t["c_request"])}</a></div>')
    pos = "".join(f"""<li class="tl-item"><span class="tl-p">{e(p['p'])}</span><div><h3>{e(pg.tr(p['t']))}</h3><p class="tl-f">{e(pg.tr(p['o']))}</p><p>{e(pg.tr(p['d']))}</p></div></li>""" for p in C.POSITIONS)
    edu = "".join(f"""<li class="tl-item"><span class="tl-p">{d['y']}</span><div><h3>{e(pg.tr(d['t']))}</h3><p class="tl-f">{e(pg.tr(d['o']))}</p>
{f'<p><span class="mini-h">{e(t["c_thesis"])}</span> {e(pg.tr(d["x"]))}</p>' if d['x'] else ''}{f'<p class="honour">{e(pg.tr(d["h"]))}</p>' if d['h'] else ''}</div></li>""" for d in C.EDUCATION)
    train = "".join(f'<li><span class="yr">{y}</span><span>{e(pg.tr(x))} <span class="muted">· {e(o)}</span></span></li>' for y, x, o in C.TRAINING)
    adm = "".join(f'<li><span class="yr">{y}</span><span>{e(pg.tr(x))}</span></li>' for y, x in C.ADMIN)
    langs = "".join(f'<li><strong>{e(pg.tr(a))}</strong><span class="muted">{e(pg.tr(b))}</span></li>' for a, b in C.LANGS)
    meth = "".join(f'<li>{e(m)}</li>' for m in pg.tr(C.METHODS))
    soft = "".join(f'<li>{e(s)}</li>' for s in C.SOFTWARE)
    body = f"""{tools}
<div class="cv-grid">
<div class="cv-main">
 <h2 class="sec-h">{e(t['c_pos'])}</h2><ol class="timeline">{pos}</ol>
 <h2 class="sec-h">{e(t['c_edu'])}</h2><ol class="timeline">{edu}</ol>
 <p class="note">{e(t['wes'])}</p>
 <h2 class="sec-h">{e(t['c_admin'])}</h2><ul class="rows">{adm}</ul>
 <h2 class="sec-h">{e(t['c_train'])}</h2><ul class="rows">{train}</ul>
</div>
<aside class="cv-side">
 <div class="side-card"><p class="mini-h">{e(t['contact'])}</p>{contact_links(pg, 'clinks stack')}</div>
 <div class="side-card"><p class="mini-h">{e(t['c_lang'])}</p><ul class="langs-list">{langs}</ul></div>
 <div class="side-card"><p class="mini-h">{e(t['c_methods'])}</p><ul class="pills">{meth}</ul></div>
 <div class="side-card"><p class="mini-h">{e(t['c_soft'])}</p><ul class="pills">{soft}</ul></div>
 <div class="side-card"><p class="mini-h">{e(t['nav']['publications'])}</p><p><a class="more" href="{pg.href('publications')}">{len(C.PUBS)} {e(t['p_count'])} {icon('arrow', 'ic arr')}</a></p>
 <p><a class="more" href="{pg.href('advisory')}">{e(t['nav']['advisory'])} {icon('arrow', 'ic arr')}</a></p><p><a class="more" href="{pg.href('teaching')}">{e(t['nav']['teaching'])} {icon('arrow', 'ic arr')}</a></p></div>
</aside>
</div>"""
    out += f'<section class="sec"><div class="wrap">{body}</div></section>'
    return out


RENDER = {"index": page_index, "research": page_research, "publications": page_publications,
          "teaching": page_teaching, "advisory": page_advisory, "talks": page_talks, "cv": page_cv}


YEARS = re.compile(r"(?<![\w./-])(\d{4}(?:\s*[–,-]\s*(?:\d{2,4})?)+)(?![\w])")


def isolate_years(html):
    """In RTL pages, keep '2018–2026' and '2021, 2025' in left-to-right order (text nodes only)."""
    return re.sub(r">([^<]+)<", lambda m: ">" + YEARS.sub(lambda y: '<span class="nw" dir="ltr">' + y.group(1) + "</span>", m.group(1)) + "<", html)


def build():
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "assets").mkdir(parents=True)
    for f in ["style.css", "site.js", "portrait.jpg", "favicon.svg"]:
        shutil.copy(ROOT / "assets" / f, OUT / "assets" / f)
    (OUT / ".nojekyll").write_text("")
    for lang in LANGS:
        for slug in PAGES:
            pg = Page(lang, slug)
            name = pg.tr(C.PERSON["display"])
            title = f"{name} · {pg.t['title'][slug]}"
            desc = pg.tr(C.PERSON["headline"])
            html = head(pg, title, desc) + header(pg) + RENDER[slug](pg) + footer(pg)
            if lang == "ar":
                html = isolate_years(html)
            d = OUT if lang == "en" else OUT / lang
            d.mkdir(exist_ok=True)
            (d / f"{slug}.html").write_text(html, encoding="utf-8")
    # 404 for GitHub Pages
    shutil.copy(OUT / "index.html", OUT / "404.html")
    print("built", len(LANGS) * len(PAGES), "pages ->", OUT)


if __name__ == "__main__":
    build()
