# -*- coding: utf-8 -*-
# filename: _crawl_weather.py

# from urllib2 import urlopen # python 2.x
from urllib.request import urlopen #python 3.x
uc = urlopen("http://www.zhmb.gov.cn:8000/jeecms/web/index")
for line in uc:
    line = line.decode('utf-8')  # Decoding the binary data to text.
    if '<span>珠海市</span>' in line:
        cnt = 0
        sr = ''
        for cnt in range(0, 4):
            uc.readline()
        for cnt in range(0, 7):
            line = uc.readline().decode('utf-8')
            # print(line)
            sl = line.split('>')
            sl = sl[1].split('<')
            sl = sl[0].replace('&nbsp;', '')
            sr = sr + sl + '\n'
            # print(sl)
        break
print(sr)
uc.close()
# print('---END---')
