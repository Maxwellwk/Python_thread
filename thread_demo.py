from threading import Thread
import time


def sing():
    for i in range(3):
        print("唱歌")
        time.sleep(0.1)

t = Thread(target=sing)  # 创建一个线程对象

t.start()  # 开启线程对象

for i in range(3):
    print("跳舞")
    time.sleep(0.1)

t.join()