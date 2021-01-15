This project was created with [Django](https://www.djangoproject.com/) and [Create React App](https://www.django-rest-framework.org/).
Install requirements to work and migrations

## Runs the app <br>
### `python manage.py runserver`

## Avaible script to save pokemon
if the script is successful it will respond to the following message (`Save pokemon`) otherwise (`An error occurred querying the API, or id does not exist`)
### `./myscript.sh {id}`

## Endpoints
Open [http://127.0.0.1:8000/fetch/pokemons](http://127.0.0.1:8000/fetch/pokemons) to view pokemon list in the browser.<br>
Open [http://127.0.0.1:8000/fetch/pokemons/?search=charm](http://127.0.0.1:8000/fetch/pokemons/?search=charm) to view pokemons that contain part of this name in the browser.<br>
Open [http://127.0.0.1:8000/fetch/pokemon/{name}/](http://127.0.0.1:8000/fetch/pokemon/<str:name>/) to view pokemon detail in the browser.(replace `name` with the exact pokemon name)<br>

Note: remember you only can see pokemons available in db.