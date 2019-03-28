import requests
import re
import time
import datetime

page = int(input("请输入你要爬取得页数："))

songID = []
songName = []

for i in range(0, page):
    url = "http://www.htqyy.com/top/musicList/hot?pageIndex="+str(i)+"&pageSize=20"
    # 获取音乐榜单的网页信息
    html = requests.get(url)
    strr = html.text

    pat1 = 'title="(.*?)" sid'
    pat2 = 'sid="(.*?)"'

    idList = re.findall(pat2, strr)
    titleList = re.findall(pat1, strr)

    songID.extend(idList)
    songName.extend(titleList)

nowTime = datetime.datetime.now()
nowMonth = nowTime.month
print(nowMonth)
for i in range(0, len(songID)):
    # http://f2.htqyy.com/play7/1430/mp3/3
    songUrl = "http://f2.htqyy.com/play7/"+str(songID[i])+"/mp3/"+str(nowMonth)
    songname = songName[i]
    data = requests.get(songUrl).content
    print(songUrl)

    print("正在下载第", i+1, "首，歌曲名：", songname)
    with open("/Users/yostar/XYPythonTest/Downloads/{}.mp3".format(songname), "wb") as f:
        f.write(data)
    time.sleep(0.1)

print(len(songID))
print(len(songName))