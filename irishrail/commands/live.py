import itertools
import time
from datetime import datetime

from rich.table import Table
from rich.text import Text
from rich.live import Live
from rich import box, print as rich_print

from irishrail import api


COLOR_GREEN = "light_green"
COLOR_ORANGE = "sandy_brown"
COLOR_GRAY = "gray70"
NEWLINE = "\n"


def format_duein(station):
    due = station.get("Duein", "")
    return f"{due} min" if due else ""


def split_per_direction(data):
    northbound = []
    southbound = []
    for train in data:
        if train["Direction"] == "Southbound":
            southbound.append(train)
        else:
            northbound.append(train)

    return northbound, southbound


def render_title(station_name):
    DIVIDER = " - "

    return Text.assemble(
        NEWLINE,
        (station_name.title(), "bold"),
        NEWLINE,
        ("Northbound", "light_green bold"),
        DIVIDER,
        ("Southbound", "sandy_brown bold"),
    )


def render_caption(updated_at, follow):
    updated_at_label = Text(f"Updated at: {updated_at}")
    if follow:
        updated_at_label.append(
            f"{NEWLINE} Press CTRL-C to exit {NEWLINE}", style=COLOR_GRAY
        )

    return updated_at_label


def render_station(station, northbound, southbound, updated_at, follow):
    title = render_title(station)

    table = Table(
        title=title,
        caption=render_caption(updated_at, follow),
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
    stations = api.list_stations()
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


def render_live(station, follow):
    data = api.next_trains(station)
    if not data:
        render_station_not_found(station)
        return None

    updated_at = datetime.now()

    northbound, southbound = split_per_direction(data)
    return render_station(station, northbound, southbound, updated_at, follow)


def live(station, follow):
    REFRESH_PER_SECOND = 30

    with Live(render_live(station, follow)) as live:
        while follow:
            time.sleep(REFRESH_PER_SECOND)
            table = render_live(station, follow)
            if not table:
                break
            live.update(table)
