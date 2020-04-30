import _sqlite3
import requests
import os
import dotenv
import json
import time


connection = _sqlite3.connect('Flat_Crawler_Scrapy/Flat_Crawler_Scrapy/flat_data.db', check_same_thread=False)
cursor = connection.cursor()


def data_for_berlin() -> tuple:
    cursor.execute("""SELECT * FROM flat_data WHERE city='Berlin'""")

    for row in cursor.fetchall():
        yield row


def data_for_munich() -> tuple:
    cursor.execute("""SELECT * FROM flat_data WHERE city='München'""")

    for row in cursor.fetchall():
        yield row


def data_for_hamburg() -> tuple:
    cursor.execute("""SELECT * FROM flat_data WHERE city='Hamburg'""")

    for row in cursor.fetchall():
        yield row


def get_lat_long_(street: str) -> tuple:
    """Fetches latitude and longitude from locationiq API.

    Given a string that represents a valid street address,
    this function calls the locationiq.com API in order to
    retrieve the latitude and longitude for that street.
    In case the API is down, which may be reflected with
    different Exceptions, this Exception will be caught
    gracefully and a tuple "(None, None)" will be returned.

    Args:
        street: A string containing a valid street address

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




