from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from data import Credentials


class TestExitAccount:
    # выход из аккаунта
    def test_exit_account_button_personal_account_success(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()  # вход в ЛК

        email_account = driver.find_element(*Locators.EMAIL_ACCOUNT)
        email_account.send_keys(Credentials.VALID_EMAIL)

        password_account = driver.find_element(*Locators.PASSWORD_ACCOUNT)
        password_account.send_keys(Credentials.VALID_PASSWORD)

        driver.find_element(*Locators.LOGIN_BUTTON).click()  # вход

        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()  # вход в ЛК снова

        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.EXIT_BUTTON))
        driver.find_element(*Locators.EXIT_BUTTON).click()  # выход
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON))
        assert driver.find_element(*Locators.LOGIN_BUTTON).is_displayed()