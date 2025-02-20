# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CphonesItem(scrapy.Item):
    phoneUrl = scrapy.Field()
    name = scrapy.Field()
    upgrade_price = scrapy.Field()
    price = scrapy.Field()
    contain = scrapy.Field()
    description = scrapy.Field()
    highlight = scrapy.Field()
    pass
