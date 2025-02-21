import requests

from configurations.body import (
    body_to_creating_location,
    body_for_location_update,
)
from configurations.path_key import (
    BASE_URL,
    POST_RESOURCE,
    KEY,
    GET_RESOURCE,
    PUT_RESOURCE,
)


class GoogleMapsApi:
    # создание новой локации
    @staticmethod
    def create_new_place(address):
        post_url = BASE_URL + POST_RESOURCE + "?key=" + KEY
        print(f"URL для создания локации:\n{post_url}")

        result_post = requests.post(
            url=post_url,
            json=body_to_creating_location(address)
        )

        print(f"Ответ сервера:\n{result_post.json()}")
        return result_post

    # получить локацию
    @staticmethod
    def get_place(place_id):
        get_url = BASE_URL + GET_RESOURCE + "?key=" + KEY + "&place_id=" + place_id
        print(f"URL для получения локации:\n{get_url}")

        result_get = requests.get(url=get_url)

        print(f"Ответ сервера:\n{result_get.json()}")
        return result_get

    # обновить локацию
    @staticmethod
    def put_place(place_id, address):
        put_url = BASE_URL + PUT_RESOURCE + "?key=" + KEY
        print(f"URL для обновления локации:\n{put_url}")

        result_put = requests.put(
            url=put_url,
            json=body_for_location_update(
                place_id=place_id,
                key=KEY,
                address=address
            ))

        print(f"Ответ сервера:\n{result_put.json()}")
        return result_put
