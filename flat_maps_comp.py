import flat_maps_data
import sys
sys.path.append('$(pwd)/Flat_Crawler_Django')


class FlatData:

    def __init__(self):
        self.mean_table_hamburg = {}
        self.mean_table_berlin = {}
        self.mean_table_munich = {}
        self.all_city_hash_tables = {'München': self.mean_table_munich, 'Berlin': self.mean_table_berlin, 'Hamburg': self.mean_table_hamburg}
        self.avrg_berlin = {}
        self.avrg_munich = {}
        self.avrg_hamburg = {}
        self.all_avrg_sqm = {'München': self.avrg_munich, 'Berlin': self.avrg_berlin, 'Hamburg': self.avrg_hamburg}

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
        return price / count

    def get_all_areas(self, city: str) -> dict:
        current_hash_table = self.all_city_hash_tables.get(city)

        return current_hash_table



def get_area_data() -> FlatData:
        # TODO: Put an additional flag so that you only query for specific cities in flat_statistics/views.py

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








