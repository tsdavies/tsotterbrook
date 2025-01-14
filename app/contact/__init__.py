from flask import Blueprint

from .routes import contact

# Create a blueprint for the contact feature
contact_bp = Blueprint("contact", __name__, template_folder="templates")

# Map the contact function to the root URL, allowing GET and POST methods
contact_bp.add_url_rule("/", view_func=contact, methods=["GET", "POST"])
