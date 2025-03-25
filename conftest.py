import os
import allure
import pytest
from utilities.configuration import Configuration
import logging.config

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Выбери браузер: chrome или firefox"
    )

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        driver = item.funcargs.get('browser')
        if driver:
            allure.attach(driver.get_screenshot_as_png(),
                          name="screenshot",
                          attachment_type=allure.attachment_type.PNG)

@pytest.fixture(scope="session")
def config():
    return Configuration()

@pytest.fixture(scope='session', autouse=True)
def configure_logging():
    config_file_path = os.path.join(os.path.dirname(__file__), 'logging.ini')
    logging.config.fileConfig(config_file_path, disable_existing_loggers=False)
    logging.info('✅ Конфигурация логов успешно загружена!')

@pytest.fixture
def browser(request, config):
    browser_name = request.config.getoption("--browser")
    driver = config.get_driver(browser_name)
    yield driver
    driver.quit()
