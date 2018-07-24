# -*- coding: utf-8 -*-

# development
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class FanjianprojectPipeline(object):
    # 重写构造方法
    def __init__(self):
        # 在这里打开文件即可
        self.fp = open('jian.txt', 'w', encoding='utf8')

    # 也可以在这里打开文件
    # def open_spider(self, spider):
    #   self.fp = open('jian.txt', 'w', encoding='utf8')

    # 处理数据函数，item就是爬虫文件给你扔的数据
    # 给一个item，这个函数就会被调用一次
    def process_item(self, item, spider):
        # 保存到文件中
        # 先将item转化为字典
        d = dict(item)
        # 将字典转化为json格式的字符串
        string = json.dumps(d, ensure_ascii=False)
        self.fp.write(string + '\n')
        return item

    def close_spider(self, spider):
        self.fp.close()
