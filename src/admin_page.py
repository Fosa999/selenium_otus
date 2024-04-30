import allure
from selenium.webdriver.common.by import By
from src.base_page import BasePage


class AdminPage(BasePage):
    PATH = "/administration"
    TITLE = By.XPATH, "//*[text()='Administration']"
    USERNAME_FIELD = By.XPATH, "//*[@id='input-username']"
    PASSWORD_FIELD = By.XPATH, "//*[@id='input-password']"
    LOGIN_BUTTON = By.XPATH, "//*[@type='submit']"
    LOGOUT = By.XPATH, "//*[@id='nav-logout']/a/span"

    NAVIGATION_CATALOG = By.XPATH, "//*[@id='menu-catalog']"
    CATALOG_PRODUCTS = By.XPATH, "//*[text()='Products']"
    ADD_NEW = By.XPATH, "//div[@class='float-end']/a[@class='btn btn-primary']"
    PRODUCT_NAME_INPUT = By.XPATH, "//*[@placeholder='Product Name']"
    META_TAG_TITLE_INPUT = By.XPATH, "//*[@placeholder='Meta Tag Title']"
    DATA_ADD_PRODUCT = By.XPATH, "//*[text()='Data']"
    MODEL = By.XPATH, "//*[@placeholder='Model']"
    SEO = By.XPATH, "//*[text()='SEO']"
    SEO_KEYWORD = By.XPATH, "//*[@placeholder='Keyword']"
    SAVE_BUTTON = By.XPATH, "//*[@class='fa-solid fa-floppy-disk']"
    FILTER_BUTTON = By.XPATH, "//*[@id='button-filter']"
    CHECKBOX = By.XPATH, "//*[@type='checkbox' and @name='selected[]']"
    DELETE_PRODUCT = By.XPATH, "//*[@class='btn btn-danger']"

    @allure.step("Клик по каталогу")
    def choose_catalog(self):
        self.get_element(self.NAVIGATION_CATALOG).click()

    @allure.step("Клик по каталогу товаров")
    def choose_products(self):
        self.get_element(self.CATALOG_PRODUCTS).click()

    @allure.step("Клик по кнопке добавления нового товара")
    def add_new_product(self):
        self.get_element(self.ADD_NEW).click()

    @allure.step("Ввод наименования товара")
    def input_product_name(self, name):
        self.get_element(self.PRODUCT_NAME_INPUT).send_keys(name)

    @allure.step("Ввод meta tag")
    def input_meta_tag(self, meta_tag):
        self.get_element(self.META_TAG_TITLE_INPUT).send_keys(meta_tag)

    @allure.step("Переход на вкладку данных прподукта")
    def choose_data(self):
        self.get_element(self.DATA_ADD_PRODUCT).click()

    @allure.step("Ввод модели")
    def input_model(self, model):
        self.get_element(self.MODEL).send_keys(model)

    @allure.step("Клик на вкладку СЕО")
    def choose_seo(self):
        self.get_element(self.SEO).click()

    @allure.step("Ввод значения СЕО")
    def input_seo_keyword(self, keyword):
        self.get_element(self.SEO_KEYWORD).send_keys(keyword)

    @allure.step("Клик по кнопке 'Сохранить'")
    def save_product(self):
        self.get_element(self.SAVE_BUTTON).click()

    @allure.step("Клик по кнопке 'Применить фильтр'")
    def apply_filter(self):
        self.get_element(self.FILTER_BUTTON).click()

    @allure.step("Клик по чекбоксу")
    def click_checkbox(self):
        self.get_element(self.CHECKBOX).click()

    @allure.step("Клик по кнопке 'Удалить продукт'")
    def delete_product(self):
        self.get_element(self.DELETE_PRODUCT).click()

    @allure.step("Проверка наличия поля Username")
    def check_username_field(self):
        self.get_element(self.USERNAME_FIELD)

    @allure.step("Проверка наличия поля Password")
    def check_password_field(self):
        self.get_element(self.PASSWORD_FIELD)

    @allure.step("Проверка наличия кнопки Login")
    def check_login_button(self):
        self.get_element(self.LOGIN_BUTTON)

    @allure.step("Нажатие на кнопку Login")
    def click_login_button(self):
        self.get_element(self.LOGIN_BUTTON).click()

    @allure.step("Авторизация")
    def login(self, username, password):
        self.get_element(self.USERNAME_FIELD).send_keys(username)
        self.get_element(self.PASSWORD_FIELD).send_keys(password)
        self.get_element(self.LOGIN_BUTTON).click()

    @allure.step("Проверка наличия кнопки Logout")
    def logout_text(self):
        self.get_element(self.LOGOUT)
