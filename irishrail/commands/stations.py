from rich.columns import Columns

from irishrail import api


def _print_station(station):
    name = station["StationDesc"]
    code = station["StationCode"]
    return f"{name} ({code})"


def stations():
    data = api.list_stations()

    stations = [_print_station(station) for station in data]
    columns = Columns(stations, equal=True, expand=True)
    return columns
