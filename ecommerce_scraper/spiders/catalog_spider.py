import scrapy


import scrapy
from urllib.parse import urljoin
from ecommerce_scraper.items import EcommerceScraperItem

class CatalogSpider(scrapy.Spider):
    name = "catalog_spider"
    allowed_domains = ["example.com"]
    start_urls = ["https://www.example.com/products"]  # Replace with actual URL
    
    def parse(self, response):
        # Extract product page URLs and follow pagination
        try:
            product_links = response.css('a.product-link::attr(href)').getall()
        
            for link in product_links:
                full_link = urljoin(response.url, link)
                yield scrapy.Request(full_link, callback=self.parse_product)

        # Pagination: go to the next page if available
            next_page = response.css('a.next-page::attr(href)').get()
            if next_page:
                next_page_url = urljoin(response.url, next_page)
                yield scrapy.Request(next_page_url, callback=self.parse)
        except Exception as e:
            self.logger.error(f"Error parsing page {response.url}: {e}")
    def parse_product(self, response):
        # Extract image URLs from each product page
        item = EcommerceScraperItem()
        item['product_images'] = response.css('img.product-image::attr(src)').getall()
        item['lifestyle_images'] = response.css('img.lifestyle-image::attr(src)').getall()
        
        # Ensure URLs are absolute
        item['product_images'] = [urljoin(response.url, img) for img in item['product_images']]
        item['lifestyle_images'] = [urljoin(response.url, img) for img in item['lifestyle_images']]
        
        yield item

