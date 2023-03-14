import requests
from typing import Dict, List

class PokeApiWrapper:
    def __init__(self):
        self.base_url = 'https://pokeapi.co/api/v2'

    def get_pokemon_data_from_api(self, endpoint_url: str) -> Dict:
        response = requests.get(endpoint_url)
        if response.status_code != 200:
            raise ValueError(f"Failed to get data from API endpoint: {endpoint_url}. Response code: {response.status_code}")
        return response.json()
    
    def get_pokemon_info(self, pokemon_name: str) -> Dict[str, any]:
        endpoint_url = f"{self.base_url}/pokemon/{pokemon_name}/"
        response_data = self.get_pokemon_data_from_api(endpoint_url)
        info_dict = {
            'name': response_data['name'],
            'types': [type_data['type']['name'] for type_data in response_data['types']],
            'abilities': [ability_data['ability']['name'] for ability_data in response_data['abilities']],
            'stats': {stat_data['stat']['name']: stat_data['base_stat'] for stat_data in response_data['stats']}
        }
        return info_dict