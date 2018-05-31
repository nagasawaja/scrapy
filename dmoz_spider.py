import scrapy
from scrapy.http import Request
import sys
import time
reload(sys)
sys.setdefaultencoding( "utf-8" ) 

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["cmiyu.com"]
    start_urls = []
    i = 1
    for num in range(1, 85): #35582 110 84
        #start_urls.append("http://www.cmiyu.com/qtmy/my35"+str(num)+".html")
        #start_urls.append("http://www.cmiyu.com/etmy/mytid%7D"+str(num)+".html")
        start_urls.append("http://www.cmiyu.com/dwmy/my25"+str(num)+".html")
        
    def parse(self, response):
        output2 = open('./num.txt', 'w')
        output2.write(str(self.i))
        output2.close()
        self.i+=1
        urlList = response.xpath('//div[@class="list"]/ul/li/a/@href').extract()
        for url in urlList:
            yield Request("http://www.cmiyu.com" + url, callback=self.parse2)

        # hxs = HtmlXPathSelector(response)
        # all_urls = hxs.select('//a/@href').extract()
        # output = open('./data.txt', 'w')
        # output.write(divs)
        # output.close()
        
    def parse2(self, response):
        #get miti detail
        mi = response.xpath('//div[@class="md"]/h3/text()').extract()
        tips = response.xpath('//div[@class="zy"]/p/text()').extract()
        if len(mi) > 0:
            if len(tips) == 0 :
                tips.append("null")
            output = open('./data.txt', 'a+')
            output.write(mi[0] + "----" + mi[1] + "----" + tips[0] + "\n")
            output.close()
        else:
            print self.i
            time.sleep(30)