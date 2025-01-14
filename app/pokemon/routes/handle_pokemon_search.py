from flask import request
from .fetch_pokemon_by_name import fetch_pokemon_by_name
from .utils.update_session_pokemon import update_session_pokemon


def handle_pokemon_search():
    """
    Handles the logic for Pokémon search requests.
    - Extracts the Pokémon name from the POST request form.
    - Fetches data for the specified Pokémon using the PokeAPI.
    - Updates the session's recent searches if the Pokémon data is valid.

    Returns:
        tuple:
            - dict: Pokémon data if successfully fetched, or an error message in the data.
            - str: Error message if the name is invalid or data fetching fails, otherwise None.
    """
    # Extract and clean the Pokémon name from the form input
    name = request.form.get("name", "").strip()
    if not name:
        # Return error if no name is provided
        return None, "No Pokémon name provided."

    # Fetch Pokémon data from the API
    data = fetch_pokemon_by_name(name)

    # Update recent searches in the session if data is valid
    if "error" not in data:
        update_session_pokemon(data)

    # Return the fetched data and an error message if applicable
    return data, None if "error" not in data else data["error"]
