from flask import Blueprint

from .routes.hello import hello

# Create a blueprint for the 'hello' feature
hello_bp = Blueprint("hello", __name__, template_folder="templates")

# Map the 'hello' function to the root URL and '/hello' path
hello_bp.add_url_rule("/", view_func=hello, methods=["GET", "POST"])  # Root URL
hello_bp.add_url_rule(
    "/hello", view_func=hello, methods=["GET", "POST"]
)  # '/hello' URL

# Expose the blueprint for import
__all__ = ["hello_bp"]