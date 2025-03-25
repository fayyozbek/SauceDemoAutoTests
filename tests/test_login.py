import logging

import allure

from steps.login_steps import LoginSteps

logger = logging.getLogger(__name__)


@allure.story("Login functionality")
@allure.description("Test the login functionality with 'standard_user'")
def test_login_valid(browser):
    with allure.step("Starting login test for 'standard_user'."):
        logger.info("Starting login test for 'standard_user'.")
        LoginSteps(browser).login_as("standard_user", "secret_sauce")
        assert "inventory" in browser.current_url
        logger.info("Login test for 'standard_user' completed successfully.")


@allure.story("Login functionality")
@allure.title("Test the login functionality with wrong credentials")
def test_login_invalid(browser):
    with allure.step("Starting login test for 'standard_user'."):
        logger.info("Starting login test for 'standard_user'.")
        LoginSteps(browser).login_as("standard_user", "wrong_password")
        assert LoginSteps(browser).is_error_message(), "Error message not displayed as expected."
