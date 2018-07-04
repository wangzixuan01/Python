import socket
HOST = 'localhost'
PORT = 10888
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
data = 'hello'
while data:
    s.sendall(data.encode('utf-8'))
    data = s.recv(512)
    print('receive from server',data.decode('utf-8'))
    data = input('输入消息')
s.close()