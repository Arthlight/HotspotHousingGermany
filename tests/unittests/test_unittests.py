import sys
sys.path.append('/Users/arthred/Documents/Flat_Crawler_Django')
from scripts import flat_maps_comp, flat_maps_data


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
        ]

        for i in range(9):
            flat_data.compute_mean_for_area(data=dummy_data[i])

        assert flat_data.get_mean_for(area='Kreuzberg') == 150.00
        assert flat_data.get_mean_for(area='Friedrichshain') == 119.00
        assert flat_data.get_mean_for(area='Charlottenburg') == 2250.00
        assert flat_data.get_mean_for(area='Mitte') == 923.67

    def test_lat_long(self):
        assert flat_maps_data.get_lat_long('Lohmühlenstraße 65') == ('52.4938798', '13.4467241')
        assert flat_maps_data.get_lat_long('Thi6s ST44et dües NOT exist5f') == (None, None)










