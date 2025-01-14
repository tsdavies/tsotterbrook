def get_pokemon_color(types):
    """Return the color for the primary Pokémon type."""
    type_colors = {
        "fire": "#EE8130",
        "water": "#6390F0",
        "grass": "#7AC74C",
        "electric": "#F7D02C",
        "psychic": "#F95587",
        "ice": "#96D9D6",
        "dragon": "#6F35FC",
        "dark": "#705746",
        "fairy": "#D685AD",
        "steel": "#B7B7CE",
        "poison": "#A33EA1",
        "flying": "#A98FF3",
        "bug": "#A6B91A",
        "rock": "#B6A136",
        "ground": "#E2BF65",
        "ghost": "#735797",
        "fighting": "#C22E28",
        "normal": "#A8A77A",
    }
    return type_colors.get(types[0], "#A8A77A")  # Default to normal type
