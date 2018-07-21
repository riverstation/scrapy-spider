# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 在第一页获取的电影信息
    # 电影海报
    post = scrapy.Field()
    # 电影名字
    name = scrapy.Field()
    # 电影评分
    score = scrapy.Field()
    # 电影类型
    _type = scrapy.Field()

    # 在第二页获取的电影信息
    # 导演
    director = scrapy.Field()
    # 编剧
    editor = scrapy.Field()
    # 主演
    actor = scrapy.Field()
    # 上映时间
    publish_time = scrapy.Field()
    # 电影介绍
    info = scrapy.Field()
    # 电影链接
    url = scrapy.Field()
