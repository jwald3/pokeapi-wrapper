# PokeAPI Wrapper

This is a simple Python wrapper for the [PokeAPI](https://pokeapi.co/), which allows users to easily fetch data about Pokémon from the API.

## Features

* Get Pokémon information by name
* Retrieve basic Pokémon data, including:
  * Name
  * Types
  * Abilities
  * Base stats
  
## Requirements

* Python 3.7+
* `requests` library

## Installation

1. Clone the repository

```
git clone https://github.com/your_username/pokeapi-wrapper.git
```

2. Install the `requests` library if you don't already have it installed

```
pip install requests
```

## Usage

Here's an example of how to use the `PokeApiWrapper`:

```python
from pokeapi_wrapper import PokeApiWrapper

poke_api_wrapper = PokeApiWrapper()

pokemon_info = poke_api_wrapper.get_pokemon_info("pikachu")
print(pokemon_info)
```

This will output the following Pokémon information:

```python
{
  'name': 'pikachu',
  'types': ['electric'],
  'abilities': ['static', 'lightning-rod'],
  'stats': {
    'hp': 35,
    'attack': 40,
    'defense': 50,
    'special-attack': 50,
    'special-defense': 50,
    'speed': 90
  }
}
```

## Contributing

I welcome contributions! If you'd like to contribute, please fork the repository and submit a pull request with your changes. If you're unsure about making changes, feel free to open an issue to discuss your ideas.
