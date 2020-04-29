from django.urls import path
from .views import flat_data

urlpatterns = [
    path('flatData/', flat_data, name='flatData'),
]