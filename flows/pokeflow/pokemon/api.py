import httpx
import asyncio

BASE_URL = "https://pokeapi.co/api/v2/pokemon"


def get_pokemon_by_id(_id: int) -> httpx.Request:
    return httpx.Request("GET", url=f"{BASE_URL}/{_id}")


async def fetch_requests(requests):
    async with httpx.AsyncClient() as client:
        poke_tasks = [client.send(request) for request in requests]
        return await asyncio.gather(*poke_tasks)
