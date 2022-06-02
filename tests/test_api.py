import json
from unittest.mock import patch

import pytest

from irishrail import api


@pytest.fixture
def station_data():
    with open("tests/data/station_data.json") as fp:
        return json.load(fp)


@pytest.fixture
def stations_data():
    with open("tests/data/stations.json") as fp:
        return json.load(fp)


@patch("irishrail.api.httpx.get")
def test_request(mocked_get):
    mocked_get.return_value.content = "<response></response>"
    assert api._request("url") == {"response": None}


@patch("irishrail.api._request")
def test_next_trains_right_order(mocked_request, station_data):
    mocked_request.return_value = station_data
    trains = api.next_trains("station")
    duein_0 = int(trains[0]["Duein"])
    duein_1 = int(trains[1]["Duein"])
    duein_2 = int(trains[2]["Duein"])
    assert duein_0 < duein_1 < duein_2
    assert len(trains) == 3


@patch("irishrail.api._request")
def test_no_next_trains(mocked_request):
    mocked_request.return_value = {"ArrayOfObjStationData": {}}
    assert api.next_trains("station") == []


@patch("irishrail.api._request")
def test_list_stations(mocked_request, stations_data):
    mocked_request.return_value = stations_data
    stations = api.list_stations()
    description_0 = stations[0]["StationDesc"]
    description_1 = stations[1]["StationDesc"]
    description_2 = stations[2]["StationDesc"]

    assert description_0 < description_1 < description_2
    assert len(stations) == 3
