import socket
server = socket.socket()

ipaddr = ('127.0.0.1',9999)

server.bind(ipaddr)

server.listen()
s1, raddr = server.accept()

data1 = s1.recv(1024)

print("create a branch is so quick")
<<<<<<< HEAD
print("create a branch is so quick & simple")
=======
print("create a branch is so quick and simple")
>>>>>>> feature1
print("create a branch is so quick and simple")