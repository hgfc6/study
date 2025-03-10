# 多线程
# 由于线程是操作系统直接支持的执行单元，
# 因此，高级语言通常都内置多线程的支持，Python也不例外，并且，Python的线程是真正的Posix Thread，而不是模拟出来的线程。

# Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，threading是高级模块，对_thread进行了封装。
# 绝大多数情况下，我们只需要使用threading这个高级模块。

import threading, time
def worker(n):
    print("%s is running..." % threading.current_thread().name)
    for i in range(5):
        print("%s is working %d" % (threading.current_thread().name, i))
        time.sleep(1)
    print("%s is done." % threading.current_thread().name)

t = threading.Thread(target=worker, name="LoopPrint", args=(5,))
t.start()
t.join()  # 等待线程结束
print("%s is done." % threading.current_thread().name)


# Lock
# 多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，
# 而多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，
# 因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。
# 因此，在多线程编程中，我们经常会用到锁（Lock）来实现线程之间同步。

import threading

balance = 0
lock = threading.Lock()

def change_it(n):
    global balance # 定义为全局变量
    balance += n
    balance -= n

def run_thread(n):
    for i in range(100000):
        lock.acquire() # 获取锁
        try:
            change_it(n)
        finally:
            lock.release() # 释放锁

if __name__ == '__main__':
    t1 = threading.Thread(target=run_thread, args=(5,))
    t2 = threading.Thread(target=run_thread, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance) # 0


# Python跑不了多核的原因
# 因为Python的线程虽然是真正的线程，但解释器执行代码时，有一个GIL锁：Global Interpreter Lock，
# 任何Python线程执行前，必须先获得GIL锁，然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。
# 这个GIL全局锁实际上把所有线程的执行代码都给上了锁
# 所以，多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，也只能用到1个核。
# GIL是Python解释器设计的历史遗留问题，通常我们用的解释器是官方实现的CPython，要真正利用多核，除非重写一个不带GIL的解释器。
# 所以，在Python中，可以使用多线程，但不要指望能有效利用多核。
# 如果一定要通过多线程利用多核，那只能通过C扩展来实现，不过这样就失去了Python简单易用的特点。
#
# 不过，也不用过于担心，Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。多个Python进程有各自独立的GIL锁，互不影响。