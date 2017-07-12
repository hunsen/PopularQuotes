# coding = UTF-8
import scrapy

class PopularQuotes(scrapy.Spider):
    name = "quotes"
    start_urls = ["https://www.goodreads.com/quotes"]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'quote_text': quote.css('.quoteText::text').extract_first(),
                'author': quote.css('a.authorOrTitle::text').extract_first()
            }
