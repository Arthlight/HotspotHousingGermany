from django.urls import path
from .views import BerlinStatsView, MunichStatsView, HamburgStatsView, Data

urlpatterns = [
    path('berlin/', BerlinStatsView.as_view(), name='stats_berlin'),
    path('munich/', MunichStatsView.as_view(), name='stats_munich'),
    path('hamburg/', HamburgStatsView.as_view(), name='stats_hamburg'),
    path('berlin/data', Data.as_view(), name='stats_berlin_data'),
    path('munich/data', Data.as_view(), name='stats_munich_data'),
    path('hamburg/data', Data.as_view(), name='stats_hamburg_data'),
]