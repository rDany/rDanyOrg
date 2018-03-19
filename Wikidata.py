import os
import json
import urllib
import datetime
import requests

concepts = {
    "football_player": {
        "Messi": "Q615"
    }
}

query_all = """
#Todo sobre Douglas Adams
#added before 2016-10

PREFIX entity: <http://www.wikidata.org/entity/>
#partial results

SELECT ?propUrl ?propLabel ?valUrl ?valLabel ?picture
WHERE
{{
hint:Query hint:optimizer 'None' .
{{	BIND(entity:{itemid} AS ?valUrl) .
    BIND("N/A" AS ?propUrl ) .
    BIND("identity"@en AS ?propLabel ) .
}}
UNION
{{	entity:{itemid} ?propUrl ?valUrl .
    ?property ?ref ?propUrl .
    ?property rdf:type wikibase:Property .
    ?property rdfs:label ?propLabel
}}

?valUrl rdfs:label ?valLabel
FILTER (LANG(?valLabel) = 'en') .
OPTIONAL{{ ?valUrl wdt:P18 ?picture .}}
FILTER (lang(?propLabel) = 'en' )
}}
ORDER BY ?propUrl ?valUrl
LIMIT 2000
"""

lang = "es"
query_all = """
#Data of Douglas Adams (modified version)
PREFIX entity: <http://www.wikidata.org/entity/>

#  In addition to the original query this one comes with some advantages:
#  - You will get only literals as results, (even if the values are stored as IRI in wikibase)
#  - That means you will also get properties as birth date, alphanumeric identifier and so on.
#  - The list is ordered numerically by property number. (So P19 comes before P100)
#  - All label, altLabel and description in a given Language are included.
#  You may open a separate column ?valUrl if you need also the IRI
#
#  Please advise, if there is an option to put the Q-Number  and/or the Language
#  code into a runtime variable.

SELECT ?propNumber ?propUrl ?propLabel ?valUrl ?val
WHERE
{{
    hint:Query hint:optimizer 'None' .
    {{	BIND(entity:{itemid} AS ?valUrl) .
        BIND("N/A" AS ?propUrl ) .
        BIND("Name"@{lang} AS ?propLabel ) .
        entity:{itemid} rdfs:label ?val .

        FILTER (LANG(?val) = "{lang}")
        }}
    UNION
    {{   BIND(entity:{itemid} AS ?valUrl) .

        BIND("AltLabel"@{lang} AS ?propLabel ) .
        optional{{entity:{itemid} skos:altLabel ?val}}.
        FILTER (LANG(?val) = "{lang}")
    }}
    UNION
    {{   BIND(entity:{itemid} AS ?valUrl) .

        BIND("Beschreibung"@{lang} AS ?propLabel ) .
        optional{{entity:{itemid} schema:description ?val}}.
        FILTER (LANG(?val) = "{lang}")
    }}
    UNION
    {{	entity:{itemid} ?propUrl ?valUrl .
        ?property ?ref ?propUrl .
        ?property rdf:type wikibase:Property .
        ?property rdfs:label ?propLabel.
        FILTER (lang(?propLabel) = '{lang}' )
        filter  isliteral(?valUrl)
        BIND(?valUrl AS ?val)
    }}
    UNION
    {{	entity:{itemid} ?propUrl ?valUrl .
        ?property ?ref ?propUrl .
        ?property rdf:type wikibase:Property .
        ?property rdfs:label ?propLabel.
        FILTER (lang(?propLabel) = '{lang}' )
        filter  isIRI(?valUrl)
        ?valUrl rdfs:label ?valLabel
        FILTER (LANG(?valLabel) = "{lang}")
        BIND(CONCAT(?valLabel) AS ?val)
    }}
        BIND( SUBSTR(str(?propUrl),38, 250) AS ?propNumber)
}}
ORDER BY xsd:integer(?propNumber)
"""


def fp_participated_olympics(info):
    "Did lionel messi go to Olympics"
    return None


def fp_how_many_ballon_dors(info):
    "How many Ballon D'Ors has Lionel Messi won"
    return None


def fp_how_many_golden_shoe(info):
    "How many golden shoe does messi have"
    "How many golden shoe has Lionel Messi had throughout his career"
    return None


def fp_worth(info):
    "How much is messi worth"
    return None


def fp_how_old(info):
    "How old is Lionel Messi"
    item_data = process_item(info)
    if item_data["birth_date"] is None:
        return None
    age = calculate_age(item_data["birth_date"].date())
    answer = "{name} tiene {age} años.".format(name=item_data["name"], age=age)
    question = "¿Cual es la edad de {name}?".format(name=item_data["name"])
    return question, answer


def fp_how_tall(info):
    "How tall is Lionel Messi"
    "How tall is messi"
    item_data = process_item(info)
    if item_data["height"] is None:
        return None
    answer = "{name} mide {height} centimetros de alto.".format(name=item_data["name"], height=item_data["height"])
    question = "¿Cual es la altura de {name}?".format(name=item_data["name"])
    return question, answer


def fp_how_weight(info):
    ""
    item_data = process_item(info)
    if item_data["mass"] is None:
        return None
    answer = "{name} pesa {mass} kilogramos.".format(name=item_data["name"], mass=item_data["mass"])
    question = "¿Cuánto pesa {name}?".format(name=item_data["name"])
    return question, answer


def fp_have_brothers(info):
    "Does l.messi have some brothers"
    return None


def fp_have_children(info):
    "Does messi have any children"
    return None


def fp_play_for_barcelona(info):
    "Does messi play for barcelona"
    return None


