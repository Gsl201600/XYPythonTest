# -*- coding:UTF-8 -*-
import requests
import urllib
import re
import json
import datetime

class YMediaListDataHandle(object):
    def __init__(self, data):
        self.data = data
        self.header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
        'cookie': '_ga=GA1.2.552915472.1555308528; _gid=GA1.2.140767794.1555308528; _vwo_uuid_v2=DB083B931002C3BA1787C0A12BF60EA8C|b8509eb374057231645d63cb7e2a30f7; _gcl_au=1.1.278305556.1555308529; intercom-id-e74067abd037cecbecb0662854f02aee12139f95=1edf5c89-9c62-46de-87af-fd3cf1cae535; _pk_ref.1.fd33=%5B%22%22%2C%22%22%2C1555381124%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_ses.1.fd33=*; _vis_opt_s=1%7C; _vis_opt_test_cookie=1; .SGTOKEN.SIMILARWEB.COM=uYWa4M80jpxYXqpcdiOz9_FiFKrKeykFBKuIab-yZ_VZChDq6I6l8Ez4dn8wT6TE0K-xJlCOOdolD5Hi8Em0d4h6Lh12i8qSIBNQdM-4C5GUicmlgpAfNL1N5Tkxup9l0rOqi4P07xNg0RK2TQK0KBsT5saP_h6D2n0kgSVWq9dNP7wvF-mhzUUT_WiNJUOUdohr0WolAVs0WRc5UFfszxOfrr6rjKfBidphiHSgwPsiyrFlsKdOg-MkbNkAwEJMqV6HDBBrBubUSSjwAyUmYW5kxsugZH_xlOX93nT5ekDngpGMhjn5jazgEGvGX8UPB1DNPHVnXkxdlllJsxTBeOx5mb9pnCHdW4yVvyrFDcw; locale=en-us; sgID=35de5a94-6edb-42d0-9e3b-56670b75b1d2; _fbp=fb.1.1555385325719.826792837; __utma=107333120.552915472.1555308528.1555385435.1555385435.1; __utmc=107333120; __utmz=107333120.1555385435.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmb=107333120.1.10.1555385435; _pk_id.1.fd33=aacb2cf6dfad69fb.1555308531.3.1555385470.1555381124.; _pk_ref.1.3432=%5B%22%22%2C%22%22%2C1555385729%2C%22https%3A%2F%2Fwww.similarweb.com%2F%22%5D; _pk_ses.1.3432=*; intercom-session-e74067abd037cecbecb0662854f02aee12139f95=TGl2ZXZNZ1RoZEtwdFo0ak5oVTBLbXpJcCtkWmk3elBPOVVEUHhWYVVqanJvcWFTNEcreEhGRmtlcGZpbTJaKy0tWTNSMjA1SjdDbWhDWXhuWHdGUVFUdz09--03ec3f47d033fde454357948f3bcd3d8913a94f2; _pk_id.1.3432=aacb2cf6dfad69fb.1555385325.1.1555385854.1555385723.; mp_7ccb86f5c2939026a4b5de83b5971ed9_mixpanel=%7B%22distinct_id%22%3A%20%225351221%22%2C%22%24device_id%22%3A%20%2216a1f9cc408835-09e647ee848d28-366e7e04-13c680-16a1f9cc409b2b%22%2C%22sgId%22%3A%20%2235de5a94-6edb-42d0-9e3b-56670b75b1d2%22%2C%22Site%20Type%22%3A%20%22Corp%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Dv7rGJr4srHmbnS20VVl9q00najXQX_0jxX9_svQt1VJsYKv2XHYk2GNscuQj-udT%26wd%3D%26eqid%3Df51c1b87000102ab000000045cb41fe9%22%2C%22%24initial_referring_domain%22%3A%20%22www.baidu.com%22%2C%22session%20ID%22%3A%20%227847835d-724b-4f98-99ed-e3aaa7756ccd%22%2C%22section%22%3A%20%22websiteAnalysis%22%2C%22last%20event%20time%22%3A%201555385470341%2C%22%24search_engine%22%3A%20%22google%22%2C%22sub_section%22%3A%20%22overview%22%2C%22sub_sub_section%22%3A%20%22websitePerformance%22%2C%22page_id%22%3A%20%22analysis.overview.performance.title%22%2C%22%24user_id%22%3A%20%225351221%22%2C%22site_type%22%3A%20%22Pro%22%2C%22session_id%22%3A%20%224b750b2e-814d-4acb-a477-79cedecd24ee%22%2C%22url%22%3A%20%22https%3A%2F%2Fpro.similarweb.com%2F%23%2Fwebsite%2Fworldwide-overview%2Fotakumode.com%2F*%2F999%2F3m%3FwebSource%3DTotal%22%2C%22is_sw_user%22%3A%20false%2C%22language%22%3A%20%22en-us%22%2C%22country%22%3A%20999%2C%22date_range%22%3A%20%223m%22%2C%22entity_id%22%3A%20%22otakumode.com%22%2C%22entity_name%22%3A%20%22otakumode.com%22%2C%22web_source%22%3A%20%22TOTAL%22%2C%22domain_type%22%3A%20%22WITH_SUBDOMAINS%22%2C%22main_category%22%3A%20%22Arts%20and%20Entertainment%22%2C%22custom_category_id%22%3A%20null%2C%22subscription_id%22%3A%20%222%22%2C%22base_product%22%3A%20%22Free%20Pro%202018%22%2C%22user_id%22%3A%205351221%2C%22account_id%22%3A%2010000001%2C%22email%22%3A%20%22crystal.zhou%40star-gazer.co.jp%22%2C%22last_event_time%22%3A%201555385853629%7D'
        }
    
    # 处理数据函数
    def handleData(self):
        resValues = json.dumps(self.data, ensure_ascii=False)
        httpPatStr = 'https://(.*?)/[\s\S]*'
        
        # 优先处理alexae数据
        for sourceArr in self.data:
            for content in sourceArr:
                httpPat = re.compile(httpPatStr)
                results = httpPat.findall(content)
                if len(results):
                    temp = self.getAlexaeData(results[0])
                    if len(temp) > 0:
                        subStr = '"%s", "%s"'%(content, temp)
                        pat = '"%s", "[\s\S]*?"'%content
                        resultPat = re.compile(pat)
                        resValues = resultPat.sub(subStr, resValues)
                    else:
                        temp = self.getSimilarwebData(results[0])
                        if len(temp) > 0:
                            subStr = '"%s", "%s"'%(content, temp)
                            pat = '"%s", "[\s\S]*?"'%content
                            resultPat = re.compile(pat)
                            resValues = resultPat.sub(subStr, resValues)
                        else:
                            subStr = '"%s", "%s"'%(content, '数据未公开')
                            pat = '"%s", "[\s\S]*?"'%content
                            resultPat = re.compile(pat)
                            resValues = resultPat.sub(subStr, resValues)

        resData = json.loads(resValues)
        return resData


    # 爬取alexae数据
    def getAlexaeData(self, param):
        url = 'https://alexa.chinaz.com/Handlers/GetAlexaPvNumHandler.ashx'
        pat = 'www.'
        pattern = re.compile(pat)
        param = pattern.sub('', param)
        fromdata = {
            'url': param
        }
        
        res = requests.post(url, headers=self.header, data=fromdata).text
        pat = r'data:{PvNum:"(.*?)"}}'
        patten = re.compile(pat, re.I)
        resData = patten.findall(res)
        if len(resData) > 0:
            resDataInt = int(resData[-1])*30
            resDataStr = str(resDataInt)
            return resDataStr
        else:
            return ''
            
    # 爬取similarweb数据
    def getSimilarwebData(self, param):
        year = datetime.datetime.now().year
        moth = datetime.datetime.now().month

        if moth > 1:
            toDateStr = str(year)+'|0'+str(moth-1)+'|20'
            starDateStr = str(year)+'|0'+str(moth-1)+'|01'
        else:
            toDateStr = str(year-1)+'|12|20'
            starDateStr = str(year-1)+'|12|01'

        toDate = urllib.parse.quote(toDateStr)
        starDate = urllib.parse.quote(starDateStr)

        pat = 'www.'
        pattern = re.compile(pat)
        param = pattern.sub('', param)

        subUrl = 'keys='+param+'&from='+starDate+'&to='+toDate
        url = 'https://pro.similarweb.com/widgetApi/WebsiteOverview/EngagementVisits/Graph?country=999&includeSubDomains=true&webSource=Total&'
        tolelUrl = url + subUrl

        res = requests.get(tolelUrl, headers=self.header).text
        pat = r'{"Key":"[\s\S]*","Value":(.*?)}'
        pattern = re.compile(pat)
        resResult = pattern.findall(res)

        if len(resResult) > 0:
            subRes = resResult[0].split('.')
            return subRes[0]
        else:
            return ''