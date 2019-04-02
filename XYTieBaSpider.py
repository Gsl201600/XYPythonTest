import urllib
from lxml import etree

class Spider(object):
    def __init__(self):
        self.tiebaName = "java"
        self.beginPage = 1
        self.endPage = 3
        self.url = "http://tieba.baidu.com/f?"
        self.ua_header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        self.fileName = 1

    # 构造url
    def tiebaSpider(self):
        for page in range(self.beginPage, self.endPage+1):
            pn = (page - 1)*50
            wo = {'pn':pn, 'kw':self.tiebaName}
            word = urllib.parse.urlencode(wo)
            myurl = self.url + word
            self.loadPage(myurl)

    # 爬取页面内容
    def loadPage(self, url):
        req = urllib.request.Request(url, headers=self.ua_header)
        data = urllib.request.urlopen(req).read()

        html = etree.HTML(data)
        links = html.xpath('//div[@class="threadlist_lz clearfix"]/div/a/@href')
        for link in links:
            link = "http://tieba.baidu.com" + link
            self.loadImages(link)

    # 通过帖子详情页爬取图片
    def loadImages(self, link):
        req = urllib.request.Request(link, headers=self.ua_header)
        data = urllib.request.urlopen(req).read()

        html = etree.HTML(data)
        links = html.xpath('//img[@class="BDE_Image"]/@src')
        for imageslink in links:
            self.writeImages(imageslink)

    # 通过图片所在链接，爬取图片并保存图片到本地
    def writeImages(self, imageslink):
        print('正在存储图片:', self.fileName, "......")
        image = urllib.request.urlopen(imageslink).read()
        file = open("/Users/yostar/XYPythonTest/"+str(self.fileName)+".jpg", "wb")
        file.write(image)
        file.close()
        self.fileName+=1

if __name__ == "__main__":
    mySpider = Spider()
    mySpider.tiebaSpider()


# from lxml import etree
# import requests

# url = "https://www.qiushibaike.com"

# headers = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
#     'Accept-Language': 'zh-CN,zh;q=0.9',
#     'Host': 'www.qiushibaike.com',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
# }

# response = requests.get(url, headers=headers).text

# html = etree.HTML(response)

# result1 = html.xpath('//div//a[@class="recmd-content"]/@href')

# for site in result1:
#     xurl = url+site
#     response2 = requests.get(xurl).text
#     html2 = etree.HTML(response2)
#     result2 = html2.xpath("//div[@class='content']")
#     print(result2[0].text)