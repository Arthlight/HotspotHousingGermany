import sys
sys.path.append('/Users/arthred/Documents/Flat_Crawler_Django')
import flat_maps_comp
import flat_maps
from folium.plugins import MarkerCluster


class Test:

    def test_mean(self):
        flat_data = flat_maps_comp.FlatData()
        dummy_data = [
            [('Kreuzberg', 100)],
            [('Friedrichshain', 150)],
            [('Kreuzberg', 200)],
            [('Friedrichshain', 88)],
            [('Charlottenburg', 4300)],
            [('Mitte', 333.77)],
            [('Charlottenburg', 200)],
            [('Mitte', 1033.88)],
            [('Mitte', 1405.60)],
            'Berlin'
        ]

        for i in range(9):
            flat_data.compute_mean_for_area(data=dummy_data[i], city=dummy_data[9])

        assert flat_data.get_mean(area='Kreuzberg', city='Berlin') == 150.00
        assert flat_data.get_mean(area='Friedrichshain', city='Berlin') == 119.00
        assert flat_data.get_mean(area='Charlottenburg', city='Berlin') == 2250.00
        assert flat_data.get_mean(area='Mitte', city='Berlin') == 923.67

    def test_area_by_city(self):
        berlin_areas = flat_maps_comp.get_areas_by_city(city='Berlin')
        munich_areas = flat_maps_comp.get_areas_by_city(city='München')
        hamburg_areas = flat_maps_comp.get_areas_by_city(city='Hamburg')
        dummy_areas = ['Mitte (Mitte)', 'Bogenhausen', 'Winterhude']
        dummy_instances = [berlin_areas.mean_table_berlin, munich_areas.mean_table_munich, hamburg_areas.mean_table_hamburg]

        for i in range(3):
            assert dummy_areas[i] in dummy_instances[i]


    def test_display(self):
        dummy_cluster = MarkerCluster()

        new_cluster = flat_maps.display_helper('Berlin', dummy_cluster)
        print(new_cluster.to_dict())






