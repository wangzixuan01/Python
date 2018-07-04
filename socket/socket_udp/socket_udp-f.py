import socket
tmp = ('127.0.0.1',3001)
#HOST='localhost'
#PORT=10889
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(tmp)
data = True
while data:
    data,address = s.recvfrom(1024)
    if data == 'bye':
        break
    print('received string',data.decode('utf-8'))
    s.sendto(data,address)
s.close()