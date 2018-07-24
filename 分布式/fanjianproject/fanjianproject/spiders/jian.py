# -*- coding: utf-8 -*-
import scrapy
from fanjianproject.items import FanjianprojectItem


class JianSpider(scrapy.Spider):
    name = 'jian'
    allowed_domains = ['www.fanjian.net']
    start_urls = ['http://www.fanjian.net/duanzi']

    # 定义一个page
    page = 1
    # 定义一个要拼接的url
    url = 'http://www.fanjian.net/duanzi-{}'

    def parse(self, response):
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

        if self.page < 5:
        	self.page += 1
        	# 拼接url
        	url = self.url.format(self.page)
        	# 生成请求对象，发送请求
        	yield scrapy.Request(url=url, callback=self.parse)

    # def parse_info(self, response):
    # 	pass
