#Task 1:: Set up a Python Virtual Environment and Install Required Packages
mkdir venv_project

cd venv_Project

python -m venv venv

venv\Scripts\activate

pip install requests


#Task 2: Fetch Data from the Space API
import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    for planet in planets:
        if planet['isPlanet']:
            name = planet['englishName']
            mass = planet.get('mass', {}).get('massValue', 'Unknown')
            orbit_period = planet.get('sideralOrbit', 'Unknown')
            print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")

fetch_planet_data()
#Task 3: Data Presentation and Analysis
import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']
    planet_data = []

    for planet in planets:
        if planet['isPlanet']:
            name = planet['englishName']
            mass = planet.get('mass', {}).get('massValue', 0)
            orbit_period = planet.get('sideralOrbit', 'Unknown')
            planet_data.append({'name': name, 'mass': mass, 'orbit_period': orbit_period})

    return planet_data

def find_heaviest_planet(planets):
    heaviest = max(planets, key=lambda p: p['mass'])
    return heaviest['name'], heaviest['mass']

planets = fetch_planet_data()
name, mass = find_heaviest_planet(planets)
print(f"The heaviest planet is {name} with a mass of {mass} x 10^24 kg.")
