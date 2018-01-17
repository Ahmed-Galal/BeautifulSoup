#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
import re

def has_img(tag):
    if(tag.has_attr('class') and not tag.has_attr('style') ):
        if("item_imagePic" in tag.get('class')):
            return True
    return False

def fixString(txt):
    return re.sub("'", '`', txt)


response = urllib2.urlopen('https://www.leboncoin.fr/bureaux_commerces/offres/?th=1&q=Etampes&it=1&st=a')
html = response.read()
soup = BeautifulSoup(html, 'html.parser')


data_list = []
for item in soup.find_all('li',itemtype='http://schema.org/Offer'):
    data = {
        "img":fixString(item.find('span',class_='lazyload').get('data-imgsrc') if item.find(has_img) else ''),
        "title":fixString(item.find('h2',class_='item_title').string.encode('utf-8')),
        "price":fixString(item.find('h3',class_='item_price').string.encode('utf-8')),
        "date":fixString(item.find('p',itemprop='availabilityStarts').string.encode('utf-8')),
        "id":fixString(item.find('div',class_='saveAd').get('data-savead-id').encode('utf-8')),
        "url":fixString("https://www.leboncoin.fr/bureaux_commerces/"+str(item.find('div',class_='saveAd').get('data-savead-id'))+".htm?ca=12_s")
    }
    data_list.append(data)
print(data_list)


