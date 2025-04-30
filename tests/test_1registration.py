import unittest

from selenium import webdriver
from locators import Locators
from helpers import generate_registration_data


class TestRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Используем Chrome драйвер
        self.driver.get("https://stellarburgers.nomoreparties.site/")

    def test_successful_registration(self): # 1 Проверяет успешную регистрацию нового пользователя

        driver = self.driver
        registration_data = generate_registration_data()['valid']

        # Войти в аккаунт
        enter_account_button = driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON)
        enter_account_button.click()

        # Нажатие кнопки "Зарегистрироваться"
        register_button = driver.find_element(*Locators.REGISTER_BUTTON)
        register_button.click()

        # Заполнение полей регистрационной формы
        name_input = driver.find_element(*Locators.NAME_INPUT)
        name_input.send_keys(registration_data['name'])

        email_input = driver.find_element(*Locators.EMAIL_INPUT)
        email_input.send_keys(registration_data["email"])

        password_input = driver.find_element(*Locators.PASSWORD_INPUT)
        password_input.send_keys(registration_data['password'])

        submit_button = driver.find_element(*Locators.REGISTRATION_BUTTON)
        submit_button.click()


    def test_invalid_password_error(self): # 2 Проверяет отображение ошибки при попытке зарегистрироваться с неправильным паролем
        driver = self.driver
        registration_data = generate_registration_data()['invalid']

        # Войти в аккаунт
        enter_account_button = driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON)
        enter_account_button.click()

        # Переход на страницу регистрации
        register_button = driver.find_element(*Locators.REGISTER_BUTTON)
        register_button.click()

        # Заполняем форму регистрации
        name_input = driver.find_element(*Locators.NAME_INPUT)
        name_input.send_keys(registration_data['name'])

        email_input = driver.find_element(*Locators.EMAIL_INPUT)
        email_input.send_keys(registration_data['email'])

        password_input = driver.find_element(*Locators.PASSWORD_INPUT)
        password_input.send_keys(registration_data['password'])

        submit_button = driver.find_element(*Locators.REGISTRATION_BUTTON)
        submit_button.click()

        # Проверяем наличие ошибки при неправильном пароле
        error_message = driver.find_element(*Locators.ERROR_MESSAGE).text
        expected_error = "Некорректный пароль"
        self.assertIn(expected_error, error_message)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

