from bs4 import BeautifulSoup

soup = BeautifulSoup(html, "lxml")

soup2 = BeautifulSoup(open(""))

soup.prettify()