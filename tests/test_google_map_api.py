from configurations.body import create_address
from utils.api import GoogleMapsApi


class TestGoogleMapsApi:

    def test_methods_api(self):
        print("Создание новой локации")
        address_for_new_location = create_address()
        result_post = GoogleMapsApi.create_new_place(address_for_new_location)
        place_id = result_post.json()["place_id"]
        print(f"Получен place_id локации: {place_id}\n"
              f"Адрес данной локации: {address_for_new_location}")

        print("\nОбновление адреса локации")
        location_address_update = create_address()
        GoogleMapsApi.put_place(place_id, location_address_update)
        print(f"Обновленный адрес локации: {location_address_update}")

        print("\nПроверка, что метод PUT отработал верно")
        result_get = GoogleMapsApi.get_place(place_id)
        get_updated_address = result_get.json()["address"]
        assert get_updated_address == location_address_update, \
            "Ошибка: Новый адрес не соответствует измененному!"
        print("Метод PUT отработал верно!")


if __name__ == "__main__":
    start_test = TestGoogleMapsApi()
    start_test.test_methods_api()
