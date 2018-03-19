import os
import json
import urllib.parse
import hashlib
from datawiki import datawiki_reader
from question_generators import questions

base_path = '/media/mega_disco/data_wiki_cache/'
misc = [
    "Q616",
    "Q615",
    "Q26698156",  # The shape of the water
    "Q2870",
    "Q2875",
    "Q1092",
    "Q156329",  # Star Trek: Voyager
    "Q16455",  # John Rhys-Davies
    "Q3465791",  # Star Trek: Voyager, season 1
    "Q5398426",
    "Q437693",
    "Q253977",
    "Q168756",
    "Q219124",
    "Q270691",  # Sridevi
    "Q228928",  # Eva Marie Saint
    "Q107769",  # Luke Cunningham Wilson
    "Q25136228",  # Annihilation
    "Q489831",  # Kevin Smith
    "Q998220",  # Black Panter character
    "Q931597",  # Marvel universe
    "Q188784",  # Superhero
    "Q204299",  # Frances McDormand
    "Q229487",  # Allison Janey
    "Q19020",  # Accademy Awards
    "Q193555",  # Brendan Fraser
    "Q28787",  # Star Wars Rebels
    "Q230151",  # Rita Moreno
    "Q209170",  # Mary Poppins
    "Q213326",  # The incredibles
    "Q24832112",  # The incredibles 2
    "Q269214",  # John Lasseter
    "Q172678",  # Samuel L. Jackson
    "Q27942936",  # The greatest showman
    "Q129591",  # Hugh Jackman
    "Q20762680",  # Jumanju 2
    "Q483907",  # Jack Black
    "Q25136560",  # Cloverfield paradox
    "Q47479532",  # Olivia Nova
    "Q5654923",  # Abel Pintos
    "Q467930",  # Soledad Pastorutti
    "Q180919",  # Natalie Wood
    "Q93330",  # Peron
    "Q19798734",  # Stranger Things
    "Q825197",  # Elephants Dream
    "Q925587",  # Sintel
    "Q1173161",  # Tears of Steel
    "Q282456",  # Big Buck Bunny
    "Q92642",  # Ton Roosendal
    "Q883799",  # Blender Foundation
    "Q173136",  # Blender Software
    "Q127552",  # Pixar
    "Q312",  # Apple inc
    "Q1233073",  # Walt Disney Motion Pictures Group
    "Q242446",  # Lucasfilm
    "Q483382",  # Steve Wozniak
    "Q1047410",  # Walt Disney animation studios
    "Q8704",  # Walt Disney
    "Q2290907",  # Woody
    "Q11934",  # Mickey
    "Q22983",  # Data
    "Q7810",  # Homero
    "Q246283",  # Frozen
    "Q1601158",  # Los simuladores
    "Q38263346",  # Luxor cine
    "Q1361614",
    "Q44473",
]

singers = [
    "Q2831",  # Michael Jackson
    "Q19848",  # Lady Gaga
    "Q5608",  # Eminem
    "Q34086",
    "Q15615",
    "Q4235",
    "Q36844",
    "Q83287",
    "Q26876",
    "Q6107",
    "Q15935",
    "Q162202",
    "Q42493",
    "Q23215",
    "Q44437",
    "Q62766",
    "Q7542",
    "Q5383",
    "Q11975",
    "Q303",
    "Q36153",
    "Q1744",
    "Q409",
    "Q151892",
    "Q1203",
    "Q41173",
    "Q41076",
    "Q1450",
    "Q6060",
    "Q15869",
    "Q466762"
]

scientists = [
    "Q17714"
]

actors = [
    "Q186304",
    "Q37175",
    "Q13909",
    "Q38111",
    "Q10738",
    "Q37628",
    "Q2685",
    "Q40096",
    "Q16397",
    "Q4616",
    "Q37079",
    "Q34436",
    "Q80069",
    "Q32522",
    "Q44304",
    "Q189490",
    "Q35332",
    "Q39476",
    "Q40572",
    "Q260794",
    "Q164119",
    "Q126599",
    "Q192682",
    "Q103939",
    "Q40026",
    "Q83338",
    "Q37876",
    "Q43203",
    "Q208026",
    "Q9543",
    "Q147077",
    "Q3304418",
    "Q25144",
    "Q185654",
    "Q15079",
    "Q862460",
    "Q25936414",
    "Q312124",
    "Q16759",
    "Q228603",
    "Q315271"
]

film_tv = [
    "Q8539",
    "Q23572",
    "Q147235",
    "Q152178",
    "Q232737",
    "Q462",
    "Q17738",
    "Q181795",
    "Q181803",
    "Q6074",
    "Q18486021",
    "Q20977110",
    "Q17738",
    "Q42051",
    "Q181069",
    "Q165713",
    "Q1079",
    "Q34316",
    "Q438406",
    "Q23567",
    "Q23577",
    "Q642",
    "Q12500134",
    "Q5930",
    "Q322646",
    "Q182218",
    "Q14171368",
    "Q23780914",
    "Q23558",
    "Q24871",
    "Q3604746",
    "Q29580929",
    "Q29580931",
    "Q29580932",
    "Q186219",
    "Q189330",
    "Q79784",
    "Q189267",
    "Q171254",
    "Q28537",
    "Q552314",
    "Q192837",
    "Q23831",
    "Q23673",
    "Q886",  # The Simpsons
    "Q16538",
    "Q4525",
    "Q6084",
    "Q16802335",
    "Q44578",
    "Q283799",
    "Q283696",
    "Q20856802",
    "Q21527875",
    "Q25136484",
    "Q20502242",
    "Q19946102",
    "Q179673",
    "Q24053263",
    "Q20501835",
    "Q19829521",
    "Q21001674",
    "Q21935651",
    "Q22665878"
]

