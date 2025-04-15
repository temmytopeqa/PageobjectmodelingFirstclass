import pytest
from selenium import webdriver

from ActionPage.login_page import LoginPage
from ActionPage.add_to_cart import add_products_to_cart
from ActionPage.payment_page import complete_payment_process
from ActionPage.logout_page import logout
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
    login.click_button()


def test_add_to_cart_on_automation_play_ground_website(driver_setup):
    add_products_to_cart(driver_setup)


def test_complete_payment_process(driver_setup):
    complete_payment_process(
        driver_setup,
        first_name="John",
        last_name="Doe",
        postal_code="12345"
    )

def test_logout(driver_setup):
    logout(driver_setup)

