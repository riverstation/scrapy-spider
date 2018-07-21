# -*- coding: utf-8 -*-
import scrapy

from movieproject.items import MovieprojectItem

class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['www.id97.com']
    start_urls = ['http://www.id97.com/movie/']
    page = 1
    url = 'http://www.id97.com/movie/?page={}'

    def parse(self, response):
        # 这里做什么操作？
        div_list = response.xpath('//div[@class="col-xs-1-5 col-sm-4 col-xs-6 movie-item"]')
        # 遍历所有的div_list
        for div in div_list:

            # 创建对象
            item = MovieprojectItem()

            # 电影海报
            item['post'] = div.xpath('.//div[@class="movie-item-in"]/a/img/@data-original').extract_first()
            # 电影名字
            item['name'] = div.xpath('.//div[@class="movie-item-in"]/a/@title').extract_first()
            # 获取电影评分
            item['score'] = div.xpath('.//div[@class="meta"]/h1/em/text()').extract_first().strip('- 分')
            # 获取电影的类型
            item['_type'] = div.xpath('.//div[@class="otherinfo"]/a/text()').extract_first()
            # 提取电影详情链接
            detail_url =  div.xpath('.//div[@class="meta"]/h1/a/@href').extract_first()
            # 向详情页发送请求
            yield scrapy.Request(url=detail_url, callback=self.parse_detail, meta={'item': item})
       

            

        if self.page < 2:
            self.page +=1
            url = self.url.format(self.page)
            yield scrapy.Request(url=url,callback=self.parse)

    def parse_detail(self, response):
        # 获取电影的其他六个信息
        # 将原来创建的item接受过来
        item = response.meta['item']
        # 提取导演
        item['director'] = response.xpath('//div[@class="col-xs-8"]/table[@class="table table-striped table-condensed table-bordered"]/tbody/tr[1]/td[2]/a/text()').extract()
        # 提取编剧
        item['editor'] = response.xpath('//div[@class="col-xs-8"]/table[@class="table table-striped table-condensed table-bordered"]/tbody/tr[2]/td[2]/a/text()').extract()
        item['actor'] = response.xpath('//div[@class="col-xs-8"]/table[@class="table table-striped table-condensed table-bordered"]/tbody/tr[3]/td[2]/a/text()').extract()
        item['publish_time'] = response.xpath('//div[@class="col-xs-8"]/table[@class="table table-striped table-condensed table-bordered"]/tbody/tr[7]/td[2]/text()').extract()[0]
        item['info'] = response.xpath('//div[@class="col-xs-12 movie-introduce"]/p/text()').extract_first()
        item['url'] = response.xpath('//table[@class="table table-hover"]/tbody/tr[2]/td[2]/div/a/@href').extract_first()
        

        yield item
'''


    # 主演
    actor = scrapy.Field()
    # 上映时间
    publish_time = scrapy.Field()
    # 电影介绍
    info = scrapy.Field()
    # 电影链接
    url = scrapy.Field()
'''