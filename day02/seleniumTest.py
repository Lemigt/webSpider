from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get('https://hr.tencent.com/position.php')

print(browser.page_source)