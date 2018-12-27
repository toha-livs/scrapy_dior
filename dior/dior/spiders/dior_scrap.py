# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
import json
from dior.items import DiorItem, DiorItemLoader
import logging

def get_size(response):
    text = response.xpath('/html/head/script[5]/text()').extract_first()[31:-1]
    text = json.loads(text)
    size = ''
    r = []
    try:
        r = text['CONTENT']['contents'][0]['cmsContent']['elements'][3]['variations']
    except:
        pass
    try:
        r = text['CONTENT']['cmsContent']['elements'][3]['variations']
    except:
        pass
    try:
        r = text['CONTENT']['contents'][0]['cmsContent']['elements'][4]['variations']
    except:
        pass
    if r == []:
        return 'None'
    else:
        for i in r:
            size = size + '' + str(i['detail'])[6:]
    return size


def get_color(path):
    try:
        text = path['variant']
    except KeyError:
        return 'None'
    return text


def get_small_info(response):
    text = response.xpath('/html/head/script[3]/text()').extract_first()[15:-2]
    text = json.loads(text)
    return text[0]


def get_present(path):
    if path == 'inStock':
        return 'В наличии'
    else:
        return 'Нет в наличии'


class DiorScrapSpider(CrawlSpider):
    name = 'dior_scrap'
    more_pages = True
    allowed_domains = ['dior.com']
    start_urls = ['https://www.dior.com/en_us/men/clothing/all-clothing',
                  'https://www.dior.com/en_us/men/shoes/all-shoes',
                  'https://www.dior.com/en_us/men/leather-goods/all-leather-goods',
                  'https://www.dior.com/en_us/men/accessories/all-accessories',
                  'https://www.dior.com/en_us/men/chiffre-rouge',
                  'https://www.dior.com/en_us/men/fragrance/all-products',
                  ##### women
                  'https://www.dior.com/en_us/women/ready-to-wear/all-ready-to-wear',
                  'https://www.dior.com/en_us/women/bags/all-bags',
                  'https://www.dior.com/en_us/women/shoes/all-shoes',
                  'https://www.dior.com/en_us/women/fashion-jewelry-fine-jewelry/all-jewelry',
                  'https://www.dior.com/en_us/women/fashion-jewelry-fine-jewelry/jewellery',
                  'https://www.dior.com/en_us/women/accessories/all-accessories',
                  'https://www.dior.com/en_us/women/watches/all-watches',
                  'https://www.dior.com/en_us/women/fragrance/all-products',
                  'https://www.dior.com/en_us/women/makeup/lips/all-products',
                  'https://www.dior.com/en_us/women/makeup/complexion/all-products',
                  'https://www.dior.com/en_us/women/makeup/eyes/all-products',
                  'https://www.dior.com/en_us/women/makeup/nails/all-products',
                  'https://www.dior.com/en_us/women/skincare/the-products/all-products',
                  ### kids
                  'https://www.dior.com/en_us/kids/boys-2-13-years/all-products']

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
        # l = DiorItemLoader(item=DiorItem(), response=response)
        # l.add_value('url', response.url)
        # dicts = get_small_info(response)
        # l.add_xpath('name', '/html/body/div[1]/div/main/div/div[1]/div[2]/div/div[2]/div[1]/h1/span/text()')
        # l.add_value('price', str(dicts['ecommerce']['detail']['products']['price']))
        # l.add_value('value', dicts['ecommerce']['currencyCode'])
        # l.add_value('category', dicts['ecommerce']['detail']['products']['category'])
        # l.add_value('sku',  dicts['ecommerce']['detail']['products']['id'])
        # l.add_value('present', get_present(dicts['ecommerce']['detail']['products']['dimension25']))
        # l.add_value('time_take', str(response.meta['download_latency']))
        # l.add_value('color', get_color(dicts['ecommerce']['detail']['products']))
        # l.add_value('size', get_size(response))
        # l.add_value('region', 'USA')
        # l.add_xpath('description', '/html/body/div[1]/div/main/div/div[2]/div[1]/div/div[1]/div/div/div/text()')
        # try:
        #     return l.load_item()
        # except:
        # logging.ERROR('object with url {}\n name{}\n price{}\nvalue {}\ncategory {}\nsku {}\npresent {}\ntime_take {}\ncolor {}\nsize {}\nregio n{}\ndescription "{}"'.format(l.get_value('name'),l.get_value('name'), l.get_value('name'), l.get_value('name'), l.get_value('name'), l.get_value('name'), l.get_value('name'), l.get_value('name'), l.get_value('name'), l.get_value('name'), l.get_value('name'), l.get_value('name')))
        l = DiorItemLoader(item=DiorItem(), response=response)
        l.add_value('url', 'hi')
        dicts = get_small_info(response)
        l.add_value('name', 'hi')
        l.add_value('price', 'hi')
        l.add_value('value', 'hi')
        l.add_value('category', 'hi')
        l.add_value('sku', 'hi')
        l.add_value('present', 'hi')
        l.add_value('time_take', 'hi')
        l.add_value('color', 'hi')
        l.add_value('size', 'hi')
        l.add_value('region', 'hi')
        l.add_value('description', 'hi')
        return l.load_item()