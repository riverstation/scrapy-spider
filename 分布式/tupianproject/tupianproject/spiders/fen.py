# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tupianproject.items import TupianprojectItem
from scrapy_redis.spiders import RedisCrawlSpider

class FenSpider(RedisCrawlSpider):
    name = 'fen'
    allowed_domains = ['699pic.com']
    redis_key = 'fenspider:start_urls'

    # 当前的爬虫定制自己的配置文件
    custom_settings = {
        # 去重类，使用scrapy-redis的去重类
        'DUPEFILTER_CLASS': "scrapy_redis.dupefilter.RFPDupeFilter",
        # 调度器，使用scrapy-redis的调度器
        'SCHEDULER': "scrapy_redis.scheduler.Scheduler",
        # 是否允许暂停
        'SCHEDULER_PERSIST': True,
        'ITEM_PIPELINES': {
            # 是否将数据保存到redis中，这个管道是写好的，直接开启即可
            'scrapy_redis.pipelines.RedisPipeline': 400,
        },
        'REDIS_HOST': '10.0.114.232',
        'REDIS_PORT': '6379',
    }

    # 页码链接链接提取器
    page_link = LinkExtractor(allow=r'people-\d+-0-0-0-0-0-0\.html')
    # 链接提取器提取详情页链接
    detail_link = LinkExtractor(allow=r'http://699pic\.com/tupian-\d+\.html')
    rules = (
        Rule(page_link, follow=True),
        Rule(detail_link, callback='parse_detail', follow=False),
    )


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
        
