import re

# b = "17#$E85张三678098777__*&&^^^%#@sdfafds7"

# pat1 = "[\u4e00-\u9fa5][\u4e00-\u9fa5]"
# pat2 = "[a-z][a-z]"
# pat3 = "[0-9][0-9]"

# print(re.search(pat1, b))
# print(re.search(pat2, b))
# print(re.search(pat3, b))

b = "17621065687dsa3343q346564"
pat2 = "1[3578]\d{9}"
pat1 = "\d{3}=\d{7}"
print(re.search(pat2, b))
