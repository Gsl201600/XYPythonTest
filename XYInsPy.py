import requests
import re

# url = "https://www.instagram.com/bluepanda1/"
url = "https://www.instagram.com/joey.the.anime.man/"

header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

res = requests.get(url, headers=header).content.decode()

pat = '"edge_followed_by":{"count":(.*?)}'
pattern = re.compile(pat, re.I)
result = pattern.findall(res)

print(result)