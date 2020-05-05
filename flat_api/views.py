import sys
sys.path.append('/Users/arthred/Documents/Flat_Crawler_Django')
from django.http import HttpResponse
from rest_framework.decorators import api_view
import pickle
from . import database


@api_view(['POST'])
def gather_data(request):
    decoded_data = pickle.loads(request.body)
    database.insert_into_db(decoded_data)

    return HttpResponse(status=200)


@api_view(['PUT'])
def update_data(request):
    #flat_maps.display_all_cities()

    return HttpResponse(status=200)