# pages/base_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)  # Increased timeout to 20 seconds

    def find_element(self, locator):
        try:
            return self.wait.until(EC.element_to_be_clickable(locator))
        except Exception as e:
            logger.error(f"Element with locator {locator} not found: {str(e)}")
            logger.error(f"Current URL: {self.driver.current_url}")
            logger.error(f"Page source: {self.driver.page_source[:1000]}")
            raise

    def click(self, locator):
        try:
            self.handle_alert()
            element = self.find_element(locator)
            element.click()
            logger.info(f"Clicked element with locator {locator}")
        except Exception as e:
            logger.error(f"Failed to click element with locator {locator}: {str(e)}")
            raise

    def enter_text(self, locator, text):
        try:
            self.handle_alert()
            element = self.find_element(locator)
            element.clear()
            element.send_keys(text)
            logger.info(f"Entered text '{text}' in element with locator {locator}")
        except Exception as e:
            logger.error(f"Failed to enter text in element with locator {locator}: {str(e)}")
            raise

    def wait_for_url(self, expected_url):
        try:
            self.wait.until(EC.url_contains(expected_url))
            logger.info(f"URL loaded: {self.driver.current_url}")
        except Exception as e:
            logger.error(f"Failed to load URL containing {expected_url}: {str(e)}")
            raise

    def handle_alert(self):
        try:
            alert = self.driver.switch_to.alert
            logger.info(f"Alert detected: {alert.text}")
            alert.accept()
            return True
        except:
            logger.info("No alert present")
            return False