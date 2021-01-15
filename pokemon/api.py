from rest_framework import generics
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import HttpResponse, JsonResponse

from .models import Pokemon
from .serializers import PokemonSerializer


class PokemonsAPIView(generics.ListCreateAPIView):    

    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

def PokemonName(request, name):
    try:
        pokemon = Pokemon.objects.get(name=name)
    except Pokemon.DoesNotExist:
        return HttpResponse(JsonResponse({"message":"pokemon not found in db"}), status=404)

    if request.method == 'GET':
        serializer = PokemonSerializer(pokemon)
        return JsonResponse(serializer.data)