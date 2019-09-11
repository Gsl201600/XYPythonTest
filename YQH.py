import requests
import re
from datetime import datetime

def QHMain():
    # 参数部分
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Host': '47.245.31.123:4601',
        'Referer': 'http://47.245.31.123:4601',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'
    }
    data = {"username": "cs003", "password": "daasdqsfv221"}

    # 构造seesion，获取用户cookies
    seesion = requests.session()
    # 登录post请求，获取cookies
    loginUrl = 'http://47.245.31.123:4601/login'
    seesion.post(loginUrl, headers=headers, data=data)
    # 拿到用户cookies信息，获取数据的get请求
    getUrl = 'http://47.245.31.123:4601/api/v0/world/count_distribution'
    res = seesion.get(getUrl, headers=headers)
    # 获取服务器时间并转换成相应格式的字符串
    headerDate = res.headers['Date']
    date = datetime.strptime(headerDate, "%a, %d %b %Y %H:%M:%S %Z")
    dateStr = datetime.strftime(date,'%Y%m%d%H%M%S')
    # 清洗数据，获取需要的数据
    resData = res.content.decode()
    pat = '"online_count":"(.*?)","room_playing_account_count":(.*?),"'
    patten = re.compile(pat, re.I)
    result = patten.findall(resData)
    # 构造要写入的字符串并写入文件
    writeOnlineCountStr = dateStr + ' ' + result[0][0] + '\n'
    writeRoomPlayerCountStr = dateStr + ' ' + result[0][1] + '\n'
    with open('YQHOnlineCount.txt', 'a') as f:
        f.write(writeOnlineCountStr)
    with open('YQHRoomPlayerCount.txt', 'a') as f:
        f.write(writeRoomPlayerCountStr)
    
if __name__ == "__main__":
    QHMain()