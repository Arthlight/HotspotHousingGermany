import _sqlite3
import requests
import os
import dotenv

#TODO: TOWARDS THE END, CHANGE THE CODE IN THE WAY SO THAT IT CONFORMS TO GOOGLES STYLE GUIDELINE

connection = _sqlite3.connect('Flat_Crawler_Scrapy/Flat_Crawler_Scrapy/flat_data.db')
cursor = connection.cursor()

def data_for_berlin():
    cursor.execute("""SELECT * FROM flat_data WHERE city='Berlin'""")

    for row in cursor.fetchone():
        yield row





def data_for_munich():
    cursor.execute("""SELECT * FROM flat_data WHERE city='München'""")

    for row in cursor.fetchone():
        yield row





def data_for_hamburg():
    cursor.execute("""SELECT * FROM flat_data WHERE city='Hamburg'""")

    for row in cursor.fetchone():
        yield row




def get_lat_long_(street):
    dotenv.read_dotenv()
    url = "https://us1.locationiq.com/v1/search.php"

    data = {
        'key': os.getenv('API_KEY'),
        'q': street,
        'format': 'json',
    }

    response = requests.get(url=url, params=data)
    print(response.content)
#TODO: You probably have to block here with time.sleep/wait or sth else, bc only 2 requests per second are allowed

get_lat_long_('Wichertstraße 63')

