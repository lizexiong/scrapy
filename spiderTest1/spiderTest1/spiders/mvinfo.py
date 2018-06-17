# -*- coding: utf-8 -*-
import scrapy


class MvinfoSpider(scrapy.Spider):
    name = 'mvinfo'
    #allowed_domains = ['example.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        print ("*" * 50 )
        print (response.url)
        print (response.body)
