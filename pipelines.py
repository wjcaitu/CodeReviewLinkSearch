# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

#from sqlalchemy.orm import sessionmaker
from codeReview_db import CodeReviewDb , db_connect, create_code_review_link_table

class CodereviewsearchPipeline(object):

	def process_item(self, item, spider):

		return item
