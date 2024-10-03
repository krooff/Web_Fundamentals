#Task 1: Setting Up a Python Virtual Environment and Installing Packages

#In terminal run
#mkdir venv_project

#cd venv_Project

#python -m venv venv

#venv\Scripts\activate

#pip install requests

#Task 2: Fetching Data from the Pokémon API
import requests

def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    data = response.json()
    name = data['name']
    abilities = [ability['ability']['name'] for ability in data['abilities']]
    return name, abilities

name, abilities = fetch_pokemon_data('pikachu')
print(f"Name: {name}, Abilities: {abilities}")

import requests

def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    data = response.json()
    name = data['name']
    abilities = [ability['ability']['name'] for ability in data['abilities']]
    weight = data['weight']
    return {'name': name, 'abilities': abilities, 'weight': weight}

def calculate_average_weight(pokemon_list):
    total_weight = sum(pokemon['weight'] for pokemon in pokemon_list)
    return total_weight / len(pokemon_list)

pokemon_names = ["pikachu", "bulbasaur", "charmander"]
pokemon_data = [fetch_pokemon_data(name) for name in pokemon_names]

for pokemon in pokemon_data:
    print(f"Name: {pokemon['name']}, Abilities: {pokemon['abilities']}, Weight: {pokemon['weight']}")

average_weight = calculate_average_weight(pokemon_data)
print(f"Average Weight: {average_weight}")
