from flask import session

from ..data.load_initial_pokemon_data import load_initial_pokemon


def initialise_session_pokemon():
    """
    Initialise the session with prepopulated Pokémon data.
    - Checks if the 'recent_searches' key exists in the session and is not empty.
    - If missing or empty, populates it with data loaded from the cache.
    - Marks the session as modified to ensure changes are saved.

    This function ensures that the session starts with a default list of Pokémon.
    """
    # Check if 'recent_searches' is not in the session or is empty
    if "recent_searches" not in session or not session["recent_searches"]:
        # Load prepopulated Pokémon data into the session
        session["recent_searches"] = load_initial_pokemon()

        # Mark the session as modified to save the changes
        session.modified = True
