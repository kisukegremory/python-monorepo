import httpx

BASE_URL = "https://pokeapi.co/api/v2/pokemon"


def get_pokemon_by_id(_id: int) -> httpx.Request:
    return httpx.Request("GET", url=f"{BASE_URL}/{_id}")
