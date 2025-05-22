# pages/cart_page.py
from selenium.webdriver.common.by import By
from .base_page import BasePage
import time
import logging

logger = logging.getLogger(__name__)

class CartPage(BasePage):
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def proceed_to_checkout(self):
        logger.info("Verifying cart page is loaded")
        self.wait_for_url("cart.html")
        time.sleep(1)  # Delay to ensure page stability
        logger.info("Checking if checkout button is visible")
        try:
            button = self.find_element(self.CHECKOUT_BUTTON)
            logger.info(f"Checkout button is visible: {button.is_displayed()}")
            time.sleep(1)  # Delay before clicking
            self.click(self.CHECKOUT_BUTTON)
            logger.info("Clicked checkout button successfully")
        except Exception as e:
            logger.error(f"Checkout button interaction failed: {str(e)}")
            raise