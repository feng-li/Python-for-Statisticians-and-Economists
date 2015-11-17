# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EmpCoalItem(scrapy.Item):
    location = scrapy.Field()
    position_title = scrapy.Field()
    href = scrapy.Field()
    publish_time = scrapy.Field()
    monthly_salary = scrapy.Field()
    crawler_time = scrapy.Field()
    company = scrapy.Field()



