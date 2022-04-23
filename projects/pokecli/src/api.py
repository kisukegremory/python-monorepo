import httpx
from pydantic import BaseModel

BASE_URL = 'https://pokeapi.co/api/v2/pokemon'


class Pokemon(BaseModel):
    id: int
    name: str
    height: int
    weight: int
    base_experience: int

    def __str__(self) -> str:
        return f'Pokemon - id: {self.id}, name: {self.name}, height: {self.height}, weight: {self.weight}, base_experience: {self.base_experience}'


def get_pokemon_by_id(_id: int) -> httpx.Request:
    return httpx.Request('GET', url=f'{BASE_URL}/{_id}')
