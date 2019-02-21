# -*- coding: utf-8 -*-
"""
@author: CHARU

"""

""" 
Resources Used:

1. https://docs.scrapy.org/en/latest/intro/tutorial.html
2. https://stackoverflow.com/questions/26782276/chaining-requests-with-scrapy
3. http://pythonscraping.com/blog/xpath-and-scrapy
4. https://www.yelp.com/
"""

import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ["https://www.yelp.com/biz/shake-shack-new-york-2"]  #starting url of YELP that needs to be scraped


    def parse(self,response):
        #extract 3 objects on a page - user name, user rating to restaurant, date of rating
        username = response.xpath('//meta[@itemprop="author"]/@content').extract()
        userrating = response.xpath('//meta[@itemprop="ratingValue"]/@content').extract()
        datapub = response.xpath('//meta[@itemprop="datePublished"]/@content').extract()

        for item in zip(username,userrating,datapub):   #create a dict using zip() to bind the 3 attributes for every user
            yield {
                            'User Name'               : item[0],
                            'User Rating'             : item[1],
                            'Date Published'          : item[2]
                  }
        #recursive scraping - after page is scraped, go on to next page until end.
        next_page = response.xpath('//link[@rel="next"]/@href').extract_first()  #extract url for next page
        if next_page is not None:
            yield response.follow(next_page,callback = self.parse)