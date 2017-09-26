from threading import Thread
import time


class SubThread(Thread):
    """子线程"""
    def run(self):
        """子线程执行代码"""
        for i in range(3):
            print("唱歌")
            time.sleep(0.1)

t = SubThread()

t.start()  # 开启线程对象

for i in range(3):
    print("跳舞")
    time.sleep(0.1)


t.join() # 回收线程对象