"""
Вызов всех необходимых функций
"""
from src.building_pick import pick_building
from src.price_predict import predict_price


def pick_building_and_get_price(cords):
    building = pick_building(cords)
    price = predict_price(building)

    print(price)


if __name__ == '__main__':
    pick_building_and_get_price((10, 10))
