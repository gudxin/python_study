# -*- coding: utf-8 -*-
# filename: main.py

import web
from handle import Handle
from typhoon import crawlTyphoon
from weather import crawlWeather
# from menu import createMenu
import threading

urls = (
    '/', 'Handle',
)

if __name__ == '__main__':
    # createMenu() # 公众号未认证无自定义菜单功能
    app = web.application(urls, globals())
    t1 = threading.Thread(target=crawlWeather, args=(3600,))   #args=crawlInterval
    t2 = threading.Thread(target=crawlTyphoon, args=(1800,))   #args=crawlInterval
    t1.start()
    t2.start()
    app.run()

