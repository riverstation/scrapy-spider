# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import os
import urllib.request

class MovieprojectPipeline(object):
    def open_spider(self,spider):

        self.fp = open('movie.txt','w',encoding='utf8')

    def process_item(self, item, spider):
        d = dict(item)
        string = json.dumps(d,ensure_ascii=False)
        self.fp.write(string+'\n')
        self.download(item)

        return item


    def download(self,item):
        dirname = r'D:\python1805爬虫\爬虫练习\day09\movieproject\movieproject\spiders\image'

        filename = item['name']+'.'+item['post'].split('.')[-1]
        filepath = os.path.join(dirname,filename)
        urllib.request.urlretrieve(item['post'],filepath)
    def close_spider(self,spider):
        self.fp.close()