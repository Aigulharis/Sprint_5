from faker import Faker

faker = Faker('ru_RU')

def generate_registration_data():
    name = faker.first_name()
    email = faker.email()
    valid_password = faker.password(length=9, special_chars=True, digits=True, upper_case=True, lower_case=True)
    invalid_password = '123'  # Пароль короче 6 символов для тестирования ошибок
    return {
        'valid': {'name': name, 'email': email, 'password': valid_password},
        'invalid': {'name': name, 'email': email, 'password': invalid_password}
    }
