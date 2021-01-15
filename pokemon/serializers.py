from rest_framework import serializers
from .models import Pokemon

class PokemonSerializer2(serializers.ModelSerializer):

    class Meta:
        model = Pokemon
        fields = ['pokemon_id','name']

class PokemonSerializer(serializers.ModelSerializer):
    evolutions = PokemonSerializer2(many=True)
    preEvolution = PokemonSerializer2(many=True)

    class Meta:
        model = Pokemon
        fields = '__all__'