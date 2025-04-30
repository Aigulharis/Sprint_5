import unittest
from datetime import time

from selenium import webdriver
from locators import Locators

class TestTransitionPersonalAccount(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site/")

    # Переход по клику на "Личный кабинет"
    def test_login_through_personal_account_button_success(self):
        driver = self.driver
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        # Проверяем переключение на страницу личного кабинета
        expected_url = "https://stellarburgers.nomoreparties.site/login"  # URL
        actual_url = driver.current_url
        assert actual_url == expected_url, f"Ожидался URL {expected_url}, но получен {actual_url}"

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
