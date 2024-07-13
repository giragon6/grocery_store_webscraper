# -*- coding: utf-8 -*-
import scrapy


class AldiSpider(scrapy.Spider):
    name = 'aldi_spider'
    start_urls = [
        'https://shop.aldi.us/store/aldi/storefront/?current_zip_code=27514',
    ]

    def parse(self, response):
        for product in response.xpath("//div[@contains(@aria-label, 'Product')]"):
            yield {
                'name': product.xpath('./a/div/h2[@class="e-147kl2c"]/text()').extract_first(),
            }