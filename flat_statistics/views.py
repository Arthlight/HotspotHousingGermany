import sys
sys.path.append('$(pwd)/Flat_Crawler_Django')
import flat_maps_comp
from django.http import JsonResponse
from django.views.generic import TemplateView


class BerlinStatsView(TemplateView):
    template_name = 'stats_berlin.html'


class MunichStatsView(TemplateView):
    template_name = 'stats_munich.html'


class HamburgStatsView(TemplateView):
    template_name = 'stats_hamburg.html'


def get_stats(request, *args, **kwargs):
    city = request.GET.get('city', '')
    flat_data = flat_maps_comp.get_areas_by_city(city=city)
    area_table = flat_data.get_all_areas(city=city)

    # sorted such that the areas are being displayed from the most expensive one down to the least expensive one
    labels = sorted([key for key in area_table], key=lambda key: area_table[key][1], reverse=True)
    items = sorted([area_table[area][1] // area_table[area][0] for area in labels], reverse=True)
    data = {
        'labels': labels,
        'data': items,
    }

    return JsonResponse(data)

