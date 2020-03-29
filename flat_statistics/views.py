from django.shortcuts import render
from django.views.generic import TemplateView


class BerlinStatsView(TemplateView):
    template_name = 'stats_berlin.html'

class MunichStatsView(TemplateView):
    template_name = 'stats_munich.html'

class HamburgStatsView(TemplateView):
    template_name = 'stats_hamburg.html'
