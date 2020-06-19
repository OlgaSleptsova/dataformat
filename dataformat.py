import json

from collections import Counter
def opens(filename):
    with open(filename,encoding = 'utf-8') as f:
        data = json.load(f)
    return data
def  list_word(filename):
    list1 =[]
    for items in filename['rss']['channel']["items"]:
      list1.append(items['description'].split())
    return list1
def tenmax_word(filename):
    list2 =[]
    for words in filename:
        for word in words:
            if len(word) > 6:
                list2.append(word)
    list3 = Counter(list2)
    sorted_list = sorted(list3.items(),key = lambda kv: kv[1])
    sorted_list.reverse()
    print(sorted_list[0:10])



def top_ten(falename):
    x = opens(falename)
    y = list_word(x)
    z =tenmax_word(y)
    return z

top_ten("newsarf.json")

import xml.etree.ElementTree as ET
def reading (filename):
    parser = ET.XMLParser(encoding= "utf-8")
    tree = ET.parse(filename, parser)
    root = tree.getroot()

    xml_items = root.findall("channel/item")
    return xml_items
def list_news(filename):
    list1 =[]
    for items in filename:
        for m in items.find("description").text.split():
            if len(m) > 6:
                list1.append(m)
    return list1
def listtop_ten (filename):
    list2 =Counter(filename)
    sorted_list = sorted(list2.items(), key=lambda kv: kv[1])
    sorted_list.reverse()
    print(sorted_list[0:10])
def top_ten(filename):
    x = reading(filename)
    z = list_news(x)
    y = listtop_ten(z)
    return y

top_ten("newsarf.xml")