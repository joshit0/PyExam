from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGOUT = (By.ID, 'logout2')
    LOGIN = (By.ID, 'login2')
    SIGNUP = (By.ID, 'signin2')
    HOME = (By.XPATH, '//div[@id="navbarExample"]/ul/li/a[text()="Home "]')
    CONTACT = (By.XPATH, '//div[@id="navbarExample"]/ul/li/a[text()="Contact"]')
    ABOUT_US = (By.XPATH, '//div[@id="navbarExample"]/ul/li/a[text()="About us "]')
    CART = (By.ID, 'cartur')

    CAT_PHONES = '//a[text()="Phones"]'
    STR_CATEGORY = '//a[text()="[CATEGORY_NAME]"]'
    STR_ITEM = '//h4/a[text()="[ITEM_NAME]"]'


class LoginPageLocators(object):
    USERNAME = (By.ID, 'loginusername')
    PASSWORD = (By.ID, 'loginpassword')
    LOGIN = (By.XPATH, '//button[@onclick="logIn()"]')
    CANCEL = (By.XPATH, '//button[@onclick="logIn()"]/../button[text()="Close"]')


class CartPageLocators(object):
    STR_ITEM = (By.XPATH, '//table/tbody/tr/td[2][text()="[ITEM_NAME]"]')


class ProductDetailPageLocators(object):
    STR_ITEM_TITLE = '//h2[text()="[ITEM_NAME]"]'
    ADD_TO_CART = (By.XPATH, '//a[text()="Add to cart"]')


class CartPageLocators(object):
    PAGE_TITLE = (By.XPATH, '//h2[text()="Products"]')
    STR_ITEM_ADDED = '//table/tbody/tr/td[2][text()="[ITEM_NAME]"]'
