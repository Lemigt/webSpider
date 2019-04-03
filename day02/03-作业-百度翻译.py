import re
import requests
import json

def translate(word):

    url = 'https://fanyi.baidu.com/transapi'

    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
            'Cookie':'BAIDUID=FF3087365F1193B2F9D91C4E3438C87E:FG=1; BIDUPSID=FF3087365F1193B2F9D91C4E3438C87E; PSTM=1551072518; BDUSS=5JSH5VVmFDeH5qejFMczZub2lwcDZJRFBMOFVxcDVCVjdqTTRpSzJHRkpYTHhjQVFBQUFBJCQAAAAAAAAAAAEAAACpnQVE0ru1p8fgycDT6s601bQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEnPlFxJz5RcMk; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=26523_1449_21097_28774_28720_28557_28697_28584_28640_26350_28518; PSINO=7; delPer=0; locale=zh; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1554199044,1554199119; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1554199119',
        }

    data = {
        'query': word,
        'source':'txt',
    }

    res = requests.post(url, headers=headers, data=data).json()

    # print(res)
    trans_result = res.get('result')

    json_data = json.loads(trans_result)

    mean = json_data.get('content')[0].get('mean')[0].get('cont')


    # print(mean)
    for k in mean:
        print(k)






# 数据是通过Ajax请求再渲染出来的，没法直接在标签里找
# def translate(word):
#     url = 'https://fanyi.baidu.com/?aldtype=16047#en/zh/' + word
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
#
#     }
#     res = requests.get(url, headers=headers)
#     res.encoding = 'utf-8'
#     print(res.text)
#     content = res.text
#     tranCom = re.compile('<span left-pos=.*?>(.*?)</span>')
#
#     result = re.findall(tranCom, content)
#     print(result)


# 尝试使用selenium,失败
# from selenium import webdriver
# import time
# def translate(word):
#     url = 'https://fanyi.baidu.com/?aldtype=16047#en/zh/' + word
#
#     browser = webdriver.Chrome()
#
#     browser.get(url)
#     content = browser.page_source
#     # print(content)
#     # time.sleep(5)
#
#
#     # print(content)
#     tranCom = re.compile('<p class="ordinary-output target-output clearfix">(.*?)</p>')
#     # '''<p class="ordinary-output target-output clearfix"> <span left-pos="0|3" right-pos="0|3" space="" class="">Yes</span> </p>'''
#     result = re.findall(tranCom, content)
#     print(result)
#     browser.close()



if __name__ == '__main__':
    while True:
        word = input('请输入英文：')
        translate(word)