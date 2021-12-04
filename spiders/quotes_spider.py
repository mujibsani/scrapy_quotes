import scrapy

from ..items import QuoteTutorialItem


class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://quotes.toscrape.com/'
    ]

    def parse(self, response, **kwargs):

        items = QuoteTutorialItem()
        all_dev_quotes = response.css('div.quote')
        for quotes in all_dev_quotes:
            titles = quotes.css('span.text::text').extract()
            authors = quotes.css('.author::text').extract()
            tags = quotes.css('.tag::text').extract()
            items['titles'] = titles
            items['authors'] = authors
            items['tags'] = tags
            yield items

        next_page = response.css('li.next a::attr(href)').get()

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)