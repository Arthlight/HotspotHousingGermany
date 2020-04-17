from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView, View


class BerlinStatsView(TemplateView):
    template_name = 'stats_berlin.html'

class MunichStatsView(TemplateView):
    template_name = 'stats_munich.html'

class HamburgStatsView(TemplateView):
    template_name = 'stats_hamburg.html'


class ChartData(View):
    # TODO: Probably enhance the ajax request to also include some information on where I'm calling from and then
    # TODO: read that information out of the args or kwargs. For example I pass "berlin" into args and therefore know
    # TODO: that I'll need the berlin data
    def get(request, *args, **kwargs):
        labels = ['Prenzlauer Berg', 'Kreuzberg', 'Charlottenburg', 'Friedrichshain', 'Mitte', 'Neuköln']
        items = [20, 18, 14, 12, 10, 7]
        data = {
            'labels': labels,
            'data': items,
        }

        return JsonResponse(data)

