from flask import session


def update_session_pokemon(data):
    """
    Update the session's list of recent Pokémon searches.
    - Creates a dictionary with the Pokémon's name and sprite URL from the provided data.
    - Removes any existing entries in 'recent_searches' with the same name (case-insensitive).
    - Adds the new search to the end of the list.
    - Limits the list to the 5 most recent searches.
    - Marks the session as modified to save the changes.

    Args:
        data (dict): The Pokémon data, containing at least the 'name' and 'sprites' keys.
    """
    # Create a dictionary for the recent search with name and sprite
    recent_search = {
        "name": data["name"],
        "sprite": data["sprites"]["front_default"],
    }

    # Remove duplicate entries by filtering out searches with the same name (case-insensitive)
    session["recent_searches"] = [
        search
        for search in session["recent_searches"]
        if search["name"].lower() != recent_search["name"].lower()
    ]

    # Append the new search to the session's recent searches
    session["recent_searches"].append(recent_search)

    # Keep only the 5 most recent searches
    session["recent_searches"] = session["recent_searches"][-5:]

    # Mark the session as modified to save the changes
    session.modified = True
