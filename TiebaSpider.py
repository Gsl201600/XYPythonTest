from urllib import request
import urllib
from urllib import request
import time

header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

# for i in range(1, 4):
#     print("http://tieba.baidu.com/f?kw=python&ie=utf-8&pn="+str((i-1)*50))

def loadpage(fullurl, filename):
    print("正在下载：", filename)
    req = request.Request(fullurl, headers=header)
    resp = request.urlopen(req).read()
    return resp

def writepage(html, filename):
    print("正在保存：", filename)
    with open(filename, "wb") as f:
        f.write(html)

    print("---------------------")

def tiebaSpider(url, begin, end):
    for page in range(begin, end+1):
        pn=(page-1)*50
        fullurl = url+"&pn="+str(pn)
        filename = "/Users/yostar/XYPythonTest/第"+str(page)+"页.html"

        html = loadpage(fullurl, filename)
        writepage(html, filename)

if __name__ == "__main__":
    kw = input("请输入贴吧名：")
    begin = int(input("请输入起始页："))
    end = int(input("请输入结束页："))

    url = "http://tieba.baidu.com/f?"
    key = urllib.parse.urlencode({"kw":kw})
    url = url+key

    tiebaSpider(url, begin, end)

    time.sleep(10)