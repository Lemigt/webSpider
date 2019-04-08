import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
}

url = 'https://www.qiushibaike.com/text/'

res = requests.get(url, headers=headers)

text = res.text

html = etree.HTML(text)


descs = html.xpath("//div[@class='article block untagged mb15 typs_hot']")

for desc in descs:
    jokes = desc[1].xpath('.//text()')
    joke = "\n".join(jokes).strip().replace('\n', '')
    href = desc.xpath(".//a[@class='contentHerf']/@href")[0]
    'https://www.qiushibaike.com/article/121687614'
    print(href)
    print('--------------------------------------')




# descs = html.xpath("//div[@class='j-r-list-c-desc']")
# # for desc in descs:
# #     jokes = desc.xpath(".//text()")
# #     joke = "\n".join(jokes).strip()