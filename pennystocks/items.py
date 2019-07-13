# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst, Identity, Join
from w3lib.html import remove_tags


class PennystocksItem(scrapy.Item):
    symbol = scrapy.Field(
        input_processor=MapCompose(remove_tags, str.strip),
        output_processor=Identity()
    )
    companyname = scrapy.Field(
        input_processor=MapCompose(remove_tags, str.strip),
        output_processor=Identity()
    )
    volume = scrapy.Field(
        input_processor=MapCompose(remove_tags, str.strip),
        output_processor=Identity()
    )
    price = scrapy.Field(
        input_processor=MapCompose(remove_tags, str.strip),
        output_processor=Identity()
    )
    high = scrapy.Field(
        input_processor=MapCompose(remove_tags, str.strip),
        output_processor=Identity()
    )
    low = scrapy.Field(
        input_processor=MapCompose(remove_tags, str.strip),
        output_processor=Identity()
    )
    openStock = scrapy.Field(
        input_processor=MapCompose(remove_tags, str.strip),
        output_processor=Identity()
    )
    change = scrapy.Field(
        input_processor=MapCompose(remove_tags, str.strip),
        output_processor=Identity()
    )
    link = scrapy.Field(
        input_processor=MapCompose(remove_tags, str.strip),
        output_processor=Identity()
    )
