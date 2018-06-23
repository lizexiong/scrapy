# -*- coding: utf-8 -*-
import scrapy
from scrapy import FormRequest		#post的方法来发送Form表单

class SpiderpostSpider(scrapy.Spider):
    name = 'spiderpost'
    #allowed_domains = ['httpbin.org']
    starturls = 'http://httpbin.org/post'

    #这里就要使用定义start_request的方法了,使用了start_request后,start_urls方法失效,
    #而且要讲start_urls取消,变成一个变量

    def start_requests(self):
    	yield FormRequest(self.starturls,formdata={"testkey":"lizexiong"},\
    			callback=self.parse)		#定义要发送的formdata字典

    def parse(self, response):
        print ("response:",response.text)
