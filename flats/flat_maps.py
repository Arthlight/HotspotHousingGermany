import folium
import _sqlite3
import os

connection = _sqlite3.connect('Flat_Crawler_Scrapy/Flat_Crawler_Scrapy/flat_data.db')
cursor = connection.cursor()

cursor.execute("""SELECT * FROM flat_data WHERE city='Berlin'""")
rows = cursor.fetchall()

berlin_map = folium.Map(location=[52.520008, 13.404954], zoom_start=11)
berlin_map.save('templates/berlin.html')

for data in rows:
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
                  """.format()
# TODO: FILL IN THE FORMAT METHOD

cursor.execute("""SELECT * FROM flat_data WHERE city='Hamburg'""")
rows = cursor.fetchall()

hamburg_map = folium.Map(location=[53.551086, 9.993682], zoom_start=11)
hamburg_map.save('templates/hamburg.html')

cursor.execute("""SELECT * FROM flat_data WHERE city='Münnchen'""")
rows = cursor.fetchall()

munich_map = folium.Map(location=[48.137154, 11.576124], zoom_start=11)
munich_map.save('templates/munich.html')