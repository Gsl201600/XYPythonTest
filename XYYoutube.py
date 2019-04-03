# -*- coding:UTF-8 -*-
import requests
import re

# url = "https://www.youtube.com/user/TheOtakuMoe"
# url = "https://www.youtube.com/user/TheOddBroY"
# url = "https://www.youtube.com/user/NowYouKnowAF"
# url = "https://www.youtube.com/user/ChronexiaMisty"
# url = "https://www.youtube.com/user/TheAn1meMan"
url = "https://www.youtube.com/user/TheOtakuMoe"

header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

res = requests.get(url, headers=header).content.decode()

pat1 = r'"viewCountText":{"simpleText":"收看次數：(.*?) 次"}'
pat2 = r'"subscriberCountText":{"simpleText":"(.*?)"}'

pattern1 = re.compile(pat1, re.I)
pattern2 = re.compile(pat2, re.I)

result1 = pattern1.findall(res)
result2 = pattern2.findall(res)

print(result1[0])
print(result2[-1])