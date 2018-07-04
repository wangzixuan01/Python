import socket
HOST = ''
PORT = 10888
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)
conn,addr = s.accept()
print('address',addr)
while True:
    data = conn.recv(1024)
    if not data:
        break
    print('receive data:',data.decode('utf-8'))
    conn.send(data)
conn.close()