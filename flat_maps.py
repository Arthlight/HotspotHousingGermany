import folium
from folium.plugins import MarkerCluster
import flat_maps_data
import flat_maps_comp


def display_berlin_data():

    berlin_map = folium.Map(location=[52.520008, 13.404954], zoom_start=11)
    berlin_cluster = MarkerCluster()
    for data in flat_maps_data.data_for_berlin():
        print("Entered for loop")

        mean_price_area = all_areas_data.get_mean(data[3], data[4])
        difference = abs(mean_price_area - data[0])
        price_per_sqm = data[0] / data[1]

        # TODO: Try to make the marker as good looking as poosible, maybe even with in-line css
        # TODO: If you can't figure out how to format the HTML properly, look into folium marker docs and tutorials etc
        marker_html = """
                    <ul>
                        <li>{street}</li>
                        <li>Price: {price} &euro;</li>
                        <li>Sqm: {sqm} &#13217;</li>
                        <li>Rooms: {rooms}</li>
                        <li>Price per Sqm: {psqm: .2f} &euro;</li>
                        <li>Mean price per Sqm in {area}: {mean: .2f} &euro;</li>
                        <li>Difference: {difference: .2f} &euro;</li>
                    <ul>
                    <h5><a href={url} target='_blank'>Original listing</a></h5>
                    """.format(
            street=data[2],
            price=data[0],
            sqm=data[1],
            rooms=data[5],
            url=data[6],
            psqm=price_per_sqm,
            area=data[3],
            mean=mean_price_area,
            difference=difference,
        )

        lat, long = flat_maps_data.get_lat_long_(data[2] + ' ' + data[4])
        print(lat, long)
        folium.Marker(
            location=(lat, long),
            popup=marker_html,
            tooltip='Click for more info',
            icon=folium.Icon(color='darkblue', icon='home', prefix='fa'),
        ).add_to(berlin_cluster)

        print("Next iteration about to begin")
    berlin_map.add_child(berlin_cluster)
    berlin_map.save('templates/berlin.html')


def display_hamburg_data():

    hamburg_map = folium.Map(location=[53.551086, 9.993682], zoom_start=11)
    for data in flat_maps_data.data_for_hamburg():

        mean_price_area = all_areas_data.get_mean(data[3], data[4])
        difference = abs(mean_price_area - data[0])

        marker_html = """
                    <h4><a href={url} target='_blank'>Original listing</a></h4>
                    <ul>
                        <li>{street}</li>
                        <li>Price: {price} &euro;</li>
                        <li>Sqm: {sqm} &#13217;</li>
                        <li>Rooms: {rooms}</li>
                        <li>Price per Sqm: {psqm: .2f} &euro;</li>
                        <li>Mean price per Sqm in {area}: {mean: .2f} &euro;</li>
                        <li>Difference: {difference: .2f} &euro;</li>
                    <ul>
                    """.format(
                    street=data[2],
                    price=data[0],
                    sqm=data[1],
                    rooms=data[5],
                    url=data[6],
                    psqm=6.69,
                    area=data[3],
                    mean=mean_price_area,
                    difference=difference,
                    )

        lat, long = flat_maps_data.get_lat_long_(data[2] + ' ' + data[4])
        folium.Marker(
            location=(lat, long),
            popup=marker_html,
            tooltip='Click for more info',
            icon=folium.Icon(color='blue', icon='fahome', prefix='fa'),
        ).add_to(hamburg_map)

    hamburg_map.save('templates/hamburg.html')


def display_munich_data():

    munich_map = folium.Map(location=[48.137154, 11.576124], zoom_start=11)
    for data in flat_maps_data.data_for_munich():

        mean_price_area = all_areas_data.get_mean(data[3], data[4])
        difference = abs(mean_price_area - data[0])

        marker_html = """
                    <h4><a href={url} target='_blank'>Original listing</a></h4>
                    <ul>
                        <li>{street}</li>
                        <li>Price: {price} &euro;</li>
                        <li>Sqm: {sqm} &#13217;</li>
                        <li>Rooms: {rooms}</li>
                        <li>Price per Sqm: {psqm: .2f} &euro;</li>
                        <li>Mean price per Sqm in {area}: {mean: .2f} &euro;</li>
                        <li>Difference: {difference: .2f} &euro;</li>
                    <ul>
                    """.format(
                    street=data[2],
                    price=data[0],
                    sqm=data[1],
                    rooms=data[5],
                    url=data[6],
                    psqm=6.69,
                    area=data[3],
                    mean=mean_price_area,
                    difference=difference,
                    )

        lat, long = flat_maps_data.get_lat_long_(data[2] + ' ' + data[4])
        folium.Marker(
            location=(lat, long),
            popup=marker_html,
            tooltip='Click for more info',
            icon=folium.Icon(color='blue', icon='home', prefix='fa'),
        ).add_to(munich_map)

    munich_map.save('templates/munich.html')


all_areas_data = flat_maps_comp.get_area_data()
display_berlin_data()
display_munich_data()
display_hamburg_data()
