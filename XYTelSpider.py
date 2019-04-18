import requests
import re
import xlsxwriter

header = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

url = "http://changyongdianhuahaoma.51240.com/"
res = requests.get(url, headers=header).text

pat1 = '<tr bgcolor="#EFF7F0">[\s\S]*?<td>(.*?)</td>[\s\S]*?<td>[\s\S]*?</td>[\s\S]*?</tr>'
pat2 = '<tr bgcolor="#EFF7F0">[\s\S]*?<td>[\s\S]*?</td>[\s\S]*?<td>(.*?)</td>[\s\S]*?</tr>'

pattern1 = re.compile(pat1)
pattern2 = re.compile(pat2)

data1 = pattern1.findall(res)
data2 = pattern2.findall(res)

resultList = []

# 创建表格
workBook = xlsxwriter.Workbook('Telphone.xlsx')
workSheet = workBook.add_worksheet()

for i in range(0, len(data1)):
    resultList.append(data1[i] + data2[i])

    # 写入数据
    workSheet.write('A'+str(i+1), data1[i])
    workSheet.write('B'+str(i+1), data2[i])

print(resultList)
workBook.close()