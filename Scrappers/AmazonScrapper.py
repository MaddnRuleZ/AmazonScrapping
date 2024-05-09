import time

from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Scrappers.GeneralScrapper import GeneralScrapper
from misc import FileSystem


class AmazonScrapper(GeneralScrapper):

    def __init__(self, url):
        print("Amazon Scrapper initialized")
        super().__init__(url)


    def select_categories(self):
        input("RDY")



    def get_monthly(self, asin, year, month, country_id):
        month_string = ""
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
              + asin + "&reporting-range=monthly&monthly-year=" + year + "&" + year + "-month=" + year + month_string + "&country-id=" + country_id
        print("Curling URL "  + url)
        self.driver.get(url)

    def get_quartal(self, asin, year, quater_id, country_id):
        quater_string = ""
        if quater_id == 1:
            quater_string = "-03-31"
        elif quater_id == 2:
            quater_string = "-06-30"
        elif quater_id == 3:
            quater_string = "-09-30"
        elif quater_id == 4:
            quater_string = "-12-31"
        url = "https://sellercentral.amazon.de/brand-analytics/dashboard/query-performance?view-id=query-performance-asin-view&asin=" \
              + asin + "&reporting-range=quarterly&quarterly-year=" + year + "&" + year + "-quarter=" + year + quater_string + "&country-id=" + country_id
        print("Curling URL "  + url)
        self.driver.get(url)

    def click_select_cols(self):
        time.sleep(2)
        self.find_x_click("/html/body/div[1]/div[2]/div/kat-tabs/kat-tab[2]/div[2]/div/kat-link")
        time.sleep(1)

        # firste ELEM
        # element_to_scroll_to = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/kat-tabs/kat-tab[2]/div[2]/div/kat-modal/div[2]/div/div[7]/div[6]/div/kat-checkbox//div[1]")

        p_3 = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/kat-tabs/kat-tab[2]/div[2]/div/kat-modal/div[2]")
        self.driver.execute_script("argument[0].scrollBy(0, 250);", p_3)

        p_3.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/kat-tabs/kat-tab[2]/div[2]/div/kat-modal/div[2]/div/div[5]/div[4]/div[1]").click()
        p_3.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/kat-tabs/kat-tab[2]/div[2]/div/kat-modal/div[2]/div/div[5]/div[4]/div[2]").click()
        p_3.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/kat-tabs/kat-tab[2]/div[2]/div/kat-modal/div[2]/div/div[5]/div[5]/div[1]").click()
        p_3.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/kat-tabs/kat-tab[2]/div[2]/div/kat-modal/div[2]/div/div[5]/div[5]/div[2]").click()






        '''p_3.find_element(By.XPATH,
                         "/html/body/div[1]/div[2]/div/kat-tabs/kat-tab[2]/div[2]/div/kat-modal/div[2]/div/div[5]/div[5]/div[2]").send_keys(Keys.END)

        scroll_elem = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/kat-tabs/kat-tab[2]/div[2]/div/kat-modal/div[2]")
        self.driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight)", scroll_elem)'''

        '''
        p_3.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/kat-tabs/kat-tab[2]/div[2]/div/kat-modal/div[2]/div/div[5]/div[4]/div[1]").click()
        p_3.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/kat-tabs/kat-tab[2]/div[2]/div/kat-modal/div[2]/div/div[5]/div[4]/div[2]").click()
        p_3.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/kat-tabs/kat-tab[2]/div[2]/div/kat-modal/div[2]/div/div[5]/div[5]/div[1]").click()
        p_3.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/kat-tabs/kat-tab[2]/div[2]/div/kat-modal/div[2]/div/div[5]/div[5]/div[2]").click()
        '''



        input("XXX")

        parent = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/kat-tabs/kat-tab[2]/div[2]/div/kat-modal/div[2]/div")
        checkbox_elements = parent.find_elements(By.CSS_SELECTOR, "[part='checkbox-check']")

        for checkbox in checkbox_elements:
            # Get the label attribute
            label = checkbox.get_attribute("label")
            if label == "Preis (Median)":
                checkbox.click()

            print("Label:", label)

        '''
        self.driver.find_element(By.XPATH, "//div[@aria-label='Preis (Median)']").click()

        self.find_x_click("/html/body/div[1]/div[2]/div/kat-tabs/kat-tab[2]/div[2]/div/kat-modal/div[2]/div/div[5]/div[4]/div[2]/kat-checkbox//div[1]")
        self.find_x_click("/html/body/div[1]/div[2]/div/kat-tabs/kat-tab[2]/div[2]/div/kat-modal/div[2]/div/div[5]/div[5]/div[1]/kat-checkbox//div[1]")
        self.find_x_click("/html/body/div[1]/div[2]/div/kat-tabs/kat-tab[2]/div[2]/div/kat-modal/div[2]/div/div[5]/div[5]/div[2]/kat-checkbox//div[1]")

        # scroll low
        time.sleep(2)
        scroll_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/kat-tabs/kat-tab[2]/div[2]/div/kat-modal//div/div/div[2]")
        self.driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight)", scroll_element)

        # select rest
        self.find_x_click("/html/body/div[1]/div[2]/div/kat-tabs/kat-tab[2]/div[2]/div/kat-modal/div[2]/div/div[7]/div[4]/div[1]/kat-checkbox//div[1]")
        self.find_x_click("/html/body/div[1]/div[2]/div/kat-tabs/kat-tab[2]/div[2]/div/kat-modal/div[2]/div/div[7]/div[5]/div[1]/kat-checkbox//div[1]")
        self.find_x_click("/html/body/div[1]/div[2]/div/kat-tabs/kat-tab[2]/div[2]/div/kat-modal/div[2]/div/div[7]/div[6]/div[1]/kat-checkbox//div[1]")
        time.sleep(2)

        self.find_x_click("/html/body/div[1]/div[2]/div/kat-tabs/kat-tab[2]/div[2]/div/kat-modal/div[2]/div/div[7]/div[4]/div[2]/kat-checkbox//div[1]")
        self.find_x_click("/html/body/div[1]/div[2]/div/kat-tabs/kat-tab[2]/div[2]/div/kat-modal/div[2]/div/div[7]/div[5]/div[2]/kat-checkbox//div[1]")
        time.sleep(2)

        # press finnish
        self.find_x_click("/html/body/div[1]/div[2]/div/kat-tabs/kat-tab[2]/div[2]/div/kat-modal/div[3]/div/kat-button[2]//button/div[2]/slot/span")
        time.sleep(2)
        input("done?")
        '''

    def curl_current(self):
        results = []
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[1]/div[2]/div/kat-tabs/kat-tab[2]/div[3]/div/div[1]/div/div[2]")))

        input("CHECK COLUMBS")

        # Once the element is present, find it
        root_elem = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/kat-tabs/kat-tab[2]/div[3]/div/div[1]/div/div[2]")
        lines = root_elem.find_elements(By.CLASS_NAME, "tr.css-0")
        if not lines:
            print("No Results")
            return None

        for line in lines:
            try:
                columbs = line.find_elements(By.CLASS_NAME, "css-10urxj0")

                delivery_0s = line.find_elements(By.CLASS_NAME, "css-1scl3o")
                delivery_1s = line.find_elements(By.CLASS_NAME, "css-eiin2q")
                delivery_2s = line.find_elements(By.CLASS_NAME, "css-1u3g9zy")

                name = line.find_element(By.CLASS_NAME, "css-iz47zr").text
                href = line.find_element(By.CLASS_NAME, "css-iz47zr").get_attribute("href")
                val_id = columbs[0].text
                volume_general = columbs[1].text

                impressions_general = columbs[2].text
                impressions_asin_ammount = columbs[3].text
                impressions_asin_share = columbs[4].text

                clicks_general = columbs[5].text
                clicks_click_rate = columbs[6].text
                clicks_asin_ammount = columbs[7].text
                clicks_asin_share = columbs[8].text
                click_price_median = columbs[9].text
                click_asin_price_median = columbs[10].text
                click_send_speed_0 = delivery_0s[0].text
                click_send_speed_1 = delivery_1s[0].text
                click_send_speed_2 = delivery_2s[0].text

                cart_general = columbs[11].text
                cart_add = columbs[12].text
                cart_asin_ammount = columbs[13].text
                cart_asin_share = columbs[14].text
                cart_price_median = columbs[15].text
                cart_asin_price_median = columbs[16].text
                cart_send_speed_0 = delivery_0s[1].text
                cart_send_speed_1 = delivery_1s[1].text
                cart_send_speed_2 = delivery_2s[1].text

                buy_general = columbs[17].text
                buy_ratio = columbs[18].text
                buy_asin_ammount = columbs[19].text
                buy_asin_share = columbs[20].text
                buy_price_median = columbs[21].text
                buy_asin_price_median = columbs[22].text
                buy_send_speed_0 = delivery_0s[2].text
                buy_send_speed_1 = delivery_1s[2].text
                buy_send_speed_2 = delivery_2s[2].text

                src = SearchResult(name, href, val_id, volume_general, impressions_general, impressions_asin_ammount,
                                   impressions_asin_share, clicks_general, clicks_click_rate, clicks_asin_ammount,
                                   clicks_asin_share, click_price_median, click_asin_price_median, click_send_speed_0,
                                   click_send_speed_1, click_send_speed_2, cart_general, cart_add, cart_asin_ammount,
                                   cart_asin_share, cart_price_median, cart_asin_price_median, cart_send_speed_0,
                                   cart_send_speed_1, cart_send_speed_2, buy_general, buy_ratio, buy_asin_ammount,
                                   buy_asin_share, buy_price_median, buy_asin_price_median, buy_send_speed_0,
                                   buy_send_speed_1, buy_send_speed_2)

                results.append(src)
                csv_string = src.to_csv_string()
                print(csv_string)
                FileSystem.append_string_to_file("dox/csv_final.csv", csv_string)
            except Exception as e:
                print("ERROR")

        self.get_adjacent_asins(results)



    def get_adjacent_asins(self, results):
        for res in results:
            self.driver.get(res.href)
            time.sleep(2)
            print("X")

            asin_cols = self.driver.find_elements(By.CLASS_NAME, "css-p1ypz0")
            for asin in asin_cols:
                print(asin.text)

    def set_to_100(self):
        print("Set to 100")
        self.scroll_to_bottom()
        input("COMBO")
        self.click_element()

        input("AWAIT")

    def click_element(self):
        try:

            other_elem = self.driver.find_element(By.ID, "query-performance-asin-report-table-page-size-selector")
            other_elem.click()
            time.sleep(1)

            elem = self.driver.find_element(By.XPATH, '/html/body')

            # Press the arrow down key twice
            elem.send_keys(Keys.ARROW_DOWN)
            time.sleep(1)  # Add a small delay to ensure the first arrow down key press is registered
            elem.send_keys(Keys.ARROW_DOWN)
            elem.send_keys(Keys.ENTER)


            print("Element clicked successfully")
        except Exception as e:
            print(f"Error clicking element: {e}")

    def scroll_to_bottom(self):
        try:
            # Find the <body> element
            body = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '/html/body'))
            )
            # Send the "End" key
            time.sleep(2)
            body.send_keys(Keys.END)

            print("Sent the End key successfully.")
        except Exception as e:
            print(f"Error: {e}")



    def find_x_click(self, xpath):
        try:
            button = self.driver.find_element(By.XPATH, xpath)
            button.click()
        except:
            print("Couldn t Find")


