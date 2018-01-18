#!/usr/bin/python
# -*- coding: utf-8 -*-
class Schema():
    def getSchema(self):
        json_schema = {
            "region": {
                "url": "https://www.leboncoin.fr/{LOCATION}/offres/ile_de_france/?o={SEARCHKEY}&ret=2",
                "item_url":"https://www.leboncoin.fr/{LOCATION}/{ITEMID}.htm?ca=12_s",
                "allowed_cities": ['Etampes', 'Dreux', 'Laval', 'Auxerre', 'Argentan', "L'Aigle", 'Bernay',
                                   'Lisieux', 'Falaise', 'Flers',
                                   'Vire', 'Bayeux', 'Saint-Lô', 'Coutances'
                    , 'Granville', 'Avranches', 'Deau­ville'],

                "locations": ['bureaux_commerces', 'location'],
            },
            "immo": {
                "url": "https://www.leboncoin.fr/{LOCATION}/offres/ile_de_france/?o={SEARCHKEY}&ret=2",
                "item_url": "https://www.leboncoin.fr/{LOCATION}/{ITEMID}.htm?ca=12_s",
                "allowed_cities": ['Etampes', 'Dreux', 'Laval', 'Auxerre', 'Argentan', "L'Aigle", 'Bernay',
                                   'Lisieux', 'Falaise', 'Flers',
                                   'Vire', 'Bayeux', 'Saint-Lô', 'Coutances'
                    , 'Granville', 'Avranches', 'Deau­ville'],

                "locations": ['bureaux_commerces', 'location'],
            },
            "immeuble": {
                "url": "https://www.leboncoin.fr/{LOCATION}/offres/ile_de_france/?o={SEARCHKEY}&ret=2",
                "item_url": "https://www.leboncoin.fr/{LOCATION}/{ITEMID}.htm?ca=12_s",
                "allowed_cities": ['Etampes', 'Dreux', 'Laval', 'Auxerre', 'Argentan', "L'Aigle", 'Bernay',
                                   'Lisieux', 'Falaise', 'Flers',
                                   'Vire', 'Bayeux', 'Saint-Lô', 'Coutances'
                    , 'Granville', 'Avranches', 'Deau­ville'],

                "locations": ['bureaux_commerces', 'location'],
            },
            "habitation": {
                "url": "https://www.leboncoin.fr/{LOCATION}/offres/ile_de_france/?o={SEARCHKEY}&ret=2",
                "item_url": "https://www.leboncoin.fr/{LOCATION}/{ITEMID}.htm?ca=12_s",
                "allowed_cities": ['Etampes', 'Dreux', 'Laval', 'Auxerre', 'Argentan', "L'Aigle", 'Bernay',
                                   'Lisieux', 'Falaise', 'Flers',
                                   'Vire', 'Bayeux', 'Saint-Lô', 'Coutances'
                    , 'Granville', 'Avranches', 'Deau­ville'],

                "locations": ['bureaux_commerces', 'location'],
            }
        }
        return json_schema