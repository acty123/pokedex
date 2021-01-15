from django.urls import path
from .views import savePokemon
from .api import PokemonsAPIView, PokemonName

urlpatterns = [
    path('<int:evo_id>', savePokemon),
    path('pokemons/', PokemonsAPIView.as_view()),
    path('pokemon/<str:name>/', PokemonName),
]
