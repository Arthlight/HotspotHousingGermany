"""This module contains utility functions for the scripts package.

This module provides various helper functions that are meant to
enhance the scripts package.

The following functions are contained within this module:

  function get_lat_long             - accepts a street address
                                      in form of a string and
                                      requests the corresponding
                                      latitude and longitude via
                                      the locationIQ API.

  function get_response             - accepts an url in form of
                                      a string together with a
                                      dict containing parameters,
                                      in order to make a HTTP
                                      request.

  function decode_response          - accepts a request.Response
                                      object in binary form and
                                      decodes it into a JSON
                                      object.
"""

# Standard library
import requests
import os
import json
import time
from typing import Union

# Third party
import dotenv


def get_lat_long_with_timeout(streetaddress: str, timeout: int) -> tuple:
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

    # I have to block here, in order to not infringe the restrictions by the API provider
    # ( 60 requests per minute at most )
    time.sleep(timeout)
    dotenv.read_dotenv()
    url = "https://eu1.locationiq.com/v1/search.php"
    params = {
        'key': os.getenv('API_KEY'),
        'q': streetaddress,
        'format': 'json',
    }
    response = get_response(url, params)
    if response is not None:
        decoded_response = decode_response(response)
        if decoded_response is not None:
            return decoded_response


def get_response(url: str, params: dict) -> [requests.Response, None]:
    """Calls the given url with the given parameters.

    Args:
        url:          A string depicting a valid URL address.

        params:       A dictionary containing valid parameters
                      for a HTTP request.

    Returns:
        At success:   A dictionary containing the response.

        At failure:   A None object.
    """
    try:
        response = requests.get(url=url, params=params)
    except Exception:
        return None
    else:
        return response


def decode_response(response: requests.Response) -> Union[tuple, None]:
    """decodes the given response from binary to json.

        Args:
            response:     A requests.Response object
                          in binary representation.

        Returns:
            At success:   A tuple containing a latitude and
                          longitude.

            At failure:   A None object.
        """
    try:
        decoded_response = json.loads(response.content)
        lat = decoded_response[0].get('lat')
        long = decoded_response[0].get('lon')
    except KeyError:
        return None
    else:
        return (lat, long)
