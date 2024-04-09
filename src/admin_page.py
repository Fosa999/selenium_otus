from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

    def choose_catalog(self):
        self.get_element(self.NAVIGATION_CATALOG).click()

    def choose_products(self):
        self.get_element(self.CATALOG_PRODUCTS).click()

    def add_new_product(self):
        self.get_element(self.ADD_NEW).click()

    def input_product_name(self, name):
        self.get_element(self.PRODUCT_NAME_INPUT).send_keys(name)

    def input_meta_tag(self, meta_tag):
        self.get_element(self.META_TAG_TITLE_INPUT).send_keys(meta_tag)

    def choose_data(self):
        self.get_element(self.DATA_ADD_PRODUCT).click()

    def input_model(self, model):
        self.get_element(self.MODEL).send_keys(model)

    def choose_seo(self):
        self.get_element(self.SEO).click()

    def input_seo_keyword(self, keyword):
        self.get_element(self.SEO_KEYWORD).send_keys(keyword)

    def save_product(self):
        self.get_element(self.SAVE_BUTTON).click()

    def apply_filter(self):
        self.get_element(self.FILTER_BUTTON).click()

    def click_checkbox(self):
        self.get_element(self.CHECKBOX).click()

    def delete_product(self):
        self.get_element(self.DELETE_PRODUCT).click()

    # def check_title(self):
    #     self.get_element(self.TITLE)

    def check_username_field(self):
        self.get_element(self.USERNAME_FIELD)

    def check_password_field(self):
        self.get_element(self.PASSWORD_FIELD)

    def check_login_button(self):
        self.get_element(self.LOGIN_BUTTON)

    def click_login_button(self):
        self.get_element(self.LOGIN_BUTTON).click()

    def login(self, username, password):
        self.get_element(self.USERNAME_FIELD).send_keys(username)
        self.get_element(self.PASSWORD_FIELD).send_keys(password)
        self.get_element(self.LOGIN_BUTTON).click()

    def logout_text(self):
        self.get_element(self.LOGOUT)

