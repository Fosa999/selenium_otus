import allure
from selenium.webdriver.common.by import By
from src.base_page import BasePage


class MainPage(BasePage):
    """Header"""
    SHOPPING_CART_PAGE = By.XPATH, "//*[text()='Shopping Cart']"
    CURRENCY = By.XPATH, "//*[text()='Currency']"
    CURRENCY_EURO = By.XPATH, "// *[text()='€ Euro']"
    CURRENCY_STERLING = By.XPATH, "// *[text()='£ Pound Sterling']"
    CURRENCY_DOLLAR = By.XPATH, "// *[text()='$ US Dollar']"
    LOGO = By.XPATH, '//*[text()="Your Store"]'
    CART_BUTTON = By.XPATH, '//*[@id="header-cart"]//button'
    SEARCH = By.NAME, 'search'
    EMPTY_CART = By.XPATH, "//*[text()='Your shopping cart is empty!']"
    YOUR_STORE = By.XPATH, "//*[@title='Your Store']"
    MY_ACCOUNT = By.XPATH, "//*[@class='fa-solid fa-user']"
    """Main"""
    CARUSEL_BANNER_PRODUCT = By.ID, 'carousel-banner-0'
    CARUSEL_BANNER_ADVERTISING = By.XPATH, "//*[@id='carousel-banner-1']"
    ITEM_ADD = By.XPATH, '//*[@class="fa-solid fa-shopping-cart"]'
    PRICE = By.XPATH, "//*[@class='price']/span"

    @allure.step("Поиск кнопки 'Корзина'")
    def find_the_cart_button(self):
        self.get_element(self.CART_BUTTON)

    @allure.step("Клик по кнопке 'Корзина'")
    def click_cart_button(self):
        self.get_element(self.CART_BUTTON).click()

    @allure.step("Поиск поля 'Поиск'")
    def find_search(self):
        self.get_element(self.SEARCH)

    @allure.step("Поиск баннера карусели с товарами")
    def find_carusel_banner_product(self):
        self.get_element(self.CARUSEL_BANNER_PRODUCT)

    @allure.step("Поиск баннера карусели с рекламой")
    def find_carusel_banner_advertising(self):
        self.get_element(self.CARUSEL_BANNER_ADVERTISING)

    @allure.step("Проверка, что корзина пуста")
    def find_empty_cart(self):
        self.get_element(self.EMPTY_CART)

    @allure.step("Переход на страницу корзины")
    def click_shopping_cart_page(self):
        self.get_element(self.SHOPPING_CART_PAGE).click()

    @allure.step("Поиск баннера карусели с товарами")
    def click_your_store(self):
        self.get_element(self.YOUR_STORE).click()

    @allure.step("Добавляем товар в корзину")
    def click_item_add(self):
        self.get_element(self.ITEM_ADD).click()

    @allure.step("Проверяем цены")
    def price_check(self):
        price = self.get_element(self.PRICE)
        if price:
            return price.text
        else:
            return None

    @allure.step("Изменяем валюту на евро")
    def change_currency_to_eu(self):
        self.get_element(self.CURRENCY).click()
        self.get_element(self.CURRENCY_EURO).click()

    @allure.step("Изменяем валюту на фунты")
    def change_currency_to_ster(self):
        self.get_element(self.CURRENCY).click()
        self.get_element(self.CURRENCY_STERLING).click()

    @allure.step("Изменяем валюту на доллары")
    def change_currency_to_dol(self):
        self.get_element(self.CURRENCY).click()
        self.get_element(self.CURRENCY_DOLLAR).click()
