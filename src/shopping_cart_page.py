from selenium.webdriver.common.by import By
from src.base_page import BasePage


class ShoppingCartPage(BasePage):
    EMPTY_SHOPPING_CART = By.XPATH, "//p[text()='Your shopping cart is empty!']"
    FILLED_CART = By.XPATH, "//h1[text()='Shopping Cart (0.00kg)']"

    def check_empty_shopping_cart(self):
        self.get_element(self.EMPTY_SHOPPING_CART)

    def check_cart(self):
        self.get_element(self.FILLED_CART)
