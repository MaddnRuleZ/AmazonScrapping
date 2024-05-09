import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GeneralScrapper:

    def __init__(self, url):
        print("Innit Driver")
        self.url = url
        # HEADLESS OPTION
        chrome_options = Options()
        chrome_options.add_argument("user-data-dir=C:/Users/xmadd/Desktop/ChromeSeleniumStorage")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_argument("--window-size=1920,1080")

        try:
            self.driver = webdriver.Chrome(options=chrome_options)
            self.driver.set_window_size(1800, 900)

            # Set page load timeout value in seconds
            page_load_timeout = 30
            # Set script timeout value in seconds
            script_timeout = 30

            # Set page load timeout and script timeout
            self.driver.set_page_load_timeout(page_load_timeout)
            self.driver.set_script_timeout(script_timeout)
            try:
                self.driver.get(url)
                WebDriverWait(self.driver, page_load_timeout).until(
                    EC.presence_of_element_located((By.TAG_NAME, "body")))
            except Exception as e:
                print("Error occurred while loading the page: QUITTING DRIVER", e)
                self.driver.quit()
                raise
        except Exception as e:
            print("Error occurred while initializing the driver:", e)

    '''def load_cookies(self):
        try:
            # Load cookies from file
            with open('cookies.pkl', 'rb') as cookies_file:
                cookies = pickle.load(cookies_file)
                for cookie in cookies:
                    # Check if the cookie domain matches the current domain
                    if 'domain' in cookie and self.url.endswith(cookie['domain']):
                        self.driver.add_cookie(cookie)
                    else:
                        print("Skipping cookie with invalid domain:", cookie)
        except FileNotFoundError:
            print("No saved cookies found.")

    def save_cookies(self):
        try:
            # Save cookies to file
            with open('cookies.pkl', 'wb') as cookies_file:
                pickle.dump(self.driver.get_cookies(), cookies_file)
        except Exception as e:
            print("Error occurred while saving cookies:", e)

    def quit_driver(self):
        self.save_cookies()  # Save cookies before quitting the driver
        self.driver.quit()'''

