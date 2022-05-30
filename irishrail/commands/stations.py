from rich.columns import Columns

from irishrail import irishrail


def _print_station(station):
    name = station["StationDesc"]
    code = station["StationCode"]
    return f"{name} ({code})"


def stations():
    data = irishrail.list_stations()

    stations = [_print_station(station) for station in data]
    columns = Columns(stations, equal=True, expand=True)
    return columns
