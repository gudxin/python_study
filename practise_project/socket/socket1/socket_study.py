# server = socket.socket()
#
# ipaddr = ('127.0.0.1',9999)
#
# server.bind(ipaddr)
#
# server.listen()
# s1, raddr = server.accept()
#
# while True:
#     data1 = s1.recv(1024)
#     s1.send(data1)
#     print(str(data1).encode())


# import socket
# import logging
# import  threading
# import datetime
#
# logging.basicConfig(level=logging.INFO, format="%(asctime)s %(thread)d %(message)s")
#
# class TestServer:
#     def __init__(self, ip='127.0.0.1', port=9999):      # 启动服务
#         self.sock = socket.socket()
#         self.addr = (ip, port)
#         self.clients = {}          # 客户端
#
#     def start(self):               # 启动监听
#         self.sock.bind(self.addr)   # 绑定
#         self.sock.listen()          # 监听
#         # accept会阻塞主线程，所以开一个新线程
#         threading.Thread(target=self.accept).start()
#
#     def accept(self):   # 多人连接
#         while True:
#             sock, client = self.sock.accept()   # 阻塞
#             self.clients[client] = sock         # 添加到客户端字典
#             # 准备接收数据，recv是阻塞的，开启新的线程
#             threading.Thread(target=self.recv, args=(sock, client)).start()
#
#     def recv(self, sock:socket.socket, client):
#         while True:
#             data = sock.recv(1024)  # 阻塞到数据到来
#             msg = "{:%Y/%m/%d %H:%M:%S} {}:{}\n{}\n".format(datetime.datetime.now(), *client, data.decode())
#             logging.info(msg)
#             msg = msg.encode()
#             for s in self.clients.values():
#                 s.send(msg)
#
#     def stop(self):
#         for s in self.clients.values():
#             s.close()
#             self.sock.close()
#
#
# cs = TestServer()
# cs.start()

import threading
from socketserver import ThreadingTCPServer, BaseRequestHandler
import sys
import logging

FORMAT = "%(asctime)s %(threadName)s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)


class TestHandler(BaseRequestHandler):
    clients = {}

    def setup(self):
        super().setup()
        self.event = threading.Event()  # 初始工作
        self.clients[self.client_address] = self.request

    def finish(self):
        super().finish()  # 清理工作
        self.clients.pop(self.client_address)   # 能执行到吗？
        self.event.set()

    def handle(self):
        super().handle()

        while not self.event.is_set():
            data = self.request.recv(1024).decode()
            print(data, '~~~~~~~~~')    # 增加
            if not data or data == 'quit':
                print('Broken pipe')
                break
            msg = "{} {}".format(self.client_address,data).encode()
            logging.info(msg)
            for c in self.clients.values():
                print('++++++++++++++')     # 增加
                self.request.send(msg)
        print('End')


addr = ('127.0.0.1', 9999)
server = ThreadingTCPServer(addr, TestHandler)

server_thread = threading.Thread(target=server.serve_forever, name='TestServer', daemon=True)
server_thread.start()

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
    sys.exit(0)







