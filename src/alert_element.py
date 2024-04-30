import allure
from selenium.webdriver.common.by import By
from src.base_page import BasePage


class AlertElement(BasePage):
    ALERT = By.XPATH, "//*[@class='alert alert-danger alert-dismissible']"
    CLOSE_ALERT = By.XPATH, "//*[@class='btn-close']"
    SUCCES_MODIFIED_PRODUCT = By.XPATH, "//*[text()=' Success: You have modified products! ']"

    @allure.step("Проверка наличия алерта")
    def admin_alert(self):
        self.get_element(self.ALERT)

    @allure.step("Нажатие на закрытие алерта")
    def close_alert(self):
        self.get_element(self.CLOSE_ALERT).click()

    @allure.step("Проверка наличия успешного алерта ")
    def check_succes_modified(self):
        self.get_element(self.SUCCES_MODIFIED_PRODUCT)

    @allure.step("Подтверждение алерта")
    def alert_accept(self):
        self.alert().accept()
