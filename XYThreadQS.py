import threading
import queue
import requests
import time
from lxml import etree

# https://www.qiushibaike.com/8hr/page/1/


# 采集网页线程---爬取段子列表所在的网页放进队列
class Thread1(threading.Thread):
    def __init__(self, threadName, pageQueue, dataQueue):
        super(Thread1, self).__init__()
        # threading.Thread.__init__(self)
        self.threadName = threadName #线程名
        self.pageQueue = pageQueue #页码队列
        self.dataQueue = dataQueue #数据队列
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    
    def run(self):
        print("启动线程"+self.threadName)
        while not flag1:
            try:
                page = self.pageQueue.get()
                url = "https://www.qiushibaike.com/8hr/page/"+str(page)+"/"
                content = requests.get(url, headers=self.headers).text
                time.sleep(0.5)
                self.dataQueue.put(content)
            except Exception as e:
                print(e+self.threadName)

        print("结束线程"+self.threadName)


# 解析网页线程--从队列中拿到列表网页，进行解析，并存储到本地
class Thread2(threading.Thread):
    def __init__(self, threadName, dataQueue, fileName):
        threading.Thread.__init__(self)
        self.threadName = threadName
        self.dataQueue = dataQueue
        self.fileName = fileName
    
    def run(self):
        print("启动线程"+self.threadName)
        while not flag2:
            try:
                data1 = self.dataQueue.get()
                html = etree.HTML(data1)
                nodeList = html.xpath('//div/a[@class="recmd-content"]')
                for node in nodeList:
                    data = node.text
                    self.fileName.write(data+"\n")

            except Exception as e:
                print(e+self.threadName)

        print("结束线程"+self.threadName)

flag1 = False #判断页码队列中是否为空
flag2 = False #判断数据队列中是否为空

def main():
    # 页码队列
    pageQueue = queue.Queue(10)
    for i in range(1, 11):
        pageQueue.put(i)
    # 存放采集结果的数据队列
    dataQueue = queue.Queue()
    # 保存到本地的文件
    fileName = open("/Users/yostar/XYPythonTest/duanzi.txt", "a")
    
    # 启动线程
    t1 = Thread1("采集线程", pageQueue, dataQueue)
    t1.start()

    t2 = Thread2("解析线程", dataQueue, fileName)
    t2.start()

    # 当pageQueue为空时，结束采集线程
    while not pageQueue.empty():
        pass
    global flag1
    flag1 = True

    # 当dataQueue为空时，结束解析线程
    while not dataQueue.empty():
        pass
    global flag2
    flag2 = True

    t1.join()
    t2.join()

    fileName.close()

    print("结束！")

if __name__ == "__main__":
    main()