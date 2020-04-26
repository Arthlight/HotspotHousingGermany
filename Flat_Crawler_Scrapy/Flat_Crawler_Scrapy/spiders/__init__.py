import os
#os.chdir('/Users/arthred/Documents/Flat_Crawler_Django/Flat_Crawler_Scrapy/Flat_Crawler_Scrapy')
#abspath = os.path.abspath(__file__)
#dname = os.path.dirname(abspath)
#os.chdir(dname)
import scrapy
from scrapy.utils.project import get_project_settings
from apscheduler.schedulers.twisted import TwistedScheduler
from scrapy.crawler import CrawlerProcess
from ..items import FlatCrawlerScrapyItem


class ImmobilienScoutSpider(scrapy.Spider):
    name = 'ImmobilienScout'

    # Defined in a list because then you don't need to implement a start_requests() method; If the start_urls class
    # attribute is defined scrapy will fall back to it automatically.
    start_urls = [
        'https://www.immobilienscout24.de/Suche/de/berlin/berlin/wohnung-mieten?pagenumber=1',
        'https://www.immobilienscout24.de/Suche/de/bayern/muenchen/wohnung-mieten?pagenumber=1',
        'https://www.immobilienscout24.de/Suche/de/hamburg/hamburg/wohnung-mieten?pagenumber=1',
    ]

    def parse(self, response):
        flat_items = FlatCrawlerScrapyItem()
        all_flats = response.xpath('//div[@class="result-list-entry__data"]')

        for flatdata in all_flats:
            price = flatdata.get()
            address = flatdata.get().split(', ')
            
            # If price is None we know this is not a normal listing, but a project still in progress or an ad so we
            # continue. If the length of the address is <= 2, we know we didn't get a street address and so ignore this
            # iteration.
            if price is None or len(address) <= 2:
                continue

            sqm = flatdata.xpath('.//dd[@class="font-nowrap font-highlight font-tabular"]/text()').getall()[1].split()[0]
            street = flatdata.get().split(', ')[0].strip()
            area = flatdata.get().split(', ')[1]
            city = flatdata.get().split(', ')[2]
            rooms = flatdata.get()
            detail_view_url = (
                    'https://www.immobilienscout24.de/expose/' +
                    flatdata.get()
            )

            # Special case for price
            price = price.replace('€', '')
            price = price.replace('.', '')
            if ',' in price:
                price = price.split(',')[0]
            if int(price) < 1:
                continue

            # Special case for area:
            if any(char.isdigit() for char in area):
                continue

            # Special case for street:
            if ';' in street:
                street = street.split(';')[0]

            # Special case for sqm
            sqm = sqm.replace(',', '.')
            if float(sqm) < 1:
                continue

            print(sqm)

            # Store the data in item containers instead of regular dicts in order to get access to their richer
            # interface, which supports tracking items to find memory leaks and allows customizing serialization
            flat_items['price'] = price
            flat_items['sqm'] = sqm
            flat_items['street'] = street
            flat_items['area'] = area
            flat_items['city'] = city
            flat_items['rooms'] = rooms
            flat_items['detail_view_url'] = detail_view_url

            yield flat_items

        next_page = response.get()
        if next_page:
            yield response.follow(next_page, self.parse)


def start_crawling():
    process = CrawlerProcess(get_project_settings())
    scheduler = TwistedScheduler()
    #scheduler.add_job(func=process.crawl, trigger='interval', args=[ImmobilienScoutSpider], kwargs={'seconds': 180})
    scheduler.start()
    process.start(False)

