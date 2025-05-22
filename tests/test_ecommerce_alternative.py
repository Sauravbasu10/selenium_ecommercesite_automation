# tests/test_ecommerce.py
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
import config

class EcommerceTests(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-sync")
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--disable-features=TranslateUI,PasswordManager")
        chrome_options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "safebrowsing.enabled": False,
            "autofill.profile_enabled": False
        })
        
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(config.BASE_URL)
        self.driver.maximize_window()

    def test_ecommerce_flow(self):
        login_page = LoginPage(self.driver)
        inventory_page = InventoryPage(self.driver)
        cart_page = CartPage(self.driver)
        checkout_page = CheckoutPage(self.driver)

        login_page.login()
        inventory_page.add_product_to_cart()
        cart_page.proceed_to_checkout()
        self.assertTrue(checkout_page.verify_checkout(), "Checkout page not displayed")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()