import scrapy


class SofifaSpider(scrapy.Spider):
    name = 'sofifa'
    allowed_domains = ['sofifa.com']
    start_urls = ['http://sofifa.com/']

    def parse(self, response):
        pass
