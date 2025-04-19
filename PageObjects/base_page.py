"""
This Basepage class includes common methods like find_element, click, etc.,
Common page for the different pages like login page, home page and signup page
"""
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import NoSuchElementException

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 15

    def find_element(self, locator):
        try:
            web_element = WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))
            return web_element
        except (TimeoutException, ElementNotVisibleException, NoSuchElementException) as error:
            print("ERROR: ", error)

    def is_visible(self, locator):
        try:
            web_element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))
            return web_element.is_displayed()
        except (TimeoutException, ElementNotVisibleException, NoSuchElementException) as error:
            print("ERROR: ", error)

    def click(self, locator):
        element = self.find_element(locator)
        element.click()

    def enter_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def fetch_title(self):
        return self.driver.title

    def fetch_url(self):
        return self.driver.current_url