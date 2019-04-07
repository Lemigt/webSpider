import pymysql
from lxml import etree
import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36"
}

BASE_URL = 'https://hr.tencent.com/'



def get_detail(Durl_list):
    tx_hr = []
    for Durl in Durl_list:
        one_detail = {}
        duty = ''
        require = ''
        workName = ''
        # site = ''
        # workType = ''
        # needNum = ''
        res = requests.get(Durl, headers=HEADERS)
        html = etree.HTML(res.content.decode('utf-8'))
        base_info_list = html.xpath('//tr[@class="c bottomline"]')
        detail_info_list = html.xpath('//td')

        workName += detail_info_list[0].xpath('.//text()')[0]

        for base_info in base_info_list:
            site = base_info[0].xpath('.//text()')[1]
            try:
                workType = base_info[1].xpath('.//text()')[1]
            except:
                workType = '无类别'
            needNum = base_info[2].xpath('.//text()')[1].replace('人', '')
        # print(site, workType, needNum)

        for duty_info in detail_info_list[4].xpath('.//text()')[3::]:
            duty += duty_info.strip('\r').strip(' ')

        for require_info in detail_info_list[5].xpath('.//text()')[3::]:
            require += require_info.strip('\r').strip(' ')

        one_detail['duty'] = duty
        one_detail['require'] = require
        one_detail['site'] = site
        one_detail['workType'] = workType
        if needNum == '':
            one_detail['needNum'] = 1
        one_detail['needNum'] = int(needNum)
        one_detail['workName'] = workName
        tx_hr.append(one_detail)
    return tx_hr


def get_detail_url(url):
    Durl_list = []
    res = requests.get(url, headers=HEADERS)
    html = etree.HTML(res.content.decode('utf-8'))
    e_as = html.xpath('//a[@target="_blank"]')[2:12]

    for e_a in e_as:
        href = BASE_URL + e_a.xpath('.//@href')[0]
        Durl_list.append(href)

    return Durl_list


def get_tx_hr():
    for i in range(11):
        url = 'https://hr.tencent.com/position.php?&start={}#a'.format(i*10)
        Durl_list = get_detail_url(url)
        tx_hr = get_detail(Durl_list)
        print(tx_hr)
        Save_in_mysql(tx_hr)


def Save_in_mysql(info_list):
    db = pymysql.connect(host='localhost', user='root', password='151934', port=3306, db='ws0405')
    for info in info_list:
        cursor = db.cursor()
        sql = 'INSERT INTO txjob(workName, workType, site, needNum, duty, requirement) values(%s, %s, %s, %s, %s, %s)'
        cursor.execute(sql, (info['workName'],info['workType'], info['site'], info['needNum'], info['duty'], info['require']))
        db.commit()
    db.close()






if __name__ == '__main__':
    # url = 'https://hr.tencent.com/position.php?&start=10#a'
    # Durl_list = get_detail_url(url)
    # print(Durl_list)
    # tx_hr = get_detail(Durl_list)
    # Save_in_mysql(tx_hr)
    get_tx_hr()
    # url = ['https://hr.tencent.com/position_detail.php?id=49108&keywords=&tid=0&lid=0']
    # test(url)
    # get_detail(url)
    # url = ['https://hr.tencent.com/position_detail.php?id=49155&keywords=&tid=0&lid=0',
    #        'https://hr.tencent.com/position_detail.php?id=49151&keywords=&tid=0&lid=0']
    # get_detail(url)

