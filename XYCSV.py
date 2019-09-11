import csv
import re


# /Users/yostar/Desktop/level_main_03-08_BEG.txt

if __name__ == "__main__":
    patName = r'[name="(.*?)"][\s\S]*?'
    patContent = '[name="[\s\S]*?"](.*?)'
    pattentName = re.compile(patName)
    pattentContent = re.compile(patContent)
    # with open('/Users/yostar/Desktop/level_main_03-08_BEG.txt', 'r') as f:
    #     lines = f.readlines()
    #     for line in lines:
    #         print(line)
    #         resultName = pattentName.findall(line)
    #         print(resultName)
    source = '[name="整合运动成员"]   我......'
    resultName = pattentName.findall(source)
    result 
    print(source.split())