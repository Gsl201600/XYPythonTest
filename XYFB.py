# -*- coding:UTF-8 -*-
import requests
from lxml import etree
import re

# url = "https://www.youtube.com/user/TheOtakuMoe"
# url = "https://www.youtube.com/user/TheOddBroY"
# url = "https://www.youtube.com/user/NowYouKnowAF"
# url = "https://www.youtube.com/user/ChronexiaMisty"
# url = "https://www.youtube.com/user/TheAn1meMan"


# url = "https://www.facebook.com/saimon.ma/followers"

url = "https://www.facebook.com/asuka111art"



header = {
    'cookie': 'sb=MbOuXOOi44pt9jAq-Ai1GIZH; datr=wDu5XMYtcvLxOIj-l0U8cpWK; dpr=2; locale=en_GB; c_user=100027010132639; xs=25%3A2XlUgWGn4xEJ8w%3A2%3A1557801845%3A-1%3A-1; fr=1C4o30JiwGNYhBa24.AWWcKcFu7YqKK5QmhfMTikT6V3o.BcrrMx.Dp.AAA.0.0.Bc2it1.AWVpASg3; spin=r.1000706631_b.trunk_t.1557801846_s.1_v.2_; presence=EDvF3EtimeF1557803471EuserFA21B27010132639A2EstateFDutF1557803471247CEchFDp_5f1B27010132639F8CC; wd=590x741',
    # 'cookie': 'sb=MbOuXOOi44pt9jAq-Ai1GIZH; datr=wDu5XMYtcvLxOIj-l0U8cpWK; dpr=2; locale=en_GB; c_user=100027010132639; xs=25%3A2XlUgWGn4xEJ8w%3A2%3A1557801845%3A-1%3A-1; fr=1C4o30JiwGNYhBa24.AWWcKcFu7YqKK5QmhfMTikT6V3o.BcrrMx.Dp.AAA.0.0.Bc2it1.AWVpASg3; spin=r.1000706631_b.trunk_t.1557801846_s.1_v.2_; presence=EDvF3EtimeF1557802888EuserFA21B27010132639A2EstateFDutF1557802888206CEchFDp_5f1B27010132639F6CC; wd=590x741',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}


res = requests.get(url, headers=header).content.decode()


# pat = '<div class="_6a _6b plm"><span class="fsl fcg">(.*?) followers</span></div>'
# pattern = re.compile(pat, re.I)
# result = pattern.findall(res)
# result = result[0]
# print(result)

pat = '<div class="_4bl9"><div>(.*?)</div></div>'
pattern = re.compile(pat, re.I)
result = pattern.findall(res)
result = re.sub('\D', '', result[1])
print("::::", result)



# <div class="_4bl9"><div>22,329 people follow this</div>
# html = etree.HTML(res)
# links = html.xpath('//div[@class="_4bl9"]/div')
# print("::::", links)

# result = re.sub('\D', '', links[1].text)
# print("::::", result)

# for content in links:
#     print(content.text)