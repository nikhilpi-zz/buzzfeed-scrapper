# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class BuzzlinksItem(scrapy.Item):
  # define the fields for your item here like:
  # name = scrapy.Field()
  article_title = scrapy.Field()
  link = scrapy.Field()
  depth = Field()
  current_url = Field()
  referring_url = Field()
  link_domain = Field()
  pass