# -*- coding: utf-8 -*-
import scrapy
import re
from mySpider.items import MyspiderItem

class MusicspiderSpider(scrapy.Spider):
    name = 'musicSpider' #爬虫识别名称
    allowed_domains = ['www.htqyy.com'] #爬取网页范围
    start_urls = ['http://www.htqyy.com/top/musicList/hot?pageIndex=0&pageSize=20'] #起始url

    def parse(self, response):
        data = response.body.decode() #获取相应内容
        # items = [] #存放音乐信息的列表

        # 获取所有的歌曲名
        pat = re.compile('target="play" title="(.*?)"', re.I)
        titles = pat.findall(data)
        # 获取所有的艺术家
        pat = re.compile('target="_blank">(.*?)</a>', re.I)
        artists = pat.findall(data)

        for i in range(0, len(titles)):
            item = MyspiderItem()
            item['title'] = titles[i]
            item['artist'] = artists[i]
            yield item

        # 获取当前请求的url，ti取出页码信息
        beforeurl = response.url
        pat1 = 'pageIndex=(\d)'
        page = re.search(pat1, beforeurl).group(1)
        page = int(page)+1 # 得到下一次请求的pageIndex
        if page < 5:
            # 构造下一页url
            nexturl = 'http://www.htqyy.com/top/musicList/hot?pageIndex='+str(page)+'&pageSize=20'
            # 发送下一次请求
            yield scrapy.Request(nexturl, callback=self.parse)