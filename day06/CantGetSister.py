import csv
import threading
from queue import Queue

import requests
from lxml import etree


class GetJoke(threading.Thread):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    }

    def __init__(self, page_queue, joke_queue, *args, **kwargs):
        super(GetJoke, self).__init__(*args, **kwargs)
        self.base_url = 'http://budejie.com'
        self.page_queue = page_queue
        self.joke_queue = joke_queue

    def run(self):
        while True:
            if self.page_queue.empty():
                break
            url = self.page_queue.get()
            res = requests.get(url, headers=self.headers)
            text = res.text
            html = etree.HTML(text)
            descs = html.xpath("//div[@class='j-r-list-c-desc']")
            for desc in descs:
                jokes = desc.xpath('.//text()')
                joke = "\n".join(jokes).strip().replace('\n', '')
                link = self.base_url+desc.xpath('.//a/@href')[0]
                self.joke_queue.put((joke, link))
            print('*'*20+"第%s页下载完成"%url.split('/')[-1]+'*'*20)


class Writer(threading.Thread):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    }

    def __init__(self, joke_queue, writer, gLock, *args, **kwargs):
        super(Writer, self).__init__(*args, **kwargs)
        self.joke_queue = joke_queue
        self.writer = writer
        self.lock = gLock

    def run(self):
        while True:
            try:
                joke,link = self.joke_queue.get(timeout=40)
                self.lock.acquire()
                self.writer.writerow((joke, link))
                self.lock.release()
                print('保存一条')
            except:
                break


def main():
    page_queue = Queue(10)
    joke_queue = Queue(500)
    gLock = threading.Lock()
    fp = open('bsbdj.csv', 'a', newline='', encoding='utf-8')
    writer = csv.writer(fp)
    writer.writerow(('content', 'link'))

    for i in range(1,11):
        url = 'http://www.budejie.com/text/%d' %i
        page_queue.put(url)

    for i in range(5):
        t = GetJoke(page_queue, joke_queue)
        t.start()

    for i in range(5):
        t = Writer(joke_queue, writer, gLock)
        t.start()


if __name__ == '__main__':
    main()









