from flask import Blueprint

from .routes import login, register, logout

auth_bp = Blueprint("authentication", __name__, template_folder="templates")

# Register routes
auth_bp.add_url_rule("/login", view_func=login, methods=["GET", "POST"])
auth_bp.add_url_rule("/register", view_func=register, methods=["GET", "POST"])
auth_bp.add_url_rule("/logout", view_func=logout, methods=["GET"])

# Expose the blueprint for app to register
__all__ = ["auth_bp"]
