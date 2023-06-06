#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/6/4 12:40
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : example.py
# @Version  : Python 3.10.10
# @Project  : scrapy
# @Software : PyCharm



import scrapy

class ExampleSpider(scrapy.Spider):
    name = 'example'
    #allowed_domains = ['example.com']
    start_urls = ['http://httpbin.org/get']

    def start_requests(self):
        yield scrapy.Request("http://httpbin.org/get",callback=self.parse)

    def parse(self,response):
        print (response.body)