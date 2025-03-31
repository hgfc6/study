import socket


# 服务端
def udp_server():
    udp_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # SOCK_DGRAM表示类型是UDP
    udp_s.bind(('127.0.0.1', 8888))  # UDP和TCP可以绑定同一个端口
    # 不需要listen() 表示可以接受任何客户端的请求
    print('Bind UDP on 9999...')
    while True:
        # 接收数据:
        data, addr = udp_s.recvfrom(1024)
        print('Received from %s.' % addr)
        udp_s.sendto(b'Hello, %s!' % data, addr)
        # recvfrom()方法返回数据和客户端的地址与端口，这样，服务器收到数据后，直接调用sendto()就可以把数据用UDP发给客户端。

# 客户端
def udp_client():
    # 客户端使用UDP时，首先仍然创建基于UDP的Socket，然后，不需要调用connect()，直接通过sendto()给服务器发数据：
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    for data in [b'Michael', b'Tracy', b'Sarah']:
        # 发送数据:
        s.sendto(data, ('127.0.0.1', 9999))
        # 接收数据:
        print(s.recv(1024).decode('utf-8'))
    s.close()
