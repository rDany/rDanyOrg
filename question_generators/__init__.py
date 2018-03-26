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
            self.human_is_alive(entity, lang)
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
