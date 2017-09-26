import os
import time

rett_demo = os.fork()  # 创建新的进程 一次调用，两次返回

if rett_demo == 0:
    # 子进程执行
    # 子进程拿到的返回值是0
    print("子进程：pid = %d, ppid = %d") % (os.getpid(), os.getppid())
    for i in range(3):
        print("放音乐")
        time.sleep(0.1)
else:
    # 父进程执行
    # 父进程拿到的返回值是创建的子进程的pid
    print("父进程: ret = %d" % rett_demo)
    print("父进程: pid = %d, ppid = %d" % (os.getpid(), os.getppid()))
    for i in range(3):
        print("跳舞")
        time.sleep(0.1)

