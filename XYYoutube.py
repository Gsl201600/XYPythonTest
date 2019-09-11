# -*- coding:UTF-8 -*-
import requests
import re

# url = "https://www.youtube.com/user/TheOtakuMoe"
# url = "https://www.youtube.com/user/TheOddBroY"
# url = "https://www.youtube.com/user/NowYouKnowAF"
# url = "https://www.youtube.com/user/ChronexiaMisty"
# url = "https://www.youtube.com/user/TheAn1meMan"
url = "https://www.youtube.com/user/TheAn1meMan"

header = {
    'cookie': 'SID=dAfjqdUifmFxCC-D09Odd3D2fiLltCkg-CMl2xElgy5RlITKllNjhpjMcgqOYywqWZ0sYA.; HSID=AfgJIBJwWbDrR_fJL; SSID=ApVbqlRFuorGnBWnA; APISID=xSUNIlCEPwnwmawF/AeEVKdxW5keHLm97I; SAPISID=GZTmdMWsvFVg9kWh/A32F4oB47CWMHkNz2; VISITOR_INFO1_LIVE=IwLAWtWnqpw; LOGIN_INFO=AFmmF2swRQIhALOWpqnxGTgpBkeCN2pcOQ4Q1nnK4gXpEjHrexQ3NTGJAiBHVZC7HtIEVognS8GvoKSrR4eEGga7igmcHaJN-3ZB1g:QUQ3MjNmeFNvWi05UFRDc1gyOXZXU2h5bWkzS1BlcXQ1b2lhcUswU3dKQkdLREtja1BPZ2RnWmQtcWRoMk1lemphamN2SjYzQWcyZ0xzSTlCWW9MN0ctOHVtd0NwOHFpTmRIOWlzcW5pLTlheEdzVG9BYXNfZnRZTTdDZVo3MmpTaGJueVJWZm5WZFZsM1JTbnpQZHhoV0RpSzBnOTVQTXBmdUNaZldLaFk0RHR4UC1PWko4LU1n; PREF=al=zh-CN&f4=4000000&f1=50000000; YSC=swPQ0_Egz0g; SIDCC=AN0-TYtQDc-ZZu2msOvFBitdGu9_QBP2as5D4mTEi6D17lE6uwCkFJE8xswNWE7-1aD43P948g',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}

res = requests.get(url, headers=header).content.decode()

pat1 = r'"viewCountText":{"simpleText":"(.*?)"}'
pat2 = r'"subscriberCountText":{"simpleText":"(.*?)"}'

# {"simpleText":"57,268 次观看"}

pattern1 = re.compile(pat1, re.I)
pattern2 = re.compile(pat2, re.I)

result1 = pattern1.findall(res)
result2 = pattern2.findall(res)

print(':::::', result2)

result2 = re.sub('\D', '', result2[-1])
result = re.sub('\D', '', result1[0])

print(':::::', result2)
print(':::::', result1)
print(':::::', result)

# print(result1[0])
# print(result2[-1])