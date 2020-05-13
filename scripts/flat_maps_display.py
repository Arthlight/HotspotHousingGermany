"""This module contains the display logic for rendering the flat data onto the Folium Map.

This module queries the scraped flat data for all three cities (Berlin, Munich, Hamburg)
from a sqlite3 database with help of the flat_maps_data module and manages the display logic
for the marker on the Folium Map. Furthermore, this module interacts with the locationIQ API
via the flat_maps_data module, in order to fetch the latitude and longitude for a given address.

  Typical usage example if imported inside another module:

  import flat_maps
  flat_maps.display_data()
"""
# Standard library
import sys
sys.path.append('/Users/arthred/Documents/Flat_Crawler_Django')
sys.path.append('/Users/arthred/Documents/Flat_Crawler_Django/scripts')

# Third party
import folium
from folium.plugins import MarkerCluster
from scripts import flat_maps_comp, flat_db, flat_maps_utils


# Module level CSS template used for Folium Markers
DATA_CSS = """
            <html>
            <head>
            <style>
            table, th, td {
                border: 1px solid black;
                border-collapse: collapse;
            }
            th, td {
                padding: 5px;
                text-align: left;
            }
            </style>
            </head>
            <body>
           """

# Module level HTML template used for Folium Markers
DATA_HTML = """
            <table style="width:500px">
                <tr>
                    <th>Street:</th>
                    <td>{street}</td>
                </tr>
                <tr>
                    <th>Price:</th>
                    <td>{price} &euro;</td>
                </tr>
                <tr>
                    <th>Mean price in {area}:</th>
                    <td>{mean: .2f} &euro;</td>
                </tr>
                <tr>
                    <th>Difference:</th>
                    <td>{difference: .2f} &euro;</td>
                </tr>
                <tr>
                    <th>Sqm:</th>
                    <td>{sqm} &#13217;</td>
                </tr>
                <tr>
                    <th>Rooms:</th>
                    <td>{rooms}</td>
                </tr>
                <tr>
                    <th>Price Per Sqm:</th>
                    <td>{psqm: .2f} &euro;</td>
                </tr>
                <tr>
                    <th>Original Listing:</th>
                    <td><a href={url} target='_blank'>Click here to see original offer</a></td>
                </tr>
            </table>
            </body>
            </html>
            """


def display_data_for(city: str, *, lat: float, long: float):
    """Creates a map and populates it with scraped data"""
    city_map = folium.Map(location=[lat, long], zoom_start=11)
    cluster = MarkerCluster()
    cluster = display_helper(f'{city}', cluster)
    city_map.add_child(cluster)
    city_map.save(f'templates/{city}.html')


def display_helper(city: str, cluster: MarkerCluster) -> MarkerCluster:
    """Iterates through the flat data of a given city,
       labels it and finalizes it for display on the
       map.

       Given a city and a MarkerCluster instance, this
       function queries the complete sqlite3 table for
       all rows where the city name matches the name in
       the city column. After it received the data of
       such a row, the HTML template for the Marker
       will be popularized and finally added to the
       MarkerCluster.


      Args:
          city:    A string containing a valid city name.
                   Valid in this context means that it
                   must be present in the sqlite3 table
                   before calling this function.

          cluster: A MarkerCluster instance.

      Returns:
          cluster: A populated MarkerCluster instance.

    """
    city_data = flat_maps_comp.get_area_data_for(city)
    for data in flat_db.data_for(city):
        print(data)
        price = data[0]
        sqm = data[1]
        street = data[2]
        area = data[3]
        city = data[4]
        rooms = data[5]
        url = data[6]
        mean_price_area = city_data.get_mean_for(area)
        price_per_sqm = float(price) / float(sqm)
        difference = float(price) - mean_price_area

        marker_html = DATA_HTML.format(
                        street=street,
                        price=price,
                        sqm=sqm,
                        rooms=rooms,
                        url=url,
                        psqm=price_per_sqm,
                        area=area,
                        mean=mean_price_area,
                        difference=difference,
                    )

        lat, long = flat_maps_utils.get_lat_long(street + ' ' + city)
        if (lat, long) == (None, None):
            continue
        folium.Marker(
            location=(lat, long),
            popup=DATA_CSS + marker_html,
            tooltip='Click for more info',
            icon=folium.Icon(color='darkblue', icon='home', prefix='fa'),
        ).add_to(cluster)
        print("Next iteration about to begin")

    print('out of the for loop')
    return cluster


def display_all_cities():
    """Primer for displaying
       flat data for all cities"""
    display_data_for('Berlin',  lat=52.520008, long=13.404954)
    display_data_for('München', lat=48.137154, long=11.576124)
    display_data_for('Hamburg', lat=53.551086, long=9.993682)



