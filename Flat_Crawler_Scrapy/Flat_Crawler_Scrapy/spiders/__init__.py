import scrapy
from scrapy.crawler import CrawlerProcess
from ..items import FlatCrawlerScrapyItem
import os


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
            price = flatdata.xpath('.//dd[@class="font-nowrap font-highlight font-tabular"]/text()').get()
            address = flatdata.xpath('.//button[@title="Auf der Karte anzeigen"]/text()').get().split(', ')
            
            # If price is None we know this is not a normal listing, but a project still in progress or an ad so we
            # continue. If the length of the address is <= 2, we know we didn't get a street address and so ignore this
            # iteration.
            if price is None or len(address) <= 2:
                continue

            sqm = flatdata.xpath('.//dd[@class="font-nowrap font-highlight font-tabular"]/text()').getall()[1].split()[0]
            street = flatdata.xpath('.//button[@title="Auf der Karte anzeigen"]/text()').get().split(', ')[0].strip()
            area = flatdata.xpath('.//button[@title="Auf der Karte anzeigen"]/text()').get().split(', ')[1]
            city = flatdata.xpath('.//button[@title="Auf der Karte anzeigen"]/text()').get().split(', ')[2]
            rooms = flatdata.xpath('.//span[@class="onlyLarge"]/text()').get()
            detail_view_url = (
                    'https://www.immobilienscout24.de/expose/' +
                    flatdata.xpath('.//button[@aria-label="zum Merkzettel hinzufügen"]/@data-id').get()
            )

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

        next_page = response.xpath('//a[@data-nav-next-page="true"]/@href').get()
        if next_page:
            yield response.follow(next_page, self.parse)


class HousinganywhereSpider(scrapy.Spider):
    name = 'Housinganywhere'

    start_urls = [
        'https://housinganywhere.com/s/Berlin--Germany?page=1',
        'https://housinganywhere.com/s/Munich--Germany?page=1',
        'https://housinganywhere.com/s/Hamburg--Germany?page=1',
    ]

    def parse(self, response):
        all_flats = response.xpath(
            '//div[@class="MuiGrid-root MuiGrid-item MuiGrid-grid-xs-12 MuiGrid-grid-sm-12 MuiGrid-grid-md-6"]'
        )
        flat_items = FlatCrawlerScrapyItem()
        city = response.xpath(
            '//h1[@class="MuiTypography-root jss378 MuiTypography-subtitle1 MuiTypography-noWrap"]/text()'
        ).get().split()[-2].replace(',', '')

        for flat in all_flats:
            price = flat.xpath('.//span[@data-test-locator="Listing Card Rent"]/text()').get()
            street = flat.xpath('.//h2[@data-test-locator="Listing Card Title"]/text()').get().split('at ')[1]
            sqm = flat.xpath('.//li[@data-test-locator="Listing Card Extra Info"]/text()').getall()[-1].split()[1]
            detail_view_url = (
                    'https://housinganywhere.com' +
                    flat.xpath('.//a[@data-test-locator="Listing Card"]/@href').get()
            )

            flat_items['price'] = price
            flat_items['street'] = street
            flat_items['sqm'] = sqm
            flat_items['city'] = city
            flat_items['detail_view_url'] = detail_view_url

            yield flat_items

        next_page = response.xpath('//a[@data-test-locator="Pager Next Page"]/@href').get()

        if next_page:
            yield response.follow(next_page, self.parse)


def start_crawling():
    #process = CrawlerProcess()
    #process.crawl(ImmobilienScoutSpider)
    #process.crawl(HousinganywhereSpider)
    #process.start()
    print(os.getcwd())

    #TODO: try adding more directories to syspath, otherwise try splitting the app and do it with containers
    #TODO: evtl auch probieren die relevanten files zu flatcrawlerdjango directory zu adden