# 多进程
# linux/unix中有系统调用fork()来复制进程
# 在python中，可以使用os.fork()来创建子进程
# fork()非常特殊。普通的函数调用，调用一次，返回一次，但是fork()调用一次，返回两次
# 因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。
#
# 子进程永远返回0，而父进程返回子进程的ID。
# 这样做的理由是，一个父进程可以fork出很多子进程，所以，父进程要记下每个子进程的ID，而子进程只需要调用getppid()就可以拿到父进程的ID。

# import os
#
# print("Process ID (before fork):", os.getpid())
# # 创建子进程
# pid = os.fork()
#
# if pid == 0:
#     # 子进程
#     print("Child process ID:", os.getpid())
# else:
#     # 父进程
#     print("Parent process ID:", os.getpid())
#     print("Child process ID (after fork):", pid)
# 以上代码只能在linux/unix系统中运行，windows系统中没有fork()系统调用
# 假如想跨平台运行，可以使用multiprocessing模块

from multiprocessing import Process
import os

# 子进程要执行的代码
def worker(name):
    print("Child process(%s) ID: %s Parent process ID: %s" % (name, os.getpid(), os.getppid()))
    print("Chile process(%s) is running..." % name)
    print("Chile process(%s) is done." % name)



# --------------进程池 如果要创建多个进程，可以用池化技术，先创建进程池，然后把任务放到池中，池中有空闲进程时，就去执行任务，否则就等待。
from multiprocessing import Pool
import random, time
def long_time_task(name):
    print("Long time task(%s) is running..." % name)
    start = time.time()
    random_num = random.randint(1, 10)
    time.sleep(random_num * 3)
    end = time.time()
    print("Long time task(%s) runs %0.2f seconds." % (name, (end - start)))
    print("Long time task(%s) is done." % name)




# -------------控制子进程的输入和输出
def process_input_output():
    # 很多时候，子进程并不是自身，而是一个外部进程。我们创建了子进程后，还需要控制子进程的输入和输出。
    # subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。
    import subprocess
    # 启动子进程，并传入命令行参数
    r = subprocess.call(['nslookup', 'www.python.org'])
    print('Exit code:', r)

    # 如果子进程还需要输入，则可以通过communicate()方法输入
    p = subprocess.Popen(['nslookup', 'www.python.org'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    output, err = p.communicate(input=b'set q=mx\npython.org\nexit\n')
    # 上面的代码相当于在命令行执行命令nslookup，然后手动输入：
    # set q=mx
    # python.org
    # exit
    print(output.decode('utf-8'))
    print('Exit code:', p.returncode)


# --------------进程间通信
# Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。
def write(q):
    for value in ['A', 'B', 'C']:
        q.put(value)
        print("Put %s to queue" % value)
        time.sleep(1)
def read(q):
    while True:
        value = q.get(True)
        print("Get %s from queue" % value)
def process_communication_with_queue():
    # Queue是最常用的进程间通信方式。
    # 父进程创建了一个Queue，然后，把Queue的实例传给各个子进程。各个子进程就可以通过Queue来通信。
    from multiprocessing import Queue
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
    print("All subprocesses done.")


def worker2(parent_conn, child_conn):
    print("Child process received:", child_conn.recv())
    child_conn.send("Child process says hello!")
    parent_conn.close()
    child_conn.close()
    print("Child process is done.")
def process_communication_with_pipe():
    # 管道（Pipe）是另一种进程间通信方式。
    # 父进程和子进程各自创建一对管道，然后，父进程和子进程各自使用一端进行读写。
    from multiprocessing import Pipe
    parent_conn, child_conn = Pipe()
    p = Process(target=worker2, args=(parent_conn, child_conn))
    p.start()
    parent_conn.send("Hello, child process!")
    print("Parent received:", parent_conn.recv())
    p.join()
    print("Parent process is done.")



if __name__ == '__main__':
    # 创建子进程
    p = Process(target=worker, args=("worker1",))
    p.start() # 启动子进程
    p.join() # 等待子进程结束，再继续往下执行
    print("Parent process ID: %s" % os.getpid())
    print("Parent process is done.")

    # 进程池
    p = Pool(5)
    for i in range(10):
        p.apply_async(long_time_task, args=(i,))
    p.close() # 调用close()之后就不能继续添加新的Process
    p.join()
    print("All subprocesses done.")
    # 进程池的另一种写法
    with Pool(5) as p:
        for i in range(10):
            p.apply_async(long_time_task, args=(i,))
        p.close()
        p.join()
        print("All subprocesses done.")
    # 进程池的map()方法 map()方法就是把任务分发到进程池中，然后等待所有进程执行完毕，然后返回结果列表。
    with Pool(5) as p:
        result = p.map(long_time_task, range(10))


    process_input_output()

    process_communication_with_queue()

    process_communication_with_pipe()