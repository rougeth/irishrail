import click
from rich import print

from irishrail import commands


@click.group()
def cli():
    ...


@cli.command()
def stations():
    stations = commands.stations()
    print(stations)


@cli.command()
@click.option("-s", "--station", required=True)
@click.option("-f", "--follow", is_flag=True, default=False)
def live(station, follow):
    commands.live(station, follow)


if __name__ == "__main__":
    cli()
