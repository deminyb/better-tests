from .base_page import BasePage
from pages.locators import LoginPageLocators
from selenium import webdriver


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        url = str(self.browser.current_url)
        assert 'login' in url, f"Login word is not in current URL{url}"


    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        email_field.send_keys(email)
        password1_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1)
        password1_field.send_keys(password)
        password2_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2)
        password2_field.send_keys(password)
        registration_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        registration_button.click()
