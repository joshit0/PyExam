import time

from behave import *
from pages.login_page import LoginPage
from pages.main_page import MainPage
from selenium import webdriver

from pages.product_detail_page import ProductDetailPage
from pages.cart_page import CartPage


@given('Abro la pagina de DemoBlaze')
def me_logeo_con_mis_credencuales(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.demoblaze.com/")
    context.driver.maximize_window()
    assert "STORE" in context.driver.title


@given('me logeo con mis credenciales')
def me_logeo_con_mis_credenciales(context):
    login = LoginPage(context.driver)
    main = MainPage(context.driver)

    main.click_login_option()
    for row in context.table:
        login.login(row['username'], row['password'])
        main.visible_logout_option()


@when('selecciono categoria "{category}"')
def step_impl(context, category):
    main = MainPage(context.driver)
    main.select_category(category)


@when('selecciono el producto "{item}"')
def step_impl(context, item):
    main = MainPage(context.driver)
    product_detail = ProductDetailPage(context.driver)
    main.select_item(item)
    product_detail.visible_product_title(item)


@when('agrego al carrito el item seleccionado')
def step_impl(context):
    product_detail = ProductDetailPage(context.driver)
    product_detail.add_to_cart();


@then('muestra alerta con mensaje "{expected_message}"')
def step_impl(context, expected_message):
    product_detail = ProductDetailPage(context.driver)
    alert_message = product_detail.get_alert_message();
    print("ALERT MESSAGE STEPDEF: " + alert_message)
    product_detail.accept_alert();


@then('veo el producto "{item}" en el carrito de compras')
def step_impl(context, item):
    main = MainPage(context.driver)
    main.click_cart_option()
    time.sleep(4)
    cart = CartPage(context.driver)
    cart.visible_title()

