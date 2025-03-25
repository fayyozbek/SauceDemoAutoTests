import allure
import pytest

from steps.login_steps import LoginSteps


@allure.story("Inventory Functionality")
@allure.description("Test the inventory functionality")
def test_list_present(browser):
    with (allure.step("Starting inventory test.")):
        item_info=LoginSteps(browser)\
                    .login_as("standard_user", "secret_sauce")\
                    .get_item_info()
        assert item_info["title"].strip() != "", "Item name should not be empty."
        assert item_info["desc"].strip() != "", "Item description should not be empty."
        assert item_info["price"].strip() != "", "Item price should not be empty."
        assert item_info["is_table_present"], "Inventory table should be present on the page."
        assert item_info["is_btn_inventory_present"], "Inventory buttons should be visible on the page."


@allure.story("Inventory Functionality")
@allure.title("Test sorting by price")
@pytest.mark.parametrize("option", ["Price (low to high)", "Price (high to low)"])
def test_sort_by_price(browser, option):
    with (allure.step("Starting sorting by price test.")):
        item_prices = LoginSteps(browser) \
            .login_as("standard_user", "secret_sauce") \
            .select_sorting_by_price(option)

        if option == "Price (low to high)":
            assert all(item_prices[i] <= item_prices[i + 1] for i in range(len(item_prices) - 1)), \
                f"Items are not sorted in ascending order: {item_prices} ({option})"
        else:
            assert all(item_prices[i] >= item_prices[i + 1] for i in range(len(item_prices) - 1)), \
                f"Items are not sorted in descending order: {item_prices} ({option})"
