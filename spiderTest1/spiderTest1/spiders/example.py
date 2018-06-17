# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    #allowed_domains = ['example.com']
    start_urls = ['http://httpbin.org/get']

    def start_requests(self):
        yield scrapy.Request("http://httpbin.org/get",callback=self.parse)

    def parse(self, response):
        print (response.body)
