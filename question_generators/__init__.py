class questions:
    def film_producer(self, entity, lang="en"):
        ids = [
            "Q18011172",  # Film project
            "Q11424",  # Film
            "Q29168811",  # Animated Feature Film
            "Q229390",  # 3D film
            "Q202866"
        ]
        properties = ["producer"]
        if not self.filter(entity, ids, properties):
            return None
        questions_answers = []
        producer = self.get_property(entity, "producer")
        info = {
            "label": entity.properties["label"][0],
            "producer": producer
        }
        questions = [
            {
                "es": {
                    "q": "¿Quién produjo la película {label}?".format(**info),
                    "a": "La película {label} fue producida por {producer}.".format(**info)
                },
                "en": {
                    "q": "Who produced the movie {label}?".format(**info),
                    "a": "The movie {label} was produced by {producer}.".format(**info)
                },
                "zh-hans": {
                    "q": "谁制作了电影{label}？".format(**info),
                    "a": "电影{label}由{producer}制作。".format(**info)
                },
                "pt": {
                    "q": "Quem produziu o filme {label}?".format(**info),
                    "a": "O filme {label} foi produzido por {producer}.".format(**info)
                }
            }
        ]
        questions_return = []
        for question in questions:
            if lang in question:
                questions_return.append(question[lang])
        return questions_return

    def film_director(self, entity, lang="en"):
        ids = [
            "Q18011172",  # Film project
            "Q11424",  # Film
            "Q29168811",  # Animated Feature Film
            "Q229390",  # 3D film
            "Q202866"
        ]
        properties = ["director"]
        if not self.filter(entity, ids, properties):
            return None
        questions_answers = []
        director = self.get_property(entity, "director")
        info = {
            "label": entity.properties["label"][0],
            "director": director
        }
        questions = [
            {
                "es": {
                    "q": "¿Quién dirigió la película {label}?".format(**info),
                    "a": "La película {label} fue dirigida por {director}.".format(**info)
                },
                "en": {
                    "q": "Who directed the movie {label}?".format(**info),
                    "a": "The movie {label} was directed by {director}.".format(**info)
                },
                "zh-hans": {
                    "q": "谁指导了电影{label}？".format(**info),
                    "a": "电影{label}由{director}执导。".format(**info)
                },
                "pt": {
                    "q": "Quem dirigiu o filme {label}?".format(**info),
                    "a": "O filme {label} foi dirigido por {director}.".format(**info)
                }
            }
        ]
        questions_return = []
        for question in questions:
            if lang in question:
                questions_return.append(question[lang])
        return questions_return

    def film_photography_director(self, entity, lang="en"):
        ids = [
            "Q18011172",  # Film project
            "Q11424",  # Film
            "Q29168811",  # Animated Feature Film
            "Q229390",  # 3D film
            "Q202866"
        ]
        properties = ["director_of_photography"]
        if not self.filter(entity, ids, properties):
            return None
        questions_answers = []
        director_of_photography = self.get_property(entity, "director_of_photography")
        info = {
            "label": entity.properties["label"][0],
            "director_of_photography": director_of_photography
        }
        questions = [
            {
                "es": {
                    "q": "¿Quién hizo la dirección de fotografía en la película {label}?".format(**info),
                    "a": "La película {label} tuvo como director/a de fotografía a {director_of_photography}.".format(**info)
                },
                "en": {
                    "q": "Who is the director of photography in the movie {label}?".format(**info),
                    "a": "The director of photography in {label} is {director_of_photography}.".format(**info)
                },
                "zh-hans": {
                    "q": "谁是电影{label}的摄影导演？".format(**info),
                    "a": "{label}中的摄影导演是{director_of_photography}。".format(**info)
                },
                "pt": {
                    "q": "Quem é o diretor de fotografia no filme {label}?".format(**info),
                    "a": "O diretor de fotografia em {label} é {director_of_photography}.".format(**info)
                }
            }
        ]
        questions_return = []
        for question in questions:
            if lang in question:
                questions_return.append(question[lang])
        return questions_return

    def film_music_composer(self, entity, lang="en"):
        ids = [
            "Q18011172",  # Film project
            "Q11424",  # Film
            "Q29168811",  # Animated Feature Film
            "Q229390",  # 3D film
            "Q202866"
        ]
        properties = ["music_composer"]
        if not self.filter(entity, ids, properties):
            return None
        questions_answers = []
        director_of_photography = self.get_property(entity, "music_composer")
        info = {
            "label": entity.properties["label"][0],
            "music_composer": director_of_photography
        }
        questions = [
            {
                "es": {
                    "q": "¿Quién compuso la música para la película {label}?".format(**info),
                    "a": "La película {label} tuvo como compositor a {music_composer}.".format(**info)
                },
                "en": {
                    "q": "Who is the music composer in the movie {label}?".format(**info),
                    "a": "The music composer in {label} is {music_composer}.".format(**info)
                },
                "zh-hans": {
                    "q": "谁是电影{label}的音乐作曲家？".format(**info),
                    "a": "{label}中的音乐作曲者是{music_composer}。".format(**info)
                },
                "pt": {
                    "q": "Quem é o compositor de música no filme {label}?".format(**info),
                    "a": "O compositor de música em {label} é {music_composer}.".format(**info)
                }
            }
        ]
        questions_return = []
        for question in questions:
            if lang in question:
                questions_return.append(question[lang])
        return questions_return

    def film_cost_money(self, entity, lang="en"):
        ids = [
            "Q18011172",  # Film project
            "Q11424",  # Film
            "Q29168811",  # Animated Feature Film
            "Q229390",  # 3D film
            "Q202866"
        ]
        properties = ["cost_money"]
        if not self.filter(entity, ids, properties):
            return None
        questions_answers = []
        cost_money = self.get_property(entity, "cost_money")
        info = {
            "label": entity.properties["label"][0],
            "cost_money": cost_money
        }
        questions = [
            {
                "es": {
                    "q": "¿Cuanto costó la película {label}?".format(**info),
                    "a": "La película {label} tuvo un costo de ${cost_money}.".format(**info)
                },
                "en": {
                    "q": "How much did the movie {label} cost?".format(**info),
                    "a": "The movie {label} cost was ${cost_money}.".format(**info)
                },
                "zh-hans": {
                    "q": "电影{label}的成本是多少？".format(**info),
                    "a": "电影的{label}成本为$ {cost_money}。".format(**info)
                },
                "pt": {
                    "q": "Quanto custa o filme {label}?".format(**info),
                    "a": "O custo do filme {label} foi $ {cost_money}.".format(**info)
                }
            }
        ]
        questions_return = []
        for question in questions:
            if lang in question:
                questions_return.append(question[lang])
        return questions_return

    def film_box_office(self, entity, lang="en"):
        ids = [
            "Q18011172",  # Film project
            "Q11424",  # Film
            "Q29168811",  # Animated Feature Film
            "Q229390",  # 3D film
            "Q202866"
        ]
        properties = ["box_office"]
        if not self.filter(entity, ids, properties):
            return None
        questions_answers = []
        box_office = self.get_property(entity, "box_office")
        info = {
            "label": entity.properties["label"][0],
            "box_office": box_office
        }
        questions = [
            {
                "es": {
                    "q": "¿Cuanto ganó la película {label}?".format(**info),
                    "a": "La película {label} tuvo una ganancia de ${box_office}.".format(**info)
                },
                "en": {
                    "q": "What was the box office of the movie {label}?".format(**info),
                    "a": "The movie {label} box office was ${box_office}.".format(**info)
                },
                "zh-hans": {
                    "q": "电影{label}票房是什么？".format(**info),
                    "a": "电影{label}票房是$ {box_office}。".format(**info)
                },
                "pt": {
                    "q": "Qual era a bilheteria do filme {label}?".format(**info),
                    "a": "A caixa de correio do filme {label} foi $ {box_office}.".format(**info)
                }
            }
        ]
        questions_return = []
        for question in questions:
            if lang in question:
                questions_return.append(question[lang])
        return questions_return

    def film_screewriter(self, entity, lang="en"):
        ids = [
            "Q18011172",  # Film project
            "Q11424",  # Film
            "Q29168811",  # Animated Feature Film
            "Q229390",  # 3D film
            "Q202866"
        ]
        properties = ["screenwriter"]
        if not self.filter(entity, ids, properties):
            return None
        questions_answers = []
        screenwriter = self.get_property(entity, "screenwriter")
        info = {
            "label": entity.properties["label"][0],
            "screenwriter": screenwriter
        }
        questions = [
            {
                "es": {
                    "q": "¿Quién es el guionista de la película {label}?".format(**info),
                    "a": "La película {label} tuvo como guionista a {screenwriter}.".format(**info)
                },
                "en": {
                    "q": "Who was the screenwriter of the movie {label}?".format(**info),
                    "a": "The screenwriter in the movie {label} was {screenwriter}.".format(**info)
                },
                "zh-hans": {
                    "q": "谁是电影{label}的编剧？".format(**info),
                    "a": "电影{label}中的编剧是{screenwriter}。".format(**info)
                },
                "pt": {
                    "q": "Quem foi o roteirista do filme {label}?".format(**info),
                    "a": "O roteirista no filme {label} foi {screenwriter}.".format(**info)
                }
            }
        ]
        questions_return = []
        for question in questions:
            if lang in question:
                questions_return.append(question[lang])
        return questions_return

    def human_age(self, entity, lang="en"):
        ids = [
            "Q5",  # Human
        ]
        properties = ["augmented_age"]
        if not self.filter(entity, ids, properties):
            return None
        questions_answers = []
        augmented_age = self.get_property(entity, "augmented_age")
        info = {
            "label": entity.properties["label"][0],
            "augmented_age": augmented_age
        }
        questions = [
            {
                "es": {
                    "q": "¿Cual es la edad de {label}?".format(**info),
                    "a": "{label} tiene {augmented_age} años.".format(**info)
                },
                "en": {
                    "q": "How old is {label}?".format(**info),
                    "a": "{label} is {augmented_age} years old.".format(**info)
                },
                "zh-hans": {
                    "q": "{label}有多大？".format(**info),
                    "a": "{label}是{augmented_age}岁。".format(**info)
                },
                "pt": {
                    "q": "Quantos anos tem {label}?".format(**info),
                    "a": "{label} é {augmented_age} anos de idade.".format(**info)
                }
            }
        ]
        questions_return = []
        for question in questions:
            if lang in question:
                questions_return.append(question[lang])
        return questions_return

    def human_birthday(self, entity, lang="en"):
        ids = [
            "Q5",  # Human
        ]
        properties = ["augmented_birthday"]
        if not self.filter(entity, ids, properties):
            return None
        questions_answers = []
        augmented_birthday = self.get_property(entity, "augmented_birthday")
        info = {
            "label": entity.properties["label"][0],
            "augmented_birthday": augmented_birthday
        }
        questions = [
            {
                "es": {
                    "q": "¿Cuando es el cumpleaños de {label}?".format(**info),
                    "a": "El cumpleaños de {label} es el {augmented_birthday}.".format(**info)
                },
                "en": {
                    "q": "When is {label} birthday?".format(**info),
                    "a": "{label} birthday is {augmented_birthday}.".format(**info)
                },
                "zh-hans": {
                    "q": "什么时候是{label}生日？".format(**info),
                    "a": "{label}生日是{augmented_birthday}。.".format(**info)
                },
                "pt": {
                    "q": "Quando é aniversário {label}?".format(**info),
                    "a": "{label} aniversário é {augmented_birthday}.".format(**info)
                }
            }
        ]
        questions_return = []
        for question in questions:
            if lang in question:
                questions_return.append(question[lang])
        return questions_return

    # Generate
    def generate(self, entity, lang="en"):
        questions = [
            self.film_director(entity, lang),
            self.film_producer(entity, lang),
            self.film_photography_director(entity, lang),
            self.film_music_composer(entity, lang),
            self.film_cost_money(entity, lang),
            self.film_box_office(entity, lang),
            self.film_screewriter(entity, lang),
            self.human_age(entity, lang),
            self.human_birthday(entity, lang)
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
            else:
                for dp in director_properties.properties:
                    if "label" in dp:
                        any_dir = True
        return any_dir
