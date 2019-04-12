# -*- coding:UTF-8 -*-
import requests
from lxml import etree
import re

# url = "https://www.youtube.com/user/TheOtakuMoe"
# url = "https://www.youtube.com/user/TheOddBroY"
# url = "https://www.youtube.com/user/NowYouKnowAF"
# url = "https://www.youtube.com/user/ChronexiaMisty"
# url = "https://www.youtube.com/user/TheAn1meMan"

url = "https://www.facebook.com/BluePandaML/"
# url = "https://www.facebook.com/AnimeBallsDeep/"

header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

res = requests.get(url, headers=header).content.decode()

html = etree.HTML(res)
links = html.xpath('//div[@class="_4bl9"]/div')

result = re.sub('\D', '', links[1].text)
print("::::", result)

for content in links:
    print(content.text)