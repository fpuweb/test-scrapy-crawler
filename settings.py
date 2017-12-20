# Scrapy settings for eraven_sample01 project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'eraven_sample01'

SPIDER_MODULES = ['eraven_sample01.spiders']
NEWSPIDER_MODULE = 'eraven_sample01.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'eraven_sample_crawl (+http://eraven.franklinpierce.edu)'
