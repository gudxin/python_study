# -*- coding: utf-8 -*-
# filename: handle.py

import web
import hashlib
import re
# import pymysql
# from urllib2 import urlopen # python 2.x
# from urllib.request import urlopen #python 3.x
# from lxml import etree

import reply
import receive
# import secretlove

class Handle(object):
    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return "<script>window.location.href='http://www.haydnliao.top';</script>"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = "haydnliao" #请按照公众平台官网\基本配置中信息填写

            list = [token, timestamp, nonce]
            list.sort()
            sha1 = hashlib.sha1()
            map(sha1.update, list)
            hashcode = sha1.hexdigest()
            # print "handle/GET func: hashcode, signature: ", hashcode, signature
            if hashcode == signature:
                return echostr
            else:
                return ""
        except Exception, Argument: # python 2.x
            return Argument
    def POST(self):
        try:
            webData = web.data()
            # print "\nHandle Post webdata is:\n", webData, "\n" #后台打日志
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg):
                if recMsg.MsgType == 'text':
                    toUser = recMsg.FromUserName
                    fromUser = recMsg.ToUserName
                    # # repCon = "Wait a minute."
                    # db = pymysql.connect("127.0.0.1", "sl", "xiaohai", "secretlove")
                    # cur = db.cursor()
                    # cur.execute("SELECT sl_flag FROM user_msg WHERE open_id=\"{}\"".format(recMsg.FromUserName))
                    # # print "SELECT sl_flag FROM user_msg WHERE open_id=\"{}\"".format(recMsg.FromUserName)
                    # sl_flag = cur.fetchone()
                    # # print "*1*", sl_flag, type(sl_flag)
                    # if sl_flag == None:
                    #     sl_flag = 0
                    # else:
                    #     sl_flag = sl_flag[0]
                    # db.close()
                    # # print "*2*", sl_flag, type(sl_flag)
                    sl_flag = 0
                    if sl_flag == 0:
                        if re.search("晚会|^0$", recMsg.Content) != None:
                            repCon = "# 晚会 晚会视频下载链接\n链接：http://pan.baidu.com/s/1hsejOjy\n密码：24yt"
                        elif re.search("暗恋|^1$", recMsg.Content) != None:
                            repCon = "# 暗恋 暗恋应用开发说明\n基本功能为：\n1.标注自身的微信号为单身或恋爱中；\n2.单身者可填写一个暗恋对象的微信号，则会收到对方的状态，为单身、恋爱中或未知；\n3.若两个单身者互相暗恋，则双方都会收到通知。\n\n微信公众号没有认证限制了大部分API，开发就此搁置！\n2017年08月27日"
                        elif re.search("^(珠海)?天气$|^2$", recMsg.Content) != None:
                            try:
                              with open('./_crawl_weather_xpath_', 'rb') as fs:
                                  repCon = fs.read()
                            except Exception, err: # python 2.x
                            # except Exception as err: # python 3.x
                                repCon = "读取天气出现错误：\n{}\n请联系管理员！".format(err)
                                pass
                        elif re.search("台风|^3$", recMsg.Content) != None:
                            try:
                              with open('./_crawl_typhoon_json_', 'rb') as fs:
                                  repCon = fs.read()
                            except Exception, err: # python 2.x
                            # except Exception as err: # python 3.x
                                repCon = "读取台风信息出现错误：\n{}\n请联系管理员！".format(err)
                                pass
                        # elif re.search("^secretlove$", recMsg.Content) != None:
                        #     # sl_flag = 1
                        #     db = pymysql.connect("127.0.0.1", "sl", "xiaohai", "secretlove")
                        #     cur = db.cursor()
                        #     cur.execute("SELECT open_id FROM user_msg WHERE open_id=\"{}\"".format(recMsg.FromUserName))
                        #     if cur.fetchone() == None:
                        #         cur.execute("INSERT INTO user_msg (open_id, sl_flag) VALUES (\"{}\", 1)".format(recMsg.FromUserName))
                        #     else:
                        #         cur.execute("UPDATE user_msg SET sl_flag=1 WHERE open_id=\"{}\"".format(recMsg.FromUserName))
                        #     db.commit()
                        #     db.close()
                        #     repCon = "已进入Secret Love！\n回复关键字执行相关操作：\n# 帮助 查看可用命令\n# 退出 退出当前应用"
                        else:
                            repCon = "回复数字或关键字获取相关信息：\n# 0 晚会 \n# 1 暗恋 \n# 2 天气/珠海天气 \n# 3 台风"
                    # else:
                    #     sl_flag, repCon = secretlove.sl_main(recMsg.FromUserName, recMsg.Content)
                    #     if sl_flag == 0:
                    #         db = pymysql.connect("127.0.0.1", "sl", "xiaohai", "secretlove")
                    #         cur = db.cursor()
                    #         cur.execute("UPDATE user_msg SET sl_flag=0 WHERE open_id=\"{}\"".format(recMsg.FromUserName))
                    #         db.commit()
                    #         db.close()
                    #         repCon = "已退出Secret Love！"
                    content = repCon
                    replyMsg = reply.TextMsg(toUser, fromUser, content)
                    return replyMsg.send()
                elif recMsg.MsgType == 'image':
                    toUser = recMsg.FromUserName
                    fromUser = recMsg.ToUserName
                    content = "image"
                    replyMsg = reply.TextMsg(toUser, fromUser, content)
                    return replyMsg.send()
                else:
                    print "others msg type"
                    return "success"
            else:
                print "others msg"
                return "success"
        except Exception, Argment:
            return Argment

