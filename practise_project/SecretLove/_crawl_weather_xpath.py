# -*- coding: utf-8 -*-
# filename: _crawl_weather_xpath.py

# import codecs
# from urllib2 import urlopen # python 2.x
from urllib.request import urlopen #python 3.x
from lxml import etree

# f = codecs.open("http://www.zhmb.gov.cn:8000/jeecms/web/index.htm","r","utf-8")
# content = f.read()
# f.close()
uc = urlopen("http://www.zhmb.gov.cn:8000/jeecms/web/index")
content = uc.read()

html = etree.HTML(content)
prefix = "//*[@id=\"con_seten_1\"]/div[1]/div/"

# nodes = html.xpath(prefix + "p/span")
# print(nodes[0].text)
# nodes = html.xpath(prefix + "p/text()")
# print(nodes[1])
# nodes = html.xpath(prefix + "div/p")
# for node in nodes:
#     print(node.text)

nodes = html.xpath(prefix + "*")
# print(nodes)
nodes_f = nodes[0].xpath("./text()")
# print(nodes_f[1])
rtn = nodes_f[1]
nodes_s = nodes[1].xpath("./p")
for node_s in nodes_s:
    # print(node_s.text)
    rtn += '\n' + node_s.text
print(rtn)
