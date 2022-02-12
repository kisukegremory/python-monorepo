from fastapi import FastAPI
from randnamegen import pokemon

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/pokemon")
def read_pokemon():
    return {"pokemon": pokemon.suggest()}