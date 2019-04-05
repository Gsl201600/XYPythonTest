import requests
from lxml import etree
import json

class SpiderDoban(object):
    def __init__(self, url):
        self.url = url
        self.header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    }

    def get_data(self):
        req = requests.get(self.url, headers=self.header)
        data = etree.HTML(req.content.decode())

        selector = data.xpath('//div[@id="nowplaying"]/div[@class="mod-bd"]/ul/li')
        
        move_data = []

        for content in selector:
            title = content.xpath('@data-title')[0]
            score = content.xpath('@data-score')[0]
            votecount = content.xpath('@data-votecount')[0]
            duration = content.xpath('@data-duration')[0]
            release = content.xpath('@data-release')[0]
            region = content.xpath('@data-region')[0]
            director = content.xpath('@data-director')[0]
            actors = content.xpath('@data-actors')[0]

            move_data.append({
                'title': title if title else '',
                'score': score if score else '',
                'votecount': votecount if votecount else '',
                'duration': duration if duration else '',
                'release': release if release else '',
                'region': region if region else '',
                'director': director if director else '',
                'actors': actors if actors else '',
            })

        with open("/Users/yangyanlei/XYPythonTest/movie_data.json", "w", encoding="utf-8") as f:
            json.dump(move_data, f, ensure_ascii=False)

        print(move_data)

if __name__ == "__main__":
    s = SpiderDoban('https://movie.douban.com/cinema/nowplaying/guangzhou/')
    s.get_data()


# json.dumps  将 Python 对象编码成 JSON 字符串
# json.loads  将 已编码的 JSON 字符串解码为 Python 对象

# json.dump  将 JSON 字符串数据写进文件
# json.load  读取 JSON 文件里面的数据

# url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=20'

# res = requests.get(url, headers=header).content.decode()