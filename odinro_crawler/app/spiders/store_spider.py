import scrapy

from app.items import StoreItem, StoreItemLoader
from app.utils.cookies import get_cookies
import datetime
import re

class StoreSpider(scrapy.Spider):
    name = 'store'

    def start_requests(self):
        username = '2064162186'
        password = 'king88628'
        self.cookies = get_cookies(username, password)
        self.base_url = 'https://odinro.online/vending/?s=/vending/&p={}'
        self.vender_url = 'https://odinro.online/vending/viewshop/?id={}'

        self.start_time = datetime.datetime.now()
        
        yield scrapy.Request(url=self.base_url.format(1), callback=self.parse_page_num, cookies=self.cookies)
        # yield scrapy.Request(url='https://odinro.online/vending/viewshop/?id=134', callback=self.parse, cookies=self.cookies, meta={'store_id':134})
    
    def parse_page_num(self, response):
        page_num_string = response.css('#ranking-page p::text') .get()
        num = int(re.findall(r'\d+', page_num_string)[1])

        for i in range(num):
            yield scrapy.Request(url=self.base_url.format(i+1), callback=self.parse_store_id, cookies=self.cookies, dont_filter=True)

    def parse_store_id(self, response):
        raw_items = response.css('table[class=table] tbody tr')

        for raw_item in raw_items:
            store_id = int(raw_item.css('td:first-child a::text').get())
            yield scrapy.Request(url=self.vender_url.format(store_id), callback=self.parse, cookies=self.cookies, meta={'store_id':store_id})
    
    def parse(self, response):
        raw_items = response.css('table[class*=db-table] tbody tr') 

        store_name = response.css('#page-content h3::text').get()
        store_id = str(response.meta['store_id'])
        position = response.css('#page-content h4::text').get()

        for raw_item in raw_items:
            l = StoreItemLoader(item=StoreItem(), selector=raw_item)
            l.add_css('item_id','td:first-child a::text')
            l.add_css('hole_1', 'td:nth-child(5) * ::text')
            l.add_css('hole_2', 'td:nth-child(6) * ::text')
            l.add_css('hole_3', 'td:nth-child(7) * ::text')
            l.add_css('hole_4', 'td:nth-child(8) * ::text')
            l.add_css('price', 'td:nth-child(9)::text')
            l.add_css('num', 'td:nth-child(10)::text')
            
            level = raw_item.css('td:nth-child(3) strong::text').get()
            level = level if level else '0'
            hole_num = raw_item.css('td:nth-child(4)::text').get().strip()
            hole_num = hole_num if hole_num else '0'
            name = raw_item.css('td:nth-child(2) a::text').get()
            name = name if name else 'No Name'

            l.add_value('name', name)
            l.add_value('store_name', store_name)
            l.add_value('store_id', store_id)
            l.add_value('position', position)
            l.add_value('level', level)
            l.add_value('hole_num', hole_num)        
            l.add_value('time', self.start_time)    

            item = l.load_item()
            yield item


    # def parse(self, response):
    #     raw_items = response.css('table[class*=db-table] tbody tr') 
        
    #     for raw_item in raw_items:
    #         l = StoreItemLoader(item=StoreItem(), raw_item)
            
    #         l.add_css('store_name', 'td:nth-child(1) a::text')
    #         l.add_css('seller_name', 'td:nth-child(2)::text ')
    #         l.add_css('position', 'td:nth-child(3)::text')
    #         l.add_css('name', 'td:nth-child(4) a::text')
    #         l.add_css('item_id', 'td:nth-child(4) a::attr(href)')
    #         l.add_css('hole_1', 'td:nth-child(5) * ::text')
    #         l.add_css('hole_2', 'td:nth-child(6) * ::text')
    #         l.add_css('hole_3', 'td:nth-child(7) * ::text')
    #         l.add_css('hole_4', 'td:nth-child(8) * ::text')
    #         l.add_css('price', 'td:nth-child(9)::text')
    #         l.add_css('num', 'td:nth-child(10)::text')  
    #         l.add_value('time', self.start_time)        

    #         level = raw_item.css('td:nth-child(4) strong::text').get()
    #         level = level if level else '0'
    #         l.add_value('level', level)

    #         item = l.load_item()
    #         yield item