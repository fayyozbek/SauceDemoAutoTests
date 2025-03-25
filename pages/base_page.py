import logging

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from utilities.configuration import Configuration

logger=logging.getLogger(__name__)

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout
        self.base_url = Configuration().get_base_url()
    @property
    def current_url(self):
        return self.driver.current_url

    def open(self, path=""):
        full_url = self.base_url + path.lstrip("/")
        self.driver.get(full_url)
        logger.info(f"Opening the page {full_url}")
        return self

    def find(self, locator):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            raise AssertionError(f"Element {locator} was not found within {self.timeout} seconds")

    def find_all(self, locator):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                lambda driver: driver.find_elements(*locator)
            )
        except TimeoutException:
            raise AssertionError(f"Elements with locator {locator} were not found within {self.timeout} seconds")

    def element(self, locator):
        """Обёртка над find — просто для читабельности"""
        logger.info(f"Looking for web element with locator {locator}")
        return self.find(locator)

    def elements(self, locator):
        """Wrapper for find_all to return a list of elements with logging."""
        logger.info(f"Looking for multiple web elements with locator {locator}")
        return self.find_all(locator)

