import allure
import pytest

from api_methods import ApiMethods
from data import Data


class TestOrderCreate:

    @allure.title('Проверка получения статус кода 201 и "track" в теле ответа  методом POST для "api/v1/orders" при выборе одного, двух, никакого цвета самоката и корректно заполненных обязательных полях.')
    @pytest.mark.parametrize('firstname,lastname,address,metrostation,phone,renttime,deliverydate,comment,color_1,color_2', Data.data_for_create_order)
    def test_order_create(self, create_order, firstname, lastname, address, metrostation, phone, renttime, deliverydate, comment, color_1, color_2):
        assert create_order.status_code == 201 and create_order.json()["track"]
