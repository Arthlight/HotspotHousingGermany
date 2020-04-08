import _sqlite3
import flat_maps_data


class FlatData:

    def __init__(self):
        self.mean_table = {}
       #self.mean_table_hamburg = {}
       #self.mean_table_berlin = {}
       #self.mean_table_munich = {}
       # TODO: In order to not repeat the same class three times, pass an additional flag to compute_mean_for_area
       # TODO: probably the city, and store the data in their respective tables and compute all of them at once
       # TODO: when all the data has been collected
       # TODO: important disclaimer: you don't have to store everyting in an array, compute the area count and
       # TODO: the accumulating prices at once and in the end do price / count
    def parse_data(self, data, city):
        count = 0
        for area, price in data:
            if self.mean_table.get(area):
                _, prev_price = self.mean_table[area]
                self.mean_table[area] = (count, prev_price + price)
                count += 1
            else:
                self.mean_table[area] = (count, price)
                count += 1

        return self.mean_table

    def compute_mean_for_area(self, data):
        mean_table = self.parse_data(data)

        for key, val in mean_table.items():
            pass


connection = _sqlite3.connect('Flat_Crawler_Scrapy/Flat_Crawler_Scrapy/flat_data.db')
cursor = connection.cursor()

for munich_data in flat_maps_data.data_for_munich():
    pass

for berlin_data in flat_maps_data.data_for_berlin():
    pass

for munich_data in flat_maps_data.data_for_berlin():
    pass




