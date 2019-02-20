# -*- coding: utf-8 -*-
# filename: _cal_distance_by_gps.py

# 华发沁园
# 经度:113.50953879356382
# 纬度:22.21451578516779

# 海葵
# 东经 114.40° +
# 北纬 17.80° +

from math import sin, asin, cos, radians, fabs, sqrt, atan2, pi

# 地球平均半径，6371km
EARTH_RADIUS=6371

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
        return "北偏东{}°".format(90 - angle)
    elif angle > -90.0 and angle < 0.0:
        return "南偏东{}°".format(90 + angle)
    elif angle > -180.0 and angle < -90.0:
        return "南偏西{}°".format(-90 - angle)
    elif angle > 90.0 and angle < 180.0:
        return "北偏西{}°".format(angle - 90)
    elif angle == 0.0:
        return "东边"
    elif angle == 90.0:
        return "北边"
    elif angle == 180.0:
        return "西边"
    elif angle == -90.0:
        return "南边"
    else:
        return "Error"

alng = 113.50953879356382
alat = 22.21451578516779
blng = 112.80
blat = 17.80
print get_distance_hav(alng, alat, blng, blat)
# print get_azimuth_angle(alng, alat, blng, blat)
print get_azimuth_string(alng, alat, blng, blat)

# print get_azimuth_angle(0,0,0,1)
# print get_azimuth_angle(0,0,1,0)
# print get_azimuth_angle(0,0,0,-1)
# print get_azimuth_angle(0,0,-1,0)
#
# print get_azimuth_angle(0,0,1,1)
# print get_azimuth_angle(0,0,1,-1)
# print get_azimuth_angle(0,0,-1,-1)
# print get_azimuth_angle(0,0,-1,1)
#
# print get_azimuth_string(0,0,0,4)
# print get_azimuth_string(0,0,3,0)
# print get_azimuth_string(0,0,0,-4)
# print get_azimuth_string(0,0,-3,0)
#
# print get_azimuth_string(0,0,3,4)
# print get_azimuth_string(0,0,3,-4)
# print get_azimuth_string(0,0,-3,-4)
# print get_azimuth_string(0,0,-3,4)