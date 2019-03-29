from lxml import etree

html = etree.HTML(text)

result = etree.tostring(html)

print(type(html))