# 1 - Bibliotecas / Imports
import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('que eu estou na página de login')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(5)
    context.driver.get("https://www.saucedemo.com/")
    context.driver.set_window_size(1552, 832)

@when('eu faço login com "{username}" e "{password}"')
def step_impl(context, username, password):
    context.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys(username)
    context.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys(password)
    context.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()

@then('eu devo ver a página de produtos')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".title").text == "Products"

@then('eu vejo o produto "{product_name}" com o preço "{price}"')
def step_impl(context, product_name, price):
    assert context.driver.find_element(By.CSS_SELECTOR, "#item_4_title_link > .inventory_item_name").text == product_name
    assert context.driver.find_element(By.CSS_SELECTOR, ".inventory_item:nth-child(1) .inventory_item_price").text == price

@when('eu adiciono o produto ao carrinho')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()

@then('o carrinho deve ter "{quantity}" item')
def step_impl(context, quantity):
    assert context.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge").text == quantity

@when('eu visualizo o carrinho')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge").click()

@then('eu vejo que o carrinho contém "{quantity}" "{product_name}" com o preço "{price}"')
def step_impl(context, quantity, product_name, price):
    assert context.driver.find_element(By.CSS_SELECTOR, ".cart_quantity").text == quantity
    assert context.driver.find_element(By.CSS_SELECTOR, ".inventory_item_name").text == product_name
    assert context.driver.find_element(By.CSS_SELECTOR, ".inventory_item_price").text == price

@when('eu removo o produto do carrinho')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"remove-sauce-labs-backpack\"]").click()

@when('eu faço logout')
def step_impl(context):
    context.driver.find_element(By.ID, "react-burger-menu-btn").click()
    context.driver.find_element(By.ID, "logout_sidebar_link").click()

def after_all(context):
    context.driver.quit()
