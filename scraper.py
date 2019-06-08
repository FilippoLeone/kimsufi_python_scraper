from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import time
import credentials
import message_strings as loginfo
from logger import Logger

class Scraper:
    def __init__(self, arguments='-headless'):
        """
        Start the scraper driver and set its arguments, by default headless mode is enabled.
        """
        self.options = Options()
        self.options.add_argument(arguments)
        self.type = 'ScraperLog'
        self.Logger = Logger()
        self.driver = None

    def __del__(self):
        self.Logger.log(loginfo.DRIVER_KILL, self.type)
        self.driver.quit()

    def create_driver(self, driver_type='Firefox'):
        """
        Creates the driver for Selenium, by default it will use Firefox. 
        """
        # Path to your geckodriver, you can download it from here https://github.com/mozilla/geckodriver/releases
        if driver_type == 'Firefox':
            self.driver = Firefox(executable_path=credentials.driver_path, options=self.options)
        elif driver_type:
            self.driver = Chrome(executable_path=credentials.driver_path, options=self.options)

        self.Logger.log(driver_type+loginfo.DRIVER_OK, self.type)

    def fetch_page(self, url, sleeptime=5):
        """
        Fetches the page through the get method, and sleeps before returning it to wait for JS execution on the target page.
        Sleeptime by default is 5.
        """
        try:
            self.driver.get(url)
            time.sleep(sleeptime)
            self.Logger.log(loginfo.FETCH_OK, self.type)
            return self.driver.page_source
        except:
            self.Logger.log(loginfo.FETCH_ERROR, self.type)


    def run_javascript(self, javascript, return_result=True):
        """
        Method to run JavaScript in the target page, by default it will return the result.
        """
        self.Logger.log(loginfo.JS_OK, self.type)
        if return_result:
            return self.driver.execute_script(javascript)

        self.driver.execute_script(javascript)

