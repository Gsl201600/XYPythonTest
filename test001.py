import tushare
import time
import smtplib
from email.mime.text import MIMEText

def sendEmail(subject, content):
    msg_from = "2509552914@qq.com"
    pwd = "plgkeuiwpzbjdice"
    to = "1728871724@qq.com"

    msg = MIMEText(content)
    msg["Subject"] = subject
    msg["From"] = msg_from
    msg["To"] = to

    try:
        ss = smtplib.SMTP_SSL("smtp.qq.com", 465)
        ss.login(msg_from, pwd)
        ss.sendmail(msg_from, to, msg.as_string())
        print("发送成功")
    except expression as identifier:
        print("发送失败：", identifier)
    




# 获取股票数据
def getRealTimeData(share):
    dataNow = tushare.get_realtime_quotes(share.code)
    share.name = dataNow.loc[0][0]
    share.price = dataNow.loc[0][3]
    share.high = dataNow.loc[0][4]
    share.low = dataNow.loc[0][5]
    share.volumn = dataNow.loc[0][8]
    share.amount = dataNow.loc[0][9]
    share.openToday = dataNow.loc[0][1]
    share.pre_close = dataNow.loc[0][2]
    share.timee = dataNow.loc[0][30]
    share.describe = "股票名："+share.name+"当前价格："+str(share.price)
    print(share.describe)
    return share

# 股票类
class Share(object):
    def __init__(self, code, buy, sale):
        self.name = ""
        self.price = ""
        self.high = ""
        self.low = ""
        self.volumn = ""
        self.amount = ""
        self.openToday = ""
        self.pre_close = ""
        self.timee = ""
        self.describe = ""
        self.code = code
        self.buy = buy
        self.sale = sale

def main(shareList):
    for share in shareList:
        result = getRealTimeData(share)

        if result.price <= result.buy:
            print("达到买点")
            sendEmail("达到买点", result.describe)
        elif result.price>= result.sale:
            print("达到卖点")
            sendEmail("达到卖点", result.describe)
        else:
            print("别买也别卖")

while 1:
    share1 = Share("600106", "3.1", "3.2")
    share2 = Share("601988", "3.5", "3.8")
    share3 = Share("000591", "3.3", "3.5")
    list1 = [share1, share2, share3]
    print("________________")
    main(list1)
    time.sleep(50)