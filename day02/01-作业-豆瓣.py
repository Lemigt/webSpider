import requests


# 作业1 : 分页获取豆瓣的数据（json数据）， 把电影图片存入本地，且图片名取电影名
# url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start="+ str(i * 20)+"&limit=20"



def getData(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    json_data = response.json()

    for j in json_data:
        # print(j)
        imgurl = j.get('cover_url')
        movieName = j.get('title')
        file_path = 'dbImg/'+ movieName + '.jpg'
        print(file_path)
        res = requests.get(imgurl)
        if res.status_code == 200:
            with open(file_path, 'wb') as f:
                f.write(res.content)


if __name__ == "__main__":

    for i in range(1, 3):
        url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=" + str(
        i * 20) + "&limit=20"
        getData(url)
    # getData('https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=20&limit=20')

