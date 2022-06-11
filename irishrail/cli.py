import click
from rich import print

from irishrail import commands


@click.group()
def cli():
    ...


@cli.command(help="List all stations available")
def stations():
    stations = commands.stations()
    print(stations)


@cli.command(help="Train station updates")
@click.argument("station", required=True)
@click.option(
    "-f",
    "--follow",
    is_flag=True,
    default=False,
    help="Keep watching for updates every couple of seconds",
)
def live(station, follow):
    commands.live(station, follow)


if __name__ == "__main__":
    cli()
