import unittest

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from locators import Locators
from helpers import generate_registration_data
from data import Credentials

class TestEnterAccount(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site/")

    # 1 Вход по кнопке "Войти в аккаунт на главной
    def test_login_through_enter_account_button(self):
        driver = self.driver
        registration_data = generate_registration_data()['valid']
        driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON).click()

        # Заполнение полей формы
        email_account = driver.find_element(*Locators.EMAIL_ACCOUNT)
        email_account.send_keys(registration_data['email'])

        password_account = driver.find_element(*Locators.PASSWORD_ACCOUNT)
        password_account.send_keys(registration_data['password'])
        time.sleep(5)

        driver.find_element(*Locators.LOGIN_BUTTON).click() #вход

    # 2 Вход через кнопку "Личный кабинет"
    def test_login_through_personal_account_button(self):
        driver = self.driver
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()

        # Заполнение полей формы
        email_account = driver.find_element(*Locators.EMAIL_ACCOUNT)
        email_account.send_keys(Credentials.VALID_EMAIL)

        password_account = driver.find_element(*Locators.PASSWORD_ACCOUNT)
        password_account.send_keys(Credentials.VALID_PASSWORD)

        driver.find_element(*Locators.LOGIN_BUTTON).click() #вход

    # 3 Вход через кнопку в форме регистрации
    def test_login_through_registration_form_button(self):
        driver = self.driver
        driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.REGISTER_BUTTON).click() # кнопка зарегистрироваться
        driver.find_element(*Locators.REGISTRATION_BUTTON).click() # кнопка войти в форме регистрации
        # Заполнение полей формы
        email_account = driver.find_element(*Locators.EMAIL_ACCOUNT)
        email_account.send_keys(Credentials.VALID_EMAIL)

        password_account = driver.find_element(*Locators.PASSWORD_ACCOUNT)
        password_account.send_keys(Credentials.VALID_PASSWORD)

        driver.find_element(*Locators.LOGIN_BUTTON).click() #вход

    # 4 Вход через кнопку в форме восстановления пароля
    def test_login_through_recover_password_button(self): # чуть сума не сошла с этим кодом, возможно я неправильно понимаю задание
        driver = self.driver

        # Переходим на страницу входа
        driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON).click()

        # Нажимаем на кнопку "Восстановить пароль?"
        recover_password_link = driver.find_element(*Locators.RECOVER_PASSVORD_BUTTON)
        recover_password_link.click()

        # Возвращаемся обратно на форму входа
        login_button_in_recovery_form = driver.find_element(*Locators.LOGIN_BUTTON_RECOVER)
        login_button_in_recovery_form.click()

        # Проверяем наличие элементов формы авторизации
        email_field = driver.find_element(*Locators.EMAIL_ACCOUNT)
        password_field = driver.find_element(*Locators.PASSWORD_ACCOUNT)
        enter_button = driver.find_element(*Locators.LOGIN_BUTTON)

        # Заполняем данные
        email_field.clear()
        email_field.send_keys(Credentials.VALID_EMAIL)
        password_field.clear()
        password_field.send_keys(Credentials.VALID_PASSWORD)

        # Отправляем форму нажатием кнопки "Войти"
        enter_button.click()

        # Ожидаем перенаправления на главную страницу после успешного входа
        wait = WebDriverWait(driver, 10)
        personal_account_button = wait.until(
            EC.visibility_of_element_located((Locators.PERSONAL_ACCOUNT_BUTTON))
        )
        assert personal_account_button.is_displayed()


if __name__ == "__main__":
    unittest.main()
