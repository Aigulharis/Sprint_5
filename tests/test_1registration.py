import pytest
import time
from selenium import webdriver
from locators import Locators
from helpers import generate_registration_data
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()


class TestSuccessfulRegistration: #Регистрация
    def test_successful_registration(self, driver):
        registration_data = generate_registration_data()['valid']

        driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON).click()

        driver.find_element(*Locators.REGISTER_BUTTON).click()

        name_input = driver.find_element(*Locators.NAME_INPUT)
        name_input.send_keys(registration_data['name'])

        email_input = driver.find_element(*Locators.EMAIL_INPUT)
        email_input.send_keys(registration_data['email'])

        password_input = driver.find_element(*Locators.PASSWORD_INPUT)
        password_input.send_keys(registration_data['password'])

        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        # Проверка успешной регистрации
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))
        assert driver.find_element(*Locators.LOGIN_BUTTON).is_displayed()

class TestInvalidPasswordError: #2 Проверяет отображение ошибки при попытке зарегистрироваться с неправильным паролем
    def test_invalid_password_error(self, driver):
        registration_data = generate_registration_data()['invalid']

        enter_account_button = driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON)
        enter_account_button.click()

        register_button = driver.find_element(*Locators.REGISTER_BUTTON)
        register_button.click()

        name_input = driver.find_element(*Locators.NAME_INPUT)
        name_input.send_keys(registration_data['name'])

        email_input = driver.find_element(*Locators.EMAIL_INPUT)
        email_input.send_keys(registration_data['email'])

        password_input = driver.find_element(*Locators.PASSWORD_INPUT)
        password_input.send_keys(registration_data['password'])

        submit_button = driver.find_element(*Locators.REGISTRATION_BUTTON)
        submit_button.click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ERROR_MESSAGE))
        assert driver.find_element(*Locators.ERROR_MESSAGE).text == "Некорректный пароль"
