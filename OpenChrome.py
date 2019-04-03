# -*- coding: utf-8 -*-

from selenium import webdriver

import time

import os
import re


# url = "https://www.hao123.com/"

# driver = webdriver.Chrome()

# driver.get(url)

# time.sleep(13)

# class Singleton(object):
#     __instance = None
#     __first_init = False

#     def __new__(cls, age, name):
#         if not cls.__instance:
#             cls.__instance = object.__new__(cls)
#         return cls.__instance
    
#     def __init__(self, age, name):
#         if not self.__first_init:
#             self.age = age
#             self.name = name
#             Singleton.__first_init = True

result = re.match('.', 'itcast,cnnn')
result.group()
print(result.group())