from .base_page import BasePage
from .locators import MainPageLocators
from .locators import LoginPageLocators
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        print("Ссылка страницы логина:", self.browser.current_url)
        assert "login" in self.browser.current_url, "Ссылка на странице неверная"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        print("Есть форма логина")
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Нет формы логина"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        print("Есть форма регистрации")
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Нет формы регистрации"

    def register_new_user(self, email, password):
        
        input_email = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        input_email.send_keys(email)
        input_pass1 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        input_pass1.send_keys(password)
        input_pass2 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_REPEAT)
        input_pass2.send_keys(password)
        btn_register = self.browser.find_element(*LoginPageLocators.BTN_REGISTER)
        btn_register.click()
