from scripts import flat_maps_comp
from django.http import JsonResponse
from django.views.generic import TemplateView


class BerlinStatsView(TemplateView):
    template_name = 'stats_berlin.html'


class MunichStatsView(TemplateView):
    template_name = 'stats_münchen.html'


class HamburgStatsView(TemplateView):
    template_name = 'stats_hamburg.html'


def get_stats(request, *args, **kwargs):
    city = request.GET.get('city', '')
    city = flat_maps_comp.compute_area_mean_prices_for(city)

    # sorted such that the areas are being displayed from the most expensive one down to the least expensive one
    labels = sorted([key for key in city.mean_table], key=lambda key: city.mean_table[key][1], reverse=True)
    items = sorted([city.mean_table[area][1] // city.mean_table[area][0] for area in labels], reverse=True)
    data = {
        'labels': labels,
        'data': items,
    }

    return JsonResponse(data)

