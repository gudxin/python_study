
# from urllib.parse import parse_qs
from webob import Request, Response
from wsgiref.simple_server import make_server

def simple_app(environ, start_response):

    request = Request(environ)
    method = request.method

    print(method)
    print(request.GET)
    print(type(request.GET))  #dict
    print(request.POST)       #dict
    print(request.path)     #路径
    print(request.params)   #所有参数
    print(request.headers)  #请求头

    # query_string = environ.get('QUERY_STRING')
    # print(query_string)
    # method = environ.get('REQUEST_METHOD')
    # print(method)
    # d = {}
    #一：与二一样的效果
    # for item in query_string.split('&'):
    #     k ,_, v = item.partition('=')
    #     d[k] = v
    #  二
    # d = {k:v  for k,_, v in map(lambda x: x.partition('='), query_string.split('&'))}
    # qs = parse_qs(query_string)
    # print(qs)
    # status = '200 OK'
    # headers = [('Content-type', 'test/plain; charset=utf-8')]

    res

    start_response(status, headers)

    ret = []
    return ret  #返回要求可迭代对象，正文就是这个列表的元素，可以使一个元素----字符串

server = make_server('0.0.0.0', 9000, simple_app)
server.serve_forever()
