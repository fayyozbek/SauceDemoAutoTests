import json
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class Configuration:
    def __init__(self, config_path='utilities/config.json'):
        self.logger = logging.getLogger(__name__)
        self.logger.info(f"Loading configuration from {config_path}.")
        with open(config_path, 'r') as file:
            self.config = json.load(file)

    def get_base_url(self):
        base_url = self.config['base_url']
        self.logger.info(f"Retrieved base URL: {base_url}")
        return base_url

    def get_driver(self, browser_name):
        browser_name = browser_name.lower()
        browsers_config = self.config['browsers']

        if browser_name not in browsers_config:
            self.logger.error(f"Browser configuration for '{browser_name}' is missing in the configuration file.")
            raise ValueError(f"Настройки браузера '{browser_name}' отсутствуют в конфигурации.")

        browser_config = browsers_config[browser_name]
        args = browser_config.get('arguments', [])

        if browser_name == 'chrome':
            self.logger.info("Initializing Chrome WebDriver.")
            options = ChromeOptions()
            for arg in args:
                options.add_argument(arg)
            service = ChromeService(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)

        elif browser_name == 'firefox':
            self.logger.info("Initializing Firefox WebDriver.")
            options = FirefoxOptions()
            for arg in args:
                options.add_argument(arg)
            service = FirefoxService(GeckoDriverManager().install())
            driver = webdriver.Firefox(service=service, options=options)

        else:
            self.logger.error(f"Browser type '{browser_name}' is not supported.")
            raise ValueError(f"Тип браузера '{browser_name}' не поддерживается.")

        driver.implicitly_wait(5)
        return driver
