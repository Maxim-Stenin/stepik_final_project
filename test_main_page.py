import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .pages.main_page import MainPage
from .pages.login_page import LoginPage



def go_to_login_page(browser):
    login_link = browser.find_element(By.CSS_SELECTOR, "#registration_link")
    login_link.click()

def test_guest_can_go_to_login_page(browser): 
   link = "http://selenium1py.pythonanywhere.com/"
   page = MainPage(browser, link)
   page.open()
   page.go_to_login_page() 
   page.should_be_login_link()
   login = LoginPage(browser, link)
   login.should_be_login_url()
   login.should_be_login_form()
   login.should_be_register_form()
