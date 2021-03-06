# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy.exceptions import DropItem #过滤信息的方法

import pymysql
pymysql.install_as_MySQLdb()
class Spidertest1MysqlPipeline(object):
	def open_spider(self, spider):
		self.con = pymysql.connect(host="192.168.100.1", user='root', password="huawei",\
									database="scrapy",charset="utf8",
			)
		self.cur = self.con.cursor()
		print ("*" * 1000)

	def close_spider(self,spider):
		self.con.commit()
		self.con.close()

	def process_item(self, item, spider):
		print (item['name'],'*' * 50)
		self.cur.execute("insert into mvtitle values(%s)",item["name"])
		return item

class Spidertest1Pipeline(object):
	def open_spider(self, spider):
		self.save = open('item.txt','w')

	def close_spider(self,spider):
		self.save.close()

	def process_item(self, item, spider):
		# raise DropItem(item)	#主动触发放弃item
		print (item['name'],'*' * 50)
		self.save.write(item['name'][0])
		self.save.write("\n")
		return item

import json
class Spidertest1JsonPipeline(object):
	def __init__(self, fpath):
		self.fpath = fpath

	def open_spider(self, spider):
		self.save = open(self.fpath,'w',encoding='utf-8')

	def close_spider(self,spider):
		self.save.close()

	def process_item(self, item, spider):
		info = json.dumps(dict(item),ensure_ascii=False) + "\n"	#ensure_ascii默认是unicode
		self.save.write(info)
		return item

	@classmethod
	def from_crawler(cls,crawler):
		return cls(fpath = crawler.settings.get("JSON_PATH"))