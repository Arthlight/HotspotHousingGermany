from django.urls import path
from .views import gather_data, before, after

urlpatterns = [
    path('flatData/', gather_data, name='flatData'),
    path('before/', before, name='before'),
    path('after/', after, name='after'),
]