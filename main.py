from Scrappers.AmazonScrapper import AmazonScrapper

if __name__ == '__main__':
    am = AmazonScrapper("https://sellercentral.amazon.de/brand-analytics/dashboard/query-performance?view-id=query-performance-asin-view&asin=B08LHFW932&reporting-range=quarterly&quarterly-year=2024&2024-quarter=2024-03-31&country-id=de")
    am.click_select_cols()

