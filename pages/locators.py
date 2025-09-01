import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BTN_BASKET = (By.CSS_SELECTOR, ".basket-mini.pull-right.hidden-xs .btn-group .btn.btn-default")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, ".form-group #id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, ".form-group #id_registration-password1")
    REGISTER_PASSWORD_REPEAT = (By.CSS_SELECTOR, ".form-group #id_registration-password2")
    BTN_REGISTER = (By.CSS_SELECTOR, "button[name='registration_submit']")

class ProductPageLocators():
    BUTTON_ADD_PRODUCT = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    NAME_PRODUCT = (By.CSS_SELECTOR, "div.col-sm-6.product_main h1")
    PRICE_PRODUCT = (By.CSS_SELECTOR, "div.col-sm-6.product_main p.price_color")
    BTN_BASKET = (By.CSS_SELECTOR, ".basket-mini.pull-right.hidden-xs .btn-group .btn.btn-default")

class BasketPageLocators():
    BANNER_ADDED_PRODUCT_NAME = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success.fade.in div.alertinner")
    BANNER_ADDED_PRODUCT_PRICE = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-info.fade.in div.alertinner p")
    PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, "#content_inner .basket_summary .basket-items")
    TEXT_BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner p") 

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")