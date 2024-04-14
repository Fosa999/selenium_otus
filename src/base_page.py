import inspect

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging


class BasePage:
    def __init__(self, browser, driver):
        self.driver = driver
        self.browser = browser
        self.logger = driver.logger
        self.class_name = type(self).__name__

    def get_element(self, locator: tuple, timeout=5):
        calling_method_name = inspect.currentframe().f_back.f_code.co_name
        self.logger.debug("Call function: %s", calling_method_name)
        self.logger.debug("%s работаю с элементом %s" % (self.class_name, str(locator)))
        return WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))

    def alert(self, timeout=5):
        return WebDriverWait(self.browser, timeout).until(EC.alert_is_present())
