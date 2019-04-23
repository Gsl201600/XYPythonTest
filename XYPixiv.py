import requests
import re

url = 'https://www.pixiv.net/member.php?id=4381986'

res = requests.get(url).text

pat = 'class="require-register int" data-title="showBookmarkRegister" data-user-id="[\s\S]*">(.*?)</a></div></div></div></div>'
patten = re.compile(pat, re.I)
result = patten.findall(res)[0]
print(result)