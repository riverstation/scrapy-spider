# -*- coding: utf-8 -*-
# 导入scrapy
import scrapy


class QiubaiSpider(scrapy.Spider):
    # 爬虫的名字，外号，人缘好，三批、狮子、光头、贱人  和尚   老和
    # 启动爬虫的时候需要使用
    name = 'qiubai'
    # 允许的域名，是一个列表，对要爬取的url进行限制，限制域名
    # 妹子图网站，src和网站的域名不是同一个，如果不注意，向图片发送的请求就都过滤掉了
    allowed_domains = ['www.qiushibaike.com', 'www.baidu.com']
    # 起始url，是一个列表，一般只写一个
    start_urls = ['http://www.qiushibaike.com/']

    # 这是重写的函数，也是一个回调函数，parse函数处理起始url的响应
    # response就是过来的响应对象
    # 如果有返回值，必须返回一个可迭代对象
    def parse(self, response):
        items = []
        # print('*' * 100)
        # print(response.text)
        # print(response.body)
        # print(response.url)
        # print(response.headers)
        # print(response.status)
        # 先获取所有的div列表
        div_list = response.xpath('//div[@id="content-left"]/div')
        # print(len(div_list))
        # 遍历所有div，依次获取每一个段子的信息
        for odiv in div_list:
            # 用户头像
            face = odiv.xpath('.//div[@class="author clearfix"]//img/@src')[0].extract()
            # 用户名字
            name = odiv.xpath('.//div[@class="author clearfix"]//h2/text()')[0].extract().strip('\t\n\r ')
            # 用户年龄
            try:
                age = odiv.xpath('.//div[@class="author clearfix"]/div/text()')[0].extract()
            except Exception as e:
                age = '没有年龄'
            # 糗事内容
            content = odiv.xpath('.//div[@class="content"]/span/text()')[0].extract().strip('\n\t\r ')
            # 好笑个数
            haha_count = odiv.xpath('.//div[@class="stats"]//i/text()')[0].extract()
            # 评论个数
            ping_count = odiv.xpath('.//div[@class="stats"]//i/text()')[1].extract()
            # print(ping_count)
            item = {
                '用户头像': face,
                '用户名': name,
                '用户年龄': age,
                '内容': content,
                '好笑个数': haha_count,
                '评论个数': ping_count,
            }
            items.append(item)
        # print('*' * 100)
        return items
