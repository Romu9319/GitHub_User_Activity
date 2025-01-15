import click
import datetime
import requests

@click.group()
def cli():
    pass

@click.command()
@click.argument('user', required=True)

