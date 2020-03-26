from django.urls import path
from flats.views import BerlinPageView, MunichPageView, HamburgPageView


urlpatterns = [
    path('berlin/', BerlinPageView.as_view(), name='berlin'),
    path('munich/', MunichPageView.as_view(), name='munich'),
    path('hamburg/', HamburgPageView.as_view(), name='hamburg'),
]