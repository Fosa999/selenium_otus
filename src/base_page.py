from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def get_element(self, locator: tuple, timeout=5):
        return WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))

    def alert(self, timeout=5):
        return WebDriverWait(self.browser, timeout).until(EC.alert_is_present())
