# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.selector import Selector

from dior.items import DiorItem, DiorItemLoader


class TestAllSpider(CrawlSpider):
    name = 'test_all'
    allowed_domains = ['dior.com']
    start_urls = ['https://www.dior.com/en_us', 'https://www.dior.com/en_us/men/clothing/all-clothing',
                  'https://www.dior.com/en_us/men/shoes/all-shoes',
                  'https://www.dior.com/en_us/men/leather-goods/all-leather-goods',
                  'https://www.dior.com/en_us/men/accessories/all-accessories',
                  'https://www.dior.com/en_us/men/chiffre-rouge',

                  ]

    rules = (
        Rule(
            LxmlLinkExtractor(
                restrict_xpaths=('//*[@id="nav"]/div/ul/li[2]/ul'),
                # allow=(r'https://www.dior.com/en_us/products/\w+'),
                allow_domains=('dior.com'),
                deny_extensions=('False'),
                unique=True
            ), 'parse_item'
        ),
    )

    def parse_item(self):
        pass






# /html/body/div[1]/div/div[1]/div[3]/div/nav/div/ul/li[2]/ul/li[1]/ul/li[3]/button

# /html/body/div[1]/div/div[1]/div[3]/div/nav/div/ul/li[2]/ul/li[1]/ul/li[4]/ul/li[2]/a