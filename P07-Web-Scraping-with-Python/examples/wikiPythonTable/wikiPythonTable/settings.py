# -*- coding: utf-8 -*-

# Scrapy settings for wikiPythonTable project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'wikiPythonTable'

SPIDER_MODULES = ['wikiPythonTable.spiders']
NEWSPIDER_MODULE = 'wikiPythonTable.spiders'
# FEED_EXPORTERS = {
#    'csv': 'wikiPythonTable.feedexport.CsvSetDelimItemExporter',
#}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'wikiPythonTable (+http://www.yourdomain.com)'
