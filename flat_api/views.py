import pickle
from . import database
from django.http import HttpResponse
from rest_framework.decorators import api_view


@api_view(['POST'])
def flat_data(request):
    decoded_data = pickle.loads(request.body)
    database.insert_into_db(decoded_data)

    return HttpResponse(status=200)

