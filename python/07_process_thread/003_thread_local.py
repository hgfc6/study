# ThreadLocal
# 在多线程环境下，每个线程都有自己的数据。一个线程使用自己的局部变量比使用全局变量好，因为局部变量只有线程自己能看见，不会影响其他线程，而全局变量的修改必须加锁。
# 但是局部变量也有问题，就是在函数调用的时候，传递起来很麻烦

# 可以使用全局dict来保存每个线程的局部变量(线程名做key)，这样就可以在任意函数中访问到线程的局部变量。
# 但是全局dict的使用也有问题，比如全局dict会占用内存，而且线程之间的数据共享也不安全。
# 所以Python提供了ThreadLocal类来解决这个问题。
import threading

# 创建一个ThreadLocal对象
local_data = threading.local()

# 定义一个函数，使用ThreadLocal对象保存局部变量
def process_data(data):
    # 获取当前线程的局部变量
    local_data.x = data
    # 处理局部变量
    print('Local data:', local_data.x)
# 创建两个线程
t1 = threading.Thread(target=process_data, args=(10,))
t2 = threading.Thread(target=process_data, args=(20,))

# 启动线程
t1.start()
t2.start()

# 等待线程结束
t1.join()
t2.join()

# ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源。
