from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage
import logging

logger = logging.getLogger(__name__)


class InventoryPage(BasePage):
    path="inventory"

    inventory_table_locator = (By.XPATH, "//*[contains(@class,'inventory_list')]")
    inventory_items_desc_locator = (By.XPATH, "//*[contains(@class, 'inventory_item_desc')]")
    inventory_items_name_locator = (By.XPATH, "//*[contains(@class,'inventory_item_name')]")
    inventory_items_price_locator = (By.XPATH, "//*[contains(@class,'inventory_item_price')]")
    add_remove_btn_inventory_locator = (By.XPATH, "//*[contains(@class, 'btn_inventory')]")
    dropdown_locator = (By.XPATH, "//*[contains(@class, 'product_sort_container')]")
    shopping_cart_badge_locator = (By.XPATH, "//*[contains(@class, 'shopping_cart_badge')]")

    @property
    def inventory_table(self):
        logger.info("Accessing the inventory table")
        return self.element(self.inventory_table_locator)

    @property
    def inventory_first_item_desc(self):
        logger.info("Accessing the description of the first inventory item")
        return self.elements(self.inventory_items_desc_locator)[0]

    @property
    def inventory_first_item_name(self):
        logger.info("Accessing the name of the first inventory item")
        return self.elements(self.inventory_items_name_locator)[0]

    @property
    def inventory_first_item_price(self):
        logger.info("Accessing the price of the first inventory item")
        return self.elements(self.inventory_items_price_locator)[0]

    @property
    def add_remove_btn_first_inventory(self):
        logger.info("Accessing the add/remove button of the first inventory item")
        return self.elements(self.add_remove_btn_inventory_locator)[0]

    @property
    def add_remove_btn_second_inventory(self):
        logger.info("Accessing the add/remove button of the second inventory item")
        return self.elements(self.add_remove_btn_inventory_locator)[1]

    @property
    def inventory_items_price(self):
        logger.info("Accessing the prices of all inventory items")
        return self.elements(self.inventory_items_price_locator)

    @property
    def dropdown(self):
        logger.info("Accessing the dropdown menu for sorting inventory items")
        return self.element(self.dropdown_locator)

    @property
    def shopping_cart_badge(self):
        logger.info("Accessing the shopping cart badge")
        return self.element(self.shopping_cart_badge_locator)

    def click_add_remove_btn_first_inventory(self):
        logger.info("Clicking the add/remove button for the first inventory item")
        self.add_remove_btn_first_inventory.click()
        return self

    def click_add_remove_btn_second_inventory(self):
        logger.info("Clicking the add/remove button for the second inventory item")
        self.add_remove_btn_second_inventory.click()
        return self

    def get_shopping_cart_badge_text(self):
        logger.info("Fetching the text from the shopping cart badge")
        return self.shopping_cart_badge.text

    def select_dropdown(self, option):
        logger.info(f"Selecting the dropdown option: {option}")
        select = Select(self.dropdown)
        select.select_by_visible_text(option)
        return self

    def get_items_price(self):
        logger.info("Fetching the prices of all inventory items")
        return [price.text for price in self.inventory_items_price]

    def get_item_info(self):
        logger.info("Fetching information about the inventory items")
        return {'is_table_present': self.inventory_table.is_displayed(),
                'title': self.inventory_first_item_name.text,
                'desc': self.inventory_first_item_desc.text,
                'price': self.inventory_first_item_price.text,
                'is_btn_inventory_present': self.add_remove_btn_first_inventory.is_displayed()}
