from pathlib import Path

import scrapy


class TestSpiderSpider(scrapy.Spider):
    name = "test_spider"
    allowed_domains = ["www.instacart.com"]
    start_urls = ["https://www.instacart.com/"]

    def parse(self, response):
        Path("instacart-test.html").write_bytes(response.body)
        self.log(f"Saved file {filename}")
