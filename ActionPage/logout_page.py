from LocatorPage.logout_locators import LogoutLocators
import time

def logout(driver):
    # Open the menu
    driver.find_element(*LogoutLocators.MENU_BUTTON).click()
    time.sleep(1)

    # Click logout link
    driver.find_element(*LogoutLocators.LOGOUT_LINK).click()
    time.sleep(2)
