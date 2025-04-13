from idlelib.mainmenu import menudefs

import pytest
from selenium import webdriver

from ActionPage.login_page import LoginPage
from ActionPage.add_to_cart_py import add_products_to_cart
from Config.configuration import Config


@pytest.fixture(scope="module")
def driver_setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    driver.maximize_window()
    yield driver
    driver.quit()
@pytest.fixture(scope="module")
def login(driver_setup):
    driver = driver_setup
    login_page = LoginPage(driver)
    login_page.open_login_page(Config.BASE_URL)
    return login_page

def test_login_page_on_automation_play_ground_website(login):
    login.username(Config.USERNAME)
    login.password(Config.PASSWORD)
    login.login()

def test_add_to_cart_on_automation_play_ground_website(driver_setup):
    add_products_to_cart(driver_setup)
    add_products_to_cart(Config)

