import scrapy
from schoolnews_haut.items import SchoolnewsHautItem

class NewsSpider(scrapy.Spider):
    name = 'zhxx-news'
    # 学校要闻
    allowed_domains = ['www.haut.edu.cn']
    start_urls = ['https://www.haut.edu.cn/xwzx/zhxx.htm']

    def parse(self, response):
        item = SchoolnewsHautItem()
        i = 1
        while 1:
            if response.xpath('/html/body/div/div[2]/div[2]/div[2]/div/div/ul/li[%d]/a/text()' % (i)).extract_first() is None:
                break
            else:
                item['news_name'] = response.xpath(
                    '/html/body/div/div[2]/div[2]/div[2]/div/div/ul/li[%d]/a/text()' % (i)).extract_first()
                item['news_href'] = response.urljoin(response.xpath(
                    '/html/body/div/div[2]/div[2]/div[2]/div/div/ul/li[%d]/a/@href' % (i)).extract_first())
                item['news_date'] = response.xpath(
                    '/html/body/div/div[2]/div[2]/div[2]/div/div/ul/li[%d]/span/text()' % (i)).extract_first()[5:]
                yield item
                i += 1
        pass
