# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.selector import Selector

from dior.items import DiorItem, DiorItemLoader


class TestAllSpider(CrawlSpider):
    name = 'test_all'
    allowed_domains = ['dior.com']
    start_urls = ['https://www.dior.com/en_us/men/clothing/all-clothing',
                  # 'https://www.dior.com/en_us/men/shoes/all-shoes',
                  # 'https://www.dior.com/en_us/men/leather-goods/all-leather-goods',
                  # 'https://www.dior.com/en_us/men/accessories/all-accessories',
                  # 'https://www.dior.com/en_us/men/chiffre-rouge',
                  # 'https://www.dior.com/en_us/men/fragrance/all-products',
                  # ##### women
                  # 'https://www.dior.com/en_us/women/ready-to-wear/all-ready-to-wear',
                  # 'https://www.dior.com/en_us/women/bags/all-bags',
                  # 'https://www.dior.com/en_us/women/shoes/all-shoes',
                  # 'https://www.dior.com/en_us/women/fashion-jewelry-fine-jewelry/all-jewelry',
                  # 'https://www.dior.com/en_us/women/fashion-jewelry-fine-jewelry/jewellery',
                  # 'https://www.dior.com/en_us/women/accessories/all-accessories',
                  # 'https://www.dior.com/en_us/women/watches/all-watches',
                  # 'https://www.dior.com/en_us/women/fragrance/all-products',
                  # 'https://www.dior.com/en_us/women/makeup/lips/all-products',
                  # 'https://www.dior.com/en_us/women/makeup/complexion/all-products',
                  # 'https://www.dior.com/en_us/women/makeup/eyes/all-products',
                  # 'https://www.dior.com/en_us/women/makeup/nails/all-products',
                  # 'https://www.dior.com/en_us/women/skincare/the-products/all-products',
                  # ### kids
                  'https://www.dior.com/en_us/kids/boys-2-13-years/all-products'




                  ]

    rules = (
        Rule(
            LxmlLinkExtractor(
                restrict_xpaths=('/html/body/div[1]/div/main/div/div[2]'),
                                # '/html/body/div[1]/div/main/div/div[2]'
                                #//*[@id="main"]/div/div[2]/div[3]/ul
                allow=(r'https://www.dior.com/en_us/products/\w+'),
                allow_domains=('dior.com'),
                deny_extensions=('False'),
                unique=True
            ), 'parse_item'
        ),
    )

    def parse_item(self, response):
        print(response.meta['download_latency'])
        print(response.url[:35])
        if response.url[:35] == 'https://www.dior.com/en_us/products/':
            l = DiorItemLoader(item=DiorItem(), response=response)
            l.add_value('url', response.url)
            l.add_xpath('name', '/html/body/div[1]/div/main/div/div[1]/div[2]/div/div[2]/div[1]/h1/span/text()')
            print('###################################################################################3')
            print(response.xpath(
                '//*[@id="react-view"]/div[2]/div/div[3]/div/div/div[2]/div/div/div/div/div/div').extract_first())
            # print('COLORS', get_color(response.xpath('/html/body/div[1]/div/main/div/div[2]/div[1]/div/div[1]/div/div/div').extract_first()))
            print('###################################################################################3')
            l.add_value('price', '/html/body/div[1]/div/main/div/div[1]/div[2]/div/div[2]/div[3]/span/text()')
            # l.add_value('price', '300')
            l.add_value('value', response.url[21:26])
            l.add_value('category', 'куртаки')
            l.add_value('sku', response.xpath(
                '/html/body/div[1]/div/main/div/div[2]/div[1]/div/div[1]/div/div/div').extract_first()[-23:-6])
            # l.add_value('sku', '1231-deop2k2p3dp')
            l.add_value('present', get_present(response.xpath(
                '/html/body/div[1]/div/main/div/div[1]/div[2]/div/div[2]/div[3]/div/button[1]').extract_first()))
            l.add_value('time_take', 'хз')
            l.add_value('color', get_color(
                response.xpath('/html/body/div[1]/div/main/div/div[2]/div[1]/div/div[1]/div/div/div').extract_first()))
            l.add_value('size', get_str(
                response.xpath('/html/body/div[1]/div/main/div/div[2]/div[1]/div/div[2]/div/div/div').extract_first(),
                'size ', ')'))
            l.add_value('region', 'USA')
            l.add_xpath('description', '/html/body/div[1]/div/main/div/div[2]/div[1]/div/div[1]/div/div/div/text()')
            # l.add_value('description', 'dad;wkod pawokdpaowk pawokdpwnpaa')
            return l.load_item()
        # else:
        #     yield response.follow()





# /html/body/div[1]/div/div[1]/div[3]/div/nav/div/ul/li[2]/ul/li[1]/ul/li[3]/button

# /html/body/div[1]/div/div[1]/div[3]/div/nav/div/ul/li[2]/ul/li[1]/ul/li[4]/ul/li[2]/a