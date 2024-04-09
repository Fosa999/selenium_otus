from src.admin_page import AdminPage
from src.alert_element import AlertElement
from src.main_page import MainPage
from src.catalog_page import CatalogPage
from src.product_card import ProductCard
from src.registration_users_page import RegistrationUsersPage
from src.shopping_cart_page import ShoppingCartPage

''' Поиск элементов'''


def test_main_page_elements(browser):
    browser.get(browser.base_url)
    MainPage(browser).find_search()
    MainPage(browser).find_carusel_banner_product()
    MainPage(browser).find_carusel_banner_advertising()
    MainPage(browser).find_the_cart_button()
    MainPage(browser).click_cart_button()
    MainPage(browser).find_empty_cart()


def test_catalog_page_elements(browser):
    browser.get(browser.base_url + "/catalog/laptop-notebook")
    CatalogPage(browser).check_product_list()
    CatalogPage(browser).find_element_show_limit()
    CatalogPage(browser).find_element_grid_button()
    CatalogPage(browser).find_element_sort_by()
    CatalogPage(browser).find_element_sort_by_name()


def test_product_card_elements(browser):
    browser.get(browser.base_url + "/product/tablet/samsung-galaxy-tab-10-1")
    ProductCard(browser).check_header_product_cart()
    ProductCard(browser).check_price()
    ProductCard(browser).check_button_add_to_cart()
    ProductCard(browser).check_image_product()
    ProductCard(browser).check_reviews()
    ProductCard(browser).click_review()
    ProductCard(browser).check_reviews_field()


def test_login_admin_page_elements(browser):
    browser.get(browser.base_url + "/administration")
    AdminPage(browser).check_username_field()
    AdminPage(browser).check_password_field()
    AdminPage(browser).check_login_button()
    AdminPage(browser).click_login_button()
    AlertElement(browser).admin_alert()


def test_register_user_page_elements(browser):
    browser.get(browser.base_url + '/en-gb?route=account/register')
    RegistrationUsersPage(browser).check_firstname_field()
    RegistrationUsersPage(browser).check_lastname_field()
    RegistrationUsersPage(browser).check_email_field()
    RegistrationUsersPage(browser).check_password_field()
    RegistrationUsersPage(browser).check_submit_button()
    RegistrationUsersPage(browser).click_submit_button()
    AlertElement(browser).admin_alert()


'''Автотесты'''


def test_auto_login_admin_page(browser):
    browser.get(browser.base_url + "/administration")
    AdminPage(browser).login("user", "bitnami")
    AdminPage(browser).logout_text()


def test_adding_item_to_cart(browser):
    browser.get(browser.base_url)
    MainPage(browser).click_shopping_cart_page()
    ShoppingCartPage(browser).check_empty_shopping_cart()
    MainPage(browser).click_your_store()
    MainPage(browser).click_item_add()
    AlertElement(browser).close_alert()
    MainPage(browser).click_shopping_cart_page()
    ShoppingCartPage(browser).check_cart()


def test_check_price_on_main(browser):
    browser.get(browser.base_url)
    price_dollars = MainPage(browser).price_check()
    MainPage(browser).change_currency_to_eu()
    price_euro = MainPage(browser).price_check()
    for old_price, new_price in zip(price_dollars, price_euro):
        assert old_price != new_price, "Валюта не изменилась"


def test_check_price_in_card(browser):
    browser.get(browser.base_url + "/en-gb/product/canon-eos-5d")
    price_dollar = ProductCard(browser).check_price()
    MainPage(browser).change_currency_to_eu()
    price_euro = ProductCard(browser).check_price()
    for old_price, new_price in zip(price_dollar, price_euro):
        assert old_price != new_price, "Валюта не изменилась"


def test_add_new_product(browser):
    browser.get(browser.base_url + "/administration")
    AdminPage(browser).login("user", "bitnami")
    AdminPage(browser).choose_catalog()
    AdminPage(browser).choose_products()
    AdminPage(browser).add_new_product()
    AdminPage(browser).input_product_name("test")
    AdminPage(browser).input_meta_tag("test")
    AdminPage(browser).choose_data()
    AdminPage(browser).input_model("test")
    AdminPage(browser).choose_seo()
    AdminPage(browser).input_seo_keyword("test")
    AdminPage(browser).save_product()
    AlertElement(browser).check_succes_modified()


def test_del_product(browser):
    browser.get(browser.base_url + "/administration")
    AdminPage(browser).login("user", "bitnami")
    AdminPage(browser).choose_catalog()
    AdminPage(browser).choose_products()
    AdminPage(browser).input_product_name("test")
    AdminPage(browser).apply_filter()
    AdminPage(browser).click_checkbox()
    AdminPage(browser).delete_product()
    AlertElement(browser).alert_accept()
    AlertElement(browser).check_succes_modified()


def test_register_user(browser):
    browser.get(browser.base_url + "/en-gb?route=account/register")
    RegistrationUsersPage(browser).input_firstname("test")
    RegistrationUsersPage(browser).input_lastname("test")
    RegistrationUsersPage(browser).input_email("test@test.test")
    RegistrationUsersPage(browser).input_password("test")
    RegistrationUsersPage(browser).click_checkbox_privaci_policy()
    RegistrationUsersPage(browser).click_continue_button()
    RegistrationUsersPage(browser).check_succes_registration()


def test_change_currency(browser):
    browser.get(browser.base_url)
    MainPage(browser).change_currency_to_eu()
    MainPage(browser).change_currency_to_ster()
    MainPage(browser).change_currency_to_dol()

