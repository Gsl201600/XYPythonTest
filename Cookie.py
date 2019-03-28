from urllib import request

url = "http://i.baidu.com/"

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;\
    q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;\
    v=b3',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': 'BAIDUID=66031BB1C012CC40CF84F0F1912509CE:FG=1; BIDUPSID=66031BB1C012CC40CF84F0F1912509CE; PSTM=1551947107; __cfduid=df8bf8191a4d9584785aa218d12e6b8ce1552466999; pgv_pvi=5288423424; delPer=0; PSINO=5; H_PS_PSSID=26523_1449_21097_28722_28558_28697_28585_28603_28625_22159; pgv_si=s8027840512; PHPSESSID=ig6dj6d6vvshgri6t0oan1e6l2; Hm_lvt_4010fd5075fcfe46a16ec4cb65e02f04=1553756156; BDUSS=Zwc29Wa1l1T3EyRmMyazNFRUJaZTRyTjNLcElvcjJmaVBXeGpBM3p0NXF-c05jQUFBQUFBJCQAAAAAAAAAAAEAAABNGu0g17fDzjIwMTEwMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGpxnFxqcZxccm; Hm_lpvt_4010fd5075fcfe46a16ec4cb65e02f04=1553756541',
    'Host': 'i.baidu.com',
    'Referer': 'https://baijiahao.baidu.com/s?id=1627984131677284289&wfr=spider&for=pc',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3)\
     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

req = request.Request(url, headers=headers)
response = request.urlopen(req)
print(response.read().decode())