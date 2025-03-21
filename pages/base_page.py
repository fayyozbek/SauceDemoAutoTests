import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

logger = logging.getLogger(__name__)
class BasePage:
    def __init__(self, driver, url=None):
        self.driver = driver
        self.url = url
        logger.info(f'Инициализация страницы: {self.__class__.__name__}')

    def open(self):
        if self.url:
            self.driver.get(self.url)
            logger.info(f'Открыта страница: {self.url}')

    def find_element(self, locator, timeout=10):
        logger.info(f'Поиск элемента {locator}')
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            logger.info(f'Элемент найден: {locator}')
            return element
        except TimeoutException:
            logger.error(f'Элемент не найден: {locator}')
            raise AssertionError(f"Элемент {locator} не найден за {timeout} секунд")

    def click(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        element.click()
        logger.info(f'Клик на элемент: {locator}')

    def send_keys(self, locator, text, timeout=10):
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)
        logger.info(f'Введён текст "{text}" в элемент {locator}')

    def is_element_present(self, locator, timeout=5):
        try:
            self.find_element(locator, timeout)
            logger.info(f'Элемент присутствует: {locator}')
            return True
        except AssertionError:
            logger.info(f'Элемент отсутствует: {locator}')
            return False
