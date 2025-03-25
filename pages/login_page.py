import logging

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

logger=logging.getLogger(__name__)


class LoginPage(BasePage):
    path = ""

    username_field_locator = (By.XPATH, "//*[@id='user-name']")
    password_field_locator = (By.XPATH, "//*[@id='password']")
    login_button_locator = (By.XPATH, "//*[@id='login-button']")
    error_message_locator = (By.XPATH, "//div[contains(@class, 'error')]")

    @property
    def username_field(self):
        logger.info("Accessing username field")
        return self.element(self.username_field_locator)

    @property
    def password_field(self):
        logger.info("Accessing password field")
        return self.element(self.password_field_locator)

    @property
    def login_button(self):
        logger.info("Accessing login button")
        return self.element(self.login_button_locator)

    @property
    def error_message(self):
        logger.info("Accessing error message")
        return self.element(self.error_message_locator)

    def open_page(self):
        logger.info("Opening login page")
        return self.open(self.path)

    def input_username(self, username):
        logger.info(f"Inputting username: {username}")
        self.username_field.clear()
        self.username_field.send_keys(username)
        return self

    def input_password(self, password):
        logger.info("Inputting password: [hidden]")
        self.password_field.clear()
        self.password_field.send_keys(password)
        return self

    def click_login(self):
        logger.info("Clicking login button")
        self.login_button.click()
        return self

    def is_error_message_present(self):
        logger.info("Checking if error message is present")
        return self.error_message.is_displayed()

