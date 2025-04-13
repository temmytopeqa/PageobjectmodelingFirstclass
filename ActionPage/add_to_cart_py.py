from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from LocatorPage.locator_page import AddToCartLocators

def add_products_to_cart(driver):
    for locator in AddToCartLocators.PRODUCT_IDS:
        driver.find_element(locator).click()
        time.sleep(1)
