# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
import re

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
        director = response.xpath("//a[@rel='v:directedBy']/text()").extract()		#导演
        starring = response.xpath("//a[@rel='v:starring']/text()").extract()		#主演
        mvtype = response.xpath("//span[@rel='v:genre']/text()").extract()			#电影类型
        showplace = self.getInfoByRe(response.text, r'制片国家/地区:</span>(.+?)<br/>')		#制作国家
        lan = self.getInfoByRe(response.text, r'语言:</span>(.+?)<br/>')			#语言
        mvnames = self.getInfoByRe(response.text, r'又名:</span>(.+?)<br/>')		#电影别名
        mvshowtime = response.xpath("//span[@property='v:initialReleaseDate']/text()").extract()		#电影上映时间
        mvtimelen = response.xpath("//span[@property='v:runtime']/text()").extract()			#电影时长
        print (director,starring,mvtype,showplace,lan,mvnames,mvshowtime,mvtimelen)