



import scrapy

from ..items import MovieInfo

class MojoSpider(scrapy.Spider):

    name = "mojo"

    start_urls = [
      "https://www.boxofficemojo.com/year/2017/",
      "https://www.boxofficemojo.com/year/2018/",
      "https://www.boxofficemojo.com/year/2019/",
      "https://www.boxofficemojo.com/year/2020/"
    ]

    def parse(self, response):

        table_rows = response.xpath('//*[@id="table"]/div/table/tr')[1:10]

        for row in table_rows:
        #for each row in the table, uses xpath selectors
            link = row.xpath('./td[2]/a/@href')
            url = response.urljoin(link[0].extract())

            yield scrapy.Request(url, self.parse_link)

    def parse_link(self, response):

        item = MovieInfo()

        movie_title = response.xpath('//*[@id="a-page"]/main/div/div[1]/div[1]/div/div/div[2]/h1/text()')[0].extract()
        #print(movie_title)

        #title and field name must match
        item['title'] = movie_title

        yield item




    #         href = tr.xpath('./td[2]/a/@href')
    #         #get href
    #         url = response.urljoin(href[0].extract())
    #         #get url from href
    #
    #         yield scrapy.Request(url, callback=self.get_data, meta={'mojo_url': url})
    #
    #
    #
    # def get_data(self, response):
    #     item = BoxItem()
    #     url = reponse.meta['mojo_url']
    #
    #     elements = []
    #
    #     for div in response.xpath('//*[@id="a-page"]/main/div/div[3]/div[4]/div')[0:]:
    #         elements.append(' '.join(div.xpath('./span[1]/text()')[0].extract().split()))
    #
    #         print(elements)
