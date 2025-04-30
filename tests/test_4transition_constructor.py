import unittest
from datetime import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators
from data import Credentials


class TestTransitionPersonalAccount(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site/")

    # Переход по клику на "Личный кабинет"
    def test_login_through_personal_account_button_success(self):
        driver = self.driver
        WebDriverWait(driver, 10)
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        # Заполняем данные
        email_account = driver.find_element(*Locators.EMAIL_ACCOUNT)
        email_account.send_keys(Credentials.VALID_EMAIL)

        password_account = driver.find_element(*Locators.PASSWORD_ACCOUNT)
        password_account.send_keys(Credentials.VALID_PASSWORD)

        driver.find_element(*Locators.LOGIN_BUTTON).click()  # вход

        driver.find_element(*Locators.CONSTRUCTOR).click()  # переход в конструктор

        # Проверяем, что URL соответствует странице конструктора
        expected_url = "https://stellarburgers.nomoreparties.site/"  # URL
        actual_url = driver.current_url
        assert actual_url == expected_url, f"Ожидался URL {expected_url}, но получен {actual_url}"
        driver.quit()

    # Переход из личного кабинета по клику на логотип "Stellar Burgers"
    def test_through_from_personal_account_in_logo_success(self):
        driver = self.driver
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        # Заполняем данные
        email_account = driver.find_element(*Locators.EMAIL_ACCOUNT)
        email_account.send_keys(Credentials.VALID_EMAIL)

        password_account = driver.find_element(*Locators.PASSWORD_ACCOUNT)
        password_account.send_keys(Credentials.VALID_PASSWORD)

        driver.find_element(*Locators.LOGIN_BUTTON).click() #вход

        driver.find_element(*Locators.LOGO_STELLA_BURGERS).click()

        # Проверяем, что URL соответствует странице с логотипом "Stellar Burgers"
        expected_url = "https://stellarburgers.nomoreparties.site/"  #URL
        actual_url = driver.current_url
        assert actual_url == expected_url, f"Ожидался URL {expected_url}, но получен {actual_url}"
        driver.quit()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()