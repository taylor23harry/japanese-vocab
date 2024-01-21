# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JishoWordItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    furigana = scrapy.Field()
    hiragana = scrapy.Field()
    meaning = scrapy.Field()
    word_type = scrapy.Field()
