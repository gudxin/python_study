# from urllib.request import urlopen
#
# response = urlopen('https://cn.bing.com/')
# print(response.closed)
# with response:
#     print(1,type(response))                     #http.client.HTTPResponse类文件对象
#     print(2,response.status, response.reason)   #状态
#     print(3,response.geturl())                  #返回真正的URL
#     print(4,response.info)                      #headers
#     print(5,response.readline())                    #读取返回的内容
#
# print(response.closed)

from urllib.request import Request, urlopen
from urllib.parse import urlencode
import requests


keyword = input('>>请输入搜索关键字 ')
data = urlencode({
    'q':keyword
})

base_url = 'http://cn.bing.com/search'
url = '{}?{}'.format(base_url, data)
print(url)

ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
request = Request(url, headers={'User-agent':ua})

response = urlopen(request)
with response:
    with open('F:/2_python_project/scrapy/bing.html', 'wb') as f:
        f.write(response.read())

print('成功')