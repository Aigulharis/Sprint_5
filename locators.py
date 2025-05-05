from selenium.webdriver.common.by import By


class Locators:
    # 1. Регистрация (создать аккаунт)
    # 1.1. Кнопка "Зарегистрироваться" +
    REGISTER_BUTTON = [By.XPATH, ".//a[@class='Auth_link__1fOlj']"]

    # 1.2. Поле ввода 'Имя' +
    NAME_INPUT = (By.XPATH, "(.//input[@name='name'])[1]")

    # 1.3. Поле ввода email +
    EMAIL_INPUT = (By.CSS_SELECTOR, "div.input_type_text input[name='name']")

    # 1.4. Поле ввода пароля +
    PASSWORD_INPUT = (By.CSS_SELECTOR, "div.input_type_password input[name='Пароль']")

    # 1.5. Кнопка "Войти" на странице регистрации
    REGISTRATION_BUTTON = (By.XPATH, ".//a[text() = 'Войти']")

    # 1.6. Сообщение об ошибке при невалидном пароле
    ERROR_MESSAGE = (By.XPATH, ".//p[text()='Некорректный пароль']")

    # 2. Главная
    # 2.1. Кнопка "Войти в аккаунт"
    ENTER_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")

    # 3. Вход в личный кабинет
    # 3.1. Кнопка "Личный кабинет"
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, ".//p[text()='Личный Кабинет']")

    # 3.2. Поле ввода email +
    EMAIL_ACCOUNT = (By.XPATH, ".//input[@type='text']")

    # 3.3. Поле ввода пароля +
    PASSWORD_ACCOUNT = (By.XPATH, ".//input[@name = 'Пароль']")

    # 3.4. Кнопка "Войти" в личном кабинете
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")

    # 3.5. Кнопка "Зарегистрироваться"
    REGISTER_BUTTON = (By.XPATH, ".//a[text()='Зарегистрироваться']")

    # 3.6. Кнопка "Восстановить пароль" в форме Личного кабинета
    RECOVER_PASSVORD_BUTTON = (By.XPATH, ".//a[text()='Восстановить пароль']")

    # 4. Восстановление пароля
    # 4.1. Кнопка "Восстановить" в форме восстановления
    RECOVER_BUTTON = (By.XPATH, ".//button[text()='Восстановить']")

    # 4.2. Кнопка "Войти" в форме восстановления
    LOGIN_BUTTON_RECOVER = (By.XPATH, ".//a[@class='Auth_link__1fOlj' and text()='Войти']")

    # 5.1 Кнопка "Выйти" в личном кабинете
    EXIT_BUTTON = (By.XPATH, ".//div[@class = 'Account_account__vgk_w']//button[text()= 'Выход']")

    # 6. Раздел "Конструкторы"
    CONSTRUCTOR = (By.XPATH, ".//a[p[text()='Конструктор']]")

    # 6.1. Кнопка "Булки"
    BUNS_BUTTON = (By.XPATH, ".//div[contains(@class, 'tab_tab__1SPyG') and not(contains(@class, 'tab_tab_type_current__2BEPc')) and .//span[text()='Булки']]")

    # 6.1.1. Активная кнопка "Булки"
    ACTIVE_TAB_BUNS = (By.XPATH, ".//div[contains(@class, 'tab_tab_type_current__2BEPc') and span[text()='Булки']]")

    # 6.2. Кнопка "Соусы"
    SAUCES_BUTTON = (By.XPATH, ".//span[text()='Соусы']")

    # 6.2.1. Активная кнопка "Соусы"
    ACTIVE_TAB_SAUCES = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc') and span[text()='Соусы']]")

    # 6.3. Кнопка "Начинки"
    FILLINGS_BUTTON = (By.XPATH, ".//span[text()='Начинки']")

    # 6.3.1. Активная кнопка "Начинки"
    ACTIVE_TAB_FILLINGS = (By.XPATH, ".//div[contains(@class, 'tab_tab_type_current__2BEPc') and span[text()='Начинки']]")

    # 7.1. Кнопка логотипа "Stella Burgers@
    LOGO_STELLA_BURGERS = (By.TAG_NAME, "svg")
