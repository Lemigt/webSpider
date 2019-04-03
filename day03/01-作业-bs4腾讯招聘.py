from selenium import webdriver
from bs4 import BeautifulSoup
import pymysql

allData = []


def getPage(url):
    browser = webdriver.Chrome()

    browser.get(url)

    html = browser.page_source

    soup = BeautifulSoup(html, 'lxml')

    data_list = soup.select('tr')

    global allData
    for i in range(1,len(data_list)-2):

        inf_list = data_list[i].select('td')
        one_data = []

        for inf in inf_list:
            one_data.append(inf.text)

        allData.append(one_data)


def insert_mysql(allData):
    db = pymysql.connect(host='localhost', user='root', password='151934', port=3306, db='webspider')

    print('*'*40)
    for i in range(len(allData)):
        cursor = db.cursor()
        id = i+1
        name = allData[i][0]
        jobType = allData[i][1]
        num = allData[i][2]
        site = allData[i][3]
        date = allData[i][4]
        sql = 'INSERT INTO txjob(id, name, type, num, site, date) values(%s, %s, %s, %s, %s, %s)'
        cursor.execute(sql,(id, name, jobType, num, site, date))
        db.commit()
    db.close()


if __name__ == '__main__':
    for i in range(1,11):
        url = 'https://hr.tencent.com/position.php?&start=' + str(i*10) + '#a'
        getPage(url)
    insert_mysql(allData)