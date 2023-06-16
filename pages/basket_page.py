from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_basket_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS_ALL), \
            "Basket is not empty, some items found"

    def should_be_message_for_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), \
            "No message about empty basket found"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*BasketPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
