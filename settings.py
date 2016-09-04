# -*- coding: utf-8 -*-

# Scrapy settings for codeReviewSearch project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'codeReviewSearch'

SPIDER_MODULES = ['codeReviewSearch.spiders']
#ITEM_PIPELINES = {'codeReviewSearch.pipelines.CodereviewsearchPipeline' : 300}
NEWSPIDER_MODULE = 'codeReviewSearch.spiders'

#DATABASE = {'drivername': 'local',
 #           'username': 'exybcdg',
  #          'password': 'exybcdg',
   #         'database': 'code_review'}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'codeReviewSearch (+http://www.yourdomain.com)'
