import flat_maps_data


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
        # TODO: The error that occurs occurs here, not in the method above, and is likely being caused in flat_maps.py here:
        # TODO: mean_price_area = all_areas_data.get_mean(data[3], data[2])
        current_hash_table = self.all_city_hash_tables.get(city)

        count, price = current_hash_table.get(area)
        return count / price

    def avrg_sqm_for_area(self, area):
        # TODO: Implement a method to gather all the prices for an area and divide it by the accumulated sum of sqmeters
        pass


def get_area_data() -> FlatData:
    data_for_all_cities = FlatData()

    for munich_data in flat_maps_data.data_for_munich():
        area = munich_data[3]
        price = munich_data[0]
        city = munich_data[4]
        data_for_all_cities.compute_mean_for_area([(area, price)], city)

    for berlin_data in flat_maps_data.data_for_berlin():
        area = berlin_data[3]
        price = berlin_data[0]
        city = berlin_data[4]
        data_for_all_cities.compute_mean_for_area([(area, price)], city)

    for hamburg_data in flat_maps_data.data_for_hamburg():
        area = hamburg_data[3]
        price = hamburg_data[0]
        city = hamburg_data[4]
        data_for_all_cities.compute_mean_for_area([(area, price)], city)

    return data_for_all_cities







