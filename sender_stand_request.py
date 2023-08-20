import requests
import configuration
import data


# Создание заказа
def get_track():
    url = configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH
    body = data.order_body

    return requests.post(url, json=body, headers=configuration.HEADERS)


# Получение заказа по его номеру
def get_order_by_track(track):
    url = configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_PATH + str(track)
    return requests.get(url, headers=configuration.HEADERS)
