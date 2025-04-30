import unittest
import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from data import Credentials


class TestExitAccount(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site/")
    # Проверяем кнопку выход в личном кабинете
    def test_exit_account_button_personal_account_success(self):
        driver = self.driver
        #WebDriverWait(driver, 10)
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()# вход в ЛК

        # Заполнение полей формы
        email_account = driver.find_element(*Locators.EMAIL_ACCOUNT)
        email_account.send_keys(Credentials.VALID_EMAIL)

        password_account = driver.find_element(*Locators.PASSWORD_ACCOUNT)
        password_account.send_keys(Credentials.VALID_PASSWORD)

        driver.find_element(*Locators.LOGIN_BUTTON).click() # вход
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()  # вход в ЛК
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.EXIT_BUTTON))
        driver.find_element(*Locators.EXIT_BUTTON).click() # выход


if __name__ == "__main__":
    unittest.main()
