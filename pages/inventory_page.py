# pages/inventory_page.py
from selenium.webdriver.common.by import By
from .base_page import BasePage
import time
import logging

logger = logging.getLogger(__name__)

class InventoryPage(BasePage):
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def add_product_to_cart(self):
        logger.info("Adding product to cart")
        self.click(self.ADD_TO_CART_BUTTON)
        time.sleep(1)  # Delay to ensure cart update
        self.click(self.CART_LINK)
        time.sleep(1)  # Delay to ensure cart page loads
        logger.info("Navigated to cart page")