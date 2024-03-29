# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from pymongo import MongoClient, InsertOne

class SpiderDoubanPipeline(object):
    def process_item(self, item, spider):
        return item

class SpiderDoubanMongoPipeline(object):
	def open_spider(self, spider):
		#默认啥都不填就是本地127.0.0.1和无密码
		self.client = MongoClient()
		self.db = self.client.mvinfo

	def close_spider(self, spider):
		self.client.close()

	def process_item(self, item, spider):
		col = self.db.mDoubaninfo
		min = InsertOne(dict(item))
		col.bulk_write([min])
		return item