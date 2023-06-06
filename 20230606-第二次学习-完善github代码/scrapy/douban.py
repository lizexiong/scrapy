import scrapy


class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["douban.com"]
    start_urls = ["https://douban.com"]

    def parse(self, response):
        pass
