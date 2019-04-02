import json
import urllib.request
import urllib.parse

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}


url = 'https://job.alibaba.com/zhaopin/socialPositionList/doList.json'


# 学历、部门、岗位要求、工作经验
datastr = ''


def get_json(page):
    parms = {
        'pageSize': '10',
        't': '0.5571018868891935',
        'pageIndex': page,
    }

    data = urllib.parse.urlencode(parms).encode()
    req = urllib.request.Request(url, headers=headers, data=data)
    response = urllib.request.urlopen(req)
    content = response.read().decode()
    print(type(content))
    jsondata = json.loads(content)
    data_list = jsondata.get('returnValue').get('datas')


    for data in data_list:
        global datastr
        datastr += '学历：'
        datastr += data.get('degree')
        datastr += '\n'
        datastr += '部门：'
        datastr += data.get('departmentName')
        datastr += '\n'
        datastr += '岗位要求：'
        datastr += data.get('requirement')
        datastr += '\n'
        datastr += '工作经验：'
        datastr += data.get('workExperience')
        datastr += '\n'
        datastr += '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        datastr += '\n'



if __name__ == '__main__':
    # print(datastr)
    for i in range(1,11):
        get_json(i)
    print(datastr)
    with open("阿里招聘.txt", "a+", encoding='utf-8') as f:
        f.write(datastr)




