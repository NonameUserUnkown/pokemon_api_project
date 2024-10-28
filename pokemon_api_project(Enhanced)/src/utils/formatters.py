from typing import Dict, Any

def format_pokemon_info(data: Dict[str, Any]) -> Dict[str, Any]:
    """Format Pokemon data into a clean structure"""
    if "error" in data:
        return data

    stats = {
        stat["stat"]["name"]: stat["base_stat"]
        for stat in data["stats"]
    }

    return {
        "name": data["name"],
        "height": data["height"],
        "weight": data["weight"],
        "abilities": [ability["ability"]["name"]
                     for ability in data["abilities"]],
        "types": [type_info["type"]["name"]
                  for type_info in data["types"]],
        "stats": stats
    }