# -*- coding: utf-8 -*-
import urlparse
import scrapy

from scrapy.http import Request


class RavencrawlerSpider(scrapy.Spider):
    name = 'ravencrawler'
    allowed_domains = ['eraven.franklinpierce.edu']
    start_urls = ['http://eraven.franklinpierce.edu/']

	#setting the location of the output csv file
    custom_settings = {
	#Export as CSV Feed
	'FEED_FORMAT' : 'csv'
    'FEED_URI' : 'eravencrawl.csv'
    }
	
	rules = (
    # Extract links matching 'category.php' (but not matching 'subsection.php')
    # and follow links from them (since no callback means follow=True by default).
    Rule(LinkExtractor(allow=('eraven.franklinpierce',)), callback='parse_item),

	)

    def parse(self, response):
        #Remove XML namespaces
        response.selector.remove_namespaces()
		
        #Extract article information
		titles = response.xpath('//item/title/text()').extract()
        links = response.xpath("//item/link/text()").extract()
        date = response.xpath('//item/pubDate/text()').extract()
		#Extract pdf
        pdf = for href in response.css('a[href$=".pdf"]::attr(href)').extract():
			yield Request(
                url=response.urljoin(href),
                callback=self
            )

       
        #Give the extracted content row wise
        for item in zip(titles,links,date,comments):
            #create a dictionary to store the scraped info
            scraped_info = {
                'titles' : item[0],
                'links' : item[1],
                'date' : item[2],
                'comments' : item[3],
            }

            #yield or give the scraped info to scrapy
            yield scraped_info