characters = [
    "Q12206942"
]

modern_political_leaders = [
    "Q22686",
    "Q76",
    "Q352",
    "Q9682",
    "Q91",
    "Q9696",
    "Q38370",
    "Q8023",
    "Q207",
    "Q9960",
    "Q9439",
    "Q1124",
    "Q23",
    "Q1317",
    "Q8007",
    "Q7207",
    "Q8016",
    "Q1001",
    "Q7322",
    "Q5809",
    "Q855",
    "Q9588",
    "Q7747",
    "Q43274",
    "Q80976",
    "Q43144",
    "Q33866",
    "Q11812",
    "Q34969",
    "Q23505",
    "Q7416"
]

items_id = misc + singers + actors + film_tv + characters + modern_political_leaders
langs = ["en", "es", "zh-hans", "pt"]
answers = []
datawikiReader = datawiki_reader(base_path)
for lang in langs:
    for item_id in items_id:
        entity = datawikiReader.get_entity(item_id, lang, 1)
        entity = datawikiReader.augment_data(entity)
        if entity is None:
            continue
        if "label" in entity.properties:
            print("\n", entity.properties["label"], "\n###")
            prop_list = list(entity.properties.keys())
            prop_list.sort()
            for prop in prop_list:
                if 0:
                    print("{}: {}".format(prop, entity.properties[prop]))
            # print()
        qg = questions()
        for qu in qg.generate(entity, lang):
            if qu is not None:
                print(qu)
                for quu in qu:
                    answers.append(quu)
                    answers[-1]["lang"] = lang

with open("answers.json", 'w') as data_file:
    json.dump(answers,
              data_file,
              sort_keys=True,
              indent=4,
              separators=(',', ': '))

with open('template.html') as f:
    template_html = f.read()

gtm_1 = """
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':
new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
}})(window,document,'script','dataLayer','GTM-N7QBGF2');</script>
<!-- End Google Tag Manager -->
"""

gtm_2 = """
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-N7QBGF2"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->
"""

homeurl = "/"

zeronet = False

if zeronet:
    gtm_1 = ""
    gtm_2 = ""
    homeurl = "/1AnKzdTDdejcyQU2nAUvsAz6r8S6u6icUq"

base_path = "www"
all_answers_links = {}
for answer in answers:
    encoded_answer = hashlib.sha224(answer["q"].encode("UTF-8")).hexdigest()
    answer_path = os.path.join(base_path, "ask", encoded_answer)
    answer_file_path = os.path.join(base_path, "ask", encoded_answer, 'index.html')
    index_file_path = os.path.join(base_path, 'index.html')
    sitemap_file_path = os.path.join(base_path, 'sitemap.txt')
    os.makedirs(answer_path, exist_ok=True)
    with open(answer_file_path, 'w') as f:
        f.write(template_html.format(question=answer["q"], answer=answer["a"], lang=answer["lang"], body="", gtm_1=gtm_1, gtm_2=gtm_2, homeurl="{}{}".format(homeurl, answer["lang"])))
    if answer["lang"] not in all_answers_links:
        all_answers_links[answer["lang"]] = ""
    if zeronet:
        all_answers_links[answer["lang"]] = "{all}<a href=\"{homeurl}/ask/{encoded_answer}\">{answer}</a><br>\n".format(all=all_answers_links[answer["lang"]], answer=answer["q"], encoded_answer=encoded_answer, homeurl=homeurl)
    else:
        all_answers_links[answer["lang"]] = "{all}<a href=\"/ask/{encoded_answer}?q={answer}&lang={lang}\">{answer}</a><br>\n".format(all=all_answers_links[answer["lang"]], answer=answer["q"], encoded_answer=encoded_answer, lang=answer["lang"])

lang_links = ""
for lang in langs:
    lang_path = os.path.join(base_path, lang)
    lang_file_path = os.path.join(base_path, lang, 'index.html')
    os.makedirs(lang_path, exist_ok=True)
    if zeronet:
        lang_links = "{all}<a href=\"{homeurl}/{lang}\">{answer}</a><br>\n".format(all=lang_links, answer=lang, lang=lang, homeurl=homeurl)
    else:
        lang_links = "{all}<a href=\"/{lang}\">{answer}</a><br>\n".format(all=lang_links, answer=lang, lang=lang)
    with open(lang_file_path, 'w') as f:
        f.write(template_html.format(question=lang, answer="", body=all_answers_links[lang], lang=lang, gtm_1=gtm_1, gtm_2=gtm_2, homeurl=homeurl))

for lang in langs:
    with open(index_file_path, 'w') as f:
        f.write(template_html.format(question="Home", answer="", body=lang_links, lang="en", gtm_1=gtm_1, gtm_2=gtm_2, homeurl=homeurl))

sitemap_text = "https://rdany.org"
for answer in answers:
    encoded_answer = hashlib.sha224(answer["q"].encode("UTF-8")).hexdigest()
    sitemap_text = "{}\nhttps://rdany.org/ask/{}?q={}&lang={}".format(sitemap_text, encoded_answer, urllib.parse.quote_plus(answer["q"]), answer["lang"])

with open(sitemap_file_path, 'w') as f:
    f.write(sitemap_text)
