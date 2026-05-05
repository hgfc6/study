# TCP Socket 示例
#
# 运行方式：
#     python 09_web/001_tcp.py
#
# 这个示例会在本机启动一个一次性的 TCP 服务端线程，然后用客户端连接它。
# 这样默认运行不会一直阻塞，也不需要手动开两个终端。

import socket
import threading
import time
from queue import Queue


HOST = "127.0.0.1"


def handle_client(sock: socket.socket, addr: tuple[str, int]) -> None:
    """处理一个客户端连接。"""

    print(f"Accept new connection from {addr[0]}:{addr[1]}")

    with sock:
        sock.sendall(b"Welcome!")

        while True:
            data = sock.recv(1024)

            if not data or data.decode("utf-8") == "exit":
                break

            message = data.decode("utf-8")
            response = f"Hello, {message}!".encode("utf-8")
            sock.sendall(response)

    print(f"Connection from {addr[0]}:{addr[1]} closed.")


def run_server(port_queue: Queue[int]) -> None:
    """启动一次性 TCP 服务端。"""

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # SO_REUSEADDR 让端口在程序重启后更快复用，学习和调试时很方便。
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # 端口写 0 表示让操作系统自动分配一个可用端口。
        server_socket.bind((HOST, 0))
        server_socket.listen(1)

        actual_port = server_socket.getsockname()[1]
        port_queue.put(actual_port)

        print(f"TCP server listening on {HOST}:{actual_port}")

        # 本示例只接受一个客户端，处理完就退出，避免脚本永久阻塞。
        client_socket, addr = server_socket.accept()
        handle_client(client_socket, addr)


def run_client(port: int) -> None:
    """启动 TCP 客户端并发送几条消息。"""

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, port))

        print(client_socket.recv(1024).decode("utf-8"))

        for data in [b"Michael", b"Tracy", b"Sarah"]:
            client_socket.sendall(data)
            print(client_socket.recv(1024).decode("utf-8"))

        client_socket.sendall(b"exit")


def main() -> None:
    """运行一个完整的本地 TCP 通信示例。"""

    port_queue: Queue[int] = Queue()
    server_thread = threading.Thread(target=run_server, args=(port_queue,))
    server_thread.start()

    port = port_queue.get()

    # 给服务端极短时间进入 accept 状态，避免非常慢的机器上客户端抢跑。
    time.sleep(0.1)

    run_client(port)
    server_thread.join()


if __name__ == "__main__":
    main()
