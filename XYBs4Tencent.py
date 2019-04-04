from bs4 import BeautifulSoup
import urllib
import urllib.request
import ssl

header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

# 全局取消证书验证
ssl._create_default_https_context = ssl._create_unverified_context

for i in range(0, 5):
    page = 10 * i
    start = {"start":page}
    start = urllib.parse.urlencode(start)
    url = "https://hr.tencent.com/position.php?&"+start+"#a"

    req = urllib.request.Request(url, headers=header)
    data = urllib.request.urlopen(req).read().decode()

    soup = BeautifulSoup(data, "lxml")
    urllist = soup.select('td a[target="_blank"]')

    for x in urllist:
        myurl = "https://hr.tencent.com/"+x.attrs["href"]
        req2 = urllib.request.Request(myurl, headers=header)
        data2 = urllib.request.urlopen(req2).read().decode()

        soup = BeautifulSoup(data2, "lxml")
        name = soup.select('tr td[id="sharetitle"]')[0].text
        textlist = soup.select('ul[class="squareli"] li')

        text = ""
        for i in textlist:
            text = text + i.text

        print(name)
        print(text)
        print("----------------------------------------------------")