# import scrapy
# from scrapy.crawler import CrawlerProcess
# from scrapy.spiders import XMLFeedSpider
#
# class GoogleSpider(scrapy.Spider):
#     name="first"
#     iterator = 'iternodes'
#     itertag = 'item'
#     def __init__(self,category=None):
#         self.category=category
#
#     def start_requests(self):
#
#         yield scrapy.FormRequest(url=f'https://www.bookchor.com/category/34/{self.category}')
#     # def start_requests(self):
#     #     try:
#     #         yield scrapy.FormRequest(url='https://www.bookchor.com/',callback=self.parse,meta={
#     #             'url':'c'
#     #         })
#     #     except Exception as e:
#     #         print("errer in data",e)
#
#     # def parse(self, response, **kwargs):
#
#     def parse_node(self,response,node):
#         try:
#             # print(self.logger.info("error"))
#             self.logger.info('Hi, this is a <%s> node!: %s', self.itertag, ''.join(node.getall()))
#             # here you would extract links to follow and return Requests for
#             # each of them, with another callback
#             print(response.body)
#             pass
#         except Exception as e:
#             print("errer in data", e)
#
# from scrapy.cmdline import execute
# execute("scrapy crawl first -a category='health,-fitness-&-medical'".split())
# # process=CrawlerProcess()
# # process.crawl(GoogleSpider, category="health,-fitness-&-medical")
# # process.start()