from .base_page import BasePage
from .locators import MainPageLocators
from .locators import BasketPageLocators
from .login_page import LoginPage
from selenium import webdriver
from selenium.webdriver.common.by import By

class BasketPage(BasePage):

    def should_be_basket_url(self):
        print("Ссылка страницы корзины:", self.browser.current_url)
        assert "basket" in self.browser.current_url, "Ссылка на странице неверная"

    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_BASKET), "Товары в корзине есть, но быть не должны"

    def should_be_text_basket_empty(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_BASKET_EMPTY), "Нет текста, что корзина пуста"
