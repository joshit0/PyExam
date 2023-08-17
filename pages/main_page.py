from utils.locators import *
from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        self.locator = MainPageLocators
        super(MainPage, self).__init__(driver)  # Python2 version

    def click_login_option(self):
        self.find_element(self.locator.LOGIN).click()

    def visible_logout_option(self):
        self.wait_to_be_visible(self.locator.LOGOUT)


    def click_cart_option(self):
        self.find_element(self.locator.CART).click()


    def select_category(self, category):
        self.build_and_find_element(self.locator.STR_CATEGORY, "[CATEGORY_NAME]", category).click()

    def select_item(self, category):
        self.build_and_find_element(self.locator.STR_ITEM, "[ITEM_NAME]", category).click()
