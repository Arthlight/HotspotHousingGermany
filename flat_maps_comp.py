import sys
sys.path.append('/Users/arthred/Documents/Flat_Crawler_Django')
import flat_maps_data


class FlatData:

    def __init__(self):
        self.mean_table = {}

    def compute_mean_for_area(self, data: list):
        for area, price in data:
            if self.mean_table.get(area):
                count, prev_price = self.mean_table[area]
                self.mean_table[area] = (count + 1, prev_price + int(price))
            else:
                self.mean_table[area] = (1, int(price))

    def get_mean(self, area: str) -> float:
        count, price = self.mean_table.get(area)

        return round(price / count, 2)


def get_area_data_for(city: str) -> FlatData:
    data = FlatData()
    for current_row in flat_maps_data.data_for(city):
        area = current_row[3]
        price = current_row[0]
        data.compute_mean_for_area([(area, price)])

    return data
