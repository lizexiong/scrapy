# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request			#发起下一次请求

class MvinfoSpider(scrapy.Spider):	
    name = 'mvinfo'
    #allowed_domains = ['example.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        print ("*" * 50 )
        movie_list = response.xpath("//div[@class='hd']/a")
        baseurl = 'https://movie.douban.com/top250'
        for i in movie_list:
        	print (i.xpath("span[1]/text()").extract(),i.xpath("@href").extract())

        nextpage = response.xpath("//span[@class='next']/a/@href").extract()
        if nextpage:
        	nexturl = baseurl + nextpage[0]
        	print (nexturl)
        	yield Request(nexturl, callback=self.parse)		#yield解析下一页
