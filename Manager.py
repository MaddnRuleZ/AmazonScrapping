import time
from datetime import datetime

from Scrappers.AmazonScrapper import AmazonScrapper
from misc import FileSystem

class Manager:

    def __init__(self):
        self.asins = []
        self.year = None
        self.month = None
        self.country_id = None
        self.quater_id = None

    # todo cpy
    def start_program(self):
        FileSystem.clear_file("dox/RESULTS/" + self.get_current_date() + ".csv")
        FileSystem.append_string_to_file("dox/RESULTS/" + self.get_current_date() + ".csv", self.get_categories())
        try:
            change_account = input("Account ändern? Tippe: y\n")
            if change_account == "y":
                ama = AmazonScrapper("https://sellercentral.amazon.de", None)
                ama.start_browser_instance()
                input("Änderungen gemacht ?, PRESS Enter, dann neustarten")
                return

            print("Select")
            print("[0] Montly")
            print("[1] Quaterly")
            quater_moth_index = input("Enter Number: \n")
            if quater_moth_index == "0":
                self.select_month()
            else:
                self.select_quater()
        except Exception as e:
            print("Failed Program Startup, restart Program", e)

    def select_month(self):
        asin_urls = []
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
            asin_urls.append(self.get_monthly(asin_url.strip()))

        print("Loaded all ASIN LINKS, Ammount:" + str(len(asin_urls)))

        for indx, asin_url in enumerate(asin_urls):
            try:
                ama = AmazonScrapper(asin_url, self.asins[indx])

                while not ama.start_browser_instance():
                    print("Retrying Starting the Instance")
                    time.sleep(10)

                ama.scrape_isin()
            except:
                print("Failed Iteration: " + str(indx))


    def select_quater(self):
        asin_urls = []
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

        for asin in self.asins:
            asin_urls.append(self.get_quartal(asin))

        print("Loaded all ASIN LINKS, Ammount:" + str(len(asin_urls)))


        for indx, asin_url in enumerate(asin_urls):
            try:
                ama = AmazonScrapper(asin_url, self.asins[indx])

                while not ama.start_browser_instance():
                    print("Retrying Starting the Instance")
                    time.sleep(10)

                ama.scrape_isin()
            except:
                print("Failed Iteration: " + str(indx))

                
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



    # todo cpy below
    def get_current_date(self):
        current_date_time = datetime.now()
        current_date = current_date_time.strftime("%Y-%m-%d")
        return current_date

    def get_categories(self):
        return "Parent ASIN#Suchanfrage#Ergebnis Suchanfrage#Volumen Suchanfrage#Eindrücke Gesamtanzahl#Eindrücke ASIN Anzahl#Eindrücke ASIN Anteil#" \
               "Klicks Gesamtanzahl# Klicks Rate# Klick ASIN Anzahl# Klicks ASIN Anteil# Klicks Preis (Median)#ASIN Preis (Median)#Versand gleicher Tag# Versand 1 Tag# Versand 2 Tage" \
               "Einkaufswagen Gesamtanzahl# Einkaufswagen hinzufügen%# ASIN Anzahl# ASIN Anzeil# Preis Median# ASIN Preis (Median)#Versand gleicher Tag# Versand 1 Tag# Versand 2 Tage" \
               "Käufe Gesamtanzahl# Kauftarif%# ASIN Anzahl# ASIN Anzeil# Preis Median# ASIN Preis (Median)#Versand gleicher Tag# Versand 1 Tag# Versand 2 Tage"