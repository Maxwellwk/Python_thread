from threading import Thread, Lock

num = 0  # 资源竞争问题
mutex = Lock()  # 创建一个互斥锁


def fun1():
    global num
    for i in range(1000000):
        mutex.acquire()
        # acquire 首先判断锁的当前状态，如果锁处于上锁状态，则默认处于阻塞等待
        # 等待直到锁处于未上锁状态的时候，才继续向下运行
        # 如果一旦发现锁处于未上锁状态，则将锁设置为上锁
        num += 1
        mutex.release()  # 释放锁


def fun2():
    global num
    for i in range(1000000):
        mutex.acquire()
        # acquire 首先判断锁的当前状态，如果锁处于上锁状态，则默认处于阻塞等待
        # 等待直到锁处于未上锁状态的时候，才继续向下运行
        # 如果一旦发现锁处于未上锁状态，则将锁设置为上锁
        num += 1
        mutex.release()  # 释放锁

t1 = Thread(target=fun1)  # 创建一个线程对象
t2 = Thread(target=fun2)  # 创建一个线程对象

t1.start()
t2.start()


t1.join()
t2.join()

print(num)
