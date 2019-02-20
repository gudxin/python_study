# -*- coding: utf-8 -*-
# filename: reply.py
import pymysql
import re

def sl_main(user_id, user_con):
    sl_main_flag = 1
    rep_main_con = "sl_main"
    mark_status = ("未知", "恋爱中", "单身") # 0 未知 1 恋爱中 -1 单身
    if user_con == "退出":
        sl_main_flag = 0
    elif user_con == "帮助":
        rep_main_con = "回复关键字执行相关操作：\n# 状态 查看当前状态\n# 单身 修改状态为单身\n# 恋爱中 修改状态为恋爱中\n# 帮助 查看可用命令\n# 退出 退出当前应用\n# @微信号 单身状态下输入暗恋对象微信号，如：@liao×××××××yer，暂不支持非ASCII字符"
    elif user_con == "状态":
        db = pymysql.connect("127.0.0.1", "sl", "xiaohai", "secretlove")
        cur = db.cursor()
        cur.execute("SELECT mark_flag, name_love FROM user_msg WHERE open_id=\"{}\"".format(user_id))
        curfo = cur.fetchone()
        db.close()
        if curfo == None: # 未知
            mark_main_flag = 0
            name_main_love = ""
        else:
            mark_main_flag, name_main_love = curfo
        # print mark_main_flag, type(mark_main_flag)
        rep_main_con = "当前状态：{}".format(mark_status[mark_main_flag])
        if mark_main_flag == -1: # 单身
            rep_main_con = "{}\n暗恋对象：{}".format(rep_main_con,name_main_love)
        # print rep_main_con
    elif user_con == "单身":
        db = pymysql.connect("127.0.0.1", "sl", "xiaohai", "secretlove")
        cur = db.cursor()
        cur.execute("UPDATE user_msg SET mark_flag=-1 WHERE open_id=\"{}\"".format(user_id))
        db.commit()
        db.close()
        rep_main_con = "状态已修改为『单身』"
    elif user_con == "恋爱中":
        db = pymysql.connect("127.0.0.1", "sl", "xiaohai", "secretlove")
        cur = db.cursor()
        cur.execute("UPDATE user_msg SET mark_flag=1 WHERE open_id=\"{}\"".format(user_id))
        db.commit()
        db.close()
        rep_main_con = "状态已修改为『恋爱中』"
    elif re.search("^@", user_con) != None:
        db = pymysql.connect("127.0.0.1", "sl", "xiaohai", "secretlove")
        cur = db.cursor()
        cur.execute("SELECT mark_flag FROM user_msg WHERE open_id=\"{}\"".format(user_id))
        mark_main_flag = cur.fetchone()
        if mark_main_flag == None:
            mark_main_flag = 0
        else:
            mark_main_flag = mark_main_flag[0]
        if mark_main_flag != -1: # 非单身
            rep_main_con = "非单身状态，无法添加或修改暗恋对象微信号"
        else:
            # print user_con, type(user_con), user_con[1:]
            cur.execute("UPDATE user_msg SET name_love=\"{}\" WHERE open_id=\"{}\"".format(user_con[1:], user_id))
            db.commit()
            rep_main_con = "暗恋对象微信号修改为『{}』".format(user_con[1:])
            # print rep_main_con
        db.close()
    else:
        rep_main_con = "回复『帮助』查看可用命令"
    return sl_main_flag, rep_main_con

