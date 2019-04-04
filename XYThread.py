import threading
import queue
import time

# def run(name):
#     print(name, "线程启动了")
#     time.sleep(5)

# t1 = threading.Thread(target=run, args=("t1",))
# t2 = threading.Thread(target=run, args=("t2",))

# t1.start()
# t2.start()

# # 等待子线程执行执行完毕在执行主线程后面的内容
# t1.join()
# t2.join()

# class myThread(threading.Thread):
    
#     def __init__(self, name):
#         threading.Thread.__init__(self)
#         self.name = name
    
#     def run(self):
#         print("开始线程", self.name)
#         print("线程执行中。。。1")
#         time.sleep(1)
#         print("线程执行中。。。2")
#         time.sleep(1)
#         print("线程执行中。。。3")
#         time.sleep(1)
#         print("线程执行中。。。4")
#         time.sleep(1)
#         print("线程执行中。。。5")
#         time.sleep(1)
#         print("结束线程", self.name)

# t1 = myThread("t1")
# t2 = myThread("t2")
# t3 = myThread("t3")

# t1.start()
# t2.start()
# t3.start()

# t1.join()
# t2.join()
# t3.join()

# print("执行完毕")

q = queue.Queue(maxsize=10)
for i in range(1, 11):
    q.put(i)

while not q.empty():
    print(q.get())
