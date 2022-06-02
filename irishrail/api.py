import httpx
import xmltodict


BASE_URL = "http://api.irishrail.ie/realtime/realtime.asmx/"


def _request(url):
    response = httpx.get(url)
    return xmltodict.parse(response.content)


def next_trains(station):
    url = f"{BASE_URL}/getStationDataByNameXML?StationDesc={station}"
    response = _request(url)
    try:
        trains = response["ArrayOfObjStationData"]["objStationData"]
    except KeyError:
        # IrishRail API returns 202 for stations that doesn't exists or has no data.
        return []

    return sorted(trains, key=lambda train: int(train["Duein"]))


def list_stations():
    response = _request(f"{BASE_URL}/getAllStationsXML")
    stations = response["ArrayOfObjStation"]["objStation"]
    return sorted(stations, key=lambda station: station["StationDesc"])
