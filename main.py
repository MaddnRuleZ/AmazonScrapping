from Manager import Manager
from Scrappers.AmazonScrapper import AmazonScrapper

def test_scrapper():
    am = AmazonScrapper("https://sellercentral.amazon.de/brand-analytics/dashboard/query-performance?view-id=query-performance-asin-view&asin=B08LHFW932&reporting-range=quarterly&quarterly-year=2024&2024-quarter=2024-03-31&country-id=de", "TB08LHFW932")
    am.scrape_isin()


if __name__ == '__main__':
    test_scrapper()
    # man = Manager()
    # man.start_program()
