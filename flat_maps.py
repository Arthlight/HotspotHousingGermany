import sys
sys.path.append('/Users/arthred/Documents/Flat_Crawler_Django')
import folium
from folium.plugins import MarkerCluster
import flat_maps_data
import flat_maps_comp


data_html = """
            <li>{street}</li>
            <li>Price: {price} &euro;</li>
            <li>Sqm: {sqm} &#13217;</li>
            <li>Rooms: {rooms}</li>
            <li>Price per Sqm: {psqm: .2f} &euro;</li>
            <li>Mean price in {area}: {mean: .2f} &euro;</li>
            <li>Difference: {difference: .2f} &euro;</li>
            
            <h6><a href={url} target='_blank'>Original listing</a></h6>
            """


def display_berlin_data():

    berlin_map = folium.Map(location=[52.520008, 13.404954], zoom_start=11)
    berlin_cluster = MarkerCluster()
    for data in flat_maps_data.data_for_berlin():
        print("Entered for loop")
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
        print(lat, long)
        folium.Marker(
            location=(lat, long),
            popup=marker_html,
            tooltip='Click for more info',
            icon=folium.Icon(color='darkblue', icon='home', prefix='fa'),
        ).add_to(berlin_cluster)

        print("Next iteration about to begin")
    print('out of the for loop')
    berlin_map.add_child(berlin_cluster)
    berlin_map.save('templates/berlin.html')


def display_hamburg_data():

    hamburg_map = folium.Map(location=[53.551086, 9.993682], zoom_start=11)
    hamburg_cluster = MarkerCluster()
    for data in flat_maps_data.data_for_hamburg():
        print('in for loop of hamburg')

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
        print(lat, long)
        folium.Marker(
            location=(lat, long),
            popup=marker_html,
            tooltip='Click for more info',
            icon=folium.Icon(color='darkblue', icon='home', prefix='fa'),
        ).add_to(hamburg_cluster)

    hamburg_map.add_child(hamburg_cluster)
    hamburg_map.save('templates/hamburg.html')
    print('Out of hamburg for loop')


def display_munich_data():

    munich_map = folium.Map(location=[48.137154, 11.576124], zoom_start=11)
    munich_cluster = MarkerCluster()
    for data in flat_maps_data.data_for_munich():

        print('in for loop of munich')

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
        print(lat, long)
        folium.Marker(
            location=(lat, long),
            popup=marker_html,
            tooltip='Click for more info',
            icon=folium.Icon(color='darkblue', icon='home', prefix='fa'),
        ).add_to(munich_cluster)

    munich_map.add_child(munich_cluster)
    munich_map.save('templates/munich.html')
    print('out of munich for loop')


all_areas_data = flat_maps_comp.get_area_data()
#display_berlin_data()
#display_munich_data()
#display_hamburg_data()
