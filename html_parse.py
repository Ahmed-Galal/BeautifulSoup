#!/usr/bin/python
# -*- coding: utf-8 -*-
from util import Util
from schema import Schema

def parseUrl(url, item_url):
    soup = Util.getUrl(url)
    data_list = []
    for item in soup.find_all('li', itemtype='http://schema.org/Offer'):
        data_list.append(Util.json_object(item,item_url))
    return data_list

def saveData(data):
    #save data in db
    pass

def generateUrl():
    json_schema = Schema.getSchema()
    for key in json_schema:
        for loc in json_schema[key].locations:
            for city in json_schema[key].allowed_cities:
                url = json_schema[key].url.replace('{LOCATION}',loc).replace('{SEARCHKEY}',city)
                item_url = json_schema[key].item_url.replace('{LOCATION}',loc)
                scarping_data = parseUrl(url,item_url)
                saveData(scarping_data)
                # need to save scarping_data in db


def __main__():
    generateUrl()