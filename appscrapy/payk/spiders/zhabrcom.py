import scrapy

#import sqlite3
from payk.spiders.database import Zhabrcom,session,conn
res = 1


class ZhabrcomSpider(scrapy.Spider):
    name = 'zhabrcom'
    custom_settings = {
        'DOWNLOAD_DELAY': 0.25,

    }
    allowed_domains = ['habr.com']
    start_urls = ['https://habr.com/ru/']
    pages_count = 50

    def start_requests(self):
        for page in range(1, 1 + self.pages_count):
            url = f'https://habr.com/ru/page{page}/'
            yield scrapy.Request(url, callback=self.parse_pages)

    def parse_pages(self, response, **kwargs):
        for href in response.css('.post__title_link::attr("href")').extract():
            url = response.urljoin(href)
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response, **kwargs):
        global res

        #data =  response.xpath('//*[@id="post-content-body"]').getall()

        data2 = response.xpath('//*[@id="post-content-body"]//p/text()').getall()

        data3 = response.xpath('//*[@id="post-content-body"]/text()').getall()

        if data2 !=[]:


            item = {
                'url': response.request.url,
                'title': response.css('.post__title-text::text').extract_first('').strip(),
                'created': response.css('.post__time::text').extract_first('').strip(),
                'author': response.css('.user-info__nickname::text').extract_first('').strip(),
                'image': response.xpath('//*[@id="post-content-body"]//img/@src').get(),
                'descript': response.xpath('//*[@id="post-content-body"]').getall(),
                'descrypt_text': data2
            }
        
        elif data3 != []:
            item = {
                'url': response.request.url,
                'title': response.css('.post__title-text::text').extract_first('').strip(),
                'created': response.css('.post__time::text').extract_first('').strip(),
                'author': response.css('.user-info__nickname::text').extract_first('').strip(),
                'image': response.xpath('//*[@id="post-content-body"]//img/@src').get(),
                'descript': response.xpath('//*[@id="post-content-body"]').getall(),
                'descrypt_text': data3
            }

        # elif data3 != []:

        #     item = {
        #         'url': response.request.url,
        #         'title': response.css('.post__title-text::text').extract_first('').strip(),
        #         'created': response.css('.post__time::text').extract_first('').strip(),
        #         'author': response.css('.user-info__nickname::text').extract_first('').strip(),
        #         'image': response.xpath('//div[@class="post__text post__text-html post__text_v1"]//img/@src').getall(),
        #         'descript': data3
        #     }
        # con = sqlite_conn()
        # cur = con.cursor()
        #postgrescreate####myresult = Zhabrcom(url=item['url'], title=item['title'], created=item['created'],author=item['author'], image=item['image'], descrypt=item['descript'],descrypt_text=item['descrypt_text'])
        conn.execute(f"UPDATE zhabrcom SET url=%s,title=%s,created=%s,author=%s,image=%s,descrypt=%s,descrypt_text=%s WHERE id = {res}", (item['url'],item['title'],item['created'],item['author'],item['image'],str(item['descript']),str(item['descrypt_text'])))
        #####create####conn.execute(f"INSERT INTO zhabrcom VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",(res,item['url'],item['title'],item['created'],item['author'],item['image'],str(item['descript']),str(item['descrypt_text'])))
        # con.commit()
        # con.close()############sqlite3
        #session.add(myresult)#################postgres
        ####rows = Zhabrcom.query.filter_by(id = res).update({'url':item['url'], 'title':item['title'], 'created':item['created'],'author':item['author'], 'image':item['image'], 'descrypt':item['descript'],'descrypt_text':item['descrypt_text']})
        ####postgresupdate

        
        print("update susses")
        res += 1

        yield item



