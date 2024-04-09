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

    def check_firstname_field(self):
        self.get_element(self.FIRSTNAME_FIELD)

    def input_firstname(self, firtsname):
        self.get_element(self.FIRSTNAME_FIELD).send_keys(firtsname)

    def check_lastname_field(self):
        self.get_element(self.LASTNAME_FIELD)

    def input_lastname(self, lastname):
        self.get_element(self.LASTNAME_FIELD).send_keys(lastname)

    def check_email_field(self):
        self.get_element(self.EMAIL_FIELD)

    def input_email(self, email):
        self.get_element(self.EMAIL_FIELD).send_keys(email)

    def check_password_field(self):
        self.get_element(self.PASSWORD_FIELD)

    def input_password(self, password):
        self.get_element(self.PASSWORD_FIELD).send_keys(password)

    def check_submit_button(self):
        self.get_element(self.SUBMIT_BUTTON)

    def click_submit_button(self):
        self.get_element(self.SUBMIT_BUTTON).click()

    def click_checkbox_privaci_policy(self):
        self.get_element(self.CHECKBOX).click()

    def click_continue_button(self):
        self.get_element(self.CONTINUE_BUTTON, 1).click()

    def check_succes_registration(self):
        self.get_element(self.SUCCESS_REGISTRATION)

