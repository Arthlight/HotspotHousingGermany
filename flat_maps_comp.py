import _sqlite3
import flat_maps_data


class FlatData:

    def __init__(self):
        self.mean_table_hamburg = {}
        self.mean_table_berlin = {}
        self.mean_table_munich = {}
       # TODO: In order to not repeat the same class three times, pass an additional flag to compute_mean_for_area
       # TODO: probably the city, and store the data in their respective tables and compute all of them at once
       # TODO: when all the data has been collected
       # TODO: important disclaimer: you don't have to store everyting in an array, compute the area count and
       # TODO: the accumulating prices at once and in the end do price / count
    def compute_mean_for_area(self, data, city):
        print(len(data) == 2)

        if city == 'München':
            munich_count = 0
            for area, price in data:
                if self.mean_table_munich.get(area):
                    _, prev_price = self.mean_table_munich[area]
                    self.mean_table_munich[area] = (munich_count, prev_price + int(price))
                    munich_count += 1
                else:
                    self.mean_table_munich[area] = (munich_count, int(price))
                    munich_count += 1

        if city == 'Hamburg':
            hamburg_count = 0
            for area, price in data:
                if self.mean_table_hamburg.get(area):
                    _, prev_price = self.mean_table_hamburg[area]
                    self.mean_table_hamburg[area] = (hamburg_count, prev_price + int(price))
                    hamburg_count += 1
                else:
                    self.mean_table_hamburg[area] = (hamburg_count, int(price))
                    hamburg_count += 1

        if city == 'Berlin':
            berlin_count = 0
            for area, price in data:
                if self.mean_table_berlin.get(area):
                    _, prev_price = self.mean_table_berlin[area]
                    self.mean_table_berlin[area] = (berlin_count, prev_price + int(price))
                    berlin_count += 1
                else:
                    self.mean_table_berlin[area] = (berlin_count, int(price))
                    berlin_count += 1



    def parse_data(self, area, city):
        if city == 'München':
            return self.mean_table_munich.get(area)

        if city == 'Berlin':
            return self.mean_table_munich.get(area)

        if city == 'Hamburg':
            return self.mean_table_munich.get(area)



data_for_all_cities = FlatData()

connection = _sqlite3.connect('Flat_Crawler_Scrapy/Flat_Crawler_Scrapy/flat_data.db')
cursor = connection.cursor()

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






