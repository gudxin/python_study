
from urllib.request import urlopen
import json

g_access_token = ""
g_appid = "wx0dd2f484442a9b44"
g_appsecret = "e652a70323d8648f77d937280abdc3d2"

def at_get():
    global g_appid, g_appsecret
    url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}".format(g_appid, g_appsecret)
    fb = urlopen(url).read()
    return json.loads(fb)

g_access_token = at_get()
print(g_access_token["access_token"], type(g_access_token))

def um_get():
    global g_access_token
    openid = "o9USNv-3flLEWzvleMOWmTbXq5Rs"
    url = "https://api.weixin.qq.com/cgi-bin/user/info?access_token={}&openid={}&lang=zh_CN".format(g_access_token, openid)
    fb = urlopen(url).read()
    print(fb)
    return json.loads(fb)

g_user_msg = um_get()
# print(g_user_msg, type(g_user_msg))

