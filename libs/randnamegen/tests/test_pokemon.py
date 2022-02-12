from randnamegen import pokemon


def test_pokemon_in_pokelist():
    assert pokemon.suggest() in ["Charmander", "Squirtle", "Bulbasaur"]
