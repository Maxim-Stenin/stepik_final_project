from .base_page import BasePage
from .locators import MainPageLocators
from .locators import LoginPageLocators
from .locators import ProductPageLocators
from .locators import BasketPageLocators
from selenium import webdriver
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def save_name_product_on_page(self):
        name_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT)
        name_product_text = name_product.text
        print("Название товара в карточке:", name_product_text)
        return name_product_text
        
    def save_price_product_on_page(self):
        price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT)
        price_product_text = price_product.text
        print("Цена товара в карточке:", price_product_text)
        return price_product_text
        
    def add_product_in_basket(self):
        button_add_in_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_PRODUCT)
        button_add_in_basket.click()

    def should_be_alert_name_product(self):
        alert_name_product = self.browser.find_element(*BasketPageLocators.BANNER_ADDED_PRODUCT_NAME)
        alert_name_product_text = alert_name_product.text
        name_product_text = self.save_name_product_on_page()
        print("Баннер с названием товара на странице успеха:", alert_name_product_text)
        assert (name_product_text+" has been added to your basket.") == alert_name_product_text, "Название товара неверное"
    
    def should_be_alert_price_product(self):
        alert_price_product = self.browser.find_element(*BasketPageLocators.BANNER_ADDED_PRODUCT_PRICE)
        alert_price_product_text = alert_price_product.text
        price_product_text = self.save_price_product_on_page()
        print("Баннер с суммой товара на странице успеха:", alert_price_product_text)
        assert ("Your basket total is now "+price_product_text) == alert_price_product_text, "Сумма товара неверная"
    
    # Негативная проверка. Тренировался по курсу
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*BasketPageLocators.BANNER_ADDED_PRODUCT_NAME), "Сообщение успеха есть, но быть не должно"
    
    # Негативная проверка. Тренировался по курсу
    def should_not_be_success_message2(self):
        assert self.is_disappeared(*BasketPageLocators.BANNER_ADDED_PRODUCT_NAME), "Сообщение успеха есть, но быть не должно"

    def go_to_basket(self):
        btn_basket = self.browser.find_element(*ProductPageLocators.BTN_BASKET)
        btn_basket.click()



