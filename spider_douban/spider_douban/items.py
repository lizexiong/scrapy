# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderDoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    director = scrapy.Field()
    starring = scrapy.Field()
    mvtype = scrapy.Field()
    showplace = scrapy.Field()
    lan = scrapy.Field()
    mvnames = scrapy.Field()
    mvshowtime = scrapy.Field()
    mvtimelen = scrapy.Field()
