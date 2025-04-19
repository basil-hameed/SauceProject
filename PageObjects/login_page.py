"""
Login page contain methods related to the login action
"""

from selenium.webdriver.common.by import By
from PageObjects.base_page import BasePage
from TestLocator.locators import Locators

class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, Locators.username_locator)
    PASSWORD_INPUT = (By.ID, Locators.password_locator)
    LOGIN_BUTTON = (By.ID, Locators.login_button_locator)

    def enter_username(self, username):
        self.enter_text(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.enter_text(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def validate_username(self):
        return self.is_visible(self.USERNAME_INPUT)

    def validate_password(self):
        return self.is_visible(self.PASSWORD_INPUT)