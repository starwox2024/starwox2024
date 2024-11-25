import scrapy
from urllib.parse import urljoin

class ProductImageSpider(scrapy.Spider):
    name = "product_image_spider"
    allowed_domains = ["lovefioyo.com"]
    start_urls = ["https://lovefioyo.com/"]

    def parse(self, response):
        # Extract product page links
        product_links = response.css('a.woocommerce-LoopProduct-link::attr(href)').getall()
        for link in product_links:
            full_link = urljoin(response.url, link)
            yield scrapy.Request(full_link, callprback=self.parse_product)

        # Follow pagination links
        next_page = response.css('a.next.page-numbers::attr(href)').get()
        if next_page:
            next_page_url = urljoin(response.url, next_page)
            yield scrapy.Request(next_page_url, callback=self.parse)

    def parse_product(self, response):
        # Extract product image
        product_image = response.css('img.woocommerce-thumbnail::attr(src)').getall()
        product_image = urljoin(response.url, product_image)

        yield {
            'product_image': product_image,
        }
