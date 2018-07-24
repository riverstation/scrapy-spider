# -*- coding: utf-8 -*-
import scrapy


class PostSpider(scrapy.Spider):
    name = 'post'
    allowed_domains = ['cn.bing.com']
    # start_urls = ['http://cn.bing.com/']

    # 需要重写这个方法
    # def start_requests(self):
    # 	for url in start_urls:
    # 		yield scrapy.Request(url=url, callback=self.parse)
    def start_requests(self):
    	post_url = 'https://cn.bing.com/ttranslationlookup?&IG=48906CCA6B9D4B7EB1F15231FB8626D0&IID=translator.5036.1'
    	# 表单数据
    	data = {
    		'from': 'zh-CHS',
			'to': 'en',
			'text': '彩虹'
    	}
    	yield scrapy.FormRequest(url=post_url, formdata=data, callback=self.parse)

    def parse(self, response):
        print('*' * 100)
        print(response.text)
        print('*' * 100)
