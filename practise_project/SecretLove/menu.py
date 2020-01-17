# -*- coding: utf-8 -*-
# filename: menu.py

from urllib2 import urlopen # python 2.x
from json import loads

def at_get():
    g_appid = "wx0dd2f484442a9b44"
    g_appsecret = "e652a70323d8648f77d937280abdc3d2"
    url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}"\
        .format(g_appid, g_appsecret)
    fb = urlopen(url).read()
    try:
        rtn = loads(fb)['access_token']
    except Exception, err:
        rtn = None
        print "Access Token Get Error:{}".format(err)
    # print rtn
    return rtn

def createMenu():
    g_access_token = at_get()
    if not g_access_token:
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token={}"\
            .format()
        # with open('menu.json', 'r') as fs:
        #     data = load(fs)
        # print data
        data = '''
{
"button":[
  {
    "name":"小功能",
    "sub_button":[
      {
        "type":"click",
        "name":"天气信息",
        "key":"weather"
      },
      {
        "type":"click",
        "name":"台风信息",
        "key":"typhoon"
      }
    ]
  }
]
}
'''
        urlopen(postUrl, data)
    else:
        print "Create Menu Error"
