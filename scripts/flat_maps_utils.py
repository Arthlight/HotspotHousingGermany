"""This module contains utility functions for the scripts package.

This module provides various helper functions that are meant to
enhance the scripts package.

The following functions are contained within this module:

  function get_lat_long             - accepts a street address
                                      in form of a string and
                                      requests the corresponding
                                      latitude and longitude via
                                      the locationIQ API.
"""

# Standard library
import requests
import os
import json
import time

# Third party
import dotenv


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