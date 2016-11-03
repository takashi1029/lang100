#coding: utf-8
import json

datas = []
with open("jawiki-country.json") as f:
    for line in f:
        datas.append(json.loads(line))