# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class CodereviewsearchItem(scrapy.Item):
    # define the fields for your item here like:
	link          = Field()
	title         = Field()
	patch       = Field()	
	time        = Field()
	owner      = Field()
	reviwer    = Field()
	time_diff  = Field()
	msg        = Field()
	desc        = Field()
	files        = Field()
     
	 
    
