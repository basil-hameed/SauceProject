import pytest
from PageObjects.login_page import LoginPage
from PageObjects.base_page import BasePage
from TestData.data import Data
from Configuration.conftest import driver

# TC-001
@pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
def test_title(driver):
    driver.get(Data.url)
    base_page = BasePage(driver)

    # asserting expected vs actual title
    assert base_page.fetch_title() == Data.expected_title
    print("SUCCESS: Title is valid")

# TC-002
@pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
def test_url(driver):
    driver.get(Data.url)
    base_page = BasePage(driver)

    # asserting expected vs actual url
    assert base_page.fetch_url() == Data.url
    print("SUCCESS: URL is valid")


# TC-003
@pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
def test_username_input(driver):
    driver.get(Data.url)
    login_page = LoginPage(driver)

    # asserting the username input as True
    username_input_box = login_page.validate_username()
    assert username_input_box == True
    print("SUCCESS: Username Textbox is visible")


# TC-004
@pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
def test_password_input(driver):
    driver.get(Data.url)
    login_page = LoginPage(driver)

    # asserting the username input as True
    password_input_box = login_page.validate_password()
    assert password_input_box == True
    print("SUCCESS: Password Textbox is visible")


# TC-005
@pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
def test_valid_login(driver):
    driver.get(Data.url)
    login_page = LoginPage(driver)

    login_page.enter_username(Data.username)
    login_page.enter_password(Data.password)
    login_page.click_login()

    # assert the login
    assert Data.expected_url == driver.current_url
    print("SUCCESS: Login successful")
