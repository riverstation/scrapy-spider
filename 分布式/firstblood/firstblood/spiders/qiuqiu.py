# -*- coding: utf-8 -*-
import scrapy
# 导入了链接提取器
from scrapy.linkextractors import LinkExtractor
# Rule：规则类，作用：用来规定提取的链接发送请求获得响应之后如何处理？
from scrapy.spiders import CrawlSpider, Rule


class QiuqiuSpider(CrawlSpider):
    name = 'qiuqiu'
    allowed_domains = ['www.qiushibaike.com']
    start_urls = ['http://www.qiushibaike.com/']

    lk = LinkExtractor(allow=r'Items/')
    # 规则元组，里面写的是一个一个规则，规则可以有多个
    rules = (
        '''
        参数1：链接提取器对象
        参数2：响应来了之后让callback处理，该写法和普通Spider的写法不同，
            普通的：self.parse_xxx
            高级的：'函数名字符串'
        参数3：follow：跟进，提取的链接响应过来之后，要不要接着按照这个规则提取链接，要得话就是True，不要的话就是False
            当然，follow有默认值，如果有callback，follow没写默认为False，如果没有callback，follow没写默认为True
        '''
        Rule(lk, callback='parse_item', follow=True),
    )

    # parse这个函数是父类的函数
    # parse_item这个函数是自定义的函数
    # parse函数在crawlspider中有自己特殊的作用，千万不能重写parse函数，如果重写了，crawlspider不能使用
    def parse_item(self, response):
        pass
