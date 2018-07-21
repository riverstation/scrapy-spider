# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import os
import urllib.request

class TupianprojectPipeline(object):
    def open_spider(self, spider):
        self.fp = open('image.txt', 'w', encoding='utf8')

    def process_item(self, item, spider):
        d = dict(item)
        string = json.dumps(d, ensure_ascii=False)
        self.fp.write(string + '\n')

        # 下载图片函数
        self.download(item)

        return item

    def download(self, item):
        dirname = r'C:\Users\ZBLi\Desktop\1805\day09\tupianproject\tupianproject\spiders\image'
        filename = item['title'] + '.' + item['image_url'].split('.')[-1]
        filepath = os.path.join(dirname, filename)
        urllib.request.urlretrieve(item['image_url'], filepath)

    def close_spider(self, spider):
        self.fp.close()
