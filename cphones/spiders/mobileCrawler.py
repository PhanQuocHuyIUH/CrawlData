import scrapy
from cphones.items import CphonesItem

class MobilecrawlerSpider(scrapy.Spider):
    name = "mobileCrawler"
    allowed_domains = ["cellphones.com.vn"]
    start_urls = ["https://cellphones.com.vn/mobile.html"]

    def parse(self, response):
        phoneList = response.css('div.product-info a::attr(href)').getall()
        for phone in phoneList:
            yield response.follow(phone, callback=self.parse_phone)

    def parse_phone(self, response):
        item = CphonesItem()
        item['phoneUrl'] = response.url
        item['name'] = response.css('div.box-product-name h1::text').get()
        prices = response.css('p.tpt---sale-price *::text').getall()
        if len(prices) == 1:
            item['upgrade_price'] = 'Can upgrade this phone'
            item['price'] = prices[0]
        item['upgrade_price'] = prices[0]
        item['price'] = prices[len(prices) - 1]
        item['contain'] = " / ".join(response.css('div.description::text').getall())
        item['description'] = " ".join(response.css('#cpsContentSEO blockquote > p *::text').getall()).replace("\xa0", " ").strip()
        item['highlight'] = " / ".join(response.css('div.ksp-content.p-2.mb-2 > div > ul > li::text').getall())
        yield item

        pass
