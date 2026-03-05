# Scrapy settings for drupal_crawler project
BOT_NAME = "drupal_crawler"

SPIDER_MODULES = ["drupal_crawler.spiders"]
NEWSPIDER_MODULE = "drupal_crawler.spiders"

USER_AGENT = "DrupalDocsUpgradeBot (+https://github.com/mgifford/drupal-docs)"

ROBOTSTXT_OBEY = True

CONCURRENT_REQUESTS = 1
DOWNLOAD_DELAY = 10 # Very conservative delay
CONCURRENT_REQUESTS_PER_DOMAIN = 1

# Limit each run to 20 pages to be a good citizen
CLOSESPIDER_PAGECOUNT = 20

AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 5
AUTOTHROTTLE_MAX_DELAY = 60
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
AUTOTHROTTLE_DEBUG = False

ITEM_PIPELINES = {
    "scrapy.pipelines.images.ImagesPipeline": 1,
    "scrapy.pipelines.files.FilesPipeline": 2,
    "drupal_crawler.pipelines.SaveHTMLPipeline": 3,
}

IMAGES_STORE = "downloads/media/images"
FILES_STORE = "downloads/media/files"

FEED_EXPORT_ENCODING = "utf-8"
