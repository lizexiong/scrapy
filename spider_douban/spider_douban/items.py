# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, Compose, Join

def mysplit(info):
	return info.split('/')


class SpiderDoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    director = scrapy.Field(output_processor=Join())
    starring = scrapy.Field(output_processor=Join('/'))
    mvtype = scrapy.Field(output_processor=Join())
    showplace = scrapy.Field(input_processor= MapCompose(str.strip), output_processor=Join())
    #先去掉两边的空格,然后用空格连接起来去掉list[]
    lan = scrapy.Field(input_processor= MapCompose(str.strip), output_processor=Join())
    mvnames = scrapy.Field(input_processor= MapCompose(mysplit,str.strip), output_processor=Join())
    #这里自定义了一个进入的时候的分割函数
    mvshowtime = scrapy.Field(output_processor=Join())
    mvtimelen = scrapy.Field(output_processor=Join())
