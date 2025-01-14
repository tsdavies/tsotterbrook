from flask import Blueprint

from .routes import search

pokemon_bp = Blueprint(
    "pokemon", __name__, template_folder="templates", static_folder="static"
)

# Add routes to the Blueprint
pokemon_bp.add_url_rule("/", view_func=search, methods=["GET", "POST"])
pokemon_bp.add_url_rule("/<string:name>", view_func=search, methods=["GET", "POST"])

__all__ = ["pokemon_bp"]
