"""
This file contains the product page related methods like get_product name etc.,
"""
from selenium.webdriver.common.by import By
from PageObjects.base_page import BasePage
from TestLocator.locators import Locators
from selenium.webdriver.support.ui import Select

class ProductPage(BasePage):
    # Locators
    PRODUCT_CARDS = (By.CLASS_NAME, Locators.product_card_locator)
    SORT_DROPDOWN = (By.CLASS_NAME, Locators.sort_dropdown_locator)
    PRODUCT_PRICE = (By.CLASS_NAME, Locators.product_price_locator)
    PRODUCT_NAME = (By.CLASS_NAME, Locators.product_name_locator)
    ADD_TO_CART_BUTTON = (By.XPATH, Locators.add_to_cart_button_locator)
    CART_ICON = (By.CLASS_NAME, Locators.cart_icon_locator)
    REMOVE_BUTTON = (By.XPATH, Locators.remove_button_locator)

    def get_all_product_cards(self):
        return self.find_element(self.PRODUCT_CARDS)

    def get_total_product_cards(self):
        return len(self.find_elements(self.PRODUCT_CARDS))

    def select_sort_option(self, option_text):
        dropdown_element = self.is_clickable(self.SORT_DROPDOWN)

        # create a select object to choose by visible text
        select = Select(dropdown_element)
        select.select_by_visible_text(option_text)

    def get_product_prices(self):
        price_elements = self.find_elements(self.PRODUCT_PRICE)
        prices = []
        for element in price_elements:
            price = element.text.strip()
            number = float(price.replace('$', ''))
            prices.append(number)
        return prices

    def click_add_to_cart_by_product_name(self, product_name):
        cards = self.find_elements(self.PRODUCT_CARDS)

        for card in cards:
            name_element = card.find_element(*self.PRODUCT_NAME)
            if name_element.text.strip() == product_name:
                add_button = card.find_element(*self.ADD_TO_CART_BUTTON)
                add_button.click()
                return

    def get_cart_item_count(self):
        count_item = self.find_element(self.CART_ICON).text.strip()
        return int(count_item) if count_item.isdigit() else 0

    def click_remove_by_product_name(self):
        remove_button = self.find_element(self.REMOVE_BUTTON)
        remove_button.click()
        return

    def click_cart_icon(self):
        self.click(self.CART_ICON)



