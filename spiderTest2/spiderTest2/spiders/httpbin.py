# -*- coding: utf-8 -*-
import scrapy


class HttpbinSpider(scrapy.Spider):
    name = 'httpbin'
    #allowed_domains = ['http://httpbin.org']
    start_urls = ['http://httpbin.org/get']

    def parse(self, response):
        pass
