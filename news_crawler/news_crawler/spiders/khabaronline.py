from time import sleep

from scrapy import Spider
from selenium import webdriver
from scrapy.selector import Selector
from scrapy.http import Request
from selenium.common.exceptions import NoSuchElementException

class KhabaronlineSpider(Spider):
    name = 'khabaronline'
    allowed_domains = ['khabaronline.ir']
    start_urls = ['http://khabaronline.ir/']

    def parse(self, response):
        # self.driver = webdriver.Chrome('/home/ariana/chromedriver')
        # self.driver.get('https://khabaronline.ir')

        # sel = Selector(text=self.driver.page_source)
        categories = response.xpath('//*[@id="menu"]/div/ul/li/a/@href').extract()
        string = 'https://www.khabaronline.ir/archive?tp='
        for num in range(1,14):
            url = string + str(num)
            yield Request(url, callback=self.parse_category)

    def parse_category(self, response):

        news_links = response.xpath('//*[@class="desc"]/h3/a/@href').extract()
        for link in news_links:
            url = 'http://khabaronline.ir' + link
            yield Request(url, callback=self.parse_news)
        next_page_url = response.xpath('//*[@class="page-link"]/@href').extract()[-1]
        next_page_url = 'http://khabaronline.ir' + next_page_url
        yield Request(next_page_url, callback=self.parse_category)

    def parse_news(self, response):
        pass

