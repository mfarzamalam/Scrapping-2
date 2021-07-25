import scrapy


class NyJobsSpider(scrapy.Spider):
    name = 'ny_jobs'
    allowed_domains = ['https://newyork.craigslist.org/search/egr']
    start_urls = ['http://https://newyork.craigslist.org/search/egr/']

    def parse(self, response):
        pass
