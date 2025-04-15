import time
from LocatorPage.payment_locators import PaymentLocators

def complete_payment_process(driver, first_name, last_name, postal_code):
    driver.find_element(*PaymentLocators.CHECKOUT_BUTTON).click()
    time.sleep(1)

    driver.find_element(*PaymentLocators.FIRST_NAME).send_keys(first_name)
    driver.find_element(*PaymentLocators.LAST_NAME).send_keys(last_name)
    driver.find_element(*PaymentLocators.POSTAL_CODE).send_keys(postal_code)
    time.sleep(1)

    driver.find_element(*PaymentLocators.CONTINUE_BUTTON).click()
    time.sleep(1)

    driver.find_element(*PaymentLocators.FINISH_BUTTON).click()
    time.sleep(2)
