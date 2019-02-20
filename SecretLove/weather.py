# -*- coding: utf-8 -*-
# filename: weather.py

from urllib2 import urlopen # python 2.x
from lxml import etree
import time

def crawlWeather(crawlInterval):
    while(True):
        try:
            uc = urlopen("http://www.zhmb.gov.cn:8000/jeecms/web/index")
            content = uc.read()
            uc.close()
            html = etree.HTML(content)
            # prefix = "//*[@id=\"con_seten_1\"]/div[1]/div/"
            nodes = html.xpath("//*[@id=\"con_seten_1\"]/div[1]/div/*")
            nodes_f = nodes[0].xpath("./text()")
            rtn = nodes_f[1]
            nodes_s = nodes[1].xpath("./p")
            for node_s in nodes_s:
                rtn += '\n' + node_s.text
        except Exception, err: # python 2.x
        # except Exception as err: # python 3.x
            rtn = "抓取天气出现错误：\n{}\n请联系管理员！".format(err)
            pass
        try:
            with open('./_crawl_weather_xpath_', 'wb') as fs:
                fs.write(rtn.strip().encode('utf-8'))
        except Exception, err: # python 2.x
        # except Exception as err: # python 3.x
            print "Weather Write Error:{}".format(err)
            pass
        print "Weather Update:{}".format(time.ctime(time.time()))
        time.sleep(crawlInterval)
