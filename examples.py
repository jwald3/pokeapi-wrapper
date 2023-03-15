from pokeapi_wrapper import PokeApiWrapper

# Create a new PokeAPI wrapper object
poke_api = PokeApiWrapper()

# Query PokeAPI for information about Pikachu
pikachu_info = poke_api.get_pokemon_info('pikachu')

# Print Pikachu's name, types, and stats
print(f"Name: {pikachu_info['name']}")
print(f"Types: {', '.join(pikachu_info['types'])}")
print(f"Stats: {pikachu_info['stats']}")

# Query PokeAPI for information about the "overgrow" ability
overgrow_info = poke_api.get_ability_info('overgrow')

# Print the name of the ability and the effect it has in battle
print(f"Name: {overgrow_info['name']}") 
print(f"Effect: {overgrow_info['effect']}")