import os
import json
import datetime

# Changes
# https://www.wikidata.org/wiki/Special:RecentChanges?hidebots=1&hidecategorization=1&limit=50&days=7&urlversion=2&action=render&enhanced=0
# https://www.wikidata.org/wiki/Special:RecentChanges?limit=50&days=7&urlversion=2&action=render&enhanced=0


class datawiki_entity:
    def __init__(self):
        self.properties = {}

    def set_property(self, property_name, property_value):
        if property_name == "id":
            self.properties[property_name] = property_value
        else:
            if property_name not in self.properties:
                self.properties[property_name] = [property_value]
            else:
                self.properties[property_name].append(property_value)

    def __str__(self):
        if "label" in self.properties and self.properties["label"] is not None:
            return "<{}>".format(self.properties["label"][0])
        else:
            return "<{}>".format(self.properties["id"])

    def __repr__(self):
        return self.__str__()


class datawiki_reader:
    def __init__(self, base_path):
        self.base_path = base_path
        self.prop_map = {
            "P17": "country",
            "P19": "place_of_birth",
            "P26": "spouse",
            # External ID
            "P3417": "external_id_quora",
            "P3827": "external_id_jstor",
            "P227": "external_id_gnd",
            "P345": "external_id_imdb",
            "P1220": "external_id_ibdb_person",
            "P214": "external_id_viaf",
            "P1207": "external_id_nukat",
            "P2529": "external_id_csfd",
            "P2605": "external_id_csfd_person",
            "P1267": "external_id_allocine",
            "P1266": "external_id_allocine_person",
            "P1265": "external_id_allocine_film",
            "P905": "external_id_port_film",
            "P2435": "external_id_port_person",
            "P1874": "external_id_netflix",
            "P2603": "external_id_kinopoisk",
            "P2604": "external_id_kinopoisk_person",
            "P4834": "external_id_deutsche_synchronkartei",
            "P2638": "external_id_tvcom",
            "P3138": "external_id_ofdb",
            "P2168": "external_id_sfdb_person",
            "P1263": "external_id_nndb_people",
            "P3346": "external_id_hkmdb_person",
            "P1649": "external_id_kmdb_person",
            "P2387": "external_id_elonet_person",
            "P2019": "external_id_allmovie_artist",
            "P1562": "external_id_allmovie_movie",
            "P1728": "external_id_allmusic_artist",
            "P3430": "external_id_snac_ark",
            "P950": "external_id_bne",
            "P268": "external_id_bnf",
            "P2626": "external_id_dnf_person",
            "P244": "external_id_library_of_congress_authority",
            "P2469": "external_id_theatricalia_id",
            "P2519": "external_id_scopedk",
            "P213": "external_id_isni",
            "P646": "external_id_freebase",
            "P2639": "external_id_filmportal",
            "P2949": "external_id_wikitree",
            "P2163": "external_id_fast",
            "P3479": "external_id_omni_topic",
            "P3219": "external_id_encyclopedia_universalis_online",
            "P3569": "external_id_cultureel_woordenboek",
            "P1969": "external_id_moviemeter_director",
            "P1771": "external_id_ipeds",
            "P409": "external_id_nla_australia",
            "P2847": "external_id_google_plus",
            "P2002": "external_id_twitter",
            "P2003": "external_id_instagram",
            "P3153": "external_id_crowwref_funder",
            "P2427": "external_id_grid",
            "P3077": "external_id_cineplex_film",
            "P480": "external_id_filmaffinity",
            "P4780": "external_id_mymovies_movie",
            "P2671": "external_id_google_knowledge_graph",
            "P4783": "external_id_movieplayer_film",
            "P3135": "external_id_elcinema_film",
            "P3136": "external_id_elcinema_person",
            "P3144": "external_id_elfilm_person",
            "P1237": "external_id_box_office_mojo_film",
            "P2688": "external_id_box_office_mojo_person",
            "P4632": "external_id_bechdel_test_movie_list",
            "P3808": "external_id_the_numbers_movie",
            "P1712": "external_id_metacritic",
            "P2755": "external_id_exploitation_visa_number",
            "P1258": "external_id_rotten_tomatoes",
            "P1017": "external_id_bav",
            "P1870": "external_id_name_assigning_authority_number",
            "P269": "external_id_sudoc_authorities",
            "P3762": "external_id_openmlol_author",
            "P1273": "external_id_cantic",
            "P4848": "external_id_librariesorg",
            "P2013": "external_id_facebook_identification_code",
            "P1566": "external_id_geonames",
            "P3348": "external_id_national_library_of_greece",
            "P3500": "external_id_ringgold",
            "P1565": "external_id_enciclopedia_de_la_literatura_en_mexico",
            "P1315": "external_id_people_australia",
            "P1006": "external_id_national_thesaurus_for_author_names",
            "P434": "external_id_musicbrainz_artist",
            "P349": "external_id_ndl",
            "P3305": "external_id_kinenote_person",
            "P1953": "external_id_discogs_artist",
            "P3478": "external_id_songkick_artist",
            "P1233": "external_id_isfdb_author",
            "P1296": "external_id_gran_enciclopedia_catalana",
            "P906": "external_id_selibr",
            "P648": "external_id_open_library",
            "P2174": "external_id_moma_artist",
            "P3056": "external_id_turner_classic_movies_person",
            "P2799": "external_id_turner_bvmc_person",
            "P1417": "external_id_encyclopedia_britannica_online",
            "P1284": "external_id_munzinger_iba",
            "P3106": "external_id_guardian_topic",
            "P3142": "external_id_edb_person",
            "P3192": "external_id_lastfm_music",
            "P3017": "external_id_rolling_stone_artist",
            "P2684": "kijwijzer_rating",  # TODO
            "P2704": "external_id_eidr",
            "P2456": "external_id_dblp",
            "P1741": "external_id_gtaa",
            "P4159": "external_id_werelate_person",
            "P3743": "external_id_itu_iso_iec",
            "P1003": "external_id_nlr_romania",
            "P3630": "external_id_babelio_author",
            "P949": "external_id_national_library_of_israel",
            "P2537": "external_id_free_software_directory",
            "P4479": "external_id_inducks_character",
            # Human
            "P463": "member_of",
            "P4570": "wikidata_project",
            "P1889": "different_from",
            "P571": "inception_time",
            "P18": "image",
            "P154": "logo_image",
            "P109": "signature_image",
            "P158": "seal_image",
            "P10": "video",
            "P51": "audio",
            "P131": "located_in",
            "P1412": "languages_spoken_written_or_signed",
            "P1971": "number_of_children",
            "P140": "religion",
            "P1853": "blood_type",
            "P108": "employer",
            "P172": "ethnic_group",
            "P2218": "net_worth_estimate",
            "P1303": "play_instrument",
            "P1477": "birth_name",
            "P263": "official_residence",
            "P451": "partner",
            "P101": "field_of_work",
            "P119": "place_of_burial",
            "P1196": "manner_of_death",
            "P509": "cause_of_death",
            "P1442": "image_of_grave",
            "P20": "place_of_death",
            "P3373": "sibling",
            "P40": "child_son",
            "P570": "date_of_death",
            "P102": "member_of_political_party",
            "P1050": "medical_condition",
            "P22": "father",
            "P25": "mother",
            "P551": "residence",
            "P607": "conflict_war",
            "P800": "notable_work",
            "P551": "residence",
            "P103": "native_language",
            "P2032": "work_period_end",

            "P1389": "product_certification",
            "P279": "subclass_of",
            "P242": "locator_map_image",
            "P1811": "list_of_episodes",
            "P86": "music_composer",
            "P580": "start_time",
            "P582": "end_time",
            "P1476": "title",
            "P527": "has_part",
            "P31": "instance_of",
            "P361": "part_of",
            "P2437": "number_of_seasons",
            "P1113": "number_of_episodes",
            "P856": "official_website",
            "P449": "original_network",
            "P373": "commons_category",
            "P935": "commons_gallery",
            "P161": "cast_member",
            "P179": "series",
            "P156": "followed_by",
            "P155": "follows",
            "P136": "genre",
            "P674": "characters",
            "P4312": "camera_setup",
            "P272": "production_company",
            "P462": "color",
            "P275": "license",
            "P138": "named_after",
            "P972": "catalog",
            "P921": "main_subject",

            "P910": "topic_main_category",
            "P1424": "topic_main_template",
            "P1151": "topic_main_wikimedia_portal",

            "P1709": "equivalent_class",
            "P2670": "has_parts_of_the_class",
            "P461": "opposite_of",
            "P3321": "male_form_of_label",
            "P2521": "female_form_of_label",

            "P162": "producer",
            "P750": "distribuitor",
            "P407": "language_of_work_or_name",
            "P364": "original_language_of_work",
            "P2512": "spinoff",
            "P495": "country_of_origin",
            "P170": "creator",
            "P21": "sex_or_gender",
            "P2031": "work_period_start",
            "P106": "occupation",
            "P27": "country_of_citizenship",
            "P734": "family_name",
            "P735": "given_name",
            "P1559": "name_in_native_language",
            "P569": "date_of_birth",
            "P69": "educated_at",
            # University
            "P969": "located_at_street_address",
            "P355": "subsidiary",
            "P749": "parent_organization",
            "P793": "significant_event",
            "P2828": "corporate_officer",
            "P585": "event_date",
            "P4195": "category_for_employees_of_organization",
            "P625": "coordinate_location",
            "P2643": "carnegie_classification_of_institutions_of_higher_education",
            "P1448": "official_name",
            "P3761": "ipv4_routing_prefix",
            "P281": "postal_code",
            "P2196": "students_count",
            "P1546": "motto",
            "P2936": "language_used",
            # Movie
            "P1657": "mpaa_film_rating",
            "P2363": "nmhh_film_rating",
            "P2758": "cnc_film_rating_france",
            "P3834": "rtc_film_rating",
            "P3306": "icaa_rating",
            "P3428": "incaa_film_rating",
            "P3402": "cnc_film_rating_romania",
            "P1411": "nominated_to_awards_for",
            "P166": "awards_received",
            "P2142": "box_office",
            "P577": "publication_date",
            "P58": "screenwriter",
            "P1040": "film_editor",
            "P344": "director_of_photography",
            "P57": "director",
            "P1431": "executive_producer",
            "P3174": "art_director",
            "P2130": "cost_money",
            "P2047": "duration",
            "P1552": "has_quality",
            "P159": "headquarters_location",
            "P3876": "category_for_alumni_of_educational_institution",
            "P942": "theme_music",
            "P2061": "aspect ratio",
            "P1680": "subtitle",
            "P840": "narrative_location",
            "P915": "filming_location",
            "P725": "voice_actor",
            "P1981": "fsk_film_rating",
            "P3650": "jmk_film_rating",
            "P406": "soundtrack_album",
            "P144": "based_on",
            "P180": "depicts",
            "P1809": "choreographer",
            "P1877": "after_a_work_by",
            "P2408": "set_in_period",
            "P2515": "costumer_designer",
            "P2554": "production_designer",
            "P2769": "budget",
            "P3092": "film_crew_member",
            "P3300": "musical_conductor",
            "P941": "inspired_by",
            "P1881": "list_of_characters",
            "P2079": "fabrication_method",
            # Company
            "P112": "founded_by",
            "P127": "owned_by",
            "P452": "industry",
            "P1056": "product_or_material_produced",
            "P1128": "number_of_employees",
            "P1343": "described_by_source",
            "P1454": "legal_form",
            "P169": "chief_executive_officer",
            "P1830": "owner_of",
            "P199": "business_division",
            "P2137": "total_equity",
            "P2138": "total_liabilities",
            "P2139": "total_revenue",
            "P2226": "market_capitalization",
            "P2295": "net_profit",
            "P2403": "total_assets",
            "P2959": "permanent_duplicated_item",
            "P3320": "board_member",
            "P3362": "operating_income",
            "P414": "stock_exchange",
            "P4776": "mac_address_clock_large_id",
            "P488": "chairperson",
            "P740": "location_of_formation_constitution",
            # Character
            "P1441": "present_in_work",
            # Software
            "P1072": "readable_file_format",
            "P1073": "writable_file_format",
            "P1324": "source_code_repository",
            "P1401": "bug_tracking_system",
            "P1482": "stack_exchange_tag",
            "P178": "developer",
            "P1814": "name_in_kana",
            "P277": "programming_language",
            "P306": "operating_system",
            "P348": "software_version",
            "P366": "use",
            "P400": "platform",
            "P437": "distribution",
            "P751": "introduced_feature",

        }

    def calculate_age(self, born):
        if type(born) == list:
            return None
        today = datetime.date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    def augment_data(self, python_entity):
        # TODO wrong age for Walt Disney
        if "date_of_birth" in python_entity.properties:
            for date_ in python_entity.properties["date_of_birth"]:
                age = self.calculate_age(date_)
                birthday = "{}/{}".format(date_.month, date_.day)
            python_entity.set_property("augmented_age", age)
            python_entity.set_property("augmented_birthday", birthday)
        # TODO
        # if "instance_of" in python_entity.properties and python_entity.properties["instance_of"].properties["id"] == "Q5":  # Human
        if "spouse" in python_entity.properties:
            python_entity.set_property("augmented_married", True)
        else:
            python_entity.set_property("augmented_married", None)
        return python_entity

    def get_entity_json(self, entity_id):
        json_path = self.base_path
        for char in entity_id[:-1]:
            json_path = os.path.join(json_path, char)
        json_file_path = os.path.join(json_path, "{}.json".format(entity_id))
        if not os.path.isfile(json_file_path):
            return None
        with open(json_file_path) as data_file:
            entity = json.load(data_file)
        return entity

    def get_snak_data(self, data, lang="en", follow=0):
        mainsnak_datatype = data["datatype"]
        if "datavalue" not in data:
            mainsnak_value = None
        elif mainsnak_datatype == "wikibase-item":
            mainsnak_value = data["datavalue"]["value"]["id"]
            if follow > 0:
                follow -= 1
                snak_entity = self.get_entity(mainsnak_value, lang=lang, follow=follow)
                if snak_entity is not None:
                    mainsnak_value = snak_entity
        elif mainsnak_datatype == "commonsMedia":
            mainsnak_value = data["datavalue"]["value"]
        elif mainsnak_datatype == "time":
            mainsnak_value = data["datavalue"]["value"]["time"]
            try:
                mainsnak_value = datetime.datetime.strptime(mainsnak_value, '+%Y-%m-%dT%H:%M:%SZ')
            except:
                try:
                    mainsnak_value = datetime.datetime.strptime(mainsnak_value, '+%Y-00-00T%H:%M:%SZ')
                except:
                    pass
                pass
        elif mainsnak_datatype == "external-id":
            mainsnak_value = data["datavalue"]["value"]
        elif mainsnak_datatype == "quantity":
            mainsnak_value = data["datavalue"]["value"]["amount"]
        elif mainsnak_datatype == "string":
            mainsnak_value = data["datavalue"]["value"]
        elif mainsnak_datatype == "monolingualtext":
            mainsnak_value = data["datavalue"]["value"]["text"]
        elif mainsnak_datatype == "url":
            mainsnak_value = data["datavalue"]["value"]
        elif mainsnak_datatype == "globe-coordinate":
            mainsnak_value = data["datavalue"]["value"]["globe"]
        elif mainsnak_datatype == "wikibase-property":
            mainsnak_value = data["datavalue"]["value"]["id"]
        elif mainsnak_datatype == "math":
            mainsnak_value = data["datavalue"]["value"]
        elif mainsnak_datatype == "tabular-data":
            mainsnak_value = data["datavalue"]["value"]
        else:
            print(data)
            mainsnak_value = None
        return mainsnak_value

    def get_entity(self, entity_id, lang="en", follow=0):
        python_entity = datawiki_entity()
        python_entity.set_property("id", entity_id)
        entity = self.get_entity_json(entity_id)
        if entity is None:
            return python_entity
        if lang in entity["labels"]:
            python_entity.set_property("label", entity["labels"][lang]["value"])
        else:
            python_entity.set_property("label", None)
        if lang in entity["descriptions"]:
            python_entity.set_property("description", entity["descriptions"][lang]["value"])
        else:
            python_entity.set_property("description", None)
        for claim in entity["claims"]:
            for statement in entity["claims"][claim]:
                rank = statement["rank"]
                property_value = self.get_snak_data(statement["mainsnak"], lang=lang, follow=follow)
                property_name = claim
                if claim in self.prop_map:
                    property_name = self.prop_map[claim]
                python_entity.set_property(property_name, property_value)
        return python_entity
