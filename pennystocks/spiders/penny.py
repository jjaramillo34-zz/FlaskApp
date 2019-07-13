# -*- coding: utf-8 -*-
import scrapy
from pennystocks.items import PennystocksItem
from scrapy.loader import ItemLoader
import datetime


class PennySpider(scrapy.Spider):
    name = 'penny'
    allowed_domains = ['www.allpennystocks.com/hotpennystocks/nsd.aspx']
    start_urls = [
        'http://www.allpennystocks.com/hotpennystocks/nsd.aspx',
        'https://www.allpennystocks.com/hotpennystocks/oto.aspx'
    ]
    
    date = datetime.datetime.today()

    def parse(self, response):
        for stock in response.xpath("//table[@class='table']/tr"):
            loader = ItemLoader(item=PennystocksItem(), selector=stock, response=response)
            loader.add_value('link', response.url)
            loader.add_xpath('symbol', './/td[1]')
            loader.add_xpath('companyname', './/td[2]')
            loader.add_xpath('volume', './/td[3]')
            loader.add_xpath('price', './/td[4]')
            loader.add_xpath('high', './/td[5]')
            loader.add_xpath('low', './/td[6]')
            loader.add_xpath('openStock', './/td[7]')
            loader.add_xpath('change', './/td[8]')
            yield loader.load_item()
