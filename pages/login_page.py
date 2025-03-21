from selenium.webdriver.common.by import By
from pages.base_page import  BasePage

# page_url = /
class LoginPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver,url)
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    PRODUCT_LABEL = (By.CLASS_NAME, "title")

    def login(self, username, password):
        self.send_keys(self.USERNAME_FIELD, username)
        self.send_keys(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)

    def is_logged_in(self):
        return self.is_element_present(self.PRODUCT_LABEL)


