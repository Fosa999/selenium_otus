from selenium.webdriver.common.by import By
from src.base_page import BasePage


class CatalogPage(BasePage):
    PRODUCT_LIST = (By.XPATH, "//*[@id='product-list']")
    SHOW_LIMIT = (By.XPATH, "//*[@id='input-limit']")
    GRID_BUTTON = (By.XPATH, "//*[@id='button-grid']")
    SORT_BY = (By.XPATH, "//*[@id='input-sort']")
    SELECTED_SORT = (By.XPATH, "//*[text()='Default' and @selected]")

    def check_product_list(self):
        self.get_element(self.PRODUCT_LIST)

    def find_element_show_limit(self):
        self.get_element(self.SHOW_LIMIT)

    def find_element_grid_button(self):
        self.get_element(self.GRID_BUTTON)

    def find_element_sort_by(self):
        self.get_element(self.SORT_BY)

    def find_element_sort_by_name(self):
        self.get_element(self.SELECTED_SORT)
