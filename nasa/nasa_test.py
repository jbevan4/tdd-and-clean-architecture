from unittest.mock import Mock
from json import load

import requests_mock

from .nasa import NasaHandler


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


def test_can_make_an_external_request():
    with open("response.json") as response_json:
        mock_response = load(response_json)

    nh = NasaHandler()

    with requests_mock.Mocker() as mock:
        mock.get("https://data.nasa.gov/resource/y77d-th95.json",
                 json=mock_response)
        response = nh.get_data()
        assert response == mock_response
