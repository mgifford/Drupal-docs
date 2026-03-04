import scrapy
import json
import os
from drupal_crawler.items import DrupalCrawlerItem

class DocumentationSpider(scrapy.Spider):
    name = "documentation"
    allowed_domains = ["drupal.org"]
    start_urls = [
        "https://www.drupal.org/docs",
        "https://www.drupal.org/documentation"
    ]
    
    state_file = "content/sync_state.json"

    def __init__(self, *args, **kwargs):
        super(DocumentationSpider, self).__init__(*args, **kwargs)
        self.sync_state = self.load_state()

    def load_state(self):
        if os.path.exists(self.state_file):
            with open(self.state_file, 'r') as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return {}
        return {}

    def save_state(self):
        os.makedirs(os.path.dirname(self.state_file), exist_ok=True)
        with open(self.state_file, 'w') as f:
            json.dump(self.sync_state, f, indent=2)

    def parse(self, response):
        item = DrupalCrawlerItem()
        item['url'] = response.url
        item['title'] = response.css('h1.page-title::text').get()
        item['html'] = response.css('div.content').get()
        
        item['image_urls'] = response.css('img::attr(src)').getall()
        item['file_urls'] = response.css('a[href$=".pdf"]::attr(href)').getall()
        
        self.sync_state[response.url] = {
            "last_crawled": "now"
        }
        self.save_state()

        yield item

        for next_page in response.css('a[href^="/docs/"]::attr(href)').getall() + response.css('a[href^="/documentation/"]::attr(href)').getall():
            yield response.follow(next_page, self.parse)
