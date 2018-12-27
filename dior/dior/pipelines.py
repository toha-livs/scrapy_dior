# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pandas as pd


class DiorPipeline(object):

    def open_spider(self, spider):
        self.csvwriter = pd.DataFrame({}, columns=['Url', 'Name', 'Price',
                                 'Value', 'Category',
                                 'SKU', 'Present', 'Time Take',
                                 'Color', 'Size', 'Region', 'Description'
                                 ])

        self.csvwriter.to_csv('my_csv.csv', encoding='utf-8', index=False)

    def close_spider(self, spider):
        pass

    def process_item(self, item, spider):
        w_r = pd.DataFrame([[item['url'], item['name'],
                                 item['price'],
                                 item['value'], item['category'],
                                 item['sku'],
                                 item['present'], item['time_take'],
                                 item['color'], item['size'],
                                 item['region'], item['description']
                                 ]],
                           columns=['Url', 'Name', 'Price',
                                     'Value', 'Category',
                                     'SKU', 'Present', 'Time Take',
                                     'Color', 'Size', 'Region', 'Description'
                                     ])
        w_r.to_csv('my_csv.csv', mode='a', header=False, encoding='utf-8', index=False)
        return item
