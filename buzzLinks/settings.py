# -*- coding: utf-8 -*-

# Scrapy settings for buzzLinks project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'buzzLinks'

SPIDER_MODULES = ['buzzLinks.spiders']
NEWSPIDER_MODULE = 'buzzLinks.spiders'
ITEM_PIPELINES = {'buzzLinks.pipelines.BuzzlinksPipeline':1}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'buzzLinks (+http://www.yourdomain.com)'
