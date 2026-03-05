import os
import json
from itemadapter import ItemAdapter

class SaveHTMLPipeline:
    def process_item(self, item, spider):
        # Save to crawler/downloads/
        # Note: Scrapy runs from 'crawler' dir, so 'downloads' will be 'crawler/downloads'
        output_dir = "downloads"
        os.makedirs(output_dir, exist_ok=True)
        
        # Use a safe filename from URL
        filename = item['url'].replace('https://', '').replace('/', '_').replace('.', '_') + ".html"
        file_path = os.path.join(output_dir, filename)
        
        with open(file_path, 'w') as f:
            f.write(item.get('html', '') or "")
            
        return item
