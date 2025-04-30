import unittest
from datetime import time

from selenium import webdriver
from locators import Locators

class TestExitAccount(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site/")

    # Переход из раздела "Булки" в раздел "Соусы"
    def test_navigate_from_constructor_in_sauces_success(self):
        driver = self.driver
        driver.find_element(*Locators.CONSTRUCTOR).click()
        driver.find_element(*Locators.SAUCES_BUTTON).click() #переход в раздел "Соусы"

    # Переход из раздела "Булки" в раздел "Начинки"
    def test_navigate_block_from_sauces_in_fillings_success(self):
        driver = self.driver
        driver.find_element(*Locators.CONSTRUCTOR).click()
        driver.find_element(*Locators.FILLINGS_BUTTON).click()  # переход в раздел "Начинки"

    # Переход из раздела "Начинки" в раздел "Булки"
    def test_navigate_block_from_fillings_in_buns_success(self):
        driver = self.driver
        driver.find_element(*Locators.CONSTRUCTOR).click()
        driver.find_element(*Locators.FILLINGS_BUTTON).click()
        driver.find_element(*Locators.BUNS_BUTTON).click()  # переход в раздел "Начинки"

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()