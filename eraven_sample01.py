from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from eraven_sample01.items import EravenSampleItem


class MySpider(BaseSpider):
    name = "eraven_sample01"
    allowed_domains = ["eraven.franklinpierce.edu"]
    start_urls = ["https://eraven.franklinpierce.edu"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.xpath("//span[@class='pl']")
        items = []
        for title in titles:
            item = EravenSampleItem()
            item["title"] = title.select('a/span[@id="titletextonly"]/text()').extract()
            item["link"] = title.select("a/@href").extract()
            items.append(item)
        return items
