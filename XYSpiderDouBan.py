import requests
import re

header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=20'

res = requests.get(url, headers=header).content.decode()

pat1 = '"rating":\["(.*?)","\d+"\]'
pat2 = '"title":"(.*?)"'

pattern1 = re.compile(pat1, re.I)
pattern2 = re.compile(pat2, re.I)

result1 = pattern1.findall(res)
result2 = pattern2.findall(res)

result = []
for i in range(0, len(result1)):
    tempStr = "排名："+str(i+1)+"电影名："+result2[i]+"豆瓣评分："+result1[i]
    result.append(tempStr)

print(result)