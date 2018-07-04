import socket
HOST = '127.0.0.1'
PORT = '3000'
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
data = 'hello'
while data:
    s.sendto(data.encode('utf-8'),(HOST,PORT))
    if data == 'bye':
        break
    data,addr = s.recvfrom(512)
    print('receive from server',data.decode('utf-8'))
    data = input('输入消息')
s.close()