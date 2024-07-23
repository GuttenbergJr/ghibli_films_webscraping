import scrapy

class FilmsSpider(scrapy.Spider):
    name = "films"
    start_urls = ['https://editorial.rottentomatoes.com/guide/all-studio-ghibli-movies-ranked-by-tomatometer/']

    def parse(self, response):
        for filme in response.css(".countdown-item"):
            yield {
                'rank': filme.css('.countdown-index ::text').get(),
                'titulo': filme.css('.article_movie_title a::text').get(),
                'lancamento': filme.css('.start-year ::text').get()
            }

