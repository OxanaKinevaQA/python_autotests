import requests
import pytest

def tests_status():
    response = requests.get('https://pokemonbattle.me:5000/trainers')
    assert response.status_code == 200

def tests_contain_name():
    response = requests.get('https://pokemonbattle.me:5000/trainers', params={'trainer_id': '2005'})
    assert response.json()['trainer_name'] == 'AngryBird'
