from scrapy import signals
from scrapy.crawler import Crawler
from twisted.internet import reactor
from scrapy.utils.project import get_project_settings
import time, os, sched
 
class manage:
  
    def setupCrawler(self, spiderName):
        crawler = Crawler(get_project_settings())
        crawler.signals.connect(self.spiderClosed, signal=signals.spider_closed)
        #crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
        crawler.configure()
 
        spider = crawler.spiders.create(spiderName)
 
        crawler.crawl(spider)
        crawler.start()
 
 
    def spiderClosed(self):
        reactor.stop()
 
    def run_cr(self):
        crawler = Crawler(get_project_settings())
        crawler.configure()
        for spiderName in crawler.spiders.list():
            if spiderName == "cr":
                self.setupCrawler(spiderName)
        reactor.run()

    def run_delta_cr(self):
       crawler = Crawler(get_project_settings())
       crawler.configure()
       log.start()
       for spiderName in crawler.spiders.list():
           if spiderName == "delta_cr":
               self.setupCrawler(spiderName)
       reactor.run()
 
if __name__ == '__main__':
   handle = manage()
   handle.run_cr()
