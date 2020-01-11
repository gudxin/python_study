# 以下一的代码，handler相当于socket的recv方法
# 但是客户端与服务器连接上后，就顺序到了finish方法里面，就断开了连接
# 一:
# import socketserver
# import threading
#
# class MyHandler(socketserver.BaseRequestHandler):
#     def handle(self):
#         print(self.request)				# new socket 用来 recv
#         print(self.client_address)		# raddr
#         print(self.server)
#         print(self.__dict__)
#         print(self.server.__dict__)
#
#
# server = socketserver.ThreadingTCPServer(('0.0.0.0', 9999), MyHandler)
# print(server)
# server.serve_forever()


# 二: 加入循环:(不同客户端也不会相互影响)
# import socketserver
# import threading
#
#
# class MyHandler(socketserver.BaseRequestHandler):
#     def handle(self):
#         print(self.request)				# new socket 用来 recv
#         # print(self.client_address)		# raddr
#         # print(self.server)
#         # print(self.__dict__)
#         # print(self.server.__dict__)
#         print(threading.enumerate())
#         print(threading.current_thread())
#         for i in range(3):
#             data = self.request.recv(1024)
#             print(data, self.client_address)
#
# # 多线程版本,异步库,同时可以处理多个连接
# #server = socketserver.ThreadingTCPServer(('0.0.0.0', 9999), MyHandler)
#
#
# # 同步库(多个客户端都可以accept,但是相当于进入了队列中等待,先来先处理recv,处理完第一个socket的recv后,继续之后的socket操作recv,数据都是缓存起来的),且只有主线程
# server = socketserver.TCPServer(('0.0.0.0', 9999), MyHandler)
# print(server)
# server.serve_forever()


# 三:TCPServer多人聊天服务器端

import socketserver
import threading


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
        print(self.request)				# new socket 用来 recv
        # print(self.client_address)		# raddr
        # print(self.server)
        # print(self.__dict__)
        # print(self.server.__dict__)
        # print(threading.enumerate())
        # print(threading.current_thread())
        while not self.event.is_set():
            data = self.request.recv(1024).decode()
            print(data, '++++++++++++++++++++++++++++++')
            if not data:
                print("Broken pipe")
                break
            msg = "{}{}".format(self.client_address, data).encode()
            # 如何实现一对多
            # 多客户端在哪里， 如何获得
            for c in self.clients.values():
                c.send(msg)
                print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')


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

