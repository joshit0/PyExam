from utils.locators import *
from pages.base_page import BasePage


class ProductDetailPage(BasePage):
    def __init__(self, driver):
        self.locator = ProductDetailPageLocators
        super(ProductDetailPage, self).__init__(driver)  # Python2 version

    def visible_product_title(self, item):
        self.build_and_wait_to_be_visible(self.locator.STR_ITEM_TITLE, "[ITEM_NAME]", item)

    def add_to_cart(self):
        self.find_element(self.locator.ADD_TO_CART).click()

    def get_alert_message(self):
        return self.get_alert_msg()

    def accept_alert(self):
        self.alert_accept()
