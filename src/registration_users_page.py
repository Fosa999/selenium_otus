import allure
from selenium.webdriver.common.by import By
from src.base_page import BasePage


class RegistrationUsersPage(BasePage):
    FIRSTNAME_FIELD = (By.XPATH, "//*[@name='firstname']")
    LASTNAME_FIELD = (By.XPATH, "//*[@name='lastname']")
    EMAIL_FIELD = (By.XPATH, "//*[@name='email']")
    PASSWORD_FIELD = (By.XPATH, "//*[@type='password']")
    SUBMIT_BUTTON = (By.XPATH, "//*[@type='submit']")
    CHECKBOX = By.XPATH, "//*[@name='agree']"
    CONTINUE_BUTTON = By.XPATH, "//*[@class='btn btn-primary']"
    SUCCESS_REGISTRATION = By.XPATH, "//h1[text()='Your Account Has Been Created!']"
    MY_ACCOUNT = By.XPATH, "//*[@class='fa-solid fa-user']"

    @allure.step("Проверка наличия поля 'Firstname'")
    def check_firstname_field(self):
        self.get_element(self.FIRSTNAME_FIELD)

    @allure.step("Ввод значения в поле 'Firstname'")
    def input_firstname(self, firtsname):
        self.get_element(self.FIRSTNAME_FIELD).send_keys(firtsname)

    @allure.step("Проверка наличия поля 'Lastname'")
    def check_lastname_field(self):
        self.get_element(self.LASTNAME_FIELD)

    @allure.step("Ввод значения в поле 'Lastname'")
    def input_lastname(self, lastname):
        self.get_element(self.LASTNAME_FIELD).send_keys(lastname)

    @allure.step("Проверка наличия поля 'EMail'")
    def check_email_field(self):
        self.get_element(self.EMAIL_FIELD)

    @allure.step("Ввод значения в поле 'EMail'")
    def input_email(self, email):
        self.get_element(self.EMAIL_FIELD).send_keys(email)

    @allure.step("Проверка наличия поля 'Password'")
    def check_password_field(self):
        self.get_element(self.PASSWORD_FIELD)

    @allure.step("Ввод значения в поле 'Password'")
    def input_password(self, password):
        self.get_element(self.PASSWORD_FIELD).send_keys(password)

    @allure.step("Проверка наличия кнопки 'Submit'")
    def check_submit_button(self):
        self.get_element(self.SUBMIT_BUTTON)

    @allure.step("Нажатие на кнопку 'Submit'")
    def click_submit_button(self):
        self.get_element(self.SUBMIT_BUTTON).click()

    @allure.step("Нажатие на кнопку 'Submit'")
    def click_checkbox_privaci_policy(self):
        self.get_element(self.CHECKBOX).click()

    @allure.step("Нажатие на кнопку 'Continue'")
    def click_continue_button(self):
        self.get_element(self.CONTINUE_BUTTON, 3).click()

    @allure.step("Проверка успешности регистрации")
    def check_succes_registration(self):
        self.get_element(self.SUCCESS_REGISTRATION, 3)
