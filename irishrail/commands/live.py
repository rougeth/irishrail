import itertools
import time
from datetime import datetime

from rich.table import Table
from rich.text import Text
from rich.live import Live
from rich import box, print as rich_print

from irishrail import IrishRail


COLOR_GREEN = "light_green"
COLOR_ORANGE = "sandy_brown"
COLOR_GRAY = "gray70"


def format_duein(station):
    due = station.get("Duein", "")
    if not due:
        return ""

    return f"{due} min"


def split_per_direction(data):
    northbound = southbound = []
    for train in data:
        if train["Direction"] == "Southbound":
            southbound.append(train)
        else:
            northbound.append(train)

    return northbound, southbound


def render_title(station_name):
    NEWLINE = "\n"
    DIVIDER = " - "

    return Text.assemble(
        NEWLINE,
        (station_name.title(), "bold"),
        NEWLINE,
        ("Northbound", "light_green bold"),
        DIVIDER,
        ("Southbound", "sandy_brown bold"),
    )


def render_station(station, northbound, southbound, updated_at):
    title = render_title(station)

    table = Table(
        title=title,
        caption=f"Updated at: {updated_at}",
        box=box.DOUBLE_EDGE,
        title_style="white bold",
        caption_style=COLOR_GRAY,
        border_style=COLOR_GRAY,
        row_styles=["", "dim"],
    )

    table.add_column("Destination", style=COLOR_GREEN)
    table.add_column("Due", style=COLOR_GREEN)
    table.add_column("Destination", style=COLOR_ORANGE)
    table.add_column("Due", style=COLOR_ORANGE)

    for north, south in itertools.zip_longest(northbound, southbound, fillvalue={}):
        table.add_row(
            north.get("Destination", ""),
            format_duein(north),
            south.get("Destination", ""),
            format_duein(south),
        )

    return table


def render_station_not_found(station):
    client = IrishRail()
    stations = client.list_stations()
    stations = [station["StationDesc"].lower() for station in stations]

    if station.lower() not in stations:
        message = Text("Station not found. Use command `stations` to list all stations")
    else:
        message = Text.assemble(
            "No trains going to ",
            (station, "bold"),
            " station",
        )

    rich_print(message)


def render_live(station):
    client = IrishRail()
    data = client.next_trains(station)
    if not data:
        render_station_not_found(station)
        return None
    updated_at = datetime.now()

    northbound, southbound = split_per_direction(data)
    return render_station(station, northbound, southbound, updated_at)


def live(station, follow):
    REFRESH_PER_SECOND = 30

    with Live(render_live(station)) as live:
        while follow:
            time.sleep(REFRESH_PER_SECOND)
            table = render_live(station)
            if not table:
                break
            live.update(table)
