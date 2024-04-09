from selenium.webdriver.common.by import By
from src.base_page import BasePage


class AlertElement(BasePage):
    ALERT = By.XPATH, "//*[@class='alert alert-danger alert-dismissible']"
    CLOSE_ALERT = By.XPATH, "//*[@class='btn-close']"
    SUCCES_MODIFIED_PRODUCT = By.XPATH, "//*[text()=' Success: You have modified products! ']"

    def admin_alert(self):
        self.get_element(self.ALERT)

    # def click_alert(self):
    #     self.get_element(self.ALERT).click()

    def close_alert(self):
        self.get_element(self.CLOSE_ALERT).click()

    def check_succes_modified(self):
        self.get_element(self.SUCCES_MODIFIED_PRODUCT)

    def alert_accept(self):
        self.alert().accept()
