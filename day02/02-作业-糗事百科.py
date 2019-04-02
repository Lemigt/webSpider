import re
import time
import urllib.request

# 作业2: 爬取糗事百科文本页的所有段子,结果如 : xx说: xxxx
# https://www.qiushibaike.com/text/page/1/   # 1表示页码

# 正则表达式提示： 
#	# 获取一个评论
#   regCom = re.compile('<div class="author clearfix">(.*?)<span class="stats-vote"><i class="number">', re.S)
#	# 获取名称
#   nameCom = re.compile('<h2>(.*?)</h2>', re.S)
#	# 获取内容
#	contentCom = re.compile('<span>(.*?)</span>', re.S)

def getData(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    }
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)

    content = response.read().decode()

    nameCom = re.compile('<h2>(.*?)</h2>', re.S)
    contentCom = re.compile('<div class="content">.*?<span>(.*?)</span>', re.S)


    name_list = re.findall(nameCom,content)
    content_list = re.findall(contentCom, content)

    all_name = []

    for name in name_list:
        namex = name.replace('\n', '')
        # print(namex)
        all_name.append(namex)
        # print(all_name)

    all_content = []
    # print(all_name)
    for con in content_list:
        conx = con.replace('<br/>', '')
        conxs = conx.replace('\n', '')
        conxsi = conxs.replace('\x01','')
        # print(conx)
        all_content.append(conxsi)

    allData = ''
    for i in range(len(all_name)):
        # oneData ={}
        # oneData[all_name[i]] = all_content[i]
        # print(oneData)
        # allData.append(oneData)

        allData += all_name[i]
        allData += ':'
        allData += all_content[i]
        allData += '\n\n'
    print(allData)

    with open('糗事百科.txt', 'a+', encoding='utf-8') as f:
        f.write(allData)


if __name__ == "__main__":

    # for i in range(1,51):
    url = 'https://www.qiushibaike.com/text/page/1/'

    for i in range(1,11):
        url = 'https://www.qiushibaike.com/text/page/'+str(i)+'/'
        getData(url)



    # # 所有数据
    # allData = []
    # # [{name1:zh, content:22},{name1:zh, content:22},{name1:zh, content:22},{name1:zh, content:22},...]
    #
    # # 遍历每一页的数据
    # for i in range(1, 4):
    #     url = "https://www.qiushibaike.com/text/page/" + str(i) + "/"
    #     list1 = getData(url)
    #     allData.extend(list1)
    #
    #     time.sleep(0.5)
    #
    #
    # # 遍历allData 把数据显示
    # for dict1 in allData:
    #     print("%s 说： %s" % (dict1["name1"], dict1["content"]))




