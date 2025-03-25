from pytest_selenium import driver

from pages.inventory_page import InventoryPage


class InventorySteps:
    def __init__(self, driver):
        self.page = InventoryPage(driver)

    def get_item_info(self):
        return self.page.get_item_info()

    def select_sorting_by_price(self, option):
        price_in_str = self.page.select_dropdown(option) \
            .get_items_price()
        price_in_float = [float(price.replace("$", "")) for price in price_in_str]
        return price_in_float
