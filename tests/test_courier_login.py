import json

import allure
import pytest

import urls
from api_methods import ApiMethods
import requests

from data import Data
from helpers import Helpers


class TestCourierLogin:

    login = None
    password = None
    firstname = None

    @classmethod
    def setup_class(cls):
        login_pass = Helpers.register_new_courier_and_return_login_password()
        cls.login =login_pass[0]
        cls.password = login_pass[1]
        cls.firstname = login_pass[2]

    @allure.title('Проверка получения статус кода 200 и id в теле ответа  методом POST для "/api/v1/courier/login" при корректном заполнении всех обязательных полей.')
    def test_login_created_courier_return_status_code_200(self):
        body = {
            "login": self.login,
            "password": self.password
        }
        response = ApiMethods.login_courier(body)

        assert response.status_code == 200 and response.json()["id"]

    @allure.title('Проверка получения статус кода 400 методом POST для "/api/v1/courier/login" при корректном заполнении поля логин и пустом поле пароль.')
    @pytest.mark.parametrize('password', [""])
    def test_login_created_courier_with_not_full_body_return_status_code_400(self, password):
        body = {
            "login": self.login,
            "password": password
        }

        response = ApiMethods.login_courier(body)
        assert response.status_code == 400 and response.text == Data.message_for_courier_login_without_data_needed

    @allure.title('Проверка получения статус кода 400 методом POST для "/api/v1/courier/login" при корректном заполнении поля пароль и пустом поле логин.')
    @pytest.mark.parametrize('login', [""])
    def test_login_created_courier_with_not_full_body_return_status_code_400(self, login):
        body = {
            "login": login,
            "password": self.password
        }

        response = ApiMethods.login_courier(body)

        assert response.status_code == 400 and response.text == Data.message_for_courier_login_without_data_needed

    @allure.title('Проверка получения статус кода 400 методом POST для "/api/v1/courier/login" при пустом теле запроса.')
    def test_login_created_courier_with_not_full_body_return_status_code_400(self):
        body = {}
        response = ApiMethods.login_courier(body)
        assert response.status_code == 400

    @allure.title('Проверка получения статус кода 404 методом POST для "/api/v1/courier/login" при заполнении логина и пароля несозданного курьера')
    def test_login_not_created_courier_return_404_status_code(self):
        body = {
            "login": Helpers.generate_random_string(10),
            "password": Helpers.generate_random_string(10)
        }
        response = ApiMethods.login_courier(body)

        assert response.status_code == 404 and response.text == Data.message_for_courier_login_not_found


    @classmethod
    def teardown_class(cls):

        payload_1 = {
            "login": cls.login,
            "password": cls.password
        }
        response_login = requests.post(urls.courier_login_url, data=payload_1)
        if response_login.status_code == 200:
            id_1 = response_login.json()["id"]
            ApiMethods.delete_courier(id_1)
