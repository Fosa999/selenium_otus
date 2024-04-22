from src.admin_page import AdminPage
from src.alert_element import AlertElement
from src.main_page import MainPage
from src.catalog_page import CatalogPage
from src.product_card import ProductCard
from src.registration_users_page import RegistrationUsersPage
from src.shopping_cart_page import ShoppingCartPage
import allure

''' Поиск элементов'''


@allure.story('Проверка наличия элементов')
@allure.title('Главная страница')
def test_main_page_elements(browser):
    browser.get(browser.base_url)
    main_page = MainPage(browser, browser)

    main_page.find_search()
    main_page.find_carusel_banner_product()
    main_page.find_carusel_banner_advertising()
    main_page.find_the_cart_button()
    main_page.click_cart_button()
    main_page.find_empty_cart()


@allure.story('Проверка наличия элементов')
@allure.title('Каталог')
def test_catalog_page_elements(browser):
    browser.get(browser.base_url + "/catalog/laptop-notebook")
    catalog_page = CatalogPage(browser, browser)

    catalog_page.check_product_list()
    catalog_page.find_element_show_limit()
    catalog_page.find_element_grid_button()
    catalog_page.find_element_sort_by()
    catalog_page.find_element_sort_by_name()


@allure.story('Проверка наличия элементов')
@allure.title('Карточка товара')
def test_product_card_elements(browser):
    browser.get(browser.base_url + "/product/tablet/samsung-galaxy-tab-10-1")
    product_card = ProductCard(browser, browser)

    product_card.check_header_product_cart()
    product_card.check_price()
    product_card.check_button_add_to_cart()
    product_card.check_image_product()
    product_card.check_reviews()
    product_card.click_review()
    product_card.check_reviews_field()


@allure.story('Проверка наличия элементов')
@allure.title('Страница авторизации в админку')
def test_login_admin_page_elements(browser):
    browser.get(browser.base_url + "/administration")
    admin_page = AdminPage(browser, browser)
    alert_element = AlertElement(browser, browser)

    admin_page.check_username_field()
    admin_page.check_password_field()
    admin_page.check_login_button()
    admin_page.click_login_button()
    alert_element.admin_alert()


@allure.story('Проверка наличия элементов')
@allure.title('Страница регистрации нового бользователя')
def test_register_user_page_elements(browser):
    browser.get(browser.base_url + '/en-gb?route=account/register')
    register_user_page = RegistrationUsersPage(browser, browser)
    alert_element = AlertElement(browser, browser)

    register_user_page.check_firstname_field()
    register_user_page.check_lastname_field()
    register_user_page.check_email_field()
    register_user_page.check_password_field()
    register_user_page.check_submit_button()
    register_user_page.click_submit_button()
    alert_element.admin_alert()


'''Автотесты'''


@allure.story('Сценарий администратора')
@allure.title('Авторизация администратором')
def test_auto_login_admin_page(browser):
    browser.get(browser.base_url + "/administration")
    admin_page = AdminPage(browser, browser)

    admin_page.login("user", "bitnami")
    admin_page.logout_text()


@allure.story('Сценарий пользователя')
@allure.title('Добавления товара в корзину')
def test_adding_item_to_cart(browser):
    browser.get(browser.base_url)
    main_page = MainPage(browser, browser)
    shopping_cart = ShoppingCartPage(browser, browser)

    main_page.click_shopping_cart_page()
    shopping_cart.check_empty_shopping_cart()
    main_page.click_your_store()
    main_page.click_item_add()
    AlertElement(browser, browser).close_alert()
    main_page.click_shopping_cart_page()
    shopping_cart.check_cart()


@allure.story('Сценарий пользователя')
@allure.title('Проверка изменения стоимости у товаров при переключении валюты с доллара на евро')
def test_check_price_on_main(browser):
    browser.get(browser.base_url)
    main_page = MainPage(browser, browser)

    price_dollars = main_page.price_check()
    main_page.change_currency_to_eu()
    price_euro = main_page.price_check()
    for old_price, new_price in zip(price_dollars, price_euro):
        assert old_price != new_price, "Валюта не изменилась"


@allure.story('Сценарий пользователя')
@allure.title('Проверка изменения стоимости в карточке товара при переключении валюты с доллара на евро')
def test_check_price_in_card(browser):
    browser.get(browser.base_url + "/en-gb/product/canon-eos-5d")
    main_page = MainPage(browser, browser)
    product_card = ProductCard(browser, browser)

    price_dollar = product_card.check_price()
    main_page.change_currency_to_eu()
    price_euro = product_card.check_price()
    for old_price, new_price in zip(price_dollar, price_euro):
        assert old_price != new_price, "Валюта не изменилась"


@allure.story('Сценарий администратора')
@allure.title('Добавление новой карточки товара')
def test_add_new_product(browser):
    browser.get(browser.base_url + "/administration")
    admin_page = AdminPage(browser, browser)
    alert_element = AlertElement(browser, browser)

    admin_page.login("user", "bitnami")
    admin_page.choose_catalog()
    admin_page.choose_products()
    admin_page.add_new_product()
    admin_page.input_product_name("test")
    admin_page.input_meta_tag("test")
    admin_page.choose_data()
    admin_page.input_model("test")
    admin_page.choose_seo()
    admin_page.input_seo_keyword("test")
    admin_page.save_product()
    alert_element.check_succes_modified()


@allure.story('Сценарий администратора')
@allure.title('Удаление существующей карточки товара')
def test_del_product(browser):
    browser.get(browser.base_url + "/administration")
    admin_page = AdminPage(browser, browser)
    alert_element = AlertElement(browser, browser)

    admin_page.login("user", "bitnami")
    admin_page.choose_catalog()
    admin_page.choose_products()
    admin_page.input_product_name("test")
    admin_page.apply_filter()
    admin_page.click_checkbox()
    admin_page.delete_product()
    alert_element.alert_accept()
    alert_element.check_succes_modified()


@allure.story('Сценарий пользователя')
@allure.title('Регистрация нового пользователя')
def test_register_user(browser):
    browser.get(browser.base_url + "/en-gb?route=account/register")
    register_user_page = RegistrationUsersPage(browser, browser)

    register_user_page.input_firstname("test")
    register_user_page.input_lastname("test")
    register_user_page.input_email("test@test.test")
    register_user_page.input_password("test")
    register_user_page.click_checkbox_privaci_policy()
    register_user_page.click_continue_button()
    register_user_page.check_succes_registration()


@allure.story('Сценарий пользователя')
@allure.title('Изменение валюты')
def test_change_currency(browser):
    browser.get(browser.base_url)
    main_page = MainPage(browser, browser)

    main_page.change_currency_to_eu()
    main_page.change_currency_to_ster()
    main_page.change_currency_to_dol()
