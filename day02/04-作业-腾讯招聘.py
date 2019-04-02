import re
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

allData = ''
def getPage(url):
    browser = webdriver.Chrome()

    browser.get(url)

    html = browser.page_source

    jobNameCom = re.compile('<a target="_blank" href="position_detail.php.*?>(.*?)</a>')
    lotCom = re.compile('<td>(.*?)</td>')


    jobNameList = re.findall(jobNameCom, html)
    otherList = re.findall(lotCom, html)[4::]


    # print(otherList)
    global allData
    for i in range(len(jobNameList)):
        allData += '职位名称:' + jobNameList[i] + '\n'

        allData += '职位类别' + otherList[i*4] + '\n'
        allData += '人数' + otherList[i * 4 + 1] + '\n'
        allData += '地点' + otherList[i * 4 + 2] + '\n'
        allData += '发布时间' + otherList[i * 4 + 3] + '\n'
        allData += '-----------------------------------------' + '\n'


    browser.close()


if __name__ == '__main__':
    url = 'https://hr.tencent.com/position.php?&start=0#a'
    getPage(url)


    for i in range(1,11):
        url = 'https://hr.tencent.com/position.php?&start=' + str(i*10) + '#a'
        getPage(url)

    with open('腾讯招聘.txt', 'a+', encoding='utf-8') as fp:
        fp.write(allData)

    print(allData)
