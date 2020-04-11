import _sqlite3
import requests
import os
import dotenv
import json
import time

#TODO: TOWARDS THE END, CHANGE THE CODE IN THE WAY SO THAT IT CONFORMS TO GOOGLES STYLE GUIDELINE

connection = _sqlite3.connect('Flat_Crawler_Scrapy/Flat_Crawler_Scrapy/flat_data.db')
cursor = connection.cursor()


def data_for_berlin() -> tuple:
    cursor.execute("""SELECT * FROM flat_data WHERE city='Berlin'""")

    print("before fetch")
    for row in cursor.fetchmany(20):
        print("fetch")
        yield row


def data_for_munich() -> tuple:
    cursor.execute("""SELECT * FROM flat_data WHERE city='München'""")

    for row in cursor.fetchmany(20):
        yield row


def data_for_hamburg() -> tuple:
    cursor.execute("""SELECT * FROM flat_data WHERE city='Hamburg'""")

    for row in cursor.fetchmany(20):
        yield row


def get_lat_long_(street: str) -> tuple:
    dotenv.read_dotenv()
    url = "https://eu1.locationiq.com/v1/search.php"
    print("waiting for api")

    data = {
        'key': os.getenv('API_KEY'),
        'q': street,
        'format': 'json',
    }

    # I can not use asyncio for asynchronous requests here because of the API limit and on top of it I have to block
    # ( 60 requests per minute )
    # TODO: Maybe put this in a try except block in case there are errors with the api or connection
    time.sleep(2)
    response = requests.get(url=url, params=data)
    decoded_response = json.loads(response.content)
    lat = decoded_response[0].get('lat')
    long = decoded_response[0].get('lon')

    return lat, long


