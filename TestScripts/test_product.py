from PageObjects.login_page import LoginPage
from PageObjects.base_page import BasePage
from PageObjects.product_page import ProductPage
from TestData.data import Data
from TestLocator.locators import Locators
from Configuration.conftest import driver

# TC-006
def test_product_cards_visibility(driver):
    driver.get(Data.url)
    login_page = LoginPage(driver)
    login_page.enter_username(Data.username)
    login_page.enter_password(Data.password)
    login_page.click_login()

    product_page = ProductPage(driver)
    product_cards = product_page.get_all_product_cards()
    assert product_cards, "No product cards found"

def test_product_cards_count(driver):
    driver.get(Data.url)
    login_page = LoginPage(driver)
    login_page.enter_username(Data.username)
    login_page.enter_password(Data.password)
    login_page.click_login()

    product_page = ProductPage(driver)
    total_product_cards = product_page.get_total_product_cards()

    assert total_product_cards == 6
    print("All product cards visible!")


def test_products_low_to_high(driver):
    driver.get(Data.url)
    login_page = LoginPage(driver)
    login_page.enter_username(Data.username)
    login_page.enter_password(Data.password)
    login_page.click_login()

    product_page = ProductPage(driver)
    product_page.select_sort_option("Price (low to high)")

    # validate the sorted product
    prices = product_page.get_product_prices()
    sorted_prices = sorted(prices)
    assert prices == sorted_prices, "Products are not sorted!"
    print("SUCCESS: Products are sorted!")

def test_add_to_cart(driver):
    driver.get(Data.url)
    login_page = LoginPage(driver)
    login_page.enter_username(Data.username)
    login_page.enter_password(Data.password)
    login_page.click_login()

    product_page = ProductPage(driver)
    product_page.click_add_to_cart_by_product_name("Sauce Labs Backpack")

    # validating the cart count
    cart_count = product_page.get_cart_item_count()
    assert cart_count == 1
    print("SUCCESS: Product added to the cart")

def test_remove_from_cart(driver):
    driver.get(Data.url)
    login_page = LoginPage(driver)
    login_page.enter_username(Data.username)
    login_page.enter_password(Data.password)
    login_page.click_login()

    product_page = ProductPage(driver)
    product_page.click_add_to_cart_by_product_name("Sauce Labs Backpack")
    product_page.click_cart_icon()
    product_page.click_remove_by_product_name()
    cart_count = product_page.get_cart_item_count()
    assert cart_count == 0
    print("SUCCESS: Product removed from cart!")