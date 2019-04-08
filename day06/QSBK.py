import csv
from queue import Queue
import threading

import requests
from lxml import etree


class Producer(threading.Thread):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    }

    def __init__(self, page_queue, joke_queue, *args, **kwargs):
        super(Producer, self).__init__(*args, **kwargs)
        self.base_url = 'https://www.qiushibaike.com'
        self.page_queue = page_queue
        self.joke_queue = joke_queue

    def run(self):
        while True:
            if self.page_queue.empty():
                break
            url = self.page_queue.get()
            res = requests.get(url,headers=self.headers)
            text = res.text
            html = etree.HTML(text)
            descs = html.xpath("//div[@class='article block untagged mb15 typs_hot']")
            for desc in descs:
                jokes = desc[1].xpath('.//text()')
                joke = "\n".join(jokes).strip().replace('\n', '')
                href = self.base_url + desc.xpath(".//a[@class='contentHerf']/@href")[0]
                self.joke_queue.put((joke, href))
            print('*' * 20 + "第%s页下载完成" % url.split('/')[-1] + '*' * 20)


class Writer(threading.Thread):

    def __init__(self, joke_queue, gLock, fp, *args, **kwargs):
        super(Writer, self).__init__(*args, **kwargs)
        self.joke_queue = joke_queue
        self.lock = gLock
        self.fp = fp

    def run(self):
        while True:
            try:
                joke,link = self.joke_queue.get(timeout=20)
                self.lock.acquire()
                self.fp.write(joke)
                self.fp.write('\n')
                self.lock.release()
                print('保存一条')
            except:
                break


def main():
    page_queue = Queue(20)
    joke_queue = Queue(500)
    gLock = threading.Lock()
    fp =  open('qsbk.txt', 'a'  ,encoding='utf-8')

    for i in range(1,11):
        url = 'https://www.qiushibaike.com/text/%s'%i
        page_queue.put(url)


    for i in range(5):
        t = Producer(page_queue, joke_queue)
        t.start()

    for i in range(5):
        t = Writer(joke_queue, gLock, fp)
        t.start()


if __name__ == '__main__':
    main()

