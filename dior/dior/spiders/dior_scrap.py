# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractor import LinkExtractor
from scrapy.selector import Selector

from dior.items import DiorItem, DiorItemLoader


class DiorScrapSpider(CrawlSpider):
    name = 'dior_scrap'
    allowed_domains = ['dior.com']
    start_urls = ['https://www.dior.com/en_us/men/clothing/all-clothing']

    rules = (
        Rule(
            LinkExtractor(
                restrict_xpaths=("//div[@class='catalog catalog-default']"),
                # allow=(r'https://www.dior.com/en_us/products/\w+$')
            ), 'parse_item'
        ),
    )

    def parse_item(self, response):
        selector = Selector(response)
        l = DiorItemLoader(DiorItem, selector)
        l.add_value('url', response.url)
        l.add_xpath('name', '/html/body/div[1]/div/main/div/div[1]/div[2]/div/div[2]/div[1]/h1/span')
        l.add_xpath('price', '/html/body/div[1]/div/main/div/div[1]/div[2]/div/div[2]/div[3]/span')
        # l.add_value('value', response.url[21:25])
        # l.add_value('category', 'куртаки')
        # l.add_xpath('sku', '/html/body/div[1]/div/main/div/div[2]/div[1]/div/div[1]/div/div/div/text()'[-17:])
        # l.add_value('present', 'True')
        # l.add_value('time_take', 'хз')
        # l.add_value('color', 'хз')
        # l.add_value('size', 'хз')
        # l.add_value('region', 'хз')
        # l.add_xpath('description', '/html/body/div[1]/div/main/div/div[2]/div[1]/div/div[1]/div/div/div/text()'[:-17])
        return l.load_item()
