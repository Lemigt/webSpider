from selenium import webdriver

browser = webdriver.Chrome()

browser.get('https://www.zhipin.com/c101280600-p100109/?ka=search_100109')

next_btn = browser.find_elements_by_xpath()