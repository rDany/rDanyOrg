class questions:
    def __init__(self):
        self.instances_of = {
            "film": [
                "Q18011172",  # Film project
                "Q11424",  # Film
                "Q29168811",  # Animated Feature Film
                "Q229390",  # 3D film
                "Q202866"
            ],
            "human": [
                "Q5",  # Human
            ],
            "planet": [
                "Q30014",  # outer planet of the Solar system
                "Q3504248",  # inner planet of the Solar System
                "Q844911",  # superior planet
                "Q3901935",  # inferior planet
            ],
            "chemical_element": [
                "Q11344",  # Chemical element
            ]
        }

    def get_properties(self, entity, instance_of, properties):
        if not self.filter(entity, instance_of, properties):
            return None
        prop_values = {}
        for property_ in properties:
            prop_values[property_] = self.get_property(entity, property_)
        prop_values["label"] = entity.properties["label"][0]
        return prop_values

    def generate_question(self, entity, instance_of, questions, info, lang):
        if info is None:
            return None
        question_return = None
        for question in questions:
            if lang in question:
                question_return = question[lang]
                question_return["q"] = question_return["q"].format(**info)
                question_return["a"] = question_return["a"].format(**info)
                question_return["lang"] = lang
                break
        return question_return

    def simple_question_generator(self, entity, instance_of, properties, questions, lang):
        p = self.get_properties(entity, instance_of, properties)
        q = self.generate_question(entity, instance_of, questions, p, lang)
        print(q)
        return q

    def film_producer(self, entity, lang="en"):
        instance_of = self.instances_of["film"]
        properties = ["producer"]
        questions = [
            {
                "es": {
                    "q": "¿Quién produjo la película {label}?",
                    "a": "La película {label} fue producida por {producer}."
                },
                "en": {
                    "q": "Who produced the movie {label}?",
                    "a": "The movie {label} was produced by {producer}."
                },
                "zh-hans": {
                    "q": "谁制作了电影{label}？",
                    "a": "电影{label}由{producer}制作。"
                },
                "pt": {
                    "q": "Quem produziu o filme {label}?",
                    "a": "O filme {label} foi produzido por {producer}."
                },
                "ru": {
                    "q": "Кто создал фильм «{label}»?",
                    "a": "Фильм «{label}» был снят {producer}."
                },
                "ko": {
                    "q": "누가 {label} 영화를 제작 했습니까?",
                    "a": "영화 {label}는 {producer} 제작했습니다."
                },
                "hi": {
                    "q": "फिल्म {label} का निर्माण किसने किया?",
                    "a": "फिल्म {label} {producer} द्वारा निर्मित किया गया था"
                },
                "ja": {
                    "q": "誰が映画「{label}」を制作しましたか？",
                    "a": "映画{label}は{producer}によって制作されました。"
                }
            }
        ]
        q = self.simple_question_generator(entity, instance_of, properties, questions, lang)
        return q

    def film_director(self, entity, lang="en"):
        instance_of = self.instances_of["film"]
        properties = ["director"]
        questions = [
            {
                "es": {
                    "q": "¿Quién dirigió la película {label}?",
                    "a": "La película {label} fue dirigida por {director}."
                },
                "en": {
                    "q": "Who directed the movie {label}?",
                    "a": "The movie {label} was directed by {director}."
                },
                "zh-hans": {
                    "q": "谁指导了电影{label}？",
                    "a": "电影{label}由{director}执导。"
                },
                "pt": {
                    "q": "Quem dirigiu o filme {label}?",
                    "a": "O filme {label} foi dirigido por {director}."
                },
                "ru": {
                    "q": "Кто руководил фильмом «{label}»?",
                    "a": "Фильм «{label}» был режиссером {director}."
                },
                "ko": {
                    "q": "누가 {label} 영화를 감독 했습니까?",  # 터미네이터  # 존이
                    "a": "영화 '{label}'는 {director} 감독했다."
                },
                "hi": {
                    "q": "फिल्म {label} का निर्देशन किसने किया?",  # टर्मिनेटर  # जॉन
                    "a": "फिल्म {label} का निर्देश {director} द्वारा किया गया था।"
                },
                "ja": {
                    "q": "誰が映画{label}を監督した？",  # ターミネーター  # ジョン
                    "a": "映画「{label}」は{director}によって監督されました。"
                }
            }
        ]
        q = self.simple_question_generator(entity, instance_of, properties, questions, lang)
        return q

    def film_photography_director(self, entity, lang="en"):
        instance_of = self.instances_of["film"]
        properties = ["director_of_photography"]
        questions = [
            {
                "es": {
                    "q": "¿Quién hizo la dirección de fotografía en la película {label}?",
                    "a": "La película {label} tuvo como director/a de fotografía a {director_of_photography}."
                },
                "en": {
                    "q": "Who is the director of photography in the movie {label}?",
                    "a": "The director of photography in {label} is {director_of_photography}."
                },
                "zh-hans": {
                    "q": "谁是电影{label}的摄影导演？",
                    "a": "{label}中的摄影导演是{director_of_photography}。"
                },
                "pt": {
                    "q": "Quem é o diretor de fotografia no filme {label}?",
                    "a": "O diretor de fotografia em {label} é {director_of_photography}."
                },
                "ru": {
                    "q": "Кто является режиссером фотографии в фильме «{label}»?",
                    "a": "Режиссер фотографии «{label}» - {director_of_photography}."
                },
                "ko": {
                    "q": "영화 {label} 촬영 감독은 누구입니까?",  # 터미네이터  # 존이
                    "a": "{label}의 사진 감독은 {director_of_photography}니다."
                },
                "hi": {
                    "q": "फिल्म {label} में फोटोग्राफी के निर्देशक कौन हैं?",  # टर्मिनेटर  # जॉन
                    "a": "{label} में फोटोग्राफी के निदेशक {director_of_photography} हैं"
                },
                "ja": {
                    "q": "映画{label}の写真監督は誰ですか？",  # ターミネーター  # ジョン
                    "a": "{label}の写真監督は{director_of_photography}です。"
                }
            }
        ]
        q = self.simple_question_generator(entity, instance_of, properties, questions, lang)
        return q

    def film_music_composer(self, entity, lang="en"):
        instance_of = self.instances_of["film"]
        properties = ["music_composer"]
        questions = [
            {
                "es": {
                    "q": "¿Quién compuso la música para la película {label}?",
                    "a": "La película {label} tuvo como compositor a {music_composer}."
                },
                "en": {
                    "q": "Who is the music composer in the movie {label}?",
                    "a": "The music composer in {label} is {music_composer}."
                },
                "zh-hans": {
                    "q": "谁是电影{label}的音乐作曲家？",
                    "a": "{label}中的音乐作曲者是{music_composer}。"
                },
                "pt": {
                    "q": "Quem é o compositor de música no filme {label}?",
                    "a": "O compositor de música em {label} é {music_composer}."
                },
                "ru": {
                    "q": "Кто музыкальный композитор в фильме «{label}»?",
                    "a": "Музыкальный композитор в {label} - {music_composer}."
                },
                "ko": {
                    "q": "영화 {label}의 음악 작곡가는 누구입니까?",  # 터미네이터  # 존이
                    "a": "{label}의 음악 작곡가는 {music_composer}니다."
                },
                "hi": {
                    "q": "फिल्म {label} में संगीत संगीतकार कौन है?",  # टर्मिनेटर  # जॉन
                    "a": "{label} में संगीत संगीतकार {music_composer} है"
                },
                "ja": {
                    "q": "映画{label}の作曲家は誰ですか？",  # ターミネーター  # ジョン
                    "a": "{label}の作曲家は{music_composer}です。"
                }
            }
        ]
        q = self.simple_question_generator(entity, instance_of, properties, questions, lang)
        return q

    def film_cost_money(self, entity, lang="en"):
        instance_of = self.instances_of["film"]
        properties = ["cost_money"]
        questions = [
            {
                "es": {
                    "q": "¿Cuanto costó la película {label}?",
                    "a": "La película {label} tuvo un costo de ${cost_money}."
                },
                "en": {
                    "q": "How much did the movie {label} cost?",
                    "a": "The movie {label} cost was ${cost_money}."
                },
                "zh-hans": {
                    "q": "电影{label}的成本是多少？",
                    "a": "电影的{label}成本为$ {cost_money}。"
                },
                "pt": {
                    "q": "Quanto custa o filme {label}?",
                    "a": "O custo do filme {label} foi $ {cost_money}."
                },
                "ru": {
                    "q": "Сколько стоил фильм «{label}»?",
                    "a": "Стоимость фильма «{label}» составляла {cost_money} долларов."
                },
                "ko": {
                    "q": "영화 {label}는 얼마였습니까?",  # 터미네이터  # 존이
                    "a": "영화 {label} 비용은 ${cost_money}입니다."
                },
                "hi": {
                    "q": "फिल्म {label} ने कितना खर्च किया?",  # टर्मिनेटर  # जॉन
                    "a": "फिल्म {label} की लागत ${cost_money} थी"
                },
                "ja": {
                    "q": "映画{label}の費用はいくらですか？",  # ターミネーター  # ジョン
                    "a": "映画の{label}費用は${cost_money}でした。"
                }
            }
        ]
        q = self.simple_question_generator(entity, instance_of, properties, questions, lang)
        return q

    def film_box_office(self, entity, lang="en"):
        instance_of = self.instances_of["film"]
        properties = ["box_office"]
        questions = [
            {
                "es": {
                    "q": "¿Cuanto ganó la película {label}?",
                    "a": "La película {label} tuvo una ganancia de ${box_office}."
                },
                "en": {
                    "q": "What was the box office of the movie {label}?",
                    "a": "The movie {label} box office was ${box_office}."
                },
                "zh-hans": {
                    "q": "电影{label}票房是什么？",
                    "a": "电影{label}票房是$ {box_office}。"
                },
                "pt": {
                    "q": "Qual era a bilheteria do filme {label}?",
                    "a": "A caixa de correio do filme {label} foi $ {box_office}."
                },
                "ru": {
                    "q": "Какова была касса фильма «{label}»?",
                    "a": "Фильм «{label}» был ${box_office}."
                },
                "ko": {
                    "q": "영화 '{label}'의 흥행작은 무엇 이었습니까?",  # 터미네이터  # 존이
                    "a": "영화 {label} 박스 오피스는 ${box_office}입니다."
                },
                "hi": {
                    "q": "फिल्म {label} का बॉक्स ऑफिस क्या था?",  # टर्मिनेटर  # जॉन
                    "a": "फिल्म {label} बॉक्स ऑफिस ${box_office} थी"
                },
                "ja": {
                    "q": "映画「{label}」の興行は何でしたか？",  # ターミネーター  # ジョン
                    "a": "映画の{label}ボックスオフィスは${box_office}でした。"
                }
            }
        ]
        q = self.simple_question_generator(entity, instance_of, properties, questions, lang)
        return q

    def film_screewriter(self, entity, lang="en"):
        instance_of = self.instances_of["film"]
        properties = ["screenwriter"]
        questions = [
            {
                "es": {
                    "q": "¿Quién es el guionista de la película {label}?",
                    "a": "La película {label} tuvo como guionista a {screenwriter}."
                },
                "en": {
                    "q": "Who was the screenwriter of the movie {label}?",
                    "a": "The screenwriter in the movie {label} was {screenwriter}."
                },
                "zh-hans": {
                    "q": "谁是电影{label}的编剧？",
                    "a": "电影{label}中的编剧是{screenwriter}。"
                },
                "pt": {
                    "q": "Quem foi o roteirista do filme {label}?",
                    "a": "O roteirista no filme {label} foi {screenwriter}."
                },
                "ru": {
                    "q": "Кто был сценаристом фильма {label}?",
                    "a": "Сценаристом в фильме {label} была {screenwriter}."
                },
                "ko": {
                    "q": "영화 {label}의 시나리오 작가는 누구였습니까?",  # 터미네이터  # 존이
                    "a": "영화 {label}의 시나리오 작가는 {screenwriter}었다."
                },
                "hi": {
                    "q": "फिल्म {label} का पटकथा लेखक कौन था?",  # टर्मिनेटर  # जॉन
                    "a": "फिल्म {label} में पटकथा लेखक {screenwriter} थे।"
                },
                "ja": {
                    "q": "映画{label}の脚本家は誰ですか？",  # ターミネーター  # ジョン
                    "a": "映画{label}の脚本家は{screenwriter}だった。"
                }
            }
        ]
        q = self.simple_question_generator(entity, instance_of, properties, questions, lang)
        return q

    def human_age(self, entity, lang="en"):
        instance_of = self.instances_of["human"]
        properties = ["augmented_age"]
        questions = [
            {
                "es": {
                    "q": "¿Cual es la edad de {label}?",
                    "a": "{label} tiene {augmented_age} años."
                },
                "en": {
                    "q": "How old is {label}?",
                    "a": "{label} is {augmented_age} years old."
                },
                "zh-hans": {
                    "q": "{label}有多大？",
                    "a": "{label}是{augmented_age}岁。"
                },
                "pt": {
                    "q": "Quantos anos tem {label}?",
                    "a": "{label} é {augmented_age} anos de idade."
                },
                "ru": {
                    "q": "Сколько лет {label}?",
                    "a": "{label} {augmented_age} лет."
                },
                "ko": {
                    "q": "{label} 몇 살입니까?",  # 존이
                    "a": "{label}은 {augmented_age} 세입니다."
                },
                "hi": {
                    "q": "{label} कितना पुराना है?",  # जॉन
                    "a": "{label} {augmented_age} साल का है।"
                },
                "ja": {
                    "q": "{label}は何歳ですか？",  # ジョン
                    "a": "{label}は{augmented_age}歳です。"
                }
            }
        ]
        q = self.simple_question_generator(entity, instance_of, properties, questions, lang)
        return q

    def human_birthday(self, entity, lang="en"):
        instance_of = self.instances_of["human"]
        properties = ["augmented_birthday"]
        questions = [
            {
                "es": {
                    "q": "¿Cuándo es el cumpleaños de {label}?",
                    "a": "El cumpleaños de {label} es el {augmented_birthday}."
                },
                "en": {
                    "q": "When is {label} birthday?",
                    "a": "{label} birthday is {augmented_birthday}."
                },
                "zh-hans": {
                    "q": "什么时候是{label}生日？",
                    "a": "{label}生日是{augmented_birthday}。"
                },
                "pt": {
                    "q": "Quando é aniversário {label}?",
                    "a": "{label} aniversário é {augmented_birthday}."
                },
                "ru": {
                    "q": "Когда будет день рождения {label}?",
                    "a": "День рождения {label} - {augmented_birthday}."
                },
                "ko": {
                    "q": "{label} 생일은 언제입니까?",  # 존
                    "a": "{label} 생일은 {augmented_birthday}입니다."
                },
                "hi": {
                    "q": "{label} जन्मदिन कब है?",  # जॉन
                    "a": "{label} जन्मदिन {augmented_birthday} है"
                },
                "ja": {
                    "q": "{label}の誕生日はいつですか？",  # ジョン
                    "a": "{label}の誕生日は{augmented_birthday}です。"
                }
            }
        ]
        q = self.simple_question_generator(entity, instance_of, properties, questions, lang)
        return q

    def human_is_alive(self, entity, lang="en"):
        instance_of = self.instances_of["human"]
        properties = ["augmented_is_alive"]
        questions = [
            {
                "es": {
                    "q": "¿Vive {label}?",
                    "a": "{label} está {augmented_is_alive}."
                },
                "en": {
                    "q": "Is {label} alive?",
                    "a": "{label} is {augmented_is_alive}."
                },
                "zh-hans": {
                    "q": "{label}活著嗎？",
                    "a": "{label} {augmented_is_alive}。"
                },
                "pt": {
                    "q": "O {label} vivo?",
                    "a": "{label} {augmented_is_alive}."
                },
                "ru": {
                    "q": "Живет ли {label}?",
                    "a": "{label} - {augmented_is_alive}."
                },
                "ko": {
                    "q": "{label}은 살아 있니?",  # 존
                    "a": "{label}{augmented_is_alive}"
                },
                "hi": {
                    "q": "क्या {label} जीवित है?",  # जॉन
                    "a": "{label}{augmented_is_alive}"
                },
                "ja": {
                    "q": "{label}は生きていますか？",  # ジョン
                    "a": "{label}{augmented_is_alive}"
                }
            }
        ]
        q = self.simple_question_generator(entity, instance_of, properties, questions, lang)
        return q

    def human_eye_color(self, entity, lang="en"):
        instance_of = self.instances_of["human"]
        properties = ["eye_color"]
        questions = [
            {
                "es": {
                    "q": "¿De que color son los ojos de {label}?",
                    "a": "{label} está {eye_color}."
                },
                "en": {
                    "q": "What color are {label}'s eyes?",
                    "a": "{label}'s eyes are {eye_color}."
                },
                "zh-hans": {
                    "q": "{label}的眼睛是什麼顏色的？",
                    "a": "{label}的眼睛是{eye_color}的。"
                },
                "pt": {
                    "q": "Que cor são os olhos de {label}?",
                    "a": "Os olhos de {label} são {eye_color}."
                },
                "ru": {
                    "q": "Какого цвета глаза {label}?",
                    "a": "Глаза {label} {eye_color}."
                },
                "ko": {
                    "q": "{label}의 눈은 어떤 색입니까?",  # 존  # 녹색
                    "a": "{label}의 눈은 {eye_color}입니다."
                },
                "hi": {
                    "q": "क्या {label} की आंखें रंग हैं?",  # जॉन  # हरा
                    "a": "{label} की आँखें {eye_color} हैं"
                },
                "ja": {
                    "q": "{label}の目はどんな色ですか？",  # ジョン  # 緑
                    "a": "{label}の目は{eye_color}色です。"
                }
            }
        ]
        q = self.simple_question_generator(entity, instance_of, properties, questions, lang)
        return q

    def human_hair_color(self, entity, lang="en"):
        instance_of = self.instances_of["human"]
        properties = ["hair_color"]
        questions = [
            {
                "es": {
                    "q": "¿De que color es el cabello de {label}?",
                    "a": "{label} está {hair_color}."
                },
                "en": {
                    "q": "What color are {label}'s hair?",
                    "a": "{label}'s hair is {hair_color}."
                },
                "zh-hans": {
                    "q": "{label}的頭髮是什麼顏色的？",
                    "a": "{label}的頭髮是{hair_color}。"
                },
                "pt": {
                    "q": "Que cor é o cabelo de {label}?",
                    "a": "O cabelo de {label} é {hair_color}."
                },
                "ru": {
                    "q": "Какого цвета волосы {label}?",
                    "a": "Волосы {label} - {hair_color}."
                },
                "ko": {
                    "q": "{label}의 머리 색깔은 어떤 색입니까?",
                    "a": "{label}의 머리카락은 {hair_color} 색이야."
                },
                "hi": {
                    "q": "{label} के बाल क्या रंग हैं?",
                    "a": "{label} के बाल {hair_color} हैं"
                },
                "ja": {
                    "q": "{label}の髪はどんな色ですか？",
                    "a": "{label}の髪は{hair_color}です。"
                }
            }
        ]
        q = self.simple_question_generator(entity, instance_of, properties, questions, lang)
        return q

    def planet_mass(self, entity, lang="en"):
        instance_of = self.instances_of["planet"]
        properties = ["mass"]
        questions = [
            {
                "es": {
                    "q": "¿Cual es el peso del planeta {label}?",
                    "a": "El planeta {label} tiene una masa de {mass}."
                },
                "en": {
                    "q": "How much weights the planet {label}?",
                    "a": "The planet {label} has a mass of {mass}."
                },
                "zh-hans": {
                    "q": "{label}的重量是多少？",
                    "a": "{label}的質量是{mass}。"
                },
                "pt": {
                    "q": "Quanto pesa o planeta {label}?",
                    "a": "O planeta {label} tem uma massa de {mass}."
                },
                "ru": {
                    "q": "Сколько весит планета {label}?",
                    "a": "Планета {label} имеет массу {mass}."
                },
                "ko": {
                    "q": "{label}의 무게는 얼마입니까?",  # 화성
                    "a": "{label} 행성의 질량은 {mass}입니다."
                },
                "hi": {
                    "q": "ग्रह {label} कितना वजन?",  # मंगल ग्रह
                    "a": "ग्रह {label} का एक द्रव्यमान है {mass}।"
                },
                "ja": {
                    "q": "どのくらいの重量の惑星{label}か？",  # 火星
                    "a": "惑星の{label}の質量は{mass}です。"
                }
            }
        ]
        q = self.simple_question_generator(entity, instance_of, properties, questions, lang)
        return q

    def chemical_element_symbol(self, entity, lang="en"):
        instance_of = self.instances_of["chemical_element"]
        properties = ["element_symbol"]
        questions = [
            {
                "es": {
                    "q": "¿Cuál es el símbolo químico del {label}?",
                    "a": "El símbolo químico del {label} es {element_symbol}."
                },
                "en": {
                    "q": "What is the element symbol of {label}?",
                    "a": "The element symbol of {label} is {element_symbol}."
                },
                "zh-hans": {
                    "q": "{label}",
                    "a": "{label}{element_symbol}"
                },
                "pt": {
                    "q": "{label}",
                    "a": "{label}{element_symbol}"
                },
                "ru": {
                    "q": "{label}",
                    "a": "{label}{element_symbol}"
                },
                "ko": {
                    "q": "{label}",
                    "a": "{label}{element_symbol}"
                },
                "hi": {
                    "q": "{label}",
                    "a": "{label}{element_symbol}"
                },
                "ja": {
                    "q": "{label}",
                    "a": "{label}{element_symbol}"
                }
            }
        ]
        q = self.simple_question_generator(entity, instance_of, properties, questions, lang)
        return q

    def chemical_atomic_number(self, entity, lang="en"):
        instance_of = self.instances_of["chemical_element"]
        properties = ["atomic_number"]
        questions = [
            {
                "es": {
                    "q": "¿Cuál es el número atómico del {label}?",
                    "a": "El número atómico del {label} es {atomic_number}."
                },
                "en": {
                    "q": "What is the atomic number of {label}?",
                    "a": "The atomic number of {label} is {atomic_number}."
                },
                "zh-hans": {
                    "q": "{label}",
                    "a": "{label}{atomic_number}"
                },
                "pt": {
                    "q": "{label}",
                    "a": "{label}{atomic_number}"
                },
                "ru": {
                    "q": "{label}",
                    "a": "{label}{atomic_number}"
                },
                "ko": {
                    "q": "{label}",
                    "a": "{label}{atomic_number}"
                },
                "hi": {
                    "q": "{label}",
                    "a": "{label}{atomic_number}"
                },
                "ja": {
                    "q": "{label}",
                    "a": "{label}{atomic_number}"
                }
            }
        ]
        q = self.simple_question_generator(entity, instance_of, properties, questions, lang)
        return q

    # Generate
    def generate(self, entity, lang="en"):
        questions = [
            self.planet_mass(entity, lang),
            self.film_director(entity, lang),
            self.film_producer(entity, lang),
            self.film_photography_director(entity, lang),
            self.film_music_composer(entity, lang),
            self.film_cost_money(entity, lang),
            self.film_box_office(entity, lang),
            self.film_screewriter(entity, lang),
            self.human_age(entity, lang),
            self.human_birthday(entity, lang),
            self.human_is_alive(entity, lang),
            self.human_eye_color(entity, lang),
            self.human_hair_color(entity, lang),
            self.chemical_atomic_number(entity, lang),
            self.chemical_element_symbol(entity, lang)
        ]
        return questions

    # Misc
    def filter(self, entity, ids, properties):
        if not self.is_instance_of(entity, ids):
            return False
        for property_ in properties:
            if not self.has_property(entity, property_):
                return False
        return True

    def get_property(self, entity, property_):
        director = ""
        for director_ in entity.properties[property_]:
            if type(director_) == str:  # TODO
                director = "{}{}, ".format(director, director_)
            elif type(director_) == int:  # TODO
                director = "{}{}, ".format(director, director_)
            elif type(director_) == bool:  # TODO
                director = "{}{}, ".format(director, director_)
            else:
                if "label" in director_.properties:
                    for director_label in director_.properties["label"]:
                        director = "{}{}, ".format(director, director_label)
        director = director[:-2]
        return director

    def is_instance_of(self, entity, instances):
        if "instance_of" not in entity.properties:
            return False
        any_id = False
        for id_ in entity.properties["instance_of"]:
            if id_.properties["id"] in instances:
                any_id = True
        return any_id

    def has_property(self, entity, property_):
        any_dir = False
        if property_ not in entity.properties:
            return False
        for director_properties in entity.properties[property_]:
            if director_properties is None:
                continue
            if type(director_properties) == str:  # TODO
                any_dir = True
            elif type(director_properties) == int:  # TODO
                any_dir = True
            elif type(director_properties) == bool:  # TODO
                any_dir = True
            else:
                for dp in director_properties.properties:
                    if "label" in dp:
                        any_dir = True
        return any_dir
