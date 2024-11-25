import scrapy
from urllib.parse import urljoin

class LoveFioyoSpider(scrapy.Spider):
    name = "lifestyle_image"
    allowed_domains = ["lovefioyo.com"]
    start_urls = ["https://lovefioyo.com/"]

    def parse(self, response):
        # Extract product page links
        product_links = response.css('a.woocommerce-LoopProduct-link::attr(href)').getall()  # Confirm selector
        for link in product_links:
            full_link = urljoin(response.url, link)
            yield scrapy.Request(full_link, callback=self.parse_product)

        # Follow pagination links
        next_page = response.css('a.next.page-numbers::attr(href)').get()  # Confirm selector
        if next_page:
            next_page_url = urljoin(response.url, next_page)
            yield scrapy.Request(next_page_url, callback=self.parse)

    def parse_product(self, response):
        # Extract lifestyle images
        lifestyle_images  = response.css('img.size-woocommerce_thumbnail::attr(src)').getall()  # Confirm selector


        # Make URLs absolute
        lifestyle_images = [urljoin(response.url, img) for img in lifestyle_images]

        yield {
            'lifestyle_images': lifestyle_images,
        }
