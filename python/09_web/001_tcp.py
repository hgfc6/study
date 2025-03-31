# server 服务端
import socket
import threading
import time


def server():
    server  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#AF_INET(ipv4)AF_INET6(ipv6)
    server.bind(('127.0.0.1', 8888))
    max_wait_connect = 5
    server.listen(max_wait_connect)
    print('Waiting for Connecting')
    while True:
        soc, addr = server.accept()
        #创建线程处理新链接
        threading.Thread(target=dial_tcp, args=(soc, addr))

def dial_tcp(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)

# client 客户端
def client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 建立连接:
    s.connect(('127.0.0.1', 8888))
    # 接收欢迎消息:
    print(s.recv(1024).decode('utf-8'))
    for data in [b'Michael', b'Tracy', b'Sarah']:
        # 发送数据:
        s.send(data)
        print(s.recv(1024).decode('utf-8'))
    s.send(b'exit')
    s.close()

if __name__ == '__main__':
    pass