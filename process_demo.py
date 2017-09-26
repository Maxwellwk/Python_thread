from multiprocessing import Process

import os
import time


def sub_process_fun(num, a):
    """子进程执行代码"""
    print("子进程 : .pid=%d" % os.getpid())
    for i in range(3):
        print("子进程: hello")
        time.sleep(0.1)


def main():
    print("父进程: pid=%d" % os.getpid())
    p = Process(target=sub_process_fun, args=(100,), kwargs={"a": 200})  # 创建一个子进程对象
    p.start()  # 开启子进程
    print("父进程: 子进程的状态 %s" % p.is_alive())

    p.terminate()  # 终止子进程的执行  存在延迟
    p.join()  # 收回子进程
    print("父进程: 结束")

if __name__ == '__main__':
    main()