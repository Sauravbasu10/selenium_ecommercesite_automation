# pages/login_page.py
from selenium.webdriver.common.by import By
from .base_page import BasePage
import config
import time
import logging

logger = logging.getLogger(__name__)

class LoginPage(BasePage):
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def login(self, username=config.USERNAME, password=config.PASSWORD):
        logger.info("Performing login")
        self.enter_text(self.USERNAME_FIELD, username)
        self.enter_text(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)
        time.sleep(1)  # Delay to ensure inventory page loads
        logger.info("Login completed")