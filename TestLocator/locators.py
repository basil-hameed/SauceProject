"""
This file contains all the web locators like xpath, id, tag name, link text etc.,
"""

class Locators:

    # Login Page
    username_locator = "user-name"                   # ID
    password_locator = "password"                    # ID
    login_button_locator = "login-button"            # ID


    # Products Page
    product_card_locator = "inventory_item"    # CLASS NAME
    sort_dropdown_locator = "product_sort_container"  # CLASS NAME
    product_price_locator = "inventory_item_price"  # CLASS NAME
    product_name_locator = "inventory_item_name "  # CLASS NAME
    add_to_cart_button_locator = "//button[contains(text(), 'Add to cart')]" # XPATH
    cart_icon_locator = "shopping_cart_link" # CLASS NAME
    remove_button_locator = "//button[contains(text(), 'Remove')]" # XPATH