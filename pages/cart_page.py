import time

from utils.locators import *
from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, driver):
        self.locator = CartPageLocators
        super(CartPage, self).__init__(driver)  # Python2 version

    def visible_title(self):
        self.wait_to_be_visible(self.locator.PAGE_TITLE)

    def visible_product_name(self, item):
        self.build_and_wait_to_be_visible(self.locator.STR_ITEM_TITLE, "[ITEM_NAME]", item)
