import socket
import time
import thread
socket.setdefaulttimeout(3)
def socket_port(ip,port):
    try:
        if port>=65535:
            print('端口扫描结束\n')
            return

        s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        result = s.connect_ex((ip,port))
        if result == 0:
            lock.acquire()
            print(ip,':',port,'端口开放\n')
            lock.release()
        s.close()
    except:
        print('端口扫描异常\n')
def ip_scan(ip):
    try:
        print('开始扫描 %s' %ip,'\n')
        start_time=time.time()
        for i in range(1,300):
            _thread.start_new_thread(socket_port,(ip,int(i)))
        print('扫描端口完成，总用时：%.2f' %(time.time()-start_time),"\n")
    except ValueError:
        print('扫描ip出错'+ValueError)
if __name__=='__main__':
    url = input('请输入要扫描的机器ip地址或网址：\n')
    ip_scan(url)

