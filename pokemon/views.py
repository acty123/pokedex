from django.shortcuts import render
from django.http import HttpResponse
from .models import Pokemon
import requests
import json

def savePokemon(request, evo_id=1):
    urlEvo = 'https://pokeapi.co/api/v2/evolution-chain/%s' % evo_id
    response = requests.get(urlEvo)
    
    if response.status_code == 200:
        dataChainEvo = json.loads(response.text)
        continueEvoTo(dataChainEvo['chain'])
        
    else:
        return HttpResponse('An error occurred querying the API, or id does not exist')
    return HttpResponse("Save pokemon")

def continueEvoTo(chain):
    pokemon = saveGeneralData(chain['species']['name'])
    
    if len(chain["evolves_to"]) != 0:
        for evo in chain["evolves_to"]:
            continueEvoTo(evo)         

def saveGeneralData(pokemonName):
    urlPoke = 'https://pokeapi.co/api/v2/pokemon/%s' % pokemonName
    response2 = requests.get(urlPoke)
    if response2.status_code == 200:
        dataGeneralPokemon = json.loads(response2.text)
        weight = dataGeneralPokemon['weight']
        height = dataGeneralPokemon['height']
        pokemonId = dataGeneralPokemon['id']
        stats = dataGeneralPokemon['stats']
        hp = defense = attack = speed =  specialDefense = specialAttack = 0
        for stat in stats:
            hp = stat['base_stat'] if stat['stat']['name'] == 'hp' else hp
            defense = stat['base_stat'] if stat['stat']['name'] == 'defense' else defense
            attack = stat['base_stat'] if stat['stat']['name'] == 'attack' else attack
            speed = stat['base_stat'] if stat['stat']['name'] == 'speed' else speed
            specialDefense = stat['base_stat'] if stat['stat']['name'] == 'special-defense' else specialDefense
            specialAttack = stat['base_stat'] if stat['stat']['name'] == 'special-attack' else specialAttack
        
        urlSpecies = dataGeneralPokemon['species']['url']
        ## save pokemon data
        pokemon = Pokemon.objects.create(
            name = pokemonName,
            pokemon_id = pokemonId,
            weight = weight,
            height = height,
            hp = hp,
            attack = attack,
            defense = defense,
            specialAttack = specialAttack,
            specialDefense = specialDefense,
            speed = speed
        )

        response3 = requests.get(urlSpecies)
        if response3.status_code == 200:
            dataSpeciesPokemon = json.loads(response3.text)
            preEvo = dataSpeciesPokemon['evolves_from_species']
            if preEvo != None:
                preEvoPokemon = Pokemon.objects.filter(name=preEvo['name'])[0]
                pokemon.preEvolution.add(preEvoPokemon.pokemon_id)
                preEvoPokemon.evolutions.add(pokemon.pokemon_id)
                
                if preEvoPokemon.preEvolution.first() != None:
                    firstPokemon = preEvoPokemon.preEvolution.first()
                    firstPokemon.evolutions.add(pokemon.pokemon_id)
                    pokemon.preEvolution.add(firstPokemon.pokemon_id)
        return pokemon


