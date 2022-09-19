#!/usr/bin/env python

import click
from dblib.querydb import querydb

# build a click group
@click.group()
def cli():
    """A simple CLI to query a SQL database"""


# build a click command
@cli.command()
@click.option(
    "--query",
    default="SELECT Country, 2022_Population FROM world_population_csv ORDER BY 2022_Population DESC LIMIT 3",
    help="SQL query to execute",
)
def cli_query(query):
    """Execute a SQL query"""
    querydb(query)


# run the CLI
if __name__ == "__main__":
    cli()
