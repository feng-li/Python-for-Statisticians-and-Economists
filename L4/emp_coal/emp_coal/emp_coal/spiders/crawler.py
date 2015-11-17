#!/usr/bin/env python  
# -*- coding:utf-8 -*-  

import re
import time
import scrapy
from emp_coal.items import EmpCoalItem

class HighlightsSpider(scrapy.Spider):
    name = "employment_coal"
    allowed_domains = ["sou.zhaopin.com"]
    page_no = "%d"
    start_urls = ["http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%85%A8%E5%9B%BD&kw=%E7%85%A4%E7%82%AD&sm=0&p="+page_no % 1+"&isfilter=0&fl=489&isadv=0&sg=d58961bda28f4cc0b1946a1b363a7a4b"]
    def __init__(self):
        self.page_number = 1
    def parse(self, response):
        print self.page_number
        print "-----------"
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())) 
        base_path = response.xpath('//table[re:test(@class,"newlist")]')
        if not base_path:
            raise scrapy.CloseSpider('No more pages')
        for i in range(1, len(base_path)):
            emp = base_path[i]
            item = EmpCoalItem()
            item['crawler_time'] = now
            item['position_title'] = ''.join(emp.xpath('.//tr/td[1]/div/a/descendant::text()').extract()).encode('utf-8')
            item['company'] = emp.xpath('.//tr/td[2]/a/text()').extract()[0].encode('utf-8')
            item['href'] = emp.xpath('.//tr/td[1]/div/a/@href').extract()[0].encode('utf-8')
            item['monthly_salary'] = emp.xpath('.//tr/td[3]/text()').extract()[0].encode('utf-8')
            item['location'] = emp.xpath('.//tr/td[4]/text()').extract()[0].encode('utf-8')
            item['publish_time'] = emp.xpath('.//tr/td[5]/span/text()').extract()[0].encode('utf-8')
            yield item
        
        self.page_number += 1
        page_no = "%d"
        yield scrapy.Request('http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%85%A8%E5%9B%BD&kw=%E7%85%A4%E7%82%AD&sm=0&p=' + page_no % self.page_number + '&isfilter=0&fl=489&isadv=0&sg=d58961bda28f4cc0b1946a1b363a7a4b')
