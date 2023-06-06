#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/6/4 12:49
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : runspider.py
# @Version  : Python 3.10.10
# @Project  : scrapy
# @Software : PyCharm

from scrapy import cmdline
cmdline.execute("scrapy crawl example".split())