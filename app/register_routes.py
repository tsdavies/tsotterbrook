from app.about import about_bp
from app.authentication import auth_bp
from app.blog import blog_bp
from app.contact import contact_bp
from app.pokemon import pokemon_bp


def register_routes(app):
    """
    Register all application blueprints with their respective URL prefixes.
    - Organises the application's routes for modularity and clarity.

    Args:
        app (Flask): The Flask application instance to register routes on.
    """
    app.register_blueprint(
        auth_bp, url_prefix="/authentication"
    )  # Authentication-related routes
    app.register_blueprint(pokemon_bp, url_prefix="/pokemon")  # Pokémon-related routes
    app.register_blueprint(blog_bp, url_prefix="/blog")  # Blog-related routes
    app.register_blueprint(about_bp, url_prefix="/")  # About page routes (default root)
    app.register_blueprint(contact_bp, url_prefix="/contact")  # Contact page routes
