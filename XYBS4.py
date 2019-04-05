from bs4 import BeautifulSoup
import re

soup = BeautifulSoup(htm, "lxml")

# 格式化html
soup.prettify()

# 根据标签名获取标签信息 soup.标签名
soup.title

# 获取标签内容
soup.title.string

# 获取标签名
soup.title.name

# 获取标签内所有属性
soup.title.attrs

soup.descendants

# 根据字符串查找所有的a标签，返回一个结果集，里面装的是标签对象
data = soup.find_all("a")
for i in data:
    print(i.string)

# 根据正则表达式查找标签
data2 = soup.find_all(re.compile("^b", re.I))
for i in data2:
    print(i.string)

# 根据属性查找标签
data3 = soup.find_all(id='link2')

# 根据内容查找标签
data4 = soup.find_all(text="内容")
data5 = soup.find_all(text=["内容", "内容"])
data6 = soup.find_all(text=re.compile("DO", re.I))

# 通过标签名查找
data7 = soup.select("a")
# 通过类名查找
data8 = soup.select(".sister")
# 通过id查找
data9 = soup.select("#link2")
