from multiprocessing import Queue, Process
import time

q = Queue(3)  # 参数表明队列只能保存三条数据


# queue = Queue(3)


def process_write(queue):
    # def process_write():

    """在这个子进程中，负责向队列里放数据"""
    for i in range(3):
        queue.put(i)
        print("子进程1 写了一个数据 %d" % i)
        time.sleep(0.5)


def process_read(queue):
    # def process_read():

    """在这个子进程中负责向队列中去数据"""
    while not queue.empty():
        ret = queue.get()
        print("子进程2 从队列中取一个数据 %d" % ret)
        time.sleep(0.5)


p1 = Process(target=process_write, args=(q,))
p2 = Process(target=process_read, args=(q,))

# p1 = Process(target=process_write)
# p2 = Process(target=process_read)


p1.start()
p1.join()

p2.start()
p2.join()
