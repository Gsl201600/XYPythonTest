# -*- coding: utf-8 -*-
import scrapy
from sunSpider.items import SunspiderItem


class SunSpider(scrapy.Spider):
    name = 'sun'
    allowed_domains = ['wz.sun0769.com']
    url = 'http://wz.sun0769.com/index.php/question/report?page='
    offset = 0
    start_urls = [url + str(offset)]

    # 获取每个帖子url
    def parse(self, response):
        # 取出每个链接的列表
        links = response.xpath('//div[@class="greyframe"]/table//td/a[@class="news14"]/@href').extract()
        # 发送每个帖子的请求,使用parse_item进行处理
        for link in links:
            yield scrapy.Request(link, callback=self.parse_item)
        
        # 设置自动翻页
        if self.offset <= 150:
            self.offset += 30
            # 重新发送新的页面
            yield scrapy.Request(self.url+str(self.offset), callback=self.parse)
    
    # 爬取帖子内容
    def parse_item(self, response):
        item = SunspiderItem()
        item['url'] = response.url
        item['title'] = response.xpath('//span[@class="niae2_top"]/text()').extract()[0]
        item['content'] =''.join(response.xpath('//td[@class="txt16_3"]/text()').extract())
        yield item
