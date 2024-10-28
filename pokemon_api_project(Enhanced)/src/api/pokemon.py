from typing import Dict, Any, List
from .base import BaseAPIClient
from utils.formatters import format_pokemon_info


class PokemonClient(BaseAPIClient):  # Class Inheritance
    def __init__(self):
        super().__init__("https://pokeapi.co/api/v2")  # Call base class init method

    def get_pokemon(self, name: str) -> Dict[str, Any]:
        """Get information about a specific Pokemon"""
        data = self.get(f"pokemon/{name.lower()}")
        return format_pokemon_info(data)

    def get_pokemon_by_type(self, type_name: str) -> List[str]:
        """Get all Pokemon of a specific type"""
        data = self.get(f"type/{type_name.lower()}")
        if "error" in data:
            return []
        return [p["pokemon"]["name"] for p in data["pokemon"]]