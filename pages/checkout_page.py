# pages/checkout_page.py
from selenium.webdriver.common.by import By
from .base_page import BasePage

class CheckoutPage(BasePage):
    CHECKOUT_INFO = (By.CLASS_NAME, "checkout_info")

    def verify_checkout(self):
        return self.find_element(self.CHECKOUT_INFO).is_displayed()