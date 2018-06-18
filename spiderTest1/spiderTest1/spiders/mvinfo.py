# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request			#发起下一次请求
from ..items import Spidertest1Item		#导入items

class MvinfoSpider(scrapy.Spider):	
    name = 'mvinfo'
    #allowed_domains = ['example.com']
    start_urls = ['https://movie.douban.com/top250']
    fsave = open('douban.txt','w',encoding='utf-8')

    def parse(self, response):
        print ("*" * 50 )
        movie_list = response.xpath("//div[@class='hd']/a")
        baseurl = 'https://movie.douban.com/top250'
        for i in movie_list:
        	# print (i.xpath("span[1]/text()").extract(),i.xpath("@href").extract())
        	# self.fsave.writelines(i.xpath('span[1]/text()').extract(),)	#writelines()   参数必须是list/string/dict/tuple 等可迭代序列对象，且里面内容须是字符，
        	# self.fsave.write(" ")
        	# self.fsave.writelines(i.xpath('@href').extract())
        	# self.fsave.write("\n")
        	item = Spidertest1Item()
        	name = i.xpath("span[1]/text()").extract()
        	item['name'] = name
        	yield item

        nextpage = response.xpath("//span[@class='next']/a/@href").extract()
        if nextpage:
        	nexturl = baseurl + nextpage[0]
        	print (nexturl)
        	yield Request(nexturl, callback=self.parse)		#yield解析下一页
