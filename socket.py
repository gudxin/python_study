import socket
server = socket.socket()

ipaddr = ('127.0.0.1',9999)

server.bind(ipaddr)

server.listen()

