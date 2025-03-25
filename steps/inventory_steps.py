import allure
from pytest_selenium import driver

from pages.inventory_page import InventoryPage


class InventorySteps:
    def __init__(self, driver):
        self.page = InventoryPage(driver)

    @allure.step("Get information about inventory items")
    def get_item_info(self):
        return self.page.get_item_info()

    @allure.step("Select sorting by price option: {option}")
    def select_sorting_by_price(self, option):
        price_in_str = self.page.select_dropdown(option) \
            .get_items_price()
        price_in_float = [float(price.replace("$", "")) for price in price_in_str]
        return price_in_float

    @allure.step("Add one item to the shopping cart")
    def add_one_item_to_cart(self):
        return self.page.click_add_remove_btn_first_inventory() \
            .get_shopping_cart_badge_text()

    @allure.step("Add two items to the shopping cart")
    def add_two_items_to_cart(self):
        return self.page.click_add_remove_btn_first_inventory() \
            .click_add_remove_btn_second_inventory() \
            .get_shopping_cart_badge_text()
