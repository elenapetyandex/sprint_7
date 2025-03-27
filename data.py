import requests
import random
import string


class Data:

    data_for_create_order = [
        ['Яна', 'Иванова', 'Ветлужская', 'Сокольники', '+79999999999', 3, '2025-04-01', 'a', None, None],
        ['Иван', 'Борисов', 'Перекресток, 7', 'Арбатская', '89999999999', 1, '2025-09-25', '', 'BLACK', None],
        ['Ян', 'Бекмамбетов', 'Новосибирская, 25', 'Павелецкая', '80000000000', 7, '2026-01-20', 'Кататься вдесятером', 'GREY', None],
        ['Николай', 'Невозмутимый', 'Менделеева, 11', 4, '+70000000000', 6, '2026-01-20', 'Кататься вдесятером!', 'GREY', 'BLACK']
    ]
    data_for_create_order_id_courier_known = [["11", 1, 0], [None, 2, 0], ["6", 29, 0], ["1", 30, 0]]
    data_for_create_order_id_courier_unknown = [["112", 10, 0]]

    @staticmethod
    def generate_string():
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(10))
        return random_string

    @staticmethod
    def register_new_courier_and_return_login_password():
        # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        # создаём список, чтобы метод мог его вернуть
        login_pass = []

        # генерируем логин, пароль и имя курьера
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        # собираем тело запроса
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

        # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
        if response.status_code == 201:
            login_pass.append(login)
            login_pass.append(password)
            login_pass.append(first_name)

        # возвращаем список
        return login_pass
