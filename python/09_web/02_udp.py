# UDP Socket 示例
#
# 运行方式：
#     python 09_web/02_udp.py
#
# UDP 不需要建立连接，客户端直接把数据发到服务端地址。
# 这个示例会启动一个本地 UDP 服务端线程，处理 3 条消息后自动退出。

import socket
import threading
from queue import Queue


HOST = "127.0.0.1"
MESSAGE_COUNT = 3


def run_udp_server(port_queue: Queue[int]) -> None:
    """启动 UDP 服务端。"""

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        # 端口写 0 表示让操作系统自动分配可用端口，避免端口冲突。
        server_socket.bind((HOST, 0))

        actual_port = server_socket.getsockname()[1]
        port_queue.put(actual_port)

        print(f"UDP server listening on {HOST}:{actual_port}")

        for _ in range(MESSAGE_COUNT):
            # recvfrom 会同时返回数据和客户端地址，服务端需要这个地址才能回包。
            data, addr = server_socket.recvfrom(1024)
            print(f"Received from {addr[0]}:{addr[1]}")

            response = b"Hello, " + data + b"!"
            server_socket.sendto(response, addr)


def run_udp_client(port: int) -> None:
    """启动 UDP 客户端并发送消息。"""

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        for data in [b"Michael", b"Tracy", b"Sarah"]:
            client_socket.sendto(data, (HOST, port))
            response = client_socket.recv(1024)
            print(response.decode("utf-8"))


def main() -> None:
    """运行一个完整的本地 UDP 通信示例。"""

    port_queue: Queue[int] = Queue()
    server_thread = threading.Thread(target=run_udp_server, args=(port_queue,))
    server_thread.start()

    port = port_queue.get()
    run_udp_client(port)
    server_thread.join()


if __name__ == "__main__":
    main()
