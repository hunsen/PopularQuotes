# coding = UTF-8
# Usage: scrapy runspider quotes_all.py -o quotes_all.json
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
        next_page = response.css('a.next_page::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
