# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.selector import Selector

from dior.items import DiorItem, DiorItemLoader


def get_str(path, a, b):
    ar = path.find(a)
    br = path.find(b)
    return path[ar:br]

def get_present(path):
    print(path)
    # path.find()
    return '-'

def get_color(path):
    colors = ["White", "silver", "grey", "black", "navy", "blue", "cerulean", "sky", "blue", "turquoise", "blue-green",
              "azure", "teal", "cyan", "green", "lime", "chartreuse", "olive", "yellow", "gold", "amber", "orange",
              "brown", "orange-red", "red", "maroon", "rose", "red-violet", "pink", "magenta", "purple", "blue-violet",
              "indigo", "violet", "peach", "apricot", "ochre", "plum"]

    br =  path.find('<br>')
    start = path.find('">')
    path = path[start:br].lower().split()
    for word in path:
        if word in colors:
            return word
        else:
            pass
    return '-'







class DiorScrapSpider(CrawlSpider):
    name = 'dior_scrap'
    allowed_domains = ['dior.com']
    start_urls = ['https://www.dior.com/en_us/men/clothing/all-clothing']

    rules = (
        Rule(
            LxmlLinkExtractor(
                restrict_xpaths=("//div[@class='catalog catalog-default']"),
                allow=(r'https://www.dior.com/en_us/products/\w+'),
                allow_domains=('dior.com'),
                deny_extensions=('False'),
                unique=True
            ), 'parse_item'
        ),
    )

    def parse_item(self, response):
        # selector = Selector(response)
        l = DiorItemLoader(item=DiorItem(), response=response)
        l.add_value('url', response.url)
        l.add_xpath('name', '/html/body/div[1]/div/main/div/div[1]/div[2]/div/div[2]/div[1]/h1/span/text()')
        print('###################################################################################3')
        print(response.xpath('//*[@id="react-view"]/div[2]/div/div[3]/div/div/div[2]/div/div/div/div/div/div').extract_first())
        # print('COLORS', get_color(response.xpath('/html/body/div[1]/div/main/div/div[2]/div[1]/div/div[1]/div/div/div').extract_first()))
        print('###################################################################################3')
        l.add_value('price', '/html/body/div[1]/div/main/div/div[1]/div[2]/div/div[2]/div[3]/span/text()')
        # l.add_value('price', '300')
        l.add_value('value', response.url[21:26])
        l.add_value('category', 'куртаки')
        l.add_value('sku', response.xpath('/html/body/div[1]/div/main/div/div[2]/div[1]/div/div[1]/div/div/div').extract_first()[-23:-6])
        # l.add_value('sku', '1231-deop2k2p3dp')
        l.add_value('present', get_present(response.xpath('/html/body/div[1]/div/main/div/div[1]/div[2]/div/div[2]/div[3]/div/button[1]').extract_first()))
        l.add_value('time_take', 'хз')
        l.add_value('color', get_color(response.xpath('/html/body/div[1]/div/main/div/div[2]/div[1]/div/div[1]/div/div/div').extract_first()))
        l.add_value('size', get_str(response.xpath('/html/body/div[1]/div/main/div/div[2]/div[1]/div/div[2]/div/div/div').extract_first(), 'size ', ')'))
        l.add_value('region', 'USA')
        l.add_xpath('description', '/html/body/div[1]/div/main/div/div[2]/div[1]/div/div[1]/div/div/div/text()')
        # l.add_value('description', 'dad;wkod pawokdpaowk pawokdpwnpaa')
        return l.load_item()
