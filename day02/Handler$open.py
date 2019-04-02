import urllib.request

http = urllib.request.HTTPHandler()

# 创建打开器对象
opener = urllib.request.build_opener(http)

# 打开url
# response = opener.open("http://www.baidu.com/")
# print(response)

# 创建全局打开器
urllib.request.install_opener(opener)

response = urllib.request.urlopen("http://www.ifeng.com/")
print(response.read().decode())




