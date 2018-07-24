# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from fanjianproject.items import FanjianprojectItem

class LangSpider(CrawlSpider):
    name = 'lang'
    allowed_domains = ['www.fanjian.net']
    start_urls = ['http://www.fanjian.net/duanzi']

    page_link = LinkExtractor(allow=r'http://www\.fanjian\.net/duanzi-\d+')
    rules = (
        Rule(page_link, callback='parse_item', follow=True),
    )
    '''
    False爬取过程：
    （1）首先向起始url发送请求
    （2）在第一页的响应中根据规则提取链接
        2 3 4 5 2
    （3）向2 3 4 5发送请求
    （4）用parse_item这个函数解析2 3 4 5的响应内容
    （5）代码运行结束

    True爬取过程
    （1）首先向起始url发送请求
    （2）在第一页的响应中根据规则提取链接
        2 3 4 5 2
    （3）向2 3 4 5发送请求
    （4）用parse_item这个函数解析2 3 4 5的响应内容
    （5）从2 3 4 5的响应中接着按照规则提取链接
        重复第2345步

    1  2345
    2  1345
    3  1245
    4  1235
    xxxx

    一共13页，但是提取了100个url，100个里面有好多重复的，只要这个100个里面包含所有的页码链接即可，因为调度器会去除重复的链接
    '''

    def parse_item(self, response):
        # 获取所有的li标签
        li_list = response.xpath('//li[@class="cont-item"]')
        # 遍历所有li，依次获取其他信息
        for oli in li_list:
            # 创建对象
            item = FanjianprojectItem()
            face = oli.xpath('.//a[@class="user-head"]/img/@data-src').extract_first()
            name = oli.xpath('./div[@class="cont-list-head"]/a/text()').extract_first()
            content = oli.xpath('./div[@class="cont-list-main"]/p/text()').extract_first()
            liulan = oli.xpath('./div[@class="cont-list-info fc-gray"]/text()').extract()[2]
            shijian = oli.xpath('./div[@class="cont-list-info fc-gray"]/text()').extract()[3]
            # 将获取的数据保存到自定义的对象中
            item['face'] = face
            item['name'] = name
            item['content'] = content
            item['liulan'] = liulan
            item['shijian'] = shijian

            # 将item仍走
            yield item
