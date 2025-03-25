from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage


class InventoryPage(BasePage):
    path="inventory"

    inventory_table_locator = (By.XPATH, "//*[contains(@class,'inventory_list')]")
    inventory_items_desc_locator = (By.XPATH, "//*[contains(@class, 'inventory_item_desc')]")
    inventory_items_name_locator = (By.XPATH, "//*[contains(@class,'inventory_item_name')]")
    inventory_items_price_locator = (By.XPATH, "//*[contains(@class,'inventory_item_price')]")
    btn_inventory_locator = (By.XPATH, "//*[contains(@class, 'btn_inventory')]")
    dropdown_locator = (By.XPATH, "//*[contains(@class, 'product_sort_container')]")
    
    @property
    def inventory_table(self):
        return self.element(self.inventory_table_locator)
    @property
    def inventory_first_item_desc(self):
        return self.elements(self.inventory_items_desc_locator)[0]
    @property
    def inventory_first_item_name(self):
        return self.elements(self.inventory_items_name_locator)[0]
    @property
    def inventory_first_item_price(self):
        return self.elements(self.inventory_items_price_locator)[0]
    @property
    def btn_first_inventory(self):
        return self.elements(self.btn_inventory_locator)[0]
    @property
    def inventory_items_price(self):
        return self.elements(self.inventory_items_price_locator)

    @property
    def dropdown(self):
        return self.element(self.dropdown_locator)

    def select_dropdown(self, option):
        select = Select(self.dropdown)
        select.select_by_visible_text(option)
        return self

    def get_items_price(self):
        return [price.text for price in self.inventory_items_price]

    def get_item_info(self):
        return {'is_table_present': self.inventory_table.is_displayed(),
                'title': self.inventory_first_item_name.text,
                'desc': self.inventory_first_item_desc.text,
                'price': self.inventory_first_item_price.text,
                'is_btn_inventory_present': self.btn_first_inventory.is_displayed()}
