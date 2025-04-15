from selenium.webdriver.common.by import By

class LoginLocators:
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN = (By.ID, "login-button")

from selenium.webdriver.common.by import By

class AddToCartLocators:
    PRODUCT_IDS = [
        (By.ID, "add-to-cart-sauce-labs-backpack"),
        (By.ID, "add-to-cart-sauce-labs-bike-light"),
        (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"),
        (By.ID, "add-to-cart-sauce-labs-fleece-jacket"),
        (By.ID, "add-to-cart-sauce-labs-onesie"),
        (By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")
    ]







