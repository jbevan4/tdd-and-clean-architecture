from requests import get

from calculator.calculator import Calculator


class NasaHandler():

    def __init__(self):
        pass

    def get_data(self):
        response = get("https://data.nasa.gov/resource/y77d-th95.json")
        return response.json()

    def calculate_planet_mass(self, data):
        return Calculator.avg(float(planet.get("mass", 0)) for planet in data)
