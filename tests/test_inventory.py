import allure
import pytest
import logging

from steps.login_steps import LoginSteps

logger = logging.getLogger(__name__)


@allure.story("Inventory Functionality")
class TestInventory:
    @allure.description("Verify that inventory items and details are present")
    def test_inventory_items_are_present(self, browser):
        with allure.step("Starting inventory presence test."):
            logger.info("Executing inventory presence test.")
            item_info = LoginSteps(browser) \
                .login_as("standard_user", "secret_sauce") \
                .get_item_info()
            assert item_info["title"].strip() != "", "Item name should not be empty."
            assert item_info["desc"].strip() != "", "Item description should not be empty."
            assert item_info["price"].strip() != "", "Item price should not be empty."
            assert item_info["is_table_present"], "Inventory table should be present on the page."
            assert item_info["is_btn_inventory_present"], "Inventory buttons should be visible on the page."
            logger.info("Inventory presence test completed successfully.")

    @allure.title("Verify sorting functionality by price")
    @pytest.mark.parametrize("option", ["Price (low to high)", "Price (high to low)"])
    def test_price_sorting_functionality(self, browser, option):
        with allure.step("Starting sorting by price test."):
            logger.info("Executing sorting by price test with option: %s", option)
            item_prices = LoginSteps(browser) \
                .login_as("standard_user", "secret_sauce") \
                .select_sorting_by_price(option)

            if option == "Price (low to high)":
                assert all(item_prices[i] <= item_prices[i + 1] for i in range(len(item_prices) - 1)), \
                    f"Items are not sorted in ascending order: {item_prices} ({option})"
            else:
                assert all(item_prices[i] >= item_prices[i + 1] for i in range(len(item_prices) - 1)), \
                    f"Items are not sorted in descending order: {item_prices} ({option})"
            logger.info("Sorting by price test passed with option: %s", option)

    @allure.title("Verify adding one item to the cart")
    def test_add_single_item_to_cart(self, browser):
        with allure.step("Starting add-to-cart test for one item."):
            logger.info("Executing add-to-cart test for a single item.")
            shopping_cart_badge = LoginSteps(browser) \
                .login_as("standard_user", "secret_sauce") \
                .add_one_item_to_cart
            assert shopping_cart_badge.text == "1", "Item should be added to cart."
            logger.info("Add-to-cart test for one item completed successfully.")

    @allure.title("Verify adding two items to the cart")
    def test_add_two_items_to_cart(self, browser):
        with allure.step("Starting add-to-cart test for two items."):
            logger.info("Executing add-to-cart test for two items.")
            shopping_cart_badge = LoginSteps(browser) \
                .login_as("standard_user", "secret_sauce") \
                .add_two_items_to_cart
            assert shopping_cart_badge.text == "2", "Items should be added to cart."
            logger.info("Add-to-cart test for two items completed successfully.")
