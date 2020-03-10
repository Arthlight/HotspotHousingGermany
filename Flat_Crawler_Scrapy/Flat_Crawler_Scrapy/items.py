# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FlatCrawlerScrapyItem(scrapy.Item):
    sqm = scrapy.Field()
    street = scrapy.Field()
    area = scrapy.Field()
    city = scrapy.Field()
    rooms = scrapy.Field()
    detail_view_url = scrapy.Field()
    price = scrapy.Field()
