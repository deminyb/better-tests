from .base_page import BasePage
from .locators import ProductPageLocators, BasePageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        assert self.is_element_present(*BasePageLocators.ADD_TO_CART_BUTTON), "No 'Add to basket' button found"
        add_to_basket_button = self.browser.find_element(*BasePageLocators.ADD_TO_CART_BUTTON)
        add_to_basket_button.click()

    def check_item_name(self):
        item_name = self.get_element_text(*ProductPageLocators.ITEM_NAME)
        notification_name = self.get_element_text(*ProductPageLocators.NOTIFICATION_NAME)
        assert item_name == notification_name, f'Name of item is {item_name} and name in notification is {notification_name}'

    def check_basket_sum(self):
        item_price = self.get_element_text(*ProductPageLocators.ITEM_PRICE)
        basket_price = self.get_element_text(*ProductPageLocators.NOTIFICATION_PRICE)
        assert item_price == basket_price, f'Item price is {item_price} and price in basket is {basket_price}'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message should disappear, but it doesn't"
