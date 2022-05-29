from rich.columns import Columns

from irishrail import IrishRail


def _print_station(station):
    name = station["StationDesc"]
    code = station["StationCode"]
    return f"{name} ({code})"


def stations():
    client = IrishRail()
    data = client.list_stations()

    stations = [_print_station(station) for station in data]
    columns = Columns(stations, equal=True, expand=True)
    return columns
