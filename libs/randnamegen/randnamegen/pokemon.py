"""Random names of pokemons."""
import random


def suggest() -> str:
    """Suggest a beginner pokemon randomly."""
    foo = ["Charmander", "Squirtle", "Bulbasaur"]
    return random.choice(foo)