def fp_total_achievements(info):
    "How many achievements has Lionel Andres Messi achieved"
    return None


def fp_is_married(info):
    "Is Lionel Messi married"
    item_data = process_item(info)
    adjetivo = "casado"
    if item_data["is_male"] is None:
        adjetivo = "casada/o"
    elif item_data["is_male"]:
        adjetivo = "casado"
    elif item_data["is_male"]:
        adjetivo = "casada"

    if item_data["spouse"] is None:
        answer = "No, {name} no está {adjetivo}".format(name=item_data["name"], adjetivo=adjetivo)
    else:
        answer = "Si, {name} está {adjetivo} con {spouse}".format(name=item_data["name"], adjetivo=adjetivo, spouse=item_data["spouse"])
    question = "¿Está {adjetivo} {name}?".format(adjetivo=adjetivo, name=item_data["name"])
    return question, answer


def fp_is_male(info):
    "Is messi a boy"
    item_data = process_item(info)
    if item_data["is_male"] is None:
        return None
    if item_data["is_male"] is True:
        answer = "Si, {name} es varón.".format(name=item_data["name"])
    else:
        answer = "No, {name} no es varón.".format(name=item_data["name"])
    question = "¿{name} es varón?".format(name=item_data["name"])
    return question, answer


def fp_skin_color(info):
    "What is Lionel Messi's skin colour"
    item_data = process_item(info)
    question = "¿Cual es el color de piel de {name}?".format(name=item_data["name"])
    answer = "No considero que el color de piel sea una característica importante en una persona."
    return question, answer


def fp_number(info):
    "What number is messi"
    return None


def fp_where_is_from(info):
    "Where is Messi from"
    "Where messi born"
    "Where was lionel messi born"
    return None


def calculate_age(born):
    today = datetime.date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


def process_item(info):
    name = ""
    is_male = None
    is_female = None
    height = None
    mass = None
    birth_date = None
    spouse = None
    for bind in info["results"]["bindings"]:
        if "propUrl" not in bind or "valUrl" not in bind:
            continue
        if bind["propUrl"]["value"] == "http://www.wikidata.org/prop/direct/P21":
            if bind["valUrl"]["value"] == "http://www.wikidata.org/entity/Q6581097":
                is_male = True
                is_female = False
            elif bind["valUrl"]["value"] == "http://www.wikidata.org/entity/Q6581072":
                is_male = False
                is_female = True
            else:
                print(bind)
                is_male = False
                is_female = False
        elif bind["propUrl"]["value"] == "http://www.wikidata.org/prop/direct/P2048":
            height = float(bind["valUrl"]["value"])
        elif bind["propUrl"]["value"] == "http://www.wikidata.org/prop/direct/P2067":
            mass = float(bind["valUrl"]["value"])
        elif bind["propUrl"]["value"] == "http://www.wikidata.org/prop/direct/P569":
            birth_date = bind["valUrl"]["value"]
            birth_date = datetime.datetime.strptime(birth_date, '%Y-%m-%dT%H:%M:%SZ')
        elif bind["propUrl"]["value"] == "http://www.wikidata.org/prop/direct/P26":
            spouse = bind["val"]["value"]
        elif bind["propUrl"]["value"] == "N/A":
            name = bind["val"]["value"]
    item_data = {
        "name": name,
        "is_male": is_male,
        "is_female": is_female,
        "height": height,
        "mass": mass,
        "birth_date": birth_date,
        "spouse": spouse
    }
    return item_data

questions = {
    "football_player": [
        fp_participated_olympics,
        fp_how_many_ballon_dors,
        fp_how_many_golden_shoe,
        fp_worth,
        fp_how_old,
        fp_how_tall,
        fp_how_weight,
        fp_have_brothers,
        fp_have_children,
        fp_play_for_barcelona,
        fp_total_achievements,
        fp_is_married,
        fp_is_male,
        fp_skin_color,
        fp_number
    ]
}

headers = {
    "Accept": "application/sparql-results+json"
}

query = """
#Cats
SELECT ?item ?itemLabel
WHERE
{
  ?item wdt:P106 wd:Q937857.
  ?item wdt:P27 wd:Q414.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "es,en". }
}
"""
use_cache = True
if not use_cache:
    params = {
        "query": query
    }
    url = "https://query.wikidata.org/sparql"
    r = requests.get(url, params=params, headers=headers)
    print(r.text)
    r_json = r.json()
    with open("futbolistas.json", 'w') as data_file:
        json.dump(r_json,
                  data_file,
                  sort_keys=True,
                  indent=4,
                  separators=(',', ': '))
else:
    with open("futbolistas.json") as data_file:
        r_json = json.load(data_file)
futbolistas_count = 0
for futbolista in r_json["results"]["bindings"]:
    # print(futbolista["itemLabel"]["value"], futbolista["item"]["value"])
    futbolistas_count += 1

print(futbolistas_count)
futbol_answers = []
for futbolista in r_json["results"]["bindings"]:
    answers = []
    itemid_index = futbolista["item"]["value"].find("/Q")
    itemid = futbolista["item"]["value"][itemid_index + 1:]
    params = {
        "query": query_all.format(itemid=itemid, lang=lang)
    }
    url = "https://query.wikidata.org/sparql"
    r = requests.get(url, params=params, headers=headers)
    r_json = r.json()
    for q_func in questions["football_player"]:
        answer = q_func(r_json)
        if answer is not None:
            answers.append(answer)
    futbol_answers.append(answers)

    with open("answers.json", 'w') as data_file:
        json.dump(futbol_answers,
                  data_file,
                  sort_keys=True,
                  indent=4,
                  separators=(',', ': '))
