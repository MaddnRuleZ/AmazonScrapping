from Scrappers.AmazonScrapper import AmazonScrapper
from misc import FileSystem


class Manager:

    def __init__(self):
        self.asins = []
        self.year = None
        self.month = None
        self.country_id = None
        self.quater_id = None


    def start_program(self):
        print("Select")
        print("[0] Montly")
        print("[1] Quaterly")
        quater_moth_index = input("Enter Number: \n")
        if quater_moth_index == "0":
            self.select_month()
        else:
            self.select_quater()

    def select_month(self):
        asin_urls =[]
        year = input("Enter Year: \n")
        self.year = year

        # default = de
        self.country_id = "de"
        print("Countries:")
        print("Deutschland: [de], USA:[us], Britt:[gb] Niederlande:[nl], Italien: [it], Spanien:[es], Schweden: [se]; Default = de")
        country_input = input("Enter Country ID \n")
        if country_input != "":
            self.country_id = country_input

        self.month = input("Enter Month Number (1-12) \n")

        input("ASINS in Document?, press Enter to Continue \n")
        self.get_asin_list()

        for asin_url in self.asins:
            asin_urls.append(self.get_monthly(asin_url))

        print("Loaded all ASIN LINKS, Ammount:" + str(len(asin_urls)))

        for asin_url in asin_urls:
            ama = AmazonScrapper(asin_url)
            ama.scrape_isin()


    def select_quater(self):
        asin_urls = []
        year = input("Enter Year: \n")
        self.year = year

        # todo print list of available countrys
        country_id = input("Enter Country ID \n")
        self.country_id = country_id
        input("ASINS in Document?, press Enter to Continue \n")

        for asin in self.asins:
            asin_urls.append(self.get_quartal(asin))

        print("Loaded all ASIN LINKS, Ammount:" + str(len(asin_urls)))

        for asin_url in asin_urls:
            ama = AmazonScrapper(asin_url)
            ama.scrape_isin()

    def get_asin_list(self):
        self.asins = FileSystem.read_text_file("dox/input_asins.txt")

    def get_monthly(self, asin):

        month_string = ""
        month = int(self.month)
        if month == 1:
            month_string = "-01-31"
        elif month == 2:
            month_string = "-02-28"
        elif month == 3:
            month_string = "-03-31"
        elif month == 4:
            month_string = "-04-30"
        elif month == 5:
            month_string = "-05-31"
        elif month == 6:
            month_string = "-06-30"
        elif month == 7:
            month_string = "-07-31"
        elif month == 8:
            month_string = "-08-31"
        elif month == 9:
            month_string = "-09-30"
        elif month == 10:
            month_string = "-10-31"
        elif month == 11:
            month_string = "-11-30"
        elif month == 12:
            month_string = "-12-31"

        url = "https://sellercentral.amazon.de/brand-analytics/dashboard/query-performance?view-id=query-performance-asin-view&asin=" \
              + asin + "&reporting-range=monthly&monthly-year=" + self.year + "&" + self.year + "-month=" + self.year + month_string + "&country-id=" + self.country_id
        return url



    def get_quartal(self, asin):
        quater_string = ""
        quater_id = self.quater_id
        if quater_id == 1:
            quater_string = "-03-31"
        elif quater_id == 2:
            quater_string = "-06-30"
        elif quater_id == 3:
            quater_string = "-09-30"
        elif quater_id == 4:
            quater_string = "-12-31"
        url = "https://sellercentral.amazon.de/brand-analytics/dashboard/query-performance?view-id=query-performance-asin-view&asin=" \
              + asin + "&reporting-range=quarterly&quarterly-year=" + self.year + "&" + self.year + "-quarter=" + self.year + quater_string + "&country-id=" + self.country_id
        return url