class SearchResult:
    def __init__(self, name, href, val_id, volume_general, impressions_general, impressions_asin_ammount,
                 impressions_asin_share, clicks_general, clicks_click_rate, clicks_asin_ammount, clicks_asin_share,
                 click_price_median, click_asin_price_median, click_send_speed_0, click_send_speed_1,
                 click_send_speed_2, cart_general, cart_add, cart_asin_ammount, cart_asin_share, cart_price_median,
                 cart_asin_price_median, cart_send_speed_0, cart_send_speed_1, cart_send_speed_2, buy_general,
                 buy_ratio, buy_asin_ammount, buy_asin_share, buy_price_median, buy_asin_price_median,
                 buy_send_speed_0, buy_send_speed_1, buy_send_speed_2):
        self.name = name
        self.href = href
        self.val_id = val_id
        self.volume_general = volume_general
        self.impressions_general = impressions_general
        self.impressions_asin_ammount = impressions_asin_ammount
        self.impressions_asin_share = impressions_asin_share
        self.clicks_general = clicks_general
        self.clicks_click_rate = clicks_click_rate
        self.clicks_asin_ammount = clicks_asin_ammount
        self.clicks_asin_share = clicks_asin_share
        self.click_price_median = click_price_median
        self.click_asin_price_median = click_asin_price_median
        self.click_send_speed_0 = click_send_speed_0
        self.click_send_speed_1 = click_send_speed_1
        self.click_send_speed_2 = click_send_speed_2
        self.cart_general = cart_general
        self.cart_add = cart_add
        self.cart_asin_ammount = cart_asin_ammount
        self.cart_asin_share = cart_asin_share
        self.cart_price_median = cart_price_median
        self.cart_asin_price_median = cart_asin_price_median
        self.cart_send_speed_0 = cart_send_speed_0
        self.cart_send_speed_1 = cart_send_speed_1
        self.cart_send_speed_2 = cart_send_speed_2
        self.buy_general = buy_general
        self.buy_ratio = buy_ratio
        self.buy_asin_ammount = buy_asin_ammount
        self.buy_asin_share = buy_asin_share
        self.buy_price_median = buy_price_median
        self.buy_asin_price_median = buy_asin_price_median
        self.buy_send_speed_0 = buy_send_speed_0
        self.buy_send_speed_1 = buy_send_speed_1
        self.buy_send_speed_2 = buy_send_speed_2
        self.adjacent_asins = None


    def to_csv_string(self):
        return f"{self.name}#{self.val_id}#{self.volume_general}#{self.impressions_general}#" \
               f"{self.impressions_asin_ammount}#{self.impressions_asin_share}#{self.clicks_general}#" \
               f"{self.clicks_click_rate}#{self.clicks_asin_ammount}#{self.clicks_asin_share}#" \
               f"{self.click_price_median}#{self.click_asin_price_median}#{self.click_send_speed_0}#" \
               f"{self.click_send_speed_1}#{self.click_send_speed_2}#{self.cart_general}#{self.cart_add}#" \
               f"{self.cart_asin_ammount}#{self.cart_asin_share}#{self.cart_price_median}#" \
               f"{self.cart_asin_price_median}#{self.cart_send_speed_0}#{self.cart_send_speed_1}#" \
               f"{self.cart_send_speed_2}#{self.buy_general}#{self.buy_ratio}#{self.buy_asin_ammount}#" \
               f"{self.buy_asin_share}#{self.buy_price_median}#{self.buy_asin_price_median}#" \
               f"{self.buy_send_speed_0}#{self.buy_send_speed_1}#{self.buy_send_speed_2}#{self.href}"

    def add_asin(self, index, asin):
        print("X")
