from multiprocessing import Queue
import time

q = Queue(3)  # 参数表明队列只能保存三条数据

print("判断队列是否为空: %s" % q.empty())
print("判断队列是否为满: %s" % q.full())

q.put(100)
print("新添加一条数据100")
print("当前队列中的数据个数: %d" % q.qsize())
q.put(200)
print("新添加一条数据200")
q.put(300)
print("新添加一条数据300")

time.sleep(0.1)
print("判断队列是否为空: %s" % q.empty())
print("判断队列是否为满: %s" % q.full())

ret = q.get()
print(ret)
ret = q.get()
print(ret)
ret = q.get()
print(ret)

print("判断队列是否为空: %s" % q.empty())
print("判断队列是否为满: %s" % q.full())