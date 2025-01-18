from flask import Blueprint

from .routes.books import books

# Create a blueprint for the 'books' feature
books_bp = Blueprint("books", __name__, template_folder="templates", static_folder="static")

# Map the 'books' function to the root URL and '/books' path
books_bp.add_url_rule("/", view_func=books, methods=["GET", "POST"])  # Root URL

# Expose the blueprint for import
__all__ = ["books_bp"]