# -*- coding: utf-8 -*-
import scrapy

from scrapy import FormRequest,Request #Request是scrapy get请求方法

class GithubSpider(scrapy.Spider):
    name = 'github'
    #allowed_domains = ['github.com']
    starturls = 'https://github.com/login'	#起始url
    loginurls = 'https://github.com/session'	#需要post认证的网页

    def start_requests(self):
    	yield Request(self.starturls, callback=self.pre_parse)	#这里的reuqest就是get请求了,获取起始页面信息

    def pre_parse(self, response):								#获取登录需要的参数
    	form = response.xpath("//form[@action='/session']")		#获取form表单
    	keys = ['utf8', 'authenticity_token', 'commit']			#需要获取的key
    	values = []
    	for key in keys:		#从网页循环获取keys的值
    		xpath = "//form[@action='/session']//input[@name='%s']/@value" %key
    		value = response.xpath(xpath).extract()[0]
    		values.append(value)
    	postdata = dict(zip(keys,values))	#转换成为字典
    	postdata['login'] = '1043460476@qq.com'
    	postdata['password'] = 'qq1043460476'
    	yield FormRequest(self.loginurls, formdata= postdata, callback=self.login_parse)	#想gitHub post表单

    def login_parse(self, response):
        print ("URL:",response.url)
        print (response.xpath("//meta[@name='user-login']/@content").extract())
#JVKeHaDMlTBlYADyLynGkbQLsdvnQ9DhhlpmNBa8d3zH2PKHP7ktnDJN/UYZIRtkUVd60OCfYf+IRSRyv3ykAQ==