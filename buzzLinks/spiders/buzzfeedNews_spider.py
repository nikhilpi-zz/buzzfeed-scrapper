import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
from buzzLinks.items import BuzzlinksItem
from urlparse import urlparse

class DmozSpider(CrawlSpider):
  name = "buzzfeedNews"
  allowed_domains = ["buzzfeed.com"]
  start_urls = [
    "http://www.buzzfeed.com/"
  ]

  rules = (
        # Extract links matching 'item.php' and parse them with the spider's method parse_item
        Rule(LxmlLinkExtractor(allow_domains=('buzzfeed.com') ), callback='parse_item'),
    )


  def parse_item(self, response):
    items = []
    depth = response.meta["depth"]
    referring_url = response.request.headers.get('Referer', None)
    current_url = response.url
    title = response.xpath('//div[@id="buzz_header"]//h1/text()').extract()
    for link in response.xpath('//div[@id="buzz_sub_buzz"]//div[not(contains(@class,"share-box"))]//a[not(@rel="nofollow")]/@href[not(contains(text(),"buzzfeed") or contains(text(),"buzzfed"))]'):
      l = link.extract()
      if str(l) != "javascript:;":
        item = BuzzlinksItem()
        item["depth"] = depth
        item["current_url"] = current_url
        item["referring_url"] = referring_url
        item["link"] = link.extract()
        item["article_title"] = title
        parsed_uri = urlparse(link.extract())
        domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
        item["link_domain"] = domain

        items.append(item)
    return items
        