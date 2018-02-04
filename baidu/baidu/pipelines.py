# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from baidu.spiders.baidu import province
def dbHandle():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        passwd='9432',
        charset='utf8',
        use_unicode=False
    )
    return conn


class BaiduPipeline(object):
    def __init__(self):
        self.dbObject = dbHandle()
        self.cursor = self.dbObject.cursor()

    def process_item(self, item, spider):
        
        sql = 'insert into company.'+province+'(url,company,province,website,industry_b,headquarters,welfare,工商注册号,组织机构代码,统一信用代码,经营状态,行业,企业类型,法定代表人,营业期限,注册资本,核准日期,登记机关,企业地址,经营范围,企业联系电话,电子邮箱,主要人员,股东信息,热招职位) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

        try:
            self.cursor.execute(sql,(item['url'],item['company'],item['province'],item['website'],item['industry_b'],item['headquarters'],item['welfare'],item['工商注册号'],item['组织机构代码'],item['统一信用代码'],item['经营状态'],item['行业'],item['企业类型'],item['法定代表人'],item['营业期限'],item['注册资本'],item['核准日期'],item['登记机关'],item['企业地址'],item['经营范围'],item['企业联系电话'],item['电子邮箱'],item['主要人员'],item['股东信息'],item['热招职位']))
            self.dbObject.commit()
            print('写入成功')
        except Exception as e:
            print(e)
            print('############写入失败！##############')
            self.dbObject.rollback()
        return item


