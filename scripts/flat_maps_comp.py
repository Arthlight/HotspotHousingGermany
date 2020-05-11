"""This module handles computing the mean prices for areas in a given city.

This module provides the FlatData class, which is used to create instances
of cities and computing the average prices for their residential areas.
Furthermore two helper functions are provided. The first is "get_area_data_for",
which is responsible for fetching all the areas for a given cities along
with their mean prices.
The second is "get_lat_long", which is responsible for fetching the latitude
and longitude for a given address.

  Typical usage example of FlatData class:

  my_city = FlatData()
  my_city.compute_mean_for([my_area, 500])
  my_city.compute_mean_for([my_area, 500])
  my_city.get_mean_for(my_area) # returns 500 (mean of 500 + 500)

  Typical usage example of get_area_data_for:

  area_data = get_area_data_for('Berlin')

  Typical usage example of get_lat_long:

  lat, long = get_lat_long('Lohmühlenstraße 65')

"""
# Standard library
import sys
sys.path.append('/Users/arthred/Documents/Flat_Crawler_Django')
sys.path.append('/Users/arthred/Documents/Flat_Crawler_Django/scripts')
import requests
import os
import json
import time

# Third party
import dotenv
from scripts import flat_db


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
    for current_row in flat_db.data_for(city):
        area = current_row[3]
        price = current_row[0]
        data.compute_mean_for_area([(area, price)])

    return data


def get_lat_long(street: str) -> tuple:
    """Fetches latitude and longitude from locationiq API.

    Given a string that represents a valid street address,
    this function calls the locationIQ.com API in order to
    retrieve the latitude and longitude for that street.
    In case the API is down, which may be reflected with
    different Exceptions, this Exception will be caught
    gracefully and a tuple "(None, None)" will be returned.

    Args:
        street:    A string containing a valid street address

    Returns:
        lat, long: A tuple containing the latitude and
                   longitude for the given street address,
                   in that order. In case the input was
                   invalid or the API happens to be down,
                   a tuple containing two None values
                   "(None, None)" will be returned.
    """

    dotenv.read_dotenv()
    url = "https://eu1.locationiq.com/v1/search.php"
    print("waiting for api")

    data = {
        'key': os.getenv('API_KEY'),
        'q': street,
        'format': 'json',
    }

    # can not use asyncio for asynchronous requests here because of the API limit and on top of it I have to block
    # ( 60 requests per minute at most, requirement by provider)
    try:
        response = requests.get(url=url, params=data)
    except Exception:
        return (None, None)
    else:
        try:
            decoded_response = json.loads(response.content)
            lat = decoded_response[0].get('lat')
            long = decoded_response[0].get('lon')
        except KeyError:
            return (None, None)
        else:
            time.sleep(2)
            return (lat, long)
