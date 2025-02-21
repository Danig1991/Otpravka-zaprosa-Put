from random import uniform, randint
from faker import Faker


# создать адрес
def create_address():
    return Faker("en_Us").street_address()


# тело для создания локации
def body_to_creating_location(address):
    return {
        "location": {
            "lat": round(uniform(-100, 100), 6),
            "lng": round(uniform(-100, 100), 6)
        },
        "accuracy": randint(10, 100),
        "name": "Frontline house",
        "phone_number": Faker("en_Us").phone_number(),
        "address": address,
        "types": [
            "shoe park",
            "shop"
        ],
        "website": "http://google.com",
        "language": "French-IN"
    }


# тело для обновления локации
def body_for_location_update(place_id, key, address):
    return {
        "place_id": place_id,
        "address": address,
        "key": key
    }
