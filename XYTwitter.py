import requests
import re

# url = "https://twitter.com/Vtuber_Moe"
# url = "https://twitter.com/BluePandaReal"
# url = "https://twitter.com/AnimeBallsDeep"
# url = "https://twitter.com/Chronexia"
url = "https://twitter.com/TheAn1meMan"

header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

res = requests.get(url, headers=header).content.decode()

pat = 'followers_count&quot;:(.*?),'
pattern = re.compile(pat, re.I)
result = pattern.findall(res)

print(result)