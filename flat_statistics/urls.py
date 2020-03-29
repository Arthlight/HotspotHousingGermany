from django.urls import path
from .views import BerlinStatsView, MunichStatsView, HamburgStatsView

urlpatterns = [
    path('berlin/', BerlinStatsView.as_view(), name='stats_berlin'),
    path('munich/', MunichStatsView.as_view(), name='stats_munich'),
    path('hamburg/', HamburgStatsView.as_view(), name='stats_hamburg'),
]