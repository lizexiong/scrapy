#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/6/4 13:02
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : mvinfospider.py
# @Version  : Python 3.10.10
# @Project  : scrapy
# @Software : PyCharm


import scrapy
from scrapy import Request
from ..items import Spidertest1Item         #导入items

class ExampleSpider(scrapy.Spider):
    name = 'mvinfo'
    #allowed_domains = ['example.com']
    start_urls = ['https://movie.douban.com/top250']
    fsave = open('douban.txt','a+',encoding='utf-8')

    def parse(self,response):
        print ("*" * 50)
        #首先提取电影的网址和a标签信息
        movie_list = response.xpath("//div[@class='hd']/a")
        baseurl = 'https://movie.douban.com/top250'
        for i  in movie_list:
            #打印出a标签信息和电影标题
            #print (i.xpath("span[1]/text()").extract(),i.xpath("@href").extract())
        #     self.fsave.writelines(i.xpath("span[1]/text()").extract(),)
        #     self.fsave.write(" ")
        #     self.fsave.writelines(i.xpath("@href").extract())
        #     self.fsave.write('\n')
        # self.fsave.close()          #不关闭文件根本写不进去，或者不要用open，可以换一个自动关闭的方式
        #
            item = Spidertest1Item()
            name = i.xpath("span[1]/text()").extract()
            item['name'] = name
            yield item

        #获取下一页的网址信息，类似入：?start=25&filter=，我们后面拼接
        nextpage = response.xpath("//span[@class='next']/a/@href").extract()
        #只要下一页的网页不为空，我们就一直拼接
        if nextpage:
            nexturl = baseurl + nextpage[0]
            print (nexturl)
            yield Request(nexturl,callback=self.parse)      #迭代请求下一页，只要有下一页的信息