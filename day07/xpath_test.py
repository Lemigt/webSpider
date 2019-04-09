import requests
from lxml import etree
from selenium import webdriver

browser = webdriver.Chrome()

browser.get('https://www.zhipin.com/job_detail/9040332d9b7bca791X153N24GVQ~.html?ka=search_list_3_blank&lid=1qK1eUh0oDG.search')

source = browser.page_source

html = etree.HTML(source)

# links = html.xpath("//*[@class='job-list']/ul/li//div[@class='company-text']//a")
# links = html.xpath("//*[@class='job-list']/ul/li//div[@class='info-primary']//a")
name = html.xpath("//*[@id='main']/div[1]/div/div/div[2]/div[2]/h1/text()")[0]
salary = html.xpath("//*[@id='main']/div[1]/div/div/div[2]/div[2]/span/text()")[0].strip()
cname = html.xpath("//*[@id='main']/div[3]/div/div[1]/div[2]/div/a[2]/text()")[0].replace('\n', '').strip()
info = html.xpath("//*[@id='main']/div[1]/div/div/div[2]/p/text()")
descs = html.xpath("//*[@id='main']/div[3]/div/div[2]/div[2]/div[1]/div/text()")
desc = "\n".join(descs).strip().replace('\n', '')

print(desc)

# for link in links:
#     print(link.xpath('.//@href')[0])
#     print('----------------')

browser.close()