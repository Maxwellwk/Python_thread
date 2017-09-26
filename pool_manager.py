from multiprocessing import Pool, Manager
import time

queue = Manager().Queue()  # 参数表明队列只能保存三条数据


def process_write():
    """在这个子进程中，负责向队列里放数据"""
    for i in range(3):
        queue.put(i)
        print("子进程1 写了一个数据 %d" % i)
        time.sleep(0.5)


def process_read():
    """在这个子进程中负责向队列中去数据"""
    while not queue.empty():
        ret = queue.get()
        print("子进程2 从队列中取一个数据 %d" % ret)
        time.sleep(0.5)

pool = Pool(3)

pool.apply(process_write)
pool.apply(process_read)

pool.close()
pool.join()

