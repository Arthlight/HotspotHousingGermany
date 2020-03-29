import folium
import _sqlite3

connection = _sqlite3.connect('Flat_Crawler_Scrapy/Flat_Crawler_Scrapy/flat_data.db')

berlin_map = folium.Map(location=[52.520008, 13.404954], zoom_start=11)
berlin_map.save('templates/berlin.html')

hamburg_map = folium.Map(location=[53.551086, 9.993682], zoom_start=11)
hamburg_map.save('templates/hamburg.html')

munich_map = folium.Map(location=[48.137154, 11.576124], zoom_start=11)
munich_map.save('templates/munich.html')