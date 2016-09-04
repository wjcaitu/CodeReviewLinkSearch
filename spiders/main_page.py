# spider to scratch the main page of code review 
# 
#

from scrapy.spider import BaseSpider, Spider
from scrapy.selector import Selector
from codeReviewSearch.items import CodereviewsearchItem
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.http import Request

		
class CRMainPageSpider(Spider):
	name = "cr"
	start_urls = ["http://pdupc-codereview.mo.sw.ericsson.se:9988/"]
	
		  
	def parse(self, response):
		sel = Selector(response) 
		sites = sel.xpath('//tr[@name="issue"]')
		print ("sites is ~~~~~%s" %sites)
		tempHref = sel.xpath('//div[@class="pagination"]')
		next_link = None
		for  a in tempHref:
			print ("text is ~~~ %s" %a.xpath('a/text()').extract())
			if a.xpath('a/text()').extract() == [u'Older \u203a']:
				next_link = a.xpath('a/@href').extract()[0]
			elif a.xpath('a/text()').extract() == [u'\u2039 Newer', u'Older \u203a']:
				next_link = a.xpath('a/@href').extract()[1]
			elif a.xpath('a/text()').extract() == [u'\xab Newest', u'\u2039 Newer', u'Older \u203a']:
				next_link = a.xpath('a/@href').extract()[2]
	    
		print ("next_link is ~~~~~%s" %next_link)
			
		for site in sites:
			item = CodereviewsearchItem()
			[url] = site.xpath('./td/div/a[@class="noul"][@id]/@href').extract()
			dateInfo = site.xpath('./td/div[@class="date"]/text()').extract()
			item['link'] = url
			item['title'] = site.xpath('./td/div/a[@class="noul"][@id]/text()').extract()
			item['time'] = site.xpath('./td/div[@class="dateraw"]/text()').extract()
			item['reviwer'] = site.xpath('./td[6]/div[@class="users"]/a/@href').extract()
			item['owner'] = site.xpath('./td[5]/div[@class="users"]/a/@href').extract()
			item['time_diff']= dateInfo
			request = Request(url = "http://pdupc-codereview.mo.sw.ericsson.se:9988"+url, callback = self.parse_item, meta={'item':item})
			yield request
			
		if next_link:
			next_link = "http://pdupc-codereview.mo.sw.ericsson.se:9988" + next_link
			yield Request(url = next_link, callback = self.parse)	
		
	def parse_item(self, response):
		sel = Selector(response)
		patchInfos = sel.xpath('//a[@class="toggled-section opentriangle"][@id!="messages-pointer" and @id!="issue-description-pointer"]/parent::*')
		print ("patchInfos is ~~~~~%s" %patchInfos)
		for patchInfo in patchInfos:
			item = response.meta["item"]
			patch = patchInfo.xpath('a/text()').extract()
			print ("patch is ~~~~~%s" %patch)
			item['msg']= sel.xpath('//pre[@name="cl-message-0" or @name="cl-message-1"]/text()').extract()  #If there is GTT case, message-0 is marvin's comments, otherwise it will be owner's commnets
			item['desc'] = sel.xpath('//div[@id="issue-description"]/pre/text()').extract()
                        item['files'] = sel.xpath('//a[@class="noul"][@title]/text()').extract()
			item['patch'] = patch
			yield item
			
			
class DeltaPageSpider(Spider):
	name = "delta_cr"	
	start_urls = ["http://pdupc-codereview.mo.sw.ericsson.se:9988/"]
	def parse(self, response):
		sel = Selector(response) 
		sites = sel.xpath('//tr[@name="issue"]')
		print ("sites is ~~~~~%s" %sites)
		tempHref = sel.xpath('//div[@class="pagination"]')
		next_link = None
		for  a in tempHref:
			print ("text is ~~~ %s" %a.xpath('a/text()').extract())
			if a.xpath('a/text()').extract() == [u'Older \u203a']:
				next_link = a.xpath('a/@href').extract()[0]
			elif a.xpath('a/text()').extract() == [u'\u2039 Newer', u'Older \u203a']:
				next_link = a.xpath('a/@href').extract()[1]
			elif a.xpath('a/text()').extract() == [u'\xab Newest', u'\u2039 Newer', u'Older \u203a']:
				next_link = a.xpath('a/@href').extract()[2]
	    
		print ("next_link is ~~~~~%s" %next_link)
		for site in sites:
			dateInfo = site.xpath('./td/div[@class="date"]/text()').extract()
			if 'minutes' in dateInfo[0]:
				item = CodereviewsearchItem()
				[url] = site.xpath('./td/div/a[@class="noul"][@id]/@href').extract()
				item['link'] = url
				item['title'] = site.xpath('./td/div/a[@class="noul"][@id]/text()').extract()
				item['time'] = site.xpath('./td/div[@class="dateraw"]/text()').extract()
				item['reviwer'] = site.xpath('./td[6]/div[@class="users"]/a/@href').extract()
				item['owner'] = site.xpath('./td[5]/div[@class="users"]/a/@href').extract()
				item['time_diff']= dateInfo
				request = Request(url = "http://pdupc-codereview.mo.sw.ericsson.se:9988"+url, callback = self.parse_item, meta={'item':item})
				yield request

		if next_link and ('minutes' in dateInfo[0]):
			next_link = "http://pdupc-codereview.mo.sw.ericsson.se:9988" + next_link
			yield Request(url = next_link, callback = self.parse)	
		
	def parse_item(self, response):
		sel = Selector(response)
		patchInfos = sel.xpath('//a[@class="toggled-section opentriangle"][@id!="messages-pointer" and @id!="issue-description-pointer"]/parent::*')
		print ("patchInfos is ~~~~~%s" %patchInfos)
		for patchInfo in patchInfos:
			item = response.meta["item"]
			patch = patchInfo.xpath('a/text()').extract()
			print ("patch is ~~~~~%s" %patch)
			item['patch'] = patch
			item['msg']= sel.xpath('//pre[@name="cl-message-1"]/text()').extract()
			item['desc'] = sel.xpath('//div[@id="issue-description"]/pre/text()').extract()
			yield item
