from locators import Locators

class TestTransitionPersonalAccount:

    # Переход по клику на "Личный кабинет"
    def test_login_through_personal_account_button_success(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        expected_url = "https://stellarburgers.nomoreparties.site/login"
        actual_url = driver.current_url
        assert actual_url == expected_url, f"Ожидался URL {expected_url}, но получен {actual_url}"
