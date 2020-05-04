"""This module handles computing the mean prices for areas in a given city.

This module provides the FlatData class, which is used to create instances
of cities and computing the average prices for their residential areas.

  Typical usage example:

  my_city = FlatData()
  my_city.compute_mean_for([my_area, 500])
  my_city.compute_mean_for([my_area, 500])
  my_city.get_mean_for(my_area) # returns 500 (mean of 500 + 500)
"""
# standard library
import sys
sys.path.append('/Users/arthred/Documents/Flat_Crawler_Django')

# third party
import flat_maps_data


class FlatData:
    """This Class computes and stores the average prices for
       each area in a given city.


    Attributes:
        mean_table: A dictionary mapping areas to their mean
                    prices.
    """

    def __init__(self):
        self.mean_table = {}

    def compute_mean_for_area(self, data: list):
        """Computes the mean price for an area
           for a given city.

        Given a list of data containing an area
        and price, this method computes the
        mean price for this area by keeping track
        of how many flats we have in this area,
        underneath represented as the variable
        "count", and the accumulating price.

        Args:
            data: A list containing the area name
                  as a string and a price, either
                  represented as a string, int, or
                  float.
        """
        for area, price in data:
            if self.mean_table.get(area):
                count, prev_price = self.mean_table[area]
                self.mean_table[area] = (count + 1, prev_price + int(price))
            else:
                self.mean_table[area] = (1, int(price))

    def get_mean_for(self, area: str) -> float:
        """fetches the mean price for an area"""
        count, price = self.mean_table.get(area)

        return round(price / count, 2)


def get_area_data_for(city: str) -> FlatData:
    """computes the mean prices of all areas
       for a given city"""
    data = FlatData()
    for current_row in flat_maps_data.data_for(city):
        area = current_row[3]
        price = current_row[0]
        data.compute_mean_for_area([(area, price)])

    return data
