# -*- coding:UTF-8 -*-
import requests
from lxml import etree
import re
import json

class YStargazerDataHandle(object):
    def __init__(self, data, isCloseYTViewCount):
        self.data = data
        self.isCloseYTViewCount = isCloseYTViewCount
        self.header = {
            'cookie': 'sb=MbOuXOOi44pt9jAq-Ai1GIZH; datr=wDu5XMYtcvLxOIj-l0U8cpWK; dpr=2; locale=en_GB; c_user=100027010132639; xs=25%3A2XlUgWGn4xEJ8w%3A2%3A1557801845%3A-1%3A-1; fr=1C4o30JiwGNYhBa24.AWWcKcFu7YqKK5QmhfMTikT6V3o.BcrrMx.Dp.AAA.0.0.Bc2it1.AWVpASg3; spin=r.1000706631_b.trunk_t.1557801846_s.1_v.2_; presence=EDvF3EtimeF1557803471EuserFA21B27010132639A2EstateFDutF1557803471247CEchFDp_5f1B27010132639F8CC; wd=590x741',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
            }
        self.headerYTB = {
            'cookie': 'SID=dAfjqdUifmFxCC-D09Odd3D2fiLltCkg-CMl2xElgy5RlITKllNjhpjMcgqOYywqWZ0sYA.; HSID=AfgJIBJwWbDrR_fJL; SSID=ApVbqlRFuorGnBWnA; APISID=xSUNIlCEPwnwmawF/AeEVKdxW5keHLm97I; SAPISID=GZTmdMWsvFVg9kWh/A32F4oB47CWMHkNz2; VISITOR_INFO1_LIVE=IwLAWtWnqpw; LOGIN_INFO=AFmmF2swRQIhALOWpqnxGTgpBkeCN2pcOQ4Q1nnK4gXpEjHrexQ3NTGJAiBHVZC7HtIEVognS8GvoKSrR4eEGga7igmcHaJN-3ZB1g:QUQ3MjNmeFNvWi05UFRDc1gyOXZXU2h5bWkzS1BlcXQ1b2lhcUswU3dKQkdLREtja1BPZ2RnWmQtcWRoMk1lemphamN2SjYzQWcyZ0xzSTlCWW9MN0ctOHVtd0NwOHFpTmRIOWlzcW5pLTlheEdzVG9BYXNfZnRZTTdDZVo3MmpTaGJueVJWZm5WZFZsM1JTbnpQZHhoV0RpSzBnOTVQTXBmdUNaZldLaFk0RHR4UC1PWko4LU1n; PREF=al=zh-CN&f4=4000000&f1=50000000; YSC=swPQ0_Egz0g; SIDCC=AN0-TYtQDc-ZZu2msOvFBitdGu9_QBP2as5D4mTEi6D17lE6uwCkFJE8xswNWE7-1aD43P948g',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
        }
        self.headers = {
            'Accept-Language': 'zh-CN',
            'Client-Id': 'kimne78kx3ncx6brgo4mv6wki5h1ko',
            'Content-Type': 'text/plain;charset=UTF-8',
            'Origin': 'https://www.twitch.tv',
            'Host': 'gql.twitch.tv',
            'Authorization': 'OAuth 5w33taccdoyegajwzngy95pg0qof9b',
            'X-Device-Id': '22199cccd5ba5388',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'
        }
    
    # 处理数据函数
    def handleData(self):
        resValues = json.dumps(self.data, ensure_ascii=False)
        youtubePatStr = 'https://www.youtube.com/.*'
        fbPatStr = 'https://www.facebook.com/.*'
        twPatStr = 'https://twitter.com/.*'
        twitchPatStr = 'https://www.twitch.tv/.*'
        insPatStr = 'https://www.instagram.com/.*'
        pixivPatStr = 'https://www.pixiv.net/.*'

        # 处理YouTube数据
        for contentArr in self.data:
            for content in contentArr:
                youtubePat = re.compile(youtubePatStr)
                results = youtubePat.findall(content)
                if len(results):
                    temp = self.getYoutubeData(results[0])

                    subStr = '"%s", "%s"'%(results[0], temp[0])
                    pat = '"%s", "[\s\S]*?"'%results[0]
                    youtubePat = re.compile(pat)
                    resValues = youtubePat.sub(subStr, resValues)
                    # # 判断是表1还是其他
                    # if int(self.isCloseYTViewCount) == 1:
                    #     subStr = '"%s", "%s", "%s"'%(results[0], temp[0], temp[1])
                    #     pat = '"%s", "[\s\S]*?", "[\s\S]*?"'%results[0]
                    #     youtubePat = re.compile(pat)
                    #     resValues = youtubePat.sub(subStr, resValues)
                    # else:
                    #     subStr = '"%s", "%s"'%(results[0], temp[0])
                    #     pat = '"%s", "[\s\S]*?"'%results[0]
                    #     youtubePat = re.compile(pat)
                    #     resValues = youtubePat.sub(subStr, resValues)

        # 处理fb数据
        for fbArr in self.data:
            for content in fbArr:
                fbPat = re.compile(fbPatStr)
                results = fbPat.findall(content)
                if len(results):
                    temp = self.getFBData(results[0])

                    subStr = '"%s", "%s"'%(results[0], temp)
                    pat = '"%s", "[\s\S]*?"'%results[0]
                    fbPat = re.compile(pat)
                    resValues = fbPat.sub(subStr, resValues)
        
        # 处理tw数据
        for twArr in self.data:
            for content in twArr:
                twPat = re.compile(twPatStr)
                results = twPat.findall(content)
                if len(results):
                    temp = self.getTWData(results[0])

                    subStr = '"%s", "%s"'%(results[0], temp[0])
                    pat = '"%s", "[\s\S]*?"'%results[0]
                    twPat = re.compile(pat)
                    resValues = twPat.sub(subStr, resValues)

        # 处理ins数据
        for insArr in self.data:
            for content in insArr:
                insPat = re.compile(insPatStr)
                results = insPat.findall(content)
                if len(results):
                    temp = self.getInsData(results[0])

                    subStr = '"%s", "%s"'%(results[0], temp[0])
                    pat = '"%s", "[\s\S]*?"'%results[0]
                    insPat = re.compile(pat)
                    resValues = insPat.sub(subStr, resValues)
        
        # 处理twitch数据
        for twitchArr in self.data:
            for content in twitchArr:
                twitchPat = re.compile(twitchPatStr)
                results = twitchPat.findall(content)
                if len(results):
                    temp = self.getTwitchData(results[0])

                    subStr = '"%s", "%s"'%(results[0], temp[0])
                    pat = '"%s", "[\s\S]*?"'%results[0]
                    twitchPat = re.compile(pat)
                    resValues = twitchPat.sub(subStr, resValues)
        
        # 处理Pixiv数据
        for pixivArr in self.data:
            for content in pixivArr:
                pixivPat = re.compile(pixivPatStr)
                results = pixivPat.findall(content)
                if len(results):
                    temp = self.getPixivData(results[0])

                    subStr = '"%s", "%s"'%(results[0], temp[0])
                    pat = '"%s", "[\s\S]*?"'%results[0]
                    pixivPat = re.compile(pat)
                    resValues = pixivPat.sub(subStr, resValues)
        
        resData = json.loads(resValues)
        return resData
    

    # 爬取YouTube数据
    def getYoutubeData(self, url):
        res = requests.get(url, headers=self.headerYTB).content.decode()
        # 观看次数
        pat1 = r'"viewCountText":{"simpleText":"(.*?)"}'
        # 订阅
        pat2 = r'"subscriberCountText":{"simpleText":"(.*?)"}'

        pattern1 = re.compile(pat1, re.I)
        pattern2 = re.compile(pat2, re.I)

        result1 = pattern1.findall(res)
        result2 = pattern2.findall(res)
        result1 = re.sub('\D', '', result1[0])
        result2 = re.sub('\D', '', result2[-1])
        return result2, result1
    
    
    # 爬取fb数据
    def getFBData(self, url):
        res = requests.get(url, headers=self.header).content.decode()
        pat = '<div class="_4bl9"><div>(.*?)</div></div>'
        pattern = re.compile(pat, re.I)
        result = pattern.findall(res)
        # 判断是否为空
        if len(result) > 0:
            result = re.sub('\D', '', result[1])
        else:
            result = 'N/A'
#        # 判断是否是个人主页 fb废弃
#        if url[-1] is '/':
#            res = requests.get(url, headers=self.header).content.decode()
#            pat = '<div class="_4bl9"><div>(.*?)</div></div>'
#            pattern = re.compile(pat, re.I)
#            result = pattern.findall(res)
#            # 判断是否为空
#            if len(result) > 0:
#                result = re.sub('\D', '', result[1])
#            else:
#                result = 'N/A'
#        else:
#            url = url + '/followers'
#            res = requests.get(url, headers=self.header).content.decode()
#            pat = '<div class="_6a _6b plm"><span class="fsl fcg">(.*?) followers</span></div>'
#            pattern = re.compile(pat, re.I)
#            result = pattern.findall(res)
#            # 判断是否为空
#            if len(result) > 0:
#                result = result[0]
#            else:
#                result = 'N/A'
        return result

    # 爬取ins数据
    def getInsData(self, url):
        res = requests.get(url, headers=self.header).content.decode()

        pat = '"edge_followed_by":{"count":(.*?)}'
        pattern = re.compile(pat, re.I)
        result = pattern.findall(res)
        return result
    
    # 爬取Twitch数据
    def getTwitchData(self, url):
        pat = re.compile('https://www.twitch.tv/(.*)')
        pages = pat.findall(url)
        url = "https://gql.twitch.tv/gql"

        datas = '[{"operationName":"ChannelRoot_Channel","variables":{"currentChannelLogin":"misty_chronexia","includeChanlets":true},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"c22e8985e3f77ceb6b460e8f8d252e7e1d77b6d1d4560aed5d18dcf1af5e93dd"}}},{"operationName":"ChannelPage__ChannelViewersCount","variables":{"login":"misty_chronexia"},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"3b5b233b59cc71f5ab273c74a30c46485fa52901d98d7850d024ad0669270184"}}},{"operationName":"Thud_Recommendations","variables":{"currentChannelLogin":"misty_chronexia"},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"0d12cafca0f97438f3fb14309f839ab52b9742ed06b7d41bd87a4226cfedadc1"}}},{"operationName":"ChannelPage_ChannelHeader","variables":{"login":"misty_chronexia"},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"6bc56115acedebbaddc681f839c9bf7c2578d05bf2ca50f823815257d2059745"}}}]'
        datas = datas.replace("misty_chronexia", pages[0])

        res = requests.post(url, headers=self.headers, data=datas).content.decode()

        pat = '"followers":{"totalCount":(.*?),'
        pattern = re.compile(pat, re.I)
        result = pattern.findall(res)
        return result
    
    # 爬取Pixiv数据
    def getPixivData(self, url):
        res = requests.get(url, headers=self.header).text
        pat = 'class="require-register int" data-title="showBookmarkRegister" data-user-id="[\s\S]*">(.*?)</a></div></div></div></div>'
        patten = re.compile(pat, re.I)
        result = patten.findall(res)
        return result
    
    # 爬取TW数据
    def getTWData(self, url):
        res = requests.get(url, headers=self.header).content.decode()

        pat = 'followers_count&quot;:(.*?),'
        pattern = re.compile(pat, re.I)
        result = pattern.findall(res)
        return result
