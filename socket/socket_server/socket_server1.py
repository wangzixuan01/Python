import socketserver
from socketserver import TCPServer,StreamRequestHandler
HOST = ''
PORT = 10888
class MyTcpHandler(socketserver.StreamRequestHandler):
    def handle(self):
        while True:
            data = self.request.recv(1024)
            if not data:
                server.shutdown()
                break
            print('receive data:',data.decode('utf-8'))
            self.request.send(data)
        return
server = TCPServer((HOST,PORT),MyTcpHandler)
server.serve_forever()