import sys
sys.path.append('/Users/arthred/Documents/Flat_Crawler_Django')
import flat_maps_data

# For the Clean Code Assessment, change this class into a SupeClass and make 3 corresponding SubClasses for the
# 3 cities (and it's also nice in general to refactor this to show that you can do Object Oriented Coding)
class FlatData:

    def __init__(self):
        self.mean_table_hamburg = {}
        self.mean_table_berlin = {}
        self.mean_table_munich = {}
        self.all_city_hash_tables = {'München': self.mean_table_munich, 'Berlin': self.mean_table_berlin, 'Hamburg': self.mean_table_hamburg}

    def compute_mean_for_area(self, data: list, city: str):
        current_hash_table = self.all_city_hash_tables.get(city)

        for area, price in data:
            if current_hash_table.get(area):
                count, prev_price = current_hash_table[area]
                current_hash_table[area] = (count + 1, prev_price + int(price))
            else:
                current_hash_table[area] = (1, int(price))

    def get_mean(self, area: str, city: str) -> float:
        current_hash_table = self.all_city_hash_tables.get(city)

        count, price = current_hash_table.get(area)
        return round(price / count, 2)

    def get_all_areas(self, city: str) -> dict:
        current_hash_table = self.all_city_hash_tables.get(city)

        return current_hash_table


def get_area_data() -> FlatData:
    data_for_all_cities = FlatData()
    for munich_data in flat_maps_data.data_for_munich():
        print('in get munich')
        area = munich_data[3]
        price = munich_data[0]
        city = munich_data[4]
        data_for_all_cities.compute_mean_for_area([(area, price)], city)

    for berlin_data in flat_maps_data.data_for_berlin():
        print('in get berlin')
        area = berlin_data[3]
        price = berlin_data[0]
        city = berlin_data[4]
        data_for_all_cities.compute_mean_for_area([(area, price)], city)

    for hamburg_data in flat_maps_data.data_for_hamburg():
        print('in get hamburg')
        area = hamburg_data[3]
        price = hamburg_data[0]
        city = hamburg_data[4]
        data_for_all_cities.compute_mean_for_area([(area, price)], city)

    return data_for_all_cities

# TODO: separate them into 3 different functions after you have refactored the above class
def get_areas_by_city(city: str) -> FlatData:

    if city == 'Berlin':
        data_for_all_cities = FlatData()
        for berlin_data in flat_maps_data.data_for_berlin():
            area = berlin_data[3]
            price = berlin_data[0]
            city = berlin_data[4]
            data_for_all_cities.compute_mean_for_area([(area, price)], city)

        return data_for_all_cities

    if city == 'München':
        data_for_all_cities = FlatData()
        for munich_data in flat_maps_data.data_for_munich():
            area = munich_data[3]
            price = munich_data[0]
            city = munich_data[4]
            data_for_all_cities.compute_mean_for_area([(area, price)], city)

        return data_for_all_cities

    if city == 'Hamburg':
        data_for_all_cities = FlatData()
        for hamburg_data in flat_maps_data.data_for_hamburg():
            area = hamburg_data[3]
            price = hamburg_data[0]
            city = hamburg_data[4]
            data_for_all_cities.compute_mean_for_area([(area, price)], city)

        return data_for_all_cities
