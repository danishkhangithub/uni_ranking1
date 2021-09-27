import scrapy
from scrapy.crawler import CrawlerProcess
import json
import os
import csv

class Olx(scrapy.Spider):
    name = 'olx'
    
    url = 'https://www.timeshighereducation.com/sites/default/files/the_data_rankings/world_impact_rankings_2020_0_en_a6948b0cf3ab518d09334ca087a0cf7a.json'
    
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
    }
    try:
       os.remove('results.csv')
    except OSError:
       pass   
    def __init__(self):
        with open('results.csv', 'w') as csv_file:
            csv_file.write('Name, rank\n')
    
    def start_requests(self):
       
          yield scrapy.Request(url=self.url , headers=self.headers, callback=self.parse)
    
    def parse(self, res):
         data = ''
         with open('res.json', 'r') as json_file:
              for line in json_file:
                  data += line

         data = json.loads(data)
         for offer in data['data']:
            items = {
                'Name': offer['name'],
                'Rank': offer['rank_order'],
              
            }
            #print(items, '\t')
            
        
        
            
            
         
         
            with open('timeshighereducation.csv', 'a') as csv_file:
             writer = csv.DictWriter(csv_file, fieldnames=items.keys())
             writer.writerow(items)
         
    

# run scraper
#process = CrawlerProcess()
#process.crawl(Olx)
#process.start()

# debug
Olx.parse(Olx, '')
