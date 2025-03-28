import json

import pytest

from api_methods import ApiMethods


@pytest.fixture
def create_order(firstname, lastname, address, metrostation, phone, renttime, deliverydate, comment, color_1, color_2):

    body = {
        "firstName": firstname,
        "lastName": lastname,
        "address": address,
        "metroStation": metrostation,
        "phone": phone,
        "rentTime": renttime,
        "deliveryDate": deliverydate,
        "comment": comment,
        "color": []

    }
    body['color'].append(color_1)
    body['color'].append(color_2)

    json_string = json.dumps(body)

    response = ApiMethods.create_order(json_string)

    yield response
    if response.status_code == 201:
        r = response.json()["track"]
        response_1 = ApiMethods.cancel_order(r)

