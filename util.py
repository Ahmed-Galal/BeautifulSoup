#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
import re


class Util():

    def has_img(self,tag):
        if (tag.has_attr('class') and not tag.has_attr('style')):
            if ("item_imagePic" in tag.get('class')):
                return True
        return False

    def fixString(self,txt):
        return re.sub("'", '`', txt)

    def getUrl(self,url):
        response = urllib2.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        return soup

    def item_json_object(self,item):
        data = {
            'availabilityStarts': self.fixString(item.find('p', itemprop='availabilityStarts').string.encode('utf-8')),
            'description': self.fixString(item.find('p', itemprop='description').string.encode('utf-8')),
            'city': self.fixString(item.find('span', itemprop='address').string.encode('utf-8')),
            'Honoraires': item.find(text=re.compile('Honoraires')).parent.next_sibling.string.encode('utf-8'),
            'Référence': item.find(text=re.compile('Référence')).parent.next_sibling.string.encode('utf-8'),
            'GES': item.find(text=re.compile('GES')).parent.next_sibling.string.encode('utf-8'),
            'Classe_énergie': item.find(text=re.compile('Classe énergie')).parent.next_sibling.string.encode('utf-8')
        }
        return data

    def json_object(self,item,item_url):
        i_url = item_url.replace('{ITEMID}',item.find('div', class_='saveAd').get('data-savead-id'))
        soup = self.getUrl(i_url)
        item_json = self.item_json_object(soup.find('section', class_="adview_main"))
        data = {
            "img": self.fixString(item.find('span', class_='lazyload').get('data-imgsrc') if item.find(self.has_img) else ''),
            "title": self.fixString(item.find('h2', class_='item_title').string.encode('utf-8')),
            "price": self.fixString(item.find('h3', class_='item_price').string.encode('utf-8')),
            "date": self.fixString(item.find('p', itemprop='availabilityStarts').get('content').string.encode('utf-8')),
            "id": self.fixString(item.find('div', class_='saveAd').get('data-savead-id').encode('utf-8')),
            "url": i_url,
            'availabilityStarts': item_json.availabilityStarts,
            'description': item_json.description,
            'city': item_json.address,
            'postal_code': item_json.address.split(' ')[1],
            'Honoraires': item_json.Honoraires,
            'Référence': item_json.Référence,
            'GES': item_json.GES,
            'Classe_énergie': item_json.Classe_énergie,
        }
        return data