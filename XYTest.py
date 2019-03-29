import requests
import re

header = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Host': 'movie.douban.com',
    'Referer': 'https://movie.douban.com/typerank?type_name=%E5%96%9C%E5%89%A7&type=24&interval_id=100:90&action=',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

url = 'https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=20'

res = requests.get(url, headers=header).content.decode()

pat1 = '"score":"(.*?)"'
pat2 = '"title":"(.*?)"'
pat3 = '"vote_count":(.*?),'

pattern1 = re.compile(pat1,re.I)
pattern2 = re.compile(pat2, re.I)
pattern3 = re.compile(pat3, re.I)

data1 = pattern1.findall(res)
data2 = pattern2.findall(res)
data3 = pattern3.findall(res)

resultList = []

for i in range(0, len(data1)):
    tempStr = "电影名:"+data2[i]+" 评分:"+data1[i]+" 投票数:"+data3[i]
    resultList.append(tempStr)

print(resultList)