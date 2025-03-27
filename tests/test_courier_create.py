

import allure
import requests

import urls

from api_methods import ApiMethods
from data import Data


class TestCourierCreate:
    login = None
    password = None
    firstname = None

    @classmethod
    def setup_class(cls):

        cls.login = Data.generate_string()
        cls.password = Data.generate_string()
        cls.firstname = Data.generate_string()

    @allure.title('Проверка получения статус кода 201 и тела ответа  методом POST для "api/v1/courier" при корректном заполнении всех обязательных полей.')
    def test_create_courier(self):
        payload = {
            "login": self.login,
            "password": self.password,
            "firstName": self.firstname
        }

        response = ApiMethods.create_courier(payload)
        assert response.status_code == 201 and response.text == '{"ok":true}'

    @allure.title('Проверка получения статус кода 400   методом POST для "api/v1/courier" при незаполненном поле логин.')
    def test_create_courier_by_empty_login(self):
        payload = {
            "login": "",
            "password": self.password,
            "firstName": self.firstname
        }
        response = ApiMethods.create_courier(payload)

        assert response.status_code == 400 and response.text == '{"message": "Недостаточно данных для создания учетной записи"}'

    @allure.title('Проверка получения статус кода 400  методом POST для "api/v1/courier" при незаполненном поле пароль.')
    def test_create_courier_by_empty_password(self):
        payload = {
            "login": self.login,
            "password": "",
            "firstName": self.firstname
        }
        response = ApiMethods.create_courier(payload)

        assert response.status_code == 400 and response.text == '{"message": "Недостаточно данных для создания учетной записи"}'

    @allure.title('Проверка получения статус кода 400  методом POST для "api/v1/courier" при пустом теле запроса.')
    def test_create_courier_by_empty_body_of_request_return_400_bad_request(self):
        payload = {}
        response = ApiMethods.create_courier(payload)

        assert response.status_code == 400 and response.text == '{"message": "Недостаточно данных для создания учетной записи"}'

    @allure.title('Проверка получения статус кода 409  методом POST для "api/v1/courier" при повторяющемся логине.')
    def test_create_courier_the_same_login_twice_return_409_status_code_and_message(self):
        payload = {
            "login": self.login,
            "password": self.password,
            "firstName": self.firstname
        }
        ApiMethods.create_courier(payload)
        response = ApiMethods.create_courier(payload)
        assert response.status_code == 409 and response.text == '{"message": "Этот логин уже используется"}'

    @classmethod
    def teardown_class(cls):
        payload_1 = {
            "login": cls.login,
            "password": cls.password
        }
        response_login = requests.post(urls.courier_login_url, data=payload_1)
        id_1 = response_login.json()["id"]
        ApiMethods.delete_courier(id_1)
