# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tupianproject.items import TupianprojectItem

class TupianSpider(CrawlSpider):
    name = 'tupian'
    allowed_domains = ['699pic.com']
    start_urls = ['http://699pic.com/people.html']

    # 页码链接链接提取器
    page_link = LinkExtractor(allow=r'people-\d+-0-0-0-0-0-0\.html')
    # 链接提取器提取详情页链接
    detail_link = LinkExtractor(allow=r'http://699pic\.com/tupian-\d+\.html')
    rules = (
        Rule(page_link, follow=True),
        Rule(detail_link, callback='parse_detail', follow=False),
    )

    # def parse_item(self, response):
    #     # 首先查找的到所有的图片详情页链接
    #     image_detail_list = response.xpath('//div[@class="list"]/a/@href').extract()
    #     # 遍历详情页列表，依次向每个连接发送请求
    #     for image_detail in image_detail_list:
    #         yield scrapy.Request(url=image_detail, callback=self.parse_detail)

    def parse_detail(self, response):
        # 创建一个对象
        item = TupianprojectItem()
        # 获取图片标题
        item['title'] = response.xpath('//div[@class="photo-view"]/h1/text()').extract_first()
        # 获取发布时间
        item['publish_time'] = response.xpath('//div[@class="photo-view"]/div/span[@class="publicityt"]/text()').extract()[0].rstrip(' 发布')
        # 获取浏览量
        item['look'] = response.xpath('//div[@class="photo-view"]/div/span[@class="look"]/read/text()').extract()[0]
        # 获取收藏量
        item['collect'] = response.xpath('//div[@class="photo-view"]/div/span[@class="collect"]/text()').extract()[0].rstrip(' 收藏')
        # 获取下载量
        item['download'] = response.xpath('//div[@class="photo-view"]/div/span[@class="download"]/text()').extract()[1].rstrip(' 下载\n\t')
        # 获取图片的src属性
        item['image_url'] = response.xpath('//img[@id="photo"]/@src').extract_first()

        yield item
        
