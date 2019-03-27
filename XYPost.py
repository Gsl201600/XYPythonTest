from urllib import request
import urllib
import re

key = ""

header = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Host': 'fanyi.youdao.com',
    'Referer': 'http://fanyi.youdao.com/',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

fromdata = {
    'i': key,
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': '15536799573791',
    'sign': '8d380fdf5864bf637788cfc0d78bafc1',
    'ts': '1553679957379',
    'bv': '8e6b97cc77d39e279300e0dc730aff3b',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTlME',
    'typoResult': 'false'
}

def translate(key):
    fromdata['i'] = key
    data = urllib.parse.urlencode(fromdata).encode(encoding='utf-8')
    req = request.Request(url, data=data, headers=header)
    res = request.urlopen(req).read().decode()

    # 提取tgt":"(.*?)"}]]中间的任意内容
    pat = '"tgt":"(.*?)"}]]'
    result = re.findall(pat, res)
    print(result[0])

if __name__ == "__main__":
    while 1:
        key = input("请输入要翻译的内容：")
        translate(key)