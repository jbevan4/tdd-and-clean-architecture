from calculator.calculator import Calculator


class NasaHandler():

    def __init__(self):
        pass

    def get_data(self):
        pass

    def calculate_planet_mass(self, data):
        return Calculator.avg(float(planet.get("mass", 0)) for planet in data)
