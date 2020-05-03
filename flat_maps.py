"""This module contains the display logic for rendering the flat data onto the Folium Map.

This module queries the scraped flat data for all three cities (Berlin, Munich, Hamburg)
from a sqlite3 database with help of the flat_maps_data module and manages the display logic
for the marker on the Folium Map. Furthermore, this module interacts with the locationiq API
via the flat_maps_data module, in order to fetch the latitude and longitude for a given address.

  Typical usage example if imported inside another module:
  import flat_maps
  flat_maps.display_data()
"""
import sys
sys.path.append('/Users/arthred/Documents/Flat_Crawler_Django')
import folium
from folium.plugins import MarkerCluster
import flat_maps_data
import flat_maps_comp


data_html = """
            <body style="font-family:courier" width="400">
                <li>Street: {street}</li>
                <li>Price: {price} &euro;</li>
                <li>Sqm: {sqm} &#13217;</li>
                <li>Rooms: {rooms}</li>
                <li>Price per Sqm: {psqm: .2f} &euro;</li>
                <li>Mean price in {area}: {mean: .2f} &euro</li>
                <li>Difference: {difference: .2f} &euro;</li>
                <li><a href={url} target='_blank'>Original listing</a>   </li>
            </body>
            """


def display_berlin_data():
    berlin_map = folium.Map(location=[52.520008, 13.404954], zoom_start=11)
    cluster = MarkerCluster()
    berlin_cluster = display_helper('Berlin', cluster)
    berlin_map.add_child(berlin_cluster)
    berlin_map.save('templates/berlin.html')


def display_hamburg_data():
    hamburg_map = folium.Map(location=[53.551086, 9.993682], zoom_start=11)
    cluster = MarkerCluster()
    hamburg_cluster = display_helper('Hamburg', cluster)
    hamburg_map.add_child(hamburg_cluster)
    hamburg_map.save('templates/hamburg.html')


def display_munich_data():
    munich_map = folium.Map(location=[48.137154, 11.576124], zoom_start=11)
    cluster = MarkerCluster()
    munich_cluster = display_helper('München', cluster)
    munich_map.add_child(munich_cluster)
    munich_map.save('templates/munich.html')


def display_helper(city: str, cluster: MarkerCluster) -> MarkerCluster:
    #TODO: Call the upcoming get_area_data_for(city: str) -> FlatData function here and use that
    #TODO: instance below instead of "all_areas_data" which is absolutely not needed
    for data in flat_maps_data.data_for(city):

        street = data[2]
        price = data[0]
        sqm = data[1]
        rooms = data[5]
        url = data[6]
        area = data[3]
        city = data[4]
        mean_price_area = all_areas_data.get_mean(area=area, city=city)
        price_per_sqm = float(price) / float(sqm)
        difference = float(price) - mean_price_area

        marker_html = data_html.format(
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

        lat, long = flat_maps_data.get_lat_long_(data[2] + ' ' + data[4])
        if (lat, long) == (None, None):
            continue
        folium.Marker(
            location=(lat, long),
            popup=marker_html,
            tooltip='Click for more info',
            icon=folium.Icon(color='darkblue', icon='home', prefix='fa'),
        ).add_to(cluster)
        print("Next iteration about to begin")

    print('out of the for loop')
    return cluster


#TODO: Ideally make a function here that you can call which iniates the display logic
#TODO: Scratch the function below here completely and instead put that logic into the display helper
#TODO: function. look at the todo above
all_areas_data = flat_maps_comp.get_area_data()
#display_berlin_data()
#display_munich_data()
#display_hamburg_data()
