import scrapy
from WebCrawler.items import BoursoramaItem
from WebCrawler.pipelines import Database
from datetime import datetime

class BoursoramaSpider(scrapy.Spider):
    name = 'boursorama'
    allowed_domains = ['www.boursorama.com']
    start_urls = [f'https://www.boursorama.com/bourse/actions/palmares/france/?page={i}?france_filter%5Bmarket%5D=1rPCAC' for i in range(1,3)]

    Database.connectDb()
    Database.createTable()

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        listAction = response.css('tbody.c-table__body > tr.c-table__row')

        for action in listAction:
            item  = BoursoramaItem()

            # Index de l'action
            try:
                item['indexStockExchange'] = str(action.css('div > a::text').get()).strip()
            except:
                item['indexStockExchange'] = 'None'
            # cours de l'action
            try:
                item['stockAction'] = str(action.css('span.c-instrument.c-instrument--last::text').get().strip())
            except:
                item['stockAction'] = 'None'
            # Variation de l'action
            try:
                item['variation'] = str(action.css('span.c-instrument.c-instrument--instant-variation::text').get().strip())
            except:
                item['variation'] = 'None'
            # Variation max de l'action
            try:
                item['vMax'] = str(action.css('span.c-instrument.c-instrument--high::text').get().strip())
            except:
                item['vMax'] = 'None'
            # Variation min de l'action
            try:
                item['vMin'] = str(action.css('span.c-instrument.c-instrument--low::text').get().strip())
            except:
                item['vMin'] = 'None'
            # Variation ouverture de l'action
            try:
                item['vOpen'] = str(action.css('span.c-instrument.c-instrument--open::text').get().strip())
            except:
                item['vOpen'] = 'None'
            # Date Collect de l'action
            try:
                item['dateCollect'] = datetime.now()
            except:
                item['dateCollect'] = 'None'
            
            Database.addRowBoursorama(item)

            yield item