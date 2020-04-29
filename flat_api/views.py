from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view


@api_view(['POST'])
def flat_data(request):
    print('This works, nice!')

    return HttpResponse(status=200)


