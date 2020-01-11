import socketserver
import threading
import pymysql
import datetime
import re

# 解释器python 3.7  C:\ProgramData\Anaconda3\python.exe


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
		print(self.request, '~~~~~~~~~~~~~~~~~~')				# new socket 用来 recv
		# print(self.client_address)		# raddr
		# print(self.server)
		# print(self.__dict__)
		# print(self.server.__dict__)
		# print(threading.enumerate())
		# print(threading.current_thread())
		while not self.event.is_set():
			data = self.request.recv(1024).decode()
			if not data[0:5].isdigit():
				msg = "ff01".encode()
				# 多客户端在哪里， 如何获得
				for c in self.clients.values():
					c.send(msg)
			else:
				pressure = data[0:2]
				pressure_flag = data[2:3]
				vibrance= data[3:8]
				vibrance_flag = data[8:9]
				temperature = data[9:13]
				temperature_flag = data[13:14]
				start = str(datetime.datetime.now())[0:19]
				time = re.sub("\D","",start)

				sql = """INSERT INTO zigbee(pressure,
								   pressure_flag,vibrance,vibrance_flag,temperature,temperature_flag,time)
								   VALUES ('%s',%s,%s,%s,%s,%s,%s)"""% \
					  (pressure, pressure_flag, vibrance, vibrance_flag, temperature, temperature_flag, time)
				# try:
				# 	# 执行sql语句
				# 	cursor.execute(sql)
				# 	# 提交到数据库执行
				# 	db.commit()
				# except:
				# 	# 如果发生错误则回滚
				# 	db.rollback()
				cursor.execute(sql)
				db.commit()

				print(data, '++++++++++++++++++++++++++++++')
			if not data:
				print("Broken pipe")
				break
			# msg = "ff01".encode()
			# # 多客户端在哪里， 如何获得
			# for c in self.clients.values():
			# 	c.send(msg)



# 多线程版本,异步库,同时可以处理多个连接
server = socketserver.ThreadingTCPServer(('0.0.0.0', 9999), MyHandler)
print(server)

# 同步库(多个客户端都可以accept,但是相当于进入了队列中等待,先来先处理recv,处理完第一个socket的recv后,继续之后的socket操作recv,数据都是缓存起来的),且只有主线程
# server = socketserver.TCPServer(('0.0.0.0', 9999), MyHandler)
# print(server)

t = threading.Thread(target=server.serve_forever, name='zigbee_network')
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

