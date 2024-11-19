# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


import scrapy

class EcommerceScraperItem(scrapy.Item):
    product_images = scrapy.Field()
    lifestyle_images = scrapy.Field()

