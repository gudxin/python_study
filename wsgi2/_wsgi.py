#server.py
#从wsgiref模块导入
from wsgiref.simple_server import make_server
#新知识学习，把自己的python文件放在同一目录下，就可直接调用
#导入我们自己编写的application函数
from _app import application

#创建一个服务器，IP地址为本地主机地址，端口号为8080，处理函数是application：
httpd = make_server('127.0.0.1', 8080, application)
print('Serving HTTP on port 8080...')
#开始监听HTTP请求：
httpd.serve_forever()