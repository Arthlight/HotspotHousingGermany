"""This module handles computing the mean prices for areas in a given city.

This module provides the City class, which is used to create instances
of cities and computing the average prices for their residential areas.
Furthermore one helper function is provided ("compute_area_mean_prices_for()"),
which is responsible for fetching all the areas for a given cities along with
their mean prices.

  Typical usage example of City class:

  my_city = City()
  my_city.insert([my_area, 500])
  my_city.insert([my_area, 500])
  my_city.get_mean_for(my_area) # returns 500 (mean of 500 + 500)

  Typical usage example of compute_area_mean_prices_for:

  area_data = compute_area_mean_prices_for('Berlin')
"""
# Standard library
import sys
sys.path.append('/Users/arthred/Documents/Flat_Crawler_Django')
sys.path.append('/Users/arthred/Documents/Flat_Crawler_Django/scripts')

# Third party
from scripts import flat_db


class City:
    """This Class computes and stores the average prices for
       each area in a given city.


    Attributes:
        mean_table: A dictionary mapping areas to their mean
                    prices.
    """

    def __init__(self):
        self.mean_table = {}

    def insert(self, data: list) -> None:
        """Inserts the area and price for
           a given flat.

        Given a list of data containing an area
        and price for a flat, this method inserts
        this information into the mean_table
        attribute of the current city instance.

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


def compute_area_mean_prices_for(city: str) -> City:
    """computes the mean prices of all areas
       for a given city"""
    current_city = City()
    for row in flat_db.data_for(city):
        row = dict(row)
        area = row['area']
        price = row['price']
        current_city.insert([(area, price)])

    return current_city
