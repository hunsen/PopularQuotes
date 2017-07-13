# coding: UTF-8
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotespider"
    start_urls = [
        "https://www.goodreads.com/quotes?page=1",
        "https://www.goodreads.com/quotes?page=2"
    ]

    def parse(self, response):
        page = response.url.split('page=')[1]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
