import folium
from folium.plugins import MarkerCluster
import flat_maps_data



berlin_map = folium.Map(location=[52.520008, 13.404954], zoom_start=11)
berlin_cluster = MarkerCluster()
for data in flat_maps_data.data_for_berlin():
    print("Entered for loop")


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
                  mean=2.22,
                  difference=2.22,
                  )

    lat, long = flat_maps_data.get_lat_long_(data[2] + ' ' + data[4])
    print(lat, long)
    folium.Marker(
        location=(lat,long),
        popup=marker_html,
        tooltip='Click for more info',
        icon=folium.Icon(color='darkblue', icon='home', prefix='fa')
    ).add_to(berlin_cluster)

    print("Next iteration about to begin")
berlin_map.add_child(berlin_cluster)
berlin_map.save('templates/berlin.html')

hamburg_map = folium.Map(location=[53.551086, 9.993682], zoom_start=11)
for data in flat_maps_data.data_for_hamburg():

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
                  mean=2.22,
                  difference=2.22,
                  )

    lat, long = flat_maps_data.get_lat_long_(data[2] + ' ' + data[4])
    folium.Marker(
        location=(lat,long),
        popup=marker_html,
        tooltip='Click for more info',
        icon=folium.Icon(color='blue', icon='fahome', prefix='fa')
    ).add_to(hamburg_map)

hamburg_map.save('templates/hamburg.html')

munich_map = folium.Map(location=[48.137154, 11.576124], zoom_start=11)
for data in flat_maps_data.data_for_munich():

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
                  mean=2.22,
                  difference=2.22,
                  )

    lat, long = flat_maps_data.get_lat_long_(data[2] + ' ' + data[4])
    folium.Marker(
        location=(lat,long),
        popup=marker_html,
        tooltip='Click for more info',
        icon=folium.Icon(color='blue', icon='home', prefix='fa')
    ).add_to(munich_map)

munich_map.save('templates/munich.html')