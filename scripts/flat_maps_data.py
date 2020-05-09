"""This module handles fetching data for geographical input.

This module contains helper functions that query or fetch data
for geographical input such as a city or street address.

The following helper functions are contained within this module:

    function data_for           - accepts a city name in form of
                                  a string and queries the local
                                  sqlite3 database for the
                                  associated information.

    function get_lat_long       - accepts a street address in form
                                  of a string and requests the
                                  corresponding latitude and longitude
                                  from the locationIQ API.
"""
# Standard library
import sys
sys.path.append('/Users/arthred/Documents/Flat_Crawler_Django')
sys.path.append('/Users/arthred/Documents/Flat_Crawler_Django/scripts')
import _sqlite3
import requests
import os
import json
import time

# Third party
import dotenv


def data_for(city: str) -> tuple:
    """Queries flat data from a sqlite3 database for a specific city

    Given a string that represents a city, which is present in the
    database (München, Berlin, Hamburg), this generator returns
    one tuple of flat data at a time.

    Args:
        city: A string that represents a valid city

    Returns:
        row:  A tuple containing all the values from
              every column in one row of the database.
              The following order is guaranteed to be
              the same every time:
              0: price
              1: sqm
              2: street
              3: area
              4: city
              5: rooms
              6: detail_view_url
    """
    connection = _sqlite3.connect('flats_data.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM flats_data WHERE city=?""", (city,))

    for row in cursor.fetchall():
        print(row)
        yield row


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

