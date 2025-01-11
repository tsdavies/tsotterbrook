import json
import os


def load_initial_pokemon():
    """
    Load prepopulated Pokémon data from a JSON cache file.
    - Checks if the cache file exists in the current directory.
    - If found, reads and returns the data as a Python list.
    - If the file does not exist, returns an empty list.

    Returns:
        list: A list of Pokémon data loaded from the cache file, or an empty list if the file is missing.
    """
    # Path to the JSON cache file containing Pokémon data
    cache_file = os.path.join(os.path.dirname(__file__), "initial_pokemon_data.json")

    # Check if the cache file exists
    if os.path.exists(cache_file):
        # Open and read the cache file, returning the parsed JSON data
        with open(cache_file, "r") as file:
            return json.load(file)

    # Return an empty list if the cache file does not exist
    return []
