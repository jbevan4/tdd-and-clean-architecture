from unittest.mock import Mock, patch
from json import load, dumps

from requests import Response

from .nasa import NasaHandler


class FakeResponse:
    def __init__(self, data):
        self.data = data

    def json(self):
        return self.data


def test_can_sum_mass_of_planets():
    nh = NasaHandler()
    nh.get_data = Mock()
    nh.get_data.return_value = [
        {
            "fall": "Fell",
            "geolocation": {
                "type": "Point",
                "coordinates": [6.08333, 50.775]
            },
            "id":"1",
            "mass":"21",
            "name":"Aachen",
            "nametype":"Valid",
            "recclass":"L5",
            "reclat":"50.775000",
            "reclong":"6.083330",
            "year":"1880-01-01T00:00:00.000"},
        {
            "fall": "Fell",
            "geolocation": {
                "type": "Point",
                "coordinates": [10.23333, 56.18333]
            },
            "id":"2",
            "mass":"720",
            "name":"Aarhus",
            "nametype":"Valid",
            "recclass":"H6",
            "reclat":"56.183330",
            "reclong":"10.233330",
            "year":"1951-01-01T00:00:00.000"
        }
    ]
    assert nh.calculate_planet_mass(nh.get_data()) == 370.5


@patch('nasa.nasa.get')
def test_can_workout_planets_average_mass(request_mock):
    test_mock = FakeResponse([{"id": 1, "mass": 20}, {"id": 2, "mass": 80}])
    request_mock.return_value = test_mock
    nh = NasaHandler()
    result = nh.get_data()
    request_mock.assert_called_once()
    assert nh.calculate_planet_mass(result) == 50
