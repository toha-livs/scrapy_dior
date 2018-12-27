# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
from lxml.html.clean import unicode
from scrapy import Item, Field
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose


class DiorItem(Item):
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

    default_output_processor = TakeFirst()

    url_in = MapCompose(unicode.strip)
    name_in = MapCompose(unicode.strip)
    price_in = MapCompose(unicode.strip)
    value_in = MapCompose(unicode.strip)
    category_in = MapCompose(unicode.strip)
    sku_in = MapCompose(unicode.strip)
    present_in = MapCompose(unicode.strip)
    time_take_in = MapCompose(unicode.strip)
    color_in = MapCompose(unicode.strip)
    size_in = MapCompose(unicode.strip)
    region_in = MapCompose(unicode.strip)
    description_in = MapCompose(unicode.strip)

