from flask import render_template, request, session, url_for, redirect

from .fetch_pokemon_by_name import fetch_pokemon_by_name
from .handle_pokemon_search import handle_pokemon_search
from .utils.initialise_session_pokemon import initialise_session_pokemon


def search(name=None):
    """
    Handles Pokémon search functionality.
    - Initialises the session with prepopulated Pokémon data if necessary.
    - Processes POST requests for Pokémon search and redirects to the GET version.
    - Fetches Pokémon data for GET requests with a name parameter.
    - Renders the Pokémon search page with results or errors.

    Args:
        name (str, optional): Pokémon name provided via the URL or search form.

    Returns:
        Response: Rendered HTML template for the Pokémon search page.
    """
    data = None
    error = None

    # Ensure the session is initialised with default recent searches
    initialise_session_pokemon()

    if request.method == "POST":
        # Handle Pokémon search logic for POST requests
        data, error = handle_pokemon_search()
        if not error and data:
            name = data.get("name", "")
            # Redirect to the GET version with the name in the query parameter
            return redirect(url_for("pokemon.search", name=name))

    # Handle Pokémon search logic for GET requests
    name = name or request.args.get("name", "").strip()
    if name:
        # Fetch Pokémon data for the provided name
        data = fetch_pokemon_by_name(name)

    # Render the Pokémon search page with the search results, errors, and recent searches
    return render_template(
        "pokemon.html",
        data=data,  # Pokémon data if available
        error=error,  # Error message if any
        name=name,  # Current Pokémon name being searched
        title="Pokémon Search",  # Page title
        recent_searches=session[
            "recent_searches"
        ],  # List of recent searches from the session
    )
