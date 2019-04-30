# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from day08.DYTT.DYTT.items import DyttItem


class DyttSpider(CrawlSpider):
    name = 'dytt'
    allowed_domains = ["dytt8.net"]
    start_urls = ['https://www.dytt8.net/']

    rules = (
        Rule(LinkExtractor(allow=r'.+/html/gndy/dyzz/.+\.html'), callback='parse_detail', follow=True),
    )

    def parse_detail(self, response):

        name = response.xpath('//*[@id="header"]/div/div[3]/div[3]/div[2]/div[2]/div[1]/h1/font/text()').get()

        if name != '>' and name:
            item = DyttItem(name=name)
            print('name:' + name )
            return item
