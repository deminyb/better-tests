from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BASKET_BUTTON = (By.XPATH, "//a[@class='btn btn-default']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")



class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTRATION_FORM = (By.ID, 'register_form')
    REGISTRATION_EMAIL = (By.ID, 'id_registration-email')
    REGISTRATION_PASSWORD1 = (By.ID, 'id_registration-password1')
    REGISTRATION_PASSWORD2 = (By.ID, 'id_registration-password2')
    REGISTRATION_BUTTON = (By.NAME, 'registration_submit')

class ProductPageLocators:
    ITEM_NAME = (By.XPATH, "//div[@class='col-sm-6 product_main']/h1")
    ITEM_PRICE = (By.XPATH, "//p[@class='price_color']")
    NOTIFICATION_NAME = (By.XPATH, "//div[@class='alertinner ']/strong")
    NOTIFICATION_PRICE = (By.XPATH, "//div[@id='messages']/div[3]/div[@class='alertinner ']/p/strong")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@id='messages']/div[@class='alert alert-safe alert-noicon alert-success  fade in'][1]")


class BasketPageLocators:
    BASKET_ITEMS_ALL = (By.CSS_SELECTOR, ".basket-items")
    BASKET_EMPTY = (By.XPATH, "//div[@id='content_inner']/p")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@id='messages']/div[@class='alert alert-safe alert-noicon alert-success  fade in'][1]")
