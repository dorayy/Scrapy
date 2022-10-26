# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from matplotlib import image
import scrapy


class WebcrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ReviewsAllocineItem(scrapy.Item):
    title = scrapy.Field()
    img = scrapy.Field()
    author = scrapy.Field()
    time = scrapy.Field()
    genre = scrapy.Field()
    score = scrapy.Field()
    desc = scrapy.Field()
    release = scrapy.Field()

class BoursoramaItem(scrapy.Item):
    indexStockExchange = scrapy.Field()
    stockAction = scrapy.Field()
    variation = scrapy.Field()
    vMax = scrapy.Field()
    vMin = scrapy.Field()
    vOpen = scrapy.Field()
    dateCollect = scrapy.Field()
