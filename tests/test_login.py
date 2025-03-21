import allure
import logging
from pages.login_page import LoginPage

logger = logging.getLogger(__name__)

@allure.epic("Авторизация пользователя")
@allure.feature("Вход на сайт")
@allure.story("Успешная авторизация")
@allure.severity(allure.severity_level.CRITICAL)
def test_login(browser, config):
    with allure.step("Открываем страницу авторизации"):
        login_page = LoginPage(browser, config.get_base_url())
        login_page.open()

    with allure.step("Вводим логин и пароль"):
        login_page.login("standard_user", "secret_sauce")

    with allure.step("Проверяем, что вход успешный"):
        assert login_page.is_logged_in()

    logger.info('Тест авторизации завершен успешно.')
