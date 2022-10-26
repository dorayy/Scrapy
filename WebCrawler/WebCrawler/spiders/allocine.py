import scrapy
from WebCrawler.items import ReviewsAllocineItem
from WebCrawler.pipelines import Database

class AllocineSpider(scrapy.Spider):
    name = 'allocine'
    allowed_domains = ['www.allocine.fr']
    start_urls = [f'http://www.allocine.fr/film/meilleurs/?page={i}' for i in range(1,11)]
    

    Database.connectDb()
    Database.createTable()
    
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        liste_film = response.css('li.mdl')
        
        # Boucle qui parcours l'ensemble des éléments de la liste des films
        for film in liste_film:
            item = ReviewsAllocineItem()

            # Nom du film
            try:
                item['title'] = str(film.css('h2 > a::text').get()).strip()
            except:
                item['title'] = 'None'
              
            # Lien de l'image du film
            try:
                item['img'] = film.css('img.thumbnail-img').attrib['src']
            except:
                item['img'] = 'None'    


            # Auteur du film
            try:
                item['author'] = str(film.css('div.meta-body-direction > a::text').get()).strip()
            except:
                item['author'] = 'None'
           
            # Durée du film
            try:
                item['time'] = str(film.css('div.meta-body-info::text').get()).strip()
            except:
                item['time'] = 'None'

            # Genre cinématographique
            try:
                item['genre'] = '-'.join(film.css('li.mdl div.meta-body-info')[0].css('span::text').extract()[1::])
            except:
                 item['genre'] = 'None'

            # Score du film
            try:
                item['score'] = '-'.join(film.css('span.stareval-note::text').extract()[1::])
            except:
                item['score'] = 'None'

            # Description du film
            try:
                item['desc'] = str(film.css('div.content-txt::text').get()).strip()
            except:
                item['desc'] = 'None'

            # Date de sortie
            try:
                item['release'] = str(film.css('span.date::text').get()).strip()
            except:
                item['release'] = 'None'

            Database.addRow(item)

            yield item         