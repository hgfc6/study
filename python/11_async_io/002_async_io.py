# asyncio 基础示例
#
# 运行方式：
#     python 11_async_io/002_async_io.py
#
# asyncio 适合 I/O 密集型任务，例如网络请求、数据库请求、文件等待等。
# 它不是让 CPU 计算变快，而是在等待 I/O 时切换去做别的任务。

import asyncio
from random import random


async def fetch_data(name: str, delay: float) -> str:
    """模拟一个异步 I/O 操作。"""

    print(f"{name}: 开始请求，预计等待 {delay:.1f} 秒")

    # asyncio.sleep 不会阻塞整个线程，等待期间事件循环可以运行其他协程。
    await asyncio.sleep(delay)

    print(f"{name}: 请求完成")
    return f"{name} result"


async def gather_demo() -> None:
    """演示 asyncio.gather 并发运行多个协程。"""

    print("\n一、gather 并发")

    # gather 会并发调度多个协程，并按传入顺序返回结果。
    results = await asyncio.gather(
        fetch_data("task-a", 0.3),
        fetch_data("task-b", 0.2),
        fetch_data("task-c", 0.1),
    )

    print(f"gather 结果: {results}")


async def timeout_demo() -> None:
    """演示超时控制。"""

    print("\n二、超时控制")

    try:
        # wait_for 可以给协程设置最大等待时间。
        await asyncio.wait_for(fetch_data("slow-task", 1.0), timeout=0.2)
    except TimeoutError:
        print("slow-task 超时，已取消")


async def producer(queue: asyncio.Queue[int]) -> None:
    """生产者：向异步队列放入任务。"""

    for number in range(1, 6):
        await asyncio.sleep(random() * 0.1)
        await queue.put(number)
        print(f"生产任务: {number}")

    # None 作为结束信号，告诉消费者可以退出。
    await queue.put(None)


async def consumer(queue: asyncio.Queue[int | None]) -> None:
    """消费者：从异步队列读取任务并处理。"""

    while True:
        item = await queue.get()

        if item is None:
            queue.task_done()
            print("消费者收到结束信号")
            break

        await asyncio.sleep(0.05)
        print(f"消费任务: {item}, 结果: {item * item}")
        queue.task_done()


async def queue_demo() -> None:
    """演示 asyncio.Queue 的生产者消费者模型。"""

    print("\n三、异步队列")

    queue: asyncio.Queue[int | None] = asyncio.Queue()

    await asyncio.gather(
        producer(queue),
        consumer(queue),
    )


async def main() -> None:
    """集中运行 asyncio 示例。"""

    await gather_demo()
    await timeout_demo()
    await queue_demo()


if __name__ == "__main__":
    asyncio.run(main())
