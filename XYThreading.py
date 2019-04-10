import threading
import time

# 创建一个线程锁，互斥锁
lock = threading.Lock()

# def run(name):
#     print(name, "线程执行了")
#     time.sleep(3)

# t1 = threading.Thread(target=run, args=("t1",))
# t2 = threading.Thread(target=run, args=("t2",))

# t1.start()
# t2.start()

# # 设置子线程执行完毕之后再执行主线程内容
# t1.join()
# t2.join()

# print("执行完毕")
# -------------------------------------------------------------
# num = 100
# def run(name):
#     # 设置锁
#     lock.acquire()
#     # 设置num为全局变量
#     global num
#     num = num - 1
#     print("线程", num, "执行了，目前num的值为：", num)
#     # 释放锁
#     lock.release()

# for i in range(0, 100):
#     t = threading.Thread(target=run, args=(i+1,))
#     t.start()

num = 100

# 卖票
def sale(name):
    lock.acquire()
    global num
    if num > 0:
        num = num - 1
        print(name, "卖出一张票，还剩", num, "张！")
    lock.release()

# 售票窗口（两个线程表示）
while 1:
    if num > 0:
        t1 = threading.Thread(target=sale, args=("A窗口",))
        t2 = threading.Thread(target=sale, args=("B窗口",))
        t1.start()
        t2.start()
    else:
        break

print("票买完了！")