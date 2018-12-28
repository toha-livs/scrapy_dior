# -*- coding: utf-8 -*-
import datetime

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from dior.items import DiorItem, DiorItemLoader
from dior.modules import get_size, get_country, get_color, get_small_info, get_present, get_description
import logging
Logger = logging.getLogger()


class DiorScrapSpider(CrawlSpider):
    name = 'dior_all'
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
                  'https://www.dior.com/en_us/kids/boys-2-13-years/all-products'
                    ######## france 
                  
                  ### man
                  'https://www.dior.com/fr_fr/homme/pret-a-porter/tout-le-pret-a-porter',
                  'https://www.dior.com/fr_fr/homme/maroquinerie/toute-la-maroquinerie',
                  'https://www.dior.com/fr_fr/homme/chaussures/toutes-les-chaussures',
                  'https://www.dior.com/fr_fr/homme/accessoires/tous-les-accessoires',
                  'https://www.dior.com/fr_fr/homme/chiffre-rouge',
                  'https://www.dior.com/fr_fr/homme/parfum/tous-les-produits',
                  ##### women
                  'https://www.dior.com/fr_fr/femme/pret-a-porter/tout-le-pret-a-porter',
                  'https://www.dior.com/fr_fr/femme/sacs/tous-les-sacs',
                  'https://www.dior.com/fr_fr/femme/souliers/tous-les-souliers',
                  'https://www.dior.com/fr_fr/femme/bijoux-joaillerie/toute-la-joaillerie',
                  'https://www.dior.com/fr_fr/femme/bijoux-joaillerie/tous-les-bijoux',
                  'https://www.dior.com/fr_fr/femme/accessoires/tous-les-accessoires',
                  'https://www.dior.com/fr_fr/femme/maison',
                  'https://www.dior.com/fr_fr/femme/horlogerie/toutes-les-pieces',
                  'https://www.dior.com/fr_fr/femme/parfum/tous-les-produits',
                  'https://www.dior.com/fr_fr/femme/maquillage/levres/tous-les-produits',
                  'https://www.dior.com/fr_fr/femme/maquillage/teint/tous-les-produits',
                  'https://www.dior.com/fr_fr/femme/maquillage/yeux/tous-les-produits',
                  'https://www.dior.com/fr_fr/femme/maquillage/ongles/tous-les-produits',
                  'https://www.dior.com/fr_fr/femme/soin/tous-les-produits',
                  ### kids
                  'https://www.dior.com/fr_fr/enfant/filles-2-13-ans/tous-les-produits',
                  'https://www.dior.com/fr_fr/enfant/garcons-2-13-ans/tous-les-produits',
                  'https://www.dior.com/fr_fr/enfant/bebes-filles-1-36-mois/tous-les-produits',
                  'https://www.dior.com/fr_fr/enfant/bebes-garcons-1-36-mois/tous-les-produits',
                  'https://www.dior.com/fr_fr/kids/boys-2-13-years/all-products']

    rules = (
        Rule(
            LxmlLinkExtractor(
                restrict_xpaths=("//div[@class='catalog catalog-default']"),
                allow=(r'https://www.dior.com/en_us/products/\w+', r'https://www.dior.com/fr_fr/products/\w+'),
                allow_domains=('dior.com'),
                deny_extensions=('False'),
                unique=True
            ), 'parse_item'
        ),
    )

    def parse_item(self, response):
        print(('{} [root] INFO: loading page from url"{}"'.format(datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'), response.url)))
        l = DiorItemLoader(item=DiorItem(), response=response)
        dicts = get_small_info(response)
        l.add_value('url', response.url)
        l.add_value('name', dicts['ecommerce']['detail']['products']['name'])
        l.add_value('price', str(dicts['ecommerce']['detail']['products']['price']))
        l.add_value('value', dicts['ecommerce']['currencyCode'])
        l.add_value('category', dicts['ecommerce']['detail']['products']['category'])
        l.add_value('sku',  dicts['ecommerce']['detail']['products']['id'])
        l.add_value('present', get_present(dicts['ecommerce']['detail']['products']['dimension25']))
        l.add_value('time_take', str(response.meta['download_latency']))
        l.add_value('color', get_color(dicts['ecommerce']['detail']['products']))
        l.add_value('size', get_size(response))
        l.add_value('region', get_country(dicts['country']))
        l.add_value('description', get_description(response))
        return l.load_item()