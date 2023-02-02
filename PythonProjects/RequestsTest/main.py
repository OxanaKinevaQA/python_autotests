import requests

token = '253bd5301c17e40ce14790c6c377f230'

#создание покемона
response_pokemons = requests.post('https://pokemonbattle.me:5000/pokemons', json = {
    'name': 'M45',
    'photo': 'https://dolnikov.ru/pokemons/05.png'
}, headers = {'Content-Type': 'application/json', 'trainer_token': token})

print(response_pokemons.text)

#изменение имени покемона
response_change = requests.put('https://pokemonbattle.me:5000/pokemons', json = {
    "pokemon_id": 4648,
    "name": "Mimimi",
    "photo": "https://dolnikov.ru/pokemons/05.png"
}, headers = {'Content-Type': 'application/json', 'trainer_token': token})

print(response_change.text)

#поимка покемона в покебол
response_add = requests.post('https://pokemonbattle.me:5000/trainers/add_pokeball', json = {
    "pokemon_id": '4648'
}, headers = {'Content-Type': 'application/json', 'trainer_token': token})

print(response_add.text)