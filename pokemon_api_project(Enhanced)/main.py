from src.api.pokemon import PokemonClient


def main():
    client = PokemonClient()

    # Get Pokemon info
    pokemon_name = input("Enter Pokemon name: ")
    pokemon_data = client.get_pokemon(pokemon_name)

    if "error" in pokemon_data:
        print(f"Error: {pokemon_data['error']}")
        return

    print("\nPokemon Information:")
    for key, value in pokemon_data.items():
        if key == "stats":
            print("\nStats:")
            for stat_name, stat_value in value.items():
                print(f"  {stat_name}: {stat_value}")
        else:
            print(f"{key.title()}: {value}")


if __name__ == "__main__":
    main()