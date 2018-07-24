# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import os
import urllib.request

class TupianprojectPipeline(object):
    def open_spider(self, spider):
        self.fp = open('image.txt', 'w', encoding='utf8')

    def process_item(self, item, spider):
        d = dict(item)
        string = json.dumps(d, ensure_ascii=False)
        self.fp.write(string + '\n')

        # 下载图片函数
        # self.download(item)

        return item

    def download(self, item):
        dirname = r'C:\Users\ZBLi\Desktop\1805\day09\tupianproject\tupianproject\spiders\image'
        filename = item['title'] + '.' + item['image_url'].split('.')[-1]
        filepath = os.path.join(dirname, filename)
        urllib.request.urlretrieve(item['image_url'], filepath)

    def close_spider(self, spider):
        self.fp.close()

import pymysql
from scrapy.utils.project import get_project_settings
class TupianmysqlPipeline(object):
    def open_spider(self, spider):
        # 读取mysql的配置信息
        settings = get_project_settings()
        host = settings['HOST']
        port = settings['PORT']
        user = settings['USER']
        password = settings['PASSWORD']
        dbname = settings['DBNAME']
        charset = settings['CHARSET']
        # 链接数据库
        self.db = pymysql.connect(host=host, port=port, user=user, password=password, db=dbname, charset=charset)

    def process_item(self, item, spider):
        # 拼接sql语句
        sql = """insert into people(title, publish_time, look, collect, download, image_url) values('%s','%s','%s','%s','%s','%s')""" % (item['title'], item['publish_time'], item['look'], item['collect'], item['download'], item['image_url'])
        cursor = self.db.cursor()
        # 执行sql语句
        try:
            cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback()

        return item


    def close_spider(self, spider):
        # 关闭数据库链接
        self.db.close()

import pymongo
class TupianmongoPipeline(object):
    def open_spider(self, spider):
        # 链接数据库
        self.mongo_client = pymongo.MongoClient('localhost', 27017)
        # 选择库
        self.db = self.mongo_client.image
        # 选择集合
        self.col = self.db.people

    def close_spider(self, spider):
        self.mongo_client.close()

    def process_item(self, item, spider):
        # 插入数据
        d = dict(item)
        self.col.insert(d)
        return item
    
        
