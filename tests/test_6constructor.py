import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from locators import Locators

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()

class TestNavigation:

    # Переход из раздела "Булки" в раздел "Соусы"
    def test_navigate_from_constructor_in_sauces_success(self, driver):
        driver.find_element(*Locators.CONSTRUCTOR).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.ACTIVE_TAB_BUNS))# активная кнопка "Булки"
        driver.find_element(*Locators.SAUCES_BUTTON).click()# переход в соусы
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BUNS_BUTTON))# не активная кнопка "Булки" появилась

        assert driver.find_element(*Locators.BUNS_BUTTON) # проверяем, что кнопка "Булки" не акивная
        assert driver.find_element(*Locators.ACTIVE_TAB_SAUCES), "Таб 'Соусы' не стал активным" # проверяем, кнопка "Соусы" акивная

        # Переход из раздела "Булки" в раздел "Начинки"
    def test_navigate_block_from_sauces_in_fillings_success(self, driver):
        driver.find_element(*Locators.CONSTRUCTOR).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.ACTIVE_TAB_BUNS))# активная кнопка "Булки"
        driver.find_element(*Locators.FILLINGS_BUTTON).click()# переход в начинки
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BUNS_BUTTON))# не активная кнопка "Булки" появилась

        assert driver.find_element(*Locators.BUNS_BUTTON) #проверяем, что кнопка "Булки" не акивная
        assert driver.find_element(*Locators.ACTIVE_TAB_FILLINGS), "Таб 'Начинки' не стал активным"  # проверяем, кнопка "Начинки" акивная

    # Переход из раздела "Начинки" в раздел "Булки"
    def test_navigate_block_from_fillings_in_buns_success(self, driver):
        driver.find_element(*Locators.FILLINGS_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BUNS_BUTTON))# не активная кнопка "Булки"
        driver.find_element(*Locators.BUNS_BUTTON).click()# переход в Булки
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.ACTIVE_TAB_BUNS))# ждем активную кнопку "Булки"

        assert driver.find_element(*Locators.ACTIVE_TAB_BUNS) # проверяем, что кнопка "Булки" акивная
        assert driver.find_element(*Locators.FILLINGS_BUTTON)  # проверяем, кнопка "Начинки" не акивная

