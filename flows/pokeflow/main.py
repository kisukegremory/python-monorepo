from typing import List
from prefect import task, flow
import httpx
import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from pokemon.typing import Pokemon
from pokemon import db, api


@task
async def poke_extract() -> List[httpx.Response]:
    poke_requests = [api.get_pokemon_by_id(n) for n in range(1, 200)]
    return await api.fetch_requests(poke_requests)


@task
def poke_transform(poke_responses: List[httpx.Response]) -> List[db.Pokemons]:
    pokemons = [Pokemon(**response.json()) for response in poke_responses]
    return [db.Pokemons(**pokemon.dict()) for pokemon in pokemons]


@task
async def poke_load(pokemons: List[db.Pokemons]):
    uri = "sqlite+aiosqlite:///example.db"
    engine = create_async_engine(uri)
    metadata = db.Pokemons.metadata
    async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

    async with engine.begin() as conn:
        await conn.run_sync(metadata.drop_all)
        await conn.run_sync(metadata.create_all)

    async with async_session() as session:
        async with session.begin():
            session.add_all(pokemons)
        await session.commit()


@flow
async def pokeflow():
    poke_responses = await poke_extract()
    pokemons = poke_transform(poke_responses)
    await poke_load(pokemons)


if __name__ == "__main__":
    asyncio.run(pokeflow())
