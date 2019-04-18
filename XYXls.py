# import xlsxwriter

# # 创建文件，并添加一个工作表
# workBook = xlsxwriter.Workbook('demo.xlsx')
# workSheet = workBook.add_worksheet()

# # 在指定位置写入数据
# workSheet.write('A1', '我要自学网')
# workSheet.write('A2', 'python教程')

# # 关闭表格文件
# workBook.close()

# from newspaper import Article

# url = 'https://news.sina.com.cn/gov/xlxw/2019-04-18/doc-ihvhiewr6864816.shtml'
# article = Article(url, language='zh') # Chinese
# article.download()
# article.parse()
# print(article.title)

import newspaper
 
# cnn_paper = newspaper.build('http://www.sina.com.cn/')
# 爬取cnn.com网站下的所有页面
# for article in cnn_paper.articles:
#     print(article.url)

# 爬取cnn.com网站下的所有子网站
# for category in cnn_paper.category_urls():
#     print(category)

url = 'https://news.sina.com.cn/gov/xlxw/2019-04-18/doc-ihvhiewr6864816.shtml'
article = newspaper.Article(url, language='zh') # Chinese

article.download()
article.parse()

print(article.title)
# print(article.html)
print(article.authors)
print(article.top_image)
print(article.movies)
print(article.summary)
print(article.text)