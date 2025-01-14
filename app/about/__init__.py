from flask import Blueprint

from .routes.about import about

# Create a blueprint for the 'About' feature
about_bp = Blueprint("about", __name__, template_folder="templates")

# Map the 'about' function to the root URL and '/about' path
about_bp.add_url_rule("/", view_func=about, methods=["GET", "POST"])  # Root URL
about_bp.add_url_rule(
    "/about", view_func=about, methods=["GET", "POST"]
)  # '/about' URL

# Expose the blueprint for import
__all__ = ["about_bp"]
