# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GamesDataItem(scrapy.Item):
    # define the fields for your item here like:
    game_name = scrapy.Field()
    platform = scrapy.Field()
    date_scrapped = scrapy.Field()
    sensor_score = scrapy.Field()
    visibility = scrapy.Field()
    internationalization_score = scrapy.Field()
    downloads = scrapy.Field()
    revenue = scrapy.Field()
    list_of_keywords = scrapy.Field()
    review_breakdown = scrapy.Field()