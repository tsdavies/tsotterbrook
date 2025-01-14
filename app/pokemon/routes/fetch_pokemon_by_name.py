import requests

from .utils.get_pokemon_color import get_pokemon_color


def fetch_pokemon_by_name(name):
    """
    Fetch and process Pokémon data from the PokeAPI.
    - Sends a GET request to the API using the Pokémon's name.
    - Processes the API response to extract and augment Pokémon attributes.
    - Handles API errors gracefully by returning an error message.

    Args:
        name (str): The name of the Pokémon to fetch.

    Returns:
        dict: A dictionary containing the Pokémon's data, including its types and colour,
              or an error message if the request fails.
    """
    try:
        # Make a request to the PokeAPI for the given Pokémon name (case-insensitive)
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name.lower()}")
        response.raise_for_status()  # Raise an HTTPError for unsuccessful requests
        data = response.json()

        # Extract Pokémon types and compute its associated colour
        data["types"] = [t["type"]["name"] for t in data["types"]]
        data["color"] = get_pokemon_color(data["types"])

        return data  # Return the processed Pokémon data

    except requests.exceptions.RequestException as e:
        # Handle and return any errors encountered during the API request
        return {"error": f"Error fetching Pokémon data: {str(e)}"}
