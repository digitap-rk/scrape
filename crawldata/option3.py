from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings

from crawldata.spiders.book import BooksSpider
from crawldata.spiders.quote import AllQuotesSpider


def main():
    configure_logging()
    settings = get_project_settings()
    runner = CrawlerRunner(settings)

    @defer.inlineCallbacks
    def crawl():
        yield runner.crawl(BooksSpider)
        yield runner.crawl(AllQuotesSpider)
        reactor.stop()

    crawl()
    reactor.run()


if __name__ == '__main__':
    main()