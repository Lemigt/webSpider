import requests
from lxml import etree

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    }

url = 'https://www.dytt8.net/html/gndy/dyzz/20190404/58430.html'


res = requests.get(url, headers=headers)

html = etree.HTML(res.content)


download_url = html.xpath('//div[@id="Zoom"]')[0][2][0]

# for i in download_url:
#     print(i.xpath('.//text()'))


contents = download_url.xpath('.//text()')[1:-3]

# url = html.xpath('//div[@id="Zoom"]//table/tbody/tr/td/a')[0]

detail = ''
for c in contents:

    detail += c

# print(url.xpath('@.'))

# print(detail)