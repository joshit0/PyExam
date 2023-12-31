from utils.locators import *
from pages.base_page import BasePage
from pages.main_page import MainPage


class LoginPage(BasePage):
    def __init__(self, driver):
        self.locator = LoginPageLocators
        super(LoginPage, self).__init__(driver)  # Python2 version

    def set_username(self, username):
        self.find_element(self.locator.USERNAME).send_keys(username)

    def set_password(self, password):
        self.find_element(self.locator.PASSWORD).send_keys(password)

    def click_login_button(self):
        self.find_element(self.locator.LOGIN).click()

    def login(self, username, password):
        print(username)
        self.set_username(username)
        self.set_password(password)
        self.click_login_button()
        return MainPage(self.driver)
