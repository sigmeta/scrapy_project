# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BaiduItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url=scrapy.Field()
    company=scrapy.Field()
    province=scrapy.Field()
    website=scrapy.Field()
    industry_b=scrapy.Field()
    headquarters=scrapy.Field()
    welfare=scrapy.Field()
    工商注册号=scrapy.Field()
    组织机构代码=scrapy.Field()
    统一信用代码=scrapy.Field()
    经营状态=scrapy.Field()
    行业=scrapy.Field()
    企业类型=scrapy.Field()
    法定代表人=scrapy.Field()
    营业期限=scrapy.Field()
    注册资本=scrapy.Field()
    核准日期=scrapy.Field()
    登记机关=scrapy.Field()
    企业地址=scrapy.Field()
    经营范围=scrapy.Field()
    企业联系电话=scrapy.Field()
    电子邮箱=scrapy.Field()
    主要人员=scrapy.Field()
    股东信息=scrapy.Field()
    热招职位=scrapy.Field()

