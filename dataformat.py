import json

from collections import Counter
def reading (filename):
    with open(filename,encoding = 'utf-8') as f:
        data = json.load(f)
    return data
def  list_news (filename):
    list1 =[]
    for items in filename['rss']['channel']["items"]:
        for word in items['description'].split():
            if len(word) > 6:
                list1.append(word.capitalize())
    return list1
def listtop_ten(filename):
    list2 = Counter(filename)
    sorted_list = sorted(list2.items(),key = lambda kv: kv[1])
    sorted_list.reverse()
    print(sorted_list[0:10])



def top_ten(falename):
    x = reading(falename)
    y = list_news(x)
    z =listtop_ten(y)
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
                list1.append(m.capitalize())
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
#
top_ten("newsarf.xml")
