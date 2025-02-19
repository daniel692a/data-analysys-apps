# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    isbn = scrapy.Field()
    title = scrapy.Field()
    authors = scrapy.Field()
    publisher = scrapy.Field()
    publication_date = scrapy.Field()
    rank = scrapy.Field()
    reviews = scrapy.Field()
    pages = scrapy.Field()
    ebook_price = scrapy.Field()
    genres = scrapy.Field()