import sys
sys.path.append('/Users/arthred/Documents/Flat_Crawler_Django')
import flat_maps_data

# TODO: change this class so that it has only one hash table (1 different instance will be created for every city,
# TODO: there's no need for subclasses or anything of the like since the all share the exact same behaviour)
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


# TODO: turn this into some sort of "get_area_data_for(city)" function which delegates the input string into the flat
# TODO: maps data.data_for(city) function an populates only that single FlatData instance. No need for helper functions
# TODO: for each city. it can look sth like this:

#def get_area_data_for(city: str) -> FlatData:
#    data = FlatData()
#    for current_row in flat_maps_data.data_for(city):
#        area = current_row[3]
#        price = current_row[0]
#        city = current_row[4]
#        data.compute_mean_for_area([(area, price)])

def get_area_data() -> FlatData:
    data_for_all_cities = FlatData()
    for munich_data in flat_maps_data.data_for('München'):
        print('in get munich')
        area = munich_data[3]
        price = munich_data[0]
        city = munich_data[4]
        data_for_all_cities.compute_mean_for_area([(area, price)], city)

    for berlin_data in flat_maps_data.data_for('Berlin'):
        print('in get berlin')
        area = berlin_data[3]
        price = berlin_data[0]
        city = berlin_data[4]
        data_for_all_cities.compute_mean_for_area([(area, price)], city)

    for hamburg_data in flat_maps_data.data_for('Hamburg'):
        print('in get hamburg')
        area = hamburg_data[3]
        price = hamburg_data[0]
        city = hamburg_data[4]
        data_for_all_cities.compute_mean_for_area([(area, price)], city)

    return data_for_all_cities

# TODO: refactor this similiar to the function above. it can look sth like this:
#def get_area_data_for(city) -> FlatData:
#    data = FlatData()
#    for current_row in flat_maps_data.data_for(city):
#        area = current_row[3]
#        price = current_row[0]
#        city = current_row[4]
#        data.compute_mean_for_area([(area, price)])

def get_areas_by_city(city: str) -> FlatData:

    if city == 'Berlin':
        # TODO: DATA FOR ALL CITIES is a wrong name here, you only get data for one specific city
        data_for_all_cities = FlatData()
        for berlin_data in flat_maps_data.data_for('Berlin'):
            area = berlin_data[3]
            price = berlin_data[0]
            city = berlin_data[4]
            data_for_all_cities.compute_mean_for_area([(area, price)], city)

        return data_for_all_cities

    if city == 'München':
        data_for_all_cities = FlatData()
        for munich_data in flat_maps_data.data_for('München'):
            area = munich_data[3]
            price = munich_data[0]
            city = munich_data[4]
            data_for_all_cities.compute_mean_for_area([(area, price)], city)

        return data_for_all_cities

    if city == 'Hamburg':
        data_for_all_cities = FlatData()
        for hamburg_data in flat_maps_data.data_for('Hamburg'):
            area = hamburg_data[3]
            price = hamburg_data[0]
            city = hamburg_data[4]
            data_for_all_cities.compute_mean_for_area([(area, price)], city)

        return data_for_all_cities
