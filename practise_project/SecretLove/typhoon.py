# -*- coding: utf-8 -*-
# filename: typhoon.py

from urllib2 import urlopen # python 2.x
from json import loads
from math import sin, asin, cos, radians, fabs, sqrt, atan2, pi
import time

# 华发沁园
# 经度:113.50953879356382
# 纬度:22.21451578516779
QINYUAN_LNG = 113.50953879356382
QINYUAN_LAT = 22.21451578516779
# 地球平均半径 6371km
EARTH_RADIUS = 6371

def hav(theta):
    s = sin(theta / 2)
    return s * s

def get_distance_hav(lng0, lat0, lng1, lat1):
    # 用haversine公式计算球面两点间的距离。
    # 经纬度转换成弧度
    lng0 = radians(lng0)
    lng1 = radians(lng1)
    lat0 = radians(lat0)
    lat1 = radians(lat1)
    # 计算经纬度差值
    dlng = fabs(lng0 - lng1)
    dlat = fabs(lat0 - lat1)
    h = hav(dlat) + cos(lat0) * cos(lat1) * hav(dlng)
    distance = 2 * EARTH_RADIUS * asin(sqrt(h))
    return distance

def get_azimuth_angle(lng0, lat0, lng1, lat1):
    dlon = lng1 - lng0
    dlat = lat1 -lat0
    aar = atan2(dlat, dlon)
    return aar*180/pi

def get_azimuth_string(lng0, lat0, lng1, lat1):
    angle = get_azimuth_angle(lng0, lat0, lng1, lat1)
    if angle > 0.0 and angle < 90.0:
        return u"北偏东{:.2f}°".format(90 - angle)
    elif angle > -90.0 and angle < 0.0:
        return u"南偏东{:.2f}°".format(90 + angle)
    elif angle > -180.0 and angle < -90.0:
        return u"南偏西{:.2f}°".format(-90 - angle)
    elif angle > 90.0 and angle < 180.0:
        return u"北偏西{:.2f}°".format(angle - 90)
    elif angle == 0.0:
        return u"东边"
    elif angle == 90.0:
        return u"北边"
    elif angle == 180.0:
        return u"西边"
    elif angle == -90.0:
        return u"南边"
    else:
        return u"Error"

def crawlTyphoon(crawlInterval):
    while(True):
        try:
            uc = urlopen("http://typhoon.zjwater.gov.cn/Api/TyhoonActivity")
            content = uc.read()[1:-1]
            uc.close()
            if '' == content:
                rst = u"暂无台风"
            else:
                tp = loads(content)
                rst = u"{year}年第{id}号{st}{name}({en})\n" \
                      u"· 位于东经{lng}°，北纬{lat}°\n" \
                      u"· 距离华发沁园{azi}约{dis:.2f}公里\n" \
                      u"· 移速{ms}公里/小时，往{md}方向移动\n" \
                      u"· 风速{sp}米/秒，气压{ps}百帕\n" \
                      u"· 近中心最大风力{power}级\n" \
                    .format(year=tp['tfid'][0:4], id=tp['tfid'][4:], st=tp['strong'], name=tp['name'], en=tp['enname'],
                            lng=tp['lng'], lat=tp['lat'],
                            azi=get_azimuth_string(QINYUAN_LNG, QINYUAN_LAT, float(tp['lng']), float(tp['lat'])),
                            dis=get_distance_hav(QINYUAN_LNG, QINYUAN_LAT, float(tp['lng']), float(tp['lat'])),
                            ms=tp['movespeed'], md=tp['movedirection'],
                            sp=tp['speed'], ps=tp['pressure'],
                            power=tp['power'])
                if tp['radius7']:
                    rst += u"· 七级风圈半径{r7}公里\n".format(r7=tp['radius7'])
                    if tp['radius10']:
                        rst += u"· 十级风圈半径{r10}公里\n".format(r10=tp['radius10'])
                rst += u"{time}".format(time=tp['time'])
        except Exception, err:  # python 2.x
        # except Exception as err: # python 3.x
            rst = "抓取台风信息出现错误：\n{}\n请联系管理员！".format(err)
            pass
        # print rst
        try:
            with open('./_crawl_typhoon_json_', 'wb') as fs:
                fs.write(rst.strip().encode('utf-8'))
        except Exception, err:  # python 2.x
        # except Exception as err: # python 3.x
            print "Typhoon Write Error:{}".format(err)
            pass
        print "Typhoon Update:{}".format(time.ctime(time.time()))
        time.sleep(crawlInterval)
