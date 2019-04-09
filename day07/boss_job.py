import time
from lxml import etree
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BossSpider(object):

    def __init__(self):
        self.begin_url = 'https://www.zhipin.com/c101280600-p100109/?page='
        self.base_url = 'https://www.zhipin.com'
        self.driver = webdriver.Chrome()
        self.informations = []

    def run(self):
        for i in range(1,11):
            url = self.begin_url+str(i)
            self.driver.get(url)

            source = self.driver.page_source

            self.parse_links(source)

            self.driver.close()


    def parse_links(self, source):
        html = etree.HTML(source)

        links = html.xpath("//*[@class='job-list']/ul/li//div[@class='info-primary']//a")
        for link in links:
            detail_url = self.base_url + link.xpath('.//@href')[0]
            print(detail_url)
            self.get_detail([detail_url])
            time.sleep(2)

    def get_detail(self, detail_url):
        self.driver.execute_script("window.open(%s)"%detail_url)  # 居然是要列表
        self.driver.switch_to_window(self.driver.window_handles[1])
        WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_all_elements_located
        )

        source = self.driver.page_source
        html = etree.HTML(source)
        self.parse_detail(html)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def parse_detail(self, html):
        name = html.xpath("//*[@id='main']/div[1]/div/div/div[2]/div[2]/h1/text()")[0]
        company_name = html.xpath("//*[@id='main']/div[3]/div/div[1]/div[2]/div/a[2]/text()")[0].replace('\n', '').strip()
        salary = html.xpath("//*[@id='main']/div[1]/div/div/div[2]/div[2]/span/text()")[0].strip()
        city = html.xpath("//*[@id='main']/div[1]/div/div/div[2]/p/text()")[0]
        work_year = html.xpath("//*[@id='main']/div[1]/div/div/div[2]/p/text()")[1]
        degrees = html.xpath("//*[@id='main']/div[1]/div/div/div[2]/p/text()")[2]
        descs = html.xpath("//*[@id='main']/div[3]/div/div[2]/div[2]/div[1]/div/text()")
        desc = "\n".join(descs).strip().replace('\n', '')
        information = {
            'name':name,
            'company_name':company_name,
            'salary':salary,
            'city':city,
            'work_year':work_year,
            'degrees':degrees,
            'desc':desc
        }
        self.informations.append(information)
        print(information)
        print('-'*40)


if __name__ == '__main__':
    boss = BossSpider()
    boss.run()