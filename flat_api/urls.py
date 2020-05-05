from django.urls import path
from .views import gather_data, update_data

urlpatterns = [
    path('flatData/', gather_data, name='flatData'),
    path('primer/', update_data, name='primer'),
]