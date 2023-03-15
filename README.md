# PokeAPI Wrapper

PokeAPI Wrapper is a Python wrapper for the [PokeAPI](https://pokeapi.co/), which provides a RESTful API interface to various information about the Pokemon universe. This wrapper makes it easy to query PokeAPI and get back structured data in a dictionary format.

## Installation
To install PokeAPI Wrapper, simply run:

```
pip install pokeapi-wrapper
```

## Usage

Here's an example of how to use PokeAPI Wrapper to get information about a Pokemon:


```python
from pokeapi_wrapper import PokeApiWrapper

# Create a new PokeAPI wrapper object
poke_api = PokeApiWrapper()

# Query PokeAPI for information about Pikachu
pikachu_info = poke_api.get_pokemon_info('pikachu')

# Print Pikachu's name, types, and stats
print(f"Name: {pikachu_info['name']}")
print(f"Types: {', '.join(pikachu_info['types'])}")
print(f"Stats: {pikachu_info['stats']}")
```

And here's an example of how to use PokeAPI Wrapper to get information about an ability:

```python
from pokeapi_wrapper import PokeApiWrapper

# Create a new PokeAPI wrapper object
poke_api = PokeApiWrapper()

# Query PokeAPI for information about the "overgrow" ability
overgrow_info = poke_api.get_ability_info('overgrow')

# Print the name of the ability and the effect it has in battle
print(f"Name: {overgrow_info['name']}")
print(f"Effect: {overgrow_info['effect']}")
```

## API Reference

PokeAPI Wrapper currently supports two API endpoints: `get_pokemon_info` and `get_ability_info`. Both functions return a dictionary with keys corresponding to different pieces of information about the Pokemon or ability.

### `get_pokemon_info(pokemon_name: str) -> Dict[str, any]`
Returns a dictionary with information about the specified Pokemon, including its name, types, abilities, and base stats.

### `get_ability_info(ability_name: str) -> Dict[str, any]`
Returns a dictionary with information about the specified ability, including its name, the generation in which it was introduced, the Pokemon that can have this ability, and the effect it has in battle.

## Contributing
If you find a bug or have a feature request, please open an issue on the GitHub repository or submit a pull request.
