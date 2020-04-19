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
    # TODO: do error handling here
    # TODO: You probably need to amend the chart configs since there are so many areas that it doesn't have enough
    # TODO: room to display them all
    city = request.GET.get('city', '')
    flat_data = flat_maps_comp.get_area_data()
    area_table = flat_data.get_all_areas(city)
    labels = [key for key in area_table]
    items = [area_table[area][1] // area_table[area][0] for area in labels]
    data = {
        'labels': labels,
        'data': items,
    }

    return JsonResponse(data)

