import pytest
from selenium import webdriver
from locators import Locators

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()

def test_login_through_personal_account_button_success(driver):
    driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
    expected_url = "https://stellarburgers.nomoreparties.site/login"
    actual_url = driver.current_url
    assert actual_url == expected_url, f"Ожидался URL {expected_url}, но получен {actual_url}"
