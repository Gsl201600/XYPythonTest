import requests
import re

# url = "https://www.twitch.tv/misty_chronexia"
# url = 'https://www.twitch.tv/thean1meman'

url = "https://gql.twitch.tv/gql"
page = "thean1meman"

header = {
    'Accept-Language': 'zh-CN',
    'Client-Id': 'kimne78kx3ncx6brgo4mv6wki5h1ko',
    'Content-Type': 'text/plain;charset=UTF-8',
    'Origin': 'https://www.twitch.tv',
    'Host': 'gql.twitch.tv',
    'Authorization': 'OAuth 5w33taccdoyegajwzngy95pg0qof9b',
    'X-Device-Id': '22199cccd5ba5388',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'
}
# datas = '[{"operationName":"ChannelRoot_Channel","variables":{"currentChannelLogin":"misty_chronexia","includeChanlets":true},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"c22e8985e3f77ceb6b460e8f8d252e7e1d77b6d1d4560aed5d18dcf1af5e93dd"}}},{"operationName":"ChannelPage__ChannelViewersCount","variables":{"login":"misty_chronexia"},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"3b5b233b59cc71f5ab273c74a30c46485fa52901d98d7850d024ad0669270184"}}},{"operationName":"Thud_Recommendations","variables":{"currentChannelLogin":"misty_chronexia"},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"0d12cafca0f97438f3fb14309f839ab52b9742ed06b7d41bd87a4226cfedadc1"}}},{"operationName":"ChannelPage_ChannelHeader","variables":{"login":"misty_chronexia"},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"6bc56115acedebbaddc681f839c9bf7c2578d05bf2ca50f823815257d2059745"}}},{"operationName":"SocialPanel_GetUser","variables":{"login":"misty_chronexia"},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"40d47bc46e7e2ee1cc6965b29391cb2c0e08ed904d54b5b1684ef7dc4d51f7ec"}}},{"operationName":"ChatRestrictions","variables":{"channelLogin":"misty_chronexia"},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"c951818670b7beab0f9332303f5a3824316e8d78423e6c6336f4235207b09e54"}}},{"operationName":"BlockedUsers","variables":{},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"8044e3fd61f8158a39e07b38f5d1a279d1fdb748faa9889fde046feae640f76b"}}},{"operationName":"MessageBuffer_Channel","variables":{"channelLogin":"misty_chronexia"},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"bfc959904f55b5003ae4674d4bea83ebdcd8867ad76e12f38957d433902d2fcc"}}},{"operationName":"SyncedSettingsReadableChatColors","variables":{},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"cd9c43ab3cb4c04515a879bbd618055aab18c6ac4081ed9de333945ca91247ba"}}},{"operationName":"UserEmotes","variables":{"withOwner":true},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"60dd19773b4682698b46bb9feda462ab60aa02c573050c6963daa097631d3283"}}},{"operationName":"Chat_UserData","variables":{},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"39985d1ff9324442a3a5df1be212e1bc4f358a31100e5025c4e61a07d7e70743"}}},{"operationName":"Chat_ChannelData","variables":{"channelLogin":"misty_chronexia"},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"fd55c6e29e8fcc0a438ef747f5f85f1e50e0da12426eb703bde43ebcf6310cc6"}}}]'

datas = '[{"operationName":"ChannelRoot_Channel","variables":{"currentChannelLogin":"misty_chronexia","includeChanlets":true},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"c22e8985e3f77ceb6b460e8f8d252e7e1d77b6d1d4560aed5d18dcf1af5e93dd"}}},{"operationName":"ChannelPage__ChannelViewersCount","variables":{"login":"misty_chronexia"},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"3b5b233b59cc71f5ab273c74a30c46485fa52901d98d7850d024ad0669270184"}}},{"operationName":"Thud_Recommendations","variables":{"currentChannelLogin":"misty_chronexia"},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"0d12cafca0f97438f3fb14309f839ab52b9742ed06b7d41bd87a4226cfedadc1"}}},{"operationName":"ChannelPage_ChannelHeader","variables":{"login":"misty_chronexia"},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"6bc56115acedebbaddc681f839c9bf7c2578d05bf2ca50f823815257d2059745"}}}]'
datas = datas.replace("misty_chronexia", page)

res = requests.post(url, headers=header, data=datas).content.decode()

pat = '"followers":{"totalCount":(.*?),'
pattern = re.compile(pat, re.I)
result = pattern.findall(res)

print(result)