# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FanjianprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 头像
    face = scrapy.Field()
    # 名字
    name = scrapy.Field()
    # 内容
    content = scrapy.Field()
    # 浏览量
    liulan = scrapy.Field()
    # 时间
    shijian = scrapy.Field()
