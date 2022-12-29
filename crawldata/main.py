# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


from scrapy.utils.project import get_project_settings

from crawldata.spiders.book import BooksSpider
from crawldata.spiders.quote import AllQuotesSpider
from scrapy.crawler import CrawlerProcess


def main():
    # Step 1
    # process = CrawlerProcess()

    # Step 2
    settings = get_project_settings()
    process = CrawlerProcess(settings)

    process.crawl(BooksSpider)
    process.crawl(AllQuotesSpider)
    process.start()  # the script will block here until the crawling is finished


if __name__ == '__main__':
    main()