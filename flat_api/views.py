# Standard library
import sys
sys.path.append('/Users/arthred/Documents/Flat_Crawler_Django')
sys.path.append('/Users/arthred/Documents/Flat_Crawler_Django/scripts')
import pickle
from . import database
from django.http import HttpResponse
from scripts import flat_maps

# Third party
from rest_framework.decorators import api_view


@api_view(['POST'])
def gather_data(request):
    print('in here')
    decoded_data = pickle.loads(request.body)
    database.insert_into_db(decoded_data)

    return HttpResponse(status=200)


@api_view(['POST'])
def before(request):
    database.reload_data()

    return HttpResponse(status=200)


@api_view(['POST'])
def after(request):
    #flat_maps.display_all_cities()

    return HttpResponse(status=200)