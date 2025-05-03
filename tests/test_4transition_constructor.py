import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from data import Credentials

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()
    # Переход из Личного кабинета в Конструктор
def test_login_through_personal_account_button_success(driver):
    WebDriverWait(driver, 5)
    driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()

    email_account = driver.find_element(*Locators.EMAIL_ACCOUNT)
    email_account.send_keys(Credentials.VALID_EMAIL)

    password_account = driver.find_element(*Locators.PASSWORD_ACCOUNT)
    password_account.send_keys(Credentials.VALID_PASSWORD)

    driver.find_element(*Locators.LOGIN_BUTTON).click()  # вход

    driver.find_element(*Locators.CONSTRUCTOR).click()  # переход в конструктор

    expected_url = "https://stellarburgers.nomoreparties.site/"
    actual_url = driver.current_url
    assert actual_url == expected_url, f"Ожидался URL {expected_url}, но получен {actual_url}"

    # Переход из Личного кабинета в Stella Burgers
def test_through_from_personal_account_in_logo_success(driver):
    driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()

    email_account = driver.find_element(*Locators.EMAIL_ACCOUNT)
    email_account.send_keys(Credentials.VALID_EMAIL)

    password_account = driver.find_element(*Locators.PASSWORD_ACCOUNT)
    password_account.send_keys(Credentials.VALID_PASSWORD)

    driver.find_element(*Locators.LOGIN_BUTTON).click()  # вход

    driver.find_element(*Locators.LOGO_STELLA_BURGERS).click()

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LOGO_STELLA_BURGERS))
    assert driver.find_element(*Locators.LOGO_STELLA_BURGERS).is_displayed()
