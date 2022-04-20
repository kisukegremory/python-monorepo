from pydoc import cli
import httpx
from src import api
import click


@click.command()
@click.option('--id', '-i', '_id', required=True, help='Pokemon ID to find')
@click.option('--full', is_flag=True, help='All pokemon information')
def cli(_id: str, full: bool):
    with httpx.Client() as client:
        request = api.get_pokemon_by_id(_id)
        response = client.send(request)
        pokemon = api.Pokemon(**response.json())
        if full:
            print(pokemon)
        else:
            print(pokemon.name)


if __name__ == '__main__':
    cli()
