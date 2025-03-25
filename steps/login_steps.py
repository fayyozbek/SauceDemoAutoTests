import allure
from pages.login_page import LoginPage
from steps.inventory_steps import InventorySteps


class LoginSteps:
    def __init__(self, driver):
        self.page = LoginPage(driver)
    def is_logged_in(self):
        return "inventory" in self.page.current_url

    @allure.step("Login as user: {username}")
    def login_as(self, username, password):
        self.page.open_page() \
            .input_username(username) \
            .input_password(password) \
            .click_login()
        if self.is_logged_in():
            return InventorySteps(self.page.driver)
        return self

    allure.step("Check if the login was unsuccessful")
    def is_error_message(self):
         return self.page.is_error_message_present()
