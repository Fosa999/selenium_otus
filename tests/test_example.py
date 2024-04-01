from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

''' Поиск элементов'''


def test_main_page_elements(browser):
    browser.get(browser.base_url)
    browser.find_element(By.XPATH, '//*[text()="Your Store"]')
    browser.find_element(By.XPATH, '//*[@id="header-cart"]//button')
    browser.find_element(By.ID, 'carousel-banner-0')
    browser.find_element(By.NAME, 'search')
    browser.find_element(By.XPATH, '//*[@id="header-cart"]//button').click()
    WebDriverWait(browser, timeout=2).until(EC.visibility_of_element_located(
        (By.XPATH, "//*[text()='Your shopping cart is empty!']")))


def test_catalog_page_elements(browser):
    browser.get(browser.base_url + "/catalog/laptop-notebook")
    browser.find_element(By.XPATH, "//*[@id='product-list']")
    browser.find_element(By.XPATH, "//*[@id='input-sort']")
    browser.find_element(By.XPATH, "//*[@id='input-limit']")
    browser.find_element(By.XPATH, "//*[@id='button-grid']")
    WebDriverWait(browser, timeout=1).until(EC.visibility_of_element_located(
        (By.XPATH, "//*[text()='Name (A - Z)']")))


def test_product_card_elements(browser):
    browser.get(browser.base_url + "/product/tablet/samsung-galaxy-tab-10-1")
    browser.find_element(By.XPATH, "//title[text()='Samsung Galaxy Tab 10.1']")
    browser.find_element(By.XPATH, "//h1[text()='Samsung Galaxy Tab 10.1']")
    browser.find_element(By.CLASS_NAME, 'price-new')
    browser.find_element(By.XPATH, "//*[@id='button-cart']")
    browser.find_element(By.XPATH, "//*[@class='image magnific-popup']")
    browser.find_element(By.XPATH, "//*[text()='Reviews (0)']").click()
    WebDriverWait(browser, timeout=1).until(EC.visibility_of_element_located(
        (By.XPATH, "//*[@id='form-review']")))


def test_login_admin_page_elements(browser):
    browser.get(browser.base_url + "/administration")
    browser.find_element(By.XPATH, '//*[text()="Administration"]')
    browser.find_element(By.XPATH, "//*[@id='input-username']")
    browser.find_element(By.XPATH, "//*[@id='input-password']")
    browser.find_element(By.XPATH, "//*[@class='btn btn-primary']").click()
    WebDriverWait(browser, timeout=2).until(EC.visibility_of_element_located(
        (By.XPATH, "//*[@class='alert alert-danger alert-dismissible']")))


def test_register_user_page_elements(browser):
    browser.get(browser.base_url + '/en-gb?route=account/register')
    browser.find_element(By.XPATH, "//*[@name='firstname']")
    browser.find_element(By.XPATH, "//*[@name='lastname']")
    browser.find_element(By.XPATH, "//*[@name='email']")
    browser.find_element(By.XPATH, "//*[@type='password']")
    browser.find_element(By.XPATH, "//*[@type='submit']").click()
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.XPATH, "//*[@class='alert alert-danger alert-dismissible']")))


'''Автотесты'''


def test_auto_login(browser):
    browser.get(browser.base_url + "/administration")
    user_field = WebDriverWait(browser, 1).until(EC.visibility_of_element_located(
        (By.XPATH, "//*[@name='username']")))
    user_field.send_keys("user")
    password_field = WebDriverWait(browser, 1).until(EC.visibility_of_element_located(
        (By.XPATH, "//*[@name='password']")))
    password_field.send_keys("bitnami")
    browser.find_element(By.XPATH, "//*[@type='submit']").click()
    el = WebDriverWait(browser, 3).until(EC.visibility_of_element_located(
        (By.XPATH, "//*[@id='nav-logout']/a/span")))
    assert el.text == "Logout", "Пользователь не авторизован"


def test_adding_item_to_cart(browser):
    browser.get(browser.base_url)
    button_cart = browser.find_element(By.XPATH, "//*[@title='Shopping Cart']")
    button_cart.click()
    empty = browser.find_element(By.XPATH, "//*[@id='content']/h1").text
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.XPATH, "//*[@title='Your Store']"))).click()
    item_add = WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@class="fa-solid fa-shopping-cart"]')))
    item_add.click()
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(
        (By.XPATH, "//*[@class='btn-close']"))).click()
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.XPATH, "//*[@title='Shopping Cart']"))).click()
    filled = browser.find_element(By.XPATH, "//*[@id='content']/h1").text
    assert empty != filled, "Корзина пуста"


def test_check_price_on_main(browser):
    browser.get(browser.base_url)
    old_prise = []
    price_dollars = browser.find_elements(By.XPATH, "//*[@class='price']/span")
    for price_dol in price_dollars:
        old_prise.append(price_dol.text)
    browser.find_element(By.XPATH, "//*[text()='Currency']").click()
    browser.find_element(By.XPATH, "// *[text()='€ Euro']").click()
    new_price = []
    price_euro = browser.find_elements(By.XPATH, "//*[@class='price']/span")
    for price_eu in price_euro:
        new_price.append(price_eu.text)
    assert old_prise != new_price, "Валюта не изменилась"


def test_check_price_in_card(browser):
    browser.get(browser.base_url + "/en-gb/product/canon-eos-5d")
    price_dollar = browser.find_element(By.XPATH, "//*[@class='price-new']").text
    browser.find_element(By.XPATH, "//*[text()='Currency']").click()
    browser.find_element(By.XPATH, "// *[text()='€ Euro']").click()
    price_euro = browser.find_element(By.XPATH, "//*[@class='price-new']").text
    assert price_euro != price_dollar, "Валюта не изменилась"
