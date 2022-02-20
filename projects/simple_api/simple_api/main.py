"""Main file of the simple api."""
from fastapi import FastAPI
from randnamegen import pokemon

app = FastAPI()


@app.get("/")
def read_root():
    """Return a simple hello world."""
    return {"Hello": "World"}


@app.get("/pokemon")
def read_pokemon():
    """Retuns a json of a random pokemon."""
    return {"pokemon": pokemon.suggest()}
