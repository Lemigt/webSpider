from bs4 import BeautifulSoup
from selenium import webdriver


def one_page_detail(url):
    browser = webdriver.Chrome()

    browser.get(url)

    html = browser.page_source

    soup = BeautifulSoup(html, 'lxml')

    for i in soup.select('li'):
        if i.text:
            print(i.text)
    browser.close()


if __name__ == '__main__':
    url = 'https://hr.tencent.com/position_detail.php?id=49099&keywords=python&tid=0&lid=0'
    one_page_detail(url)