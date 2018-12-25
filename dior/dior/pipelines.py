# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv
import os


class DiorPipeline(object):

    def open_spider(self, spider):
        if not os.path.isfile('CONTENT_psysci.csv'):
            self.csvwriter = csv.writer(open('CONTENT.csv', 'a'))
            self.csvwriter.writerow(['Url', 'Name', 'Price',
                                     'Value', 'Category',
                                     'SKU', 'Present', 'Time Take',
                                     'Color', 'Size', 'Region', 'Description'
                                     ])
        else:
            self.csvwriter = csv.writer(open('CONTENT.csv', 'a'))

    def close_spider(self, spider):
        pass

    def process_item(self, item, spider):
        self.csvwriter.writerow([item['url'], item['name'],
                                 item['price'],
                                 item['value'], item['category'],
                                 item['sku'],
                                 item['present'], item['time_take'],
                                 item['color'], item['size'],
                                 item['region'], item['description']
                                 ])
        return item
