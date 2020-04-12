from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView, View


class BerlinStatsView(TemplateView):
    template_name = 'stats_berlin.html'

class MunichStatsView(TemplateView):
    template_name = 'stats_munich.html'

class HamburgStatsView(TemplateView):
    template_name = 'stats_hamburg.html'

class Data(View):
    def get(request, *args, **kwargs):
        data = {
            'Kitkat': 80,
            'Yogurette': 99,
        }

        return JsonResponse(data)

