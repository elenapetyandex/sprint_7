import json

import requests
import allure
import urls


class ApiMethods:

    @staticmethod
    @allure.step('Логин курьера')
    def login_courier(payload):
        return requests.post(urls.courier_login_url, data=payload)


    @staticmethod
    @allure.step('Создание курьера')
    def create_courier(payload):
        return  requests.post(urls.create_courier_url, data=payload)



    @staticmethod
    @allure.step('Удаление курьера по id')
    def delete_courier(id):
        return requests.delete(f"{urls.create_courier_url}/{id}")

    @staticmethod
    @allure.step('Создание заказа')
    def create_order(body):

        return requests.post(urls.create_order_url, data=body)

    @staticmethod
    @allure.step('отмена заказа')
    def cancel_order(track):

        return requests.put(f'{urls.cancel_order_url}?track={track}')



    @staticmethod
    @allure.step('Принять заказ')
    def accept_order(order_id, courier_id):
        requests.put(f'urls.accept_order_url{order_id}?courierId={courier_id}')

    @staticmethod
    @allure.step('получение списка заказов')
    def get_order_list(courier_id=None, neareststation=None, limit=None, page=None):

        params = {
            'courierId': courier_id,
            'nearestStation': [],
            'limit': limit,
            'page': page

        }
        if neareststation:
            params['nearestStation'].append(neareststation)
        json_string = json.dumps(params)

        return requests.get(urls.get_order_list_url, params=json_string)
