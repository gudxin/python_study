from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'

@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
            <p><input name="username"></p>
            <p><input name="password" type="password"></p>
            <p><button type="submit">Sign In</button></p>
            </form>'''

@app.route('/signin', methods=['POST'])
def signin():
    #需要从request对象读取表单内容：
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Wrong username or password.Try more times</h3>'

if __name__ == '__main__':
    app.run()



import socketserver
import threading
import pymysql


db = pymysql.connect("192.168.14.130","xiaogu","lakerkobe00","TESTDB")
cursor = db.cursor()

class MyHandler(socketserver.BaseRequestHandler):
    clients = {}  # 记录多个实例

    def setup(self):
        self.event = threading.Event()
        self.clients[self.client_address] = self.request
        print(self.client_address)

    def finish(self):
        self.clients.pop(self.client_address)
        self.event.set()

    def handle(self):
        print(self.request)                # new socket 用来 recv
        # print(self.client_address)        # raddr
        # print(self.server)
        # print(self.__dict__)
        # print(self.server.__dict__)
        # print(threading.enumerate())
        # print(threading.current_thread())
        while not self.event.is_set():
            data = self.request.recv(97).decode()
            head_1 = data[0:2]
            IP_1 = data[2:14]
            PH_1= data[14:19]
            CONDI_1 = data[19:24]
            TEMP1_1 = data[24:29]
            TEMP2_1 = data[29:34]
            TEMP3_1 = data[34:39]
            TEMP4_1 = data[39:44]
            TEMP5_1 = data[44:49]
            TEMP6_1 = data[49:54]
            TEMP7_1 = data[54:59]
            TEMP8_1 = data[59:64]
            PAUSE1_1 = data[64:65]
            PAUSE2_1 = data[65:66]
            PAUSE3_1 = data[66:67]
            PAUSE4_1 = data[67:68]
            PAUSE5_1 = data[68:69]
            SPEED_1 = data[69:74]
            THICKNESS_1 = data[74:78]
            SUM_1 = data[78:81]
            DATE_1 = data[81:95]
            TAIL_1 = data[95:97]
            
            sql = """INSERT INTO ZIGBEE(HEAD,
                    IP,PH,CONDI,TEMP1,TEMP2,TEMP3,TEMP4,TEMP5,TEMP6,TEMP7,TEMP8,
                    PAUSE1,PAUSE2,PAUSE3,PAUSE4,PAUSE5,SPEED,THICKNESS,SUM,DATE,TAIL)
                    VALUES ('%s',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""%        \
                    (head_1,IP_1,PH_1,CONDI_1,TEMP1_1,TEMP2_1,TEMP3_1,TEMP4_1,TEMP5_1,TEMP6_1,TEMP7_1,TEMP8_1,
                    PAUSE1_1,PAUSE2_1,PAUSE3_1,PAUSE4_1,PAUSE5_1,SPEED_1,THICKNESS_1,SUM_1,DATE_1,TAIL_1)
            # try:
                # #执行sql语句
                # cursor.execute(sql)
                # #提交到数据库执行
                # db.commit()
            # except:
                # #如果发生错误则回滚
                # db.rollback()    
            cursor.execute(sql)
            db.commit()
            
            print(data, '++++++++++++++++++++++++++++++')
            if not data:
                print("Broken pipe")
                break
            msg = "{}{}".format(self.client_address, data).encode()
            # 如何实现一对多
            # 多客户端在哪里， 如何获得
            # for c in self.clients.values():
                # c.send(msg)
                # print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')


# 多线程版本,异步库,同时可以处理多个连接
server = socketserver.ThreadingTCPServer(('0.0.0.0', 9999), MyHandler)
print(server)

# 同步库(多个客户端都可以accept,但是相当于进入了队列中等待,先来先处理recv,处理完第一个socket的recv后,继续之后的socket操作recv,数据都是缓存起来的),且只有主线程
# server = socketserver.TCPServer(('0.0.0.0', 9999), MyHandler)
# print(server)

t = threading.Thread(target=server.serve_forever, name='chatserver')
t.start()

try:
    while True:
        cmd = input('>>>')
        if cmd.strip() == 'quit':
            break
        print(threading.enumerate())
except Exception as e:
    print(e)
except KeyboardInterrupt:
    pass
finally:
    print('Exit')
    # sys.exit(0)

