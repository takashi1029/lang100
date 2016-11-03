#coding: utf-8

import json
import gzip
import re

def get_text_wiki(title):
    with gzip.open("jawiki-country.json.gz","rb") as f:
        article_json = f.readline()
        while article_json:
            article_dict = json.loads(article_json)
            if article_dict["title"]==title:
                article = article_dict["text"]
                return article
            artcile_json = f.readline()

article = get_text_wiki(u"イギリス")