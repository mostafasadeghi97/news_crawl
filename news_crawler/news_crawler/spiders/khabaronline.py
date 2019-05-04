# -*- coding: utf-8 -*-
import scrapy


class KhabaronlineSpider(scrapy.Spider):
    name = 'khabaronline'
    allowed_domains = ['khabaronline.ir']
    start_urls = ['http://khabaronline.ir/']

    def parse(self, response):
        pass
