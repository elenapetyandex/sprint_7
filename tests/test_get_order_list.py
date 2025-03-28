import json

import allure
import pytest
import requests

import urls
from api_methods import ApiMethods
from data import Data
from helpers import Helpers


class TestGetOrderList:
    courier_id = None
    login = None
    password = None
    firstname = None
    order_track = None

    @classmethod
    def setup_class(cls):
        login_pass = Helpers.register_new_courier_and_return_login_password()
        cls.login = login_pass[0]
        cls.password = login_pass[1]
        cls.firstname = login_pass[2]
        body = {
            "login": cls.login,
            "password": cls.password
        }
        response = ApiMethods.login_courier(body)
        cls.courier_id =response.json()["id"]

        body = {
            "firstName": 'Иван',
            "lastName": 'Иванов',
            "address": 'Бульвар Молодежи',
            "metroStation": 'Павелецкая',
            "phone": '89999999999',
            "rentTime": 2,
            "deliveryDate": '2025-04-01',
            "comment": 'срочно',
            "color": []

        }
        json_string = json.dumps(body)
        response = ApiMethods.create_order(json_string)
        cls.order_track = response.json()["track"]


    @allure.title('Получение списка доступных заказов методом GET "/api/v1/orders" при незаполненных необязательных параметрах запроса')
    def test_get_order_list_witn_no_params(self):
        response = ApiMethods.get_order_list()

        assert response.status_code == 200 and len(response.json()["orders"]) > 0

    @allure.title('Получение списка доступных заказов методом GET "/api/v1/orders" при корректно запоненных необязательных полях запроса')
    @pytest.mark.parametrize('neareststation, limit, page', Data.data_for_create_order_id_courier_known)
    def test_get_order_list_witn_no_params(self, neareststation, limit, page):
        courier_id = self.courier_id
        response = ApiMethods.get_order_list(courier_id, neareststation, limit, page)

        assert response.status_code == 200 and len(response.json()["orders"]) > 0

    @allure.title('Получение статус кода 404 методом GET "/api/v1/orders" при id незарешгистрированного курьера')
    @pytest.mark.parametrize('neareststation, limit, page', Data.data_for_create_order_id_courier_unknown)
    def test_get_order_list_with_unknown_id_courier(self, neareststation, limit, page):
        courier_id = 100000000
        response = ApiMethods.get_order_list(courier_id, neareststation, limit, page)

        assert response.status_code == 200 and response.text == Data.message_for_get_order_list_courier_not_found


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
        ApiMethods.cancel_order(cls.order_track)
