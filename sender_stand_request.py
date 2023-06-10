import requests
import data
import configuration


def post_new_order():
    response = requests.post(configuration.URL_SERVICE + configuration.ORDER_CREATION, json=data.ORDER_CREATION_BODY)
    return response


def get_order_by_track_number(track_number):
    url = configuration.URL_SERVICE + f"/api/v1/orders/track?t={track_number}"
    return requests.get(url)
