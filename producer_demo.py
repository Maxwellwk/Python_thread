from threading import Thread
import queue
import time

q = queue.Queue()  # 创建一个队列容器，用来保存生产者产生的数据


class Producer(Thread):
    """生产者线程"""
    def run(self):
        count = 0
        while True:
            if q.qsize() < 50:
                for i in range(3):
                    count += 1
                    msg = "产品 %d" % count
                    q.put(msg)
                    print("生产者%s 生产了一个数据 %s" % (self.name, msg))
            time.sleep(1)


class Customer(Thread):
    """消费者线程"""
    def run(self):
        while True:
            if q.qsize() > 20:
                 for i in range(2):
                    msg = q.get()
                    print("消费者%s 消费了一个数据 %s" % (self.name, msg))
            time.sleep(1)

for i in range(3):
    p = Producer()
    p.start()

for i in range(5):
    c = Customer()
    c.start()
    