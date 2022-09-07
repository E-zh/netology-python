# import json
# import csv
#
# with open('../files/newsafr.csv', newline='', encoding='utf-8') as f:
#     # reader = csv.reader(f, delimiter=',')
#     # new_list = list(reader)
#     reader = csv.DictReader(f, delimiter=',')
#     for news in reader:
#         print(news)
#         # print(news['title'])
#
# # print(new_list)
# from pprint import pprint
#
# with open('../files/newsafr.json', encoding='utf-8') as f:
#     json_data = json.load(f)
#
# jsd = json_data["rss"]["channel"]["items"][0]
# pprint(json_data)
#
# with open('../files/newsafr2.json', 'w') as f:
#     json.dump(json_data, f, ensure_ascii=False, indent=4)

import xml.etree.ElementTree as ET
parser = ET.XMLParser(encoding='utf-8')
tree = ET.parse('../files/newsafr.xml', parser)
root = tree.getroot()
# print(root.tag)
# print(root.text)
# print(root.attrib)
# print(type(root.attrib))

news_xml = root.findall('channel/item')
print(len(news_xml))
for news in news_xml:
    print(news.find('title').text)
    print()
