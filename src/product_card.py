import allure
from selenium.webdriver.common.by import By
from src.base_page import BasePage


class ProductCard(BasePage):
    HEADER_PRODUCT_CARD = (By.XPATH, "//h1[text()='Samsung Galaxy Tab 10.1']")
    PRICE = (By.CLASS_NAME, 'price-new')
    ADD_TO_CART_BUTTON = (By.XPATH, "//*[@id='button-cart']")
    IMAGE_PRODUCT = (By.XPATH, "//*[@class='image magnific-popup']")
    REVIEWS = (By.XPATH, "//*[text()='Reviews (0)']")
    REVIEWS_FIELD = (By.XPATH, "//*[@id='form-review']")

    @allure.step("Проверка наличия заголовка товара с наименованием")
    def check_header_product_cart(self):
        self.get_element(self.HEADER_PRODUCT_CARD)

    @allure.step("Проверка наличия цены у товара")
    def check_price(self):
        price = self.get_element(self.PRICE)
        if price:
            return price.text
        else:
            return None

    @allure.step("Проверка наличия кнопки 'Добавить в корзину'")
    def check_button_add_to_cart(self):
        self.get_element(self.ADD_TO_CART_BUTTON)

    @allure.step("Проверка наличия изображения товара")
    def check_image_product(self):
        self.get_element(self.IMAGE_PRODUCT)

    @allure.step("Проверка наличия вкладки 'Reviews'")
    def check_reviews(self):
        self.get_element(self.REVIEWS)

    @allure.step("Нажатие на вкладку 'Reviews'")
    def click_review(self):
        self.get_element(self.REVIEWS).click()

    @allure.step("Проверка наличия поля 'Reviews'")
    def check_reviews_field(self):
        self.get_element(self.REVIEWS_FIELD)
