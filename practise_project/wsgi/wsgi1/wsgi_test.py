
from wsgiref.simple_server import make_server

def simple_app(environ:dict, start_response):
    for k, v in environ.items():
        print(k, v)
    print('-'*30)

    status = '200 OK'
    headers = [('Content-type', 'text/plain; charset=utf-8')]

    start_response(status, headers)

    ret = [("%s: %s\n" % (key, value)).encode("utf-8")
           for key, value in environ.items()]
    return ret

httpd = make_server('0.0.0.0', 9000, simple_app)
try:
    httpd.serve_forever()
except Exception as e:
    print(e)
except KeyboardInterrupt:
    print('stop')
    httpd.close()




