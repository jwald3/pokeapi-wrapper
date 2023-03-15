import requests
from typing import Dict, List

class PokeApiWrapper:
    def __init__(self):
        self.base_url = 'https://pokeapi.co/api/v2'

    def _request_api_data(self, endpoint_url):
        """Makes a request to the API endpoint and returns the JSON response"""
        response =  requests.get(endpoint_url)
        response.raise_for_status()
        return response.json()

    def _create_pokemon_info_dict(self, response_data: Dict) -> Dict[str, any]:
        """Creates and returns a dictionary-formatted pokemon using the response data passed in"""
        return {
            'name': response_data['name'],
            'types': [type_data['type']['name'] for type_data in response_data['types']],
            'abilities': [ability_data['ability']['name'] for ability_data in response_data['abilities']],
            'stats': {stat_data['stat']['name']: stat_data['base_stat'] for stat_data in response_data['stats']}
        }
    
    def get_pokemon_info(self, pokemon_name: str) -> Dict[str, any]:
        """Return a dictionary-formatted Pokemon for the provided query"""
        endpoint_url = f"{self.base_url}/pokemon/{pokemon_name}/"
        response_data = self._request_api_data(endpoint_url)
        return self._create_pokemon_info_dict(response_data)

    def _create_ability_info_dict(self, response_data: Dict) -> Dict[str, any]:
        """Creates and returns a dictionary-formatted ability using the response data passed in"""
        return {
            'name': response_data['name'],
            'generation': response_data['generation']['name'],
            'pokemon': [
            {'name': pokemon_data['pokemon']['name'], 'is_hidden': pokemon_data['is_hidden']} 
            for pokemon_data in response_data['pokemon']
            ],
            'effect': [entry for entry in response_data['effect_entries'] if entry['language']['name'] == 'en'][0]['effect'].replace('\n', ' ')
        }

    def get_ability_info(self, ability_name: str) -> Dict[str, any]:
        """Return a dictionary-formatted ability for the provided query"""
        endpoint_url = f"{self.base_url}/ability/{ability_name}/"
        response_data = self._request_api_data(endpoint_url)
        return self._create_ability_info_dict(response_data)