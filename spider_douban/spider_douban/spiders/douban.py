# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    # allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
    	detail_list = response.xpath("//div[@class='hd']/a/@href").extract()	#提取电影详细页面信息
    	for i in detail_list:
    		yield Request(i, callback=self.details_parse)

    def details_parse(self, response):
    	print (response.url)
