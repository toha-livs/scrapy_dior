# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pandas as pd
import json


class DiorPipeline(object):

    def open_spider(self, spider):
        self.csvwriter = pd.DataFrame({}, columns=['Url', 'Name', 'Price',
                                 'Value', 'Category',
                                 'SKU', 'Present', 'Time Take',
                                 'Color', 'Size', 'Region', 'Description'
                                 ])

        self.csvwriter.to_csv('my_csv.csv', encoding='utf-8', index=False)

    def close_spider(self, spider):
        table = pd.read_csv('my_csv.csv')
        percent = table['SKU'].count() // 100
        usa = table['Region'] == 'USA'
        usa_out = table[usa].shape[0]  # вывод
        usa_val = table['Value'] == 'USD'
        usa_val_out = table[usa & usa_val].shape[0]
        if usa_val_out == usa_out:
            usa_val_out = 'Вся валюта с региона США пришла верная (USD)'
        else:
            usa_val_out = [int(table[usa_val & usa].shape[0]), int(table[usa_val & usa].shape[1])]
        france = table['Region'] == 'FRANCE'
        france_val = table['Value'] == 'EUR'  # вывод
        france_out = table[france].shape[0]
        france_val_out = table[france_val & france].shape[0]  # вывод
        if france_val_out == france_out:
            france_val_out = 'Вся валюта с региона Франции пришла верная (EUR)'
        else:
            france_val_out = [int(table[france_val & france].shape[0]), int(table[france_val & france].shape[1])]
        color = table['Color'] != 'None'
        size = table['Size'] != 'None'
        description = table['Description'] != 'None'
        color_out = str(table[color].shape[0] // percent) + '%'  # вывод
        size_out = str(table[size].shape[0] // percent) + '%'  # вывод
        description_out = str(table[description].shape[0] // percent) + '%'
        data = {'france_all': int(france_out), 'usa_all': int(usa_out), 'currency_france': france_val_out,
                'currency_usa': usa_val_out,
                'percent_fo_color': color_out, 'percent_fo_size': size_out, 'percent_fo_description': description_out}
        with open('test_results.json', 'w', encoding='utf-8') as js_f:
            json.dump(data, js_f, ensure_ascii=False)

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
