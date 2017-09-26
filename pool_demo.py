from multiprocessing import Pool
import time
import os


def task(num):
    """定义的任务代码"""
    print("子进程: pid = %d 开始执行任务num = %d" % (os.getpid(), num))
    time.sleep(1)
    print("子进程: pid = %d 开始执行任务unm = %d" % (os.getpid(), num))

pool = Pool(4)  # 创建进程池对象， 参数表明这个进程池中进程的个数

for i in range(10):
    pool.apply_async(task, (i,))  # 想进程里添加任务，非阻塞方法
    # pool.apply(task, (i,))  # 想进程里添加任务，阻塞方法

print("主进程: 所有任务都交给进程池去做")
pool.close()  # 关闭进程池对象， 表示不能再向进程池中添加新的对象
pool.join()  # 回收进程池资源


