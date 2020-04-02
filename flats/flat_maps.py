import folium
import _sqlite3
from flats import flat_maps_data


munich_data = flat_maps_data.get_data_for_munich()
hamburg_data = flat_maps_data.get_data_for_hamburg()
berlin_data = flat_maps_data.get_data_for_berlin()


berlin_map = folium.Map(location=[52.520008, 13.404954], zoom_start=11)

for data in berlin_data:
    # This is what is going to be displayed on the marker
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
                  street=data.street,
                  price=data.price,
                  sqm=data.sqm,
                  rooms=data.rooms,
                  psqm=...,
                  mean=...,
                  difference=...,
                  )

    lat, long = flat_maps_data.get_lat_long_()
    folium.Marker(
        location=(lat,long),
        popup=marker_html,
        tooltip='Click for more info',
        icon=...,
    ).add_to(berlin_map)

berlin_map.save('templates/berlin.html')


hamburg_map = folium.Map(location=[53.551086, 9.993682], zoom_start=11)
hamburg_map.save('templates/hamburg.html')


munich_map = folium.Map(location=[48.137154, 11.576124], zoom_start=11)
munich_map.save('templates/munich.html')