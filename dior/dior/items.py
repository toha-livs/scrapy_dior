# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst


class DiorItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = Field()
    name = Field()
    price = Field()
    value = Field()
    category = Field()
    sku = Field()
    present = Field()
    time_take = Field()
    color = Field()
    size = Field()
    region = Field()
    description = Field()


class DiorItemLoader(ItemLoader):
    url_out = TakeFirst()
    name_out = TakeFirst()
    price_out = TakeFirst()
    value_out = TakeFirst()
    category_out = TakeFirst()
    sku_out = TakeFirst()
    present_out = TakeFirst()
    time_take_out = TakeFirst()
    color_out = TakeFirst()
    size_out = TakeFirst()
    region_out = TakeFirst()
    description_out = TakeFirst()