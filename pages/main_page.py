from .base_page import BasePage
from .locators import MainPageLocators
from .locators import BasketPageLocators
from .login_page import LoginPage
from selenium import webdriver
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def go_to_basket(self):
        btn_basket = self.browser.find_element(*MainPageLocators.BTN_BASKET)
        btn_basket.click()
