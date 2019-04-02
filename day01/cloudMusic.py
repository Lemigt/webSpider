import urllib.request
import urllib.parse
import json

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}


url = 'https://music.163.com/weapi/v1/resource/comments/R_SO_4_441491828?csrf_token=a73c017f5a04db410efa21d544504a0f'



body = {
    'params': '4Ovd+1eYNt3LrpmwT8Kw1dq7ENR5NAoEyl7X1sXg+sFR0s8UdfLMvzM6RwkzvXQ1ro/PVtxt1UHYcT9f1UZw4NROS7rU6fc7MaNTpi9YuzeAuaZe4uxOIvcoWNjNbzIBDtmyqS7laQmtgFBtfD0K43EUmDCrzC7xx16/s/6ZwgNdZGm+kG4XQ8wyguSw8Oq3hY8Fm2xkRx0BjqffLOoZzt2kfTPdDL4iawtZk70iklo=',
    'encSecKey': '75d18b3a4af3812b68232691536deebc064d85ca4f6056aa2f25e5fe81123b5fd6a6f302e10204dd70f500d54cabcf631007a72ac865ba1a28b264bb50d1216a0de9e78f393967dde61e9fb5f91c91b34a57159e759081ed3946d66ce2500a450e60ed8463b41c6cb635f40b9bab738a8ec6abad4a178bfb656add0a169988c8'
}

bodydata = urllib.parse.urlencode(body).encode()

req = urllib.request.Request(url, headers=headers, data=bodydata)

response = urllib.request.urlopen(req)

content = response.read().decode()
print(content)
json_data = json.loads(content)

comments = json_data.get('comments')
for comment in comments:
    print(comment.get('content'))
    print('-------------------------------')



