# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
import re
from scrapy.loader import ItemLoader
from ..items import SpiderDoubanItem



class DoubanSpider(scrapy.Spider):
    name = 'douban'
    # allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
    	detail_list = response.xpath("//div[@class='hd']/a/@href").extract()	#提取电影详细页面信息
    	for i in detail_list:
    		yield Request(i, callback=self.details_parse)
    		return 

    def getInfoByRe(self,instr,restr):
    	m = re.search(restr, instr, re.S) 	#re.S 把/n也当作字符串来匹配
    	if m:
    		info = m.groups()[0]
    	else:
    		info = ""
    	return info

    def details_parse(self, response):
    	item = ItemLoader(item=SpiderDoubanItem(), response=response)
    	item.add_xpath('director', "//a[@rel='v:directedBy']/text()")	#导演
    	item.add_xpath('starring', "//a[@rel='v:starring']/text()")		#主演
    	item.add_xpath('mvtype', "//span[@property='v:genre']/text()")		#电影类型
    	showplace = self.getInfoByRe(response.text, r'制片国家/地区:</span>(.+?)<br/>')		#制作国家
    	item.add_value('showplace',showplace)
    	lan = self.getInfoByRe(response.text, r'语言:</span>(.+?)<br/>')			#语言
    	item.add_value('lan',lan)
    	mvnames = self.getInfoByRe(response.text, r'又名:</span>(.+?)<br/>')		#电影别名
    	item.add_value('mvnames',mvnames)
    	item.add_xpath('mvshowtime', "//span[@property='v:initialReleaseDate']/text()")		#电影上映时间
    	item.add_xpath('mvtimelen', "//span[@property='v:runtime']/text()")		#电影类型
    	return item.load_item()



