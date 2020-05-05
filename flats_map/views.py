from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'

class BerlinPageView(TemplateView):
    template_name = 'Berlin.html'

class MunichPageView(TemplateView):
    template_name = 'München.html'

class HamburgPageView(TemplateView):
    template_name = 'Hamburg.html'
