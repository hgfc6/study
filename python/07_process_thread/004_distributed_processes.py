# 分布式进程示例
#
# 运行方式：
#     python 07_process_thread/004_distributed_processes.py
#
# 这个示例用 multiprocessing.managers.BaseManager 在本机模拟“分布式进程”：
# 1. manager 进程暴露两个队列：任务队列、结果队列。
# 2. worker 进程通过网络地址连接 manager，读取任务并写回结果。
# 3. 主进程再连接 manager，读取 worker 处理后的结果。

import socket
from multiprocessing import Event, Process
from multiprocessing.managers import BaseManager
from queue import Empty, Queue
from typing import Any


HOST = "127.0.0.1"
AUTH_KEY = b"study-python"


# 这两个队列会被 manager 进程暴露给其他进程。
# 注意：真实分布式场景下，worker 可以在另一台机器上，只要网络能访问 manager 地址即可。
TASK_QUEUE: Queue[int] = Queue()
RESULT_QUEUE: Queue[tuple[int, int]] = Queue()


def get_task_queue() -> Queue[int]:
    """返回任务队列，供 BaseManager 注册使用。"""

    return TASK_QUEUE


def get_result_queue() -> Queue[tuple[int, int]]:
    """返回结果队列，供 BaseManager 注册使用。"""

    return RESULT_QUEUE


class QueueManager(BaseManager):
    """自定义 Manager，用来暴露队列。"""


def find_free_port() -> int:
    """找一个本机可用端口，避免示例端口冲突。"""

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((HOST, 0))
        return sock.getsockname()[1]


def register_server_queues() -> None:
    """注册服务端队列。服务端注册时需要提供 callable。"""

    QueueManager.register("get_task_queue", callable=get_task_queue)
    QueueManager.register("get_result_queue", callable=get_result_queue)


def register_client_queues() -> None:
    """注册客户端队列。客户端只需要知道名称，不需要 callable。"""

    QueueManager.register("get_task_queue")
    QueueManager.register("get_result_queue")


def manager_server(address: tuple[str, int], ready: Event) -> None:
    """启动 Manager 服务端。"""

    register_server_queues()

    for number in range(1, 6):
        TASK_QUEUE.put(number)

    manager = QueueManager(address=address, authkey=AUTH_KEY)
    server = manager.get_server()

    # 通知主进程：服务端已经准备好，worker 可以连接了。
    ready.set()
    server.serve_forever()


def worker(address: tuple[str, int]) -> None:
    """连接 Manager，消费任务并写入结果。"""

    register_client_queues()

    manager = QueueManager(address=address, authkey=AUTH_KEY)
    manager.connect()

    task_queue = manager.get_task_queue()
    result_queue = manager.get_result_queue()

    while True:
        try:
            number = task_queue.get(timeout=1)
        except Empty:
            break

        result = number * number
        result_queue.put((number, result))


def collect_results(address: tuple[str, int]) -> list[tuple[int, int]]:
    """主进程连接 Manager，读取结果队列。"""

    register_client_queues()

    manager = QueueManager(address=address, authkey=AUTH_KEY)
    manager.connect()

    result_queue: Any = manager.get_result_queue()
    results: list[tuple[int, int]] = []

    while True:
        try:
            results.append(result_queue.get_nowait())
        except Empty:
            break

    return sorted(results)


def main() -> None:
    """运行完整的 Manager + worker 示例。"""

    port = find_free_port()
    address = (HOST, port)
    ready = Event()

    server_process = Process(target=manager_server, args=(address, ready))
    server_process.start()
    ready.wait()

    worker_process = Process(target=worker, args=(address,))
    worker_process.start()
    worker_process.join()

    results = collect_results(address)
    print(f"manager 地址: {HOST}:{port}")
    print(f"计算结果: {results}")

    # serve_forever 没有自然退出条件，示例结束后由主进程关闭 manager。
    server_process.terminate()
    server_process.join()


if __name__ == "__main__":
    main()
