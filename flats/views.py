from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'

class BerlinPageView(TemplateView):
    template_name = 'berlin.html'

class MunichPageView(TemplateView):
    template_name = 'munich.html'

class HamburgPageView(TemplateView):
    template_name = 'hamburg.html'
