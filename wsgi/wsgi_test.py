
# from wsgiref.simple_server import make_server
#
# def simple_app(environ, start_response):
#     for  k ,v in environ.items():
#         print(k, v)
#     print('-'* 30)
#
#     status = '200 OK'
#     headers = [('Content-type', 'text/plain; charset=utf-8')]
#
#     start_response(status, headers)
#
#     ret = [("%s: %s\n" % (key, value)).encode("utf-8")
#            for key, value in environ.items()]
#     return ret          #返回要求可迭代对象，正文就是这个列表的元素，可以是一个元素--字符串
#
# httpd = make_server('0.0.0.0', 9000, simple_app)
# try:
#     httpd.serve_forever()
# except Exception as e:
#     print(e)
# except KeyboardInterrupt:
#     print('stop')
#     httpd.close()




from wsgiref.simple_server import make_server

def application(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/html;charset=utf-8')]
    start_response(status, headers)
    #返回可迭代对象
    html = '<h1>Zigbee实时监控系统</h1>'.encode("utf-8")
    return [html]

server = make_server('0.0.0.0', 9000, application)
server.serve_forever()
