import pickle
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import platform
from selenium import webdriver
import time

class GeneralScrapper:

    def __init__(self, url):
        print(url)
        self.url = url


    # todo changed AUCTUNG MIT PFAD; MAYBE CHANGE ZU NEUER DIR UM KEINE ÜBERLAPPUNG ZU HABEN
    def start_browser_instance(self):
        print("Innit Driver")
        # HEADLESS OPTION
        chrome_options = Options()

        # todo EINSTELLUNG FÜR BROWSER SICHTBAR
        # chrome_options.add_argument("--headless")
        # chrome_options.add_argument("user-data-dir=C:/Users/xmadd/Desktop/ChromeSeleniumStorage")

        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        chrome_options.binary_location = "/usr/bin/google-chrome"

        try:
            self.driver = webdriver.Chrome(options=chrome_options)
            time.sleep(2)
            self.driver.set_window_size(1800, 900)
        except Exception as e:
            print(f"An error occurred: {e}")

            page_load_timeout = 30
            script_timeout = 30

            # Set page load timeout and script timeout
            self.driver.set_page_load_timeout(page_load_timeout)
            self.driver.set_script_timeout(script_timeout)
            try:
                self.driver.get(self.url)
                WebDriverWait(self.driver, page_load_timeout).until(
                    EC.presence_of_element_located((By.TAG_NAME, "body")))
                self.set_window_size()
                time.sleep(10)
                return True

            except Exception as e:
                print("Error occurred while loading the page: QUITTING DRIVER", e)
                self.driver.quit()
                return False

        except Exception as e:
            print("Error occurred while initializing the driver:", e)
            self.driver.quit()
            return False

    def set_window_size(self):
        min_width = 1920
        min_height = 1080

        # Get current window size
        current_width = self.driver.execute_script("return window.innerWidth")
        current_height = self.driver.execute_script("return window.innerHeight")

        # Check if current size is smaller than minimum size and resize if necessary
        if current_width < min_width or current_height < min_height:
            self.driver.set_window_size(max(current_width, min_width), max(current_height, min_height))


