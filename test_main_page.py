import pytest

from pages.basket_page import BasketPage
from pages.main_page import MainPage
from pages.login_page import LoginPage
import time

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)
        page.open()  # открываем страницу в браузере
        page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина

        login_page = LoginPage(browser, browser.current_url)
        time.sleep(10)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


@pytest.mark.new
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_basket_items()
    basket_page.should_be_message_for_empty_basket()
    basket_page.should_not_be_success_message()
