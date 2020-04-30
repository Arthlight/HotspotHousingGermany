import pickle
from django.http import HttpResponse
from rest_framework.decorators import api_view


@api_view(['POST'])
def flat_data(request):
    print(pickle.loads(request.body))

    return HttpResponse(status=200)


