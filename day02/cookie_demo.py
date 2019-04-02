import urllib.request
from http import cookiejar

cookies = cookiejar.CookieJar()

cookie_hander = urllib.request.HTTPCookieProcessor(cookies)



opener = urllib.request.build_opener(cookie_hander)


headers = {

}
url = ''

req = urllib.request.Request(url, headers=headers)

