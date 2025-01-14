from datetime import datetime

from flask import Flask
from flask_login import current_user
from markdown import markdown

from app.authentication.database import is_admin
from app.extensions import mail, login_manager, migrate, db
from app.register_routes import register_routes


def create_app():
    """
    Application factory function.
    - Configures the Flask application.
    - Initialises extensions.
    - Registers routes, custom template filters, and context processors.
    - Sets up database tables and Flask-Login.

    Returns:
        Flask: The configured Flask application instance.
    """
    app = Flask(__name__)
    app.config.from_object("config.Config")  # Load configuration from the Config class

    # Initialise extensions
    db.init_app(app)  # Initialise the SQLAlchemy extension
    mail.init_app(app)  # Initialise the Flask-Mail extension
    login_manager.init_app(app)  # Initialise Flask-Login
    migrate.init_app(app, db)  # Initialise Flask-Migrate for database migrations

    # Register a custom template filter for formatting datetime objects
    @app.template_filter("format_datetime")
    def format_datetime(value, format="%d %b %Y, %H:%M"):
        """Format datetime objects for display."""
        return value.strftime(format) if isinstance(value, datetime) else value

    # Register a custom template filter for rendering Markdown content as HTML
    @app.template_filter("markdown")
    def markdown_filter(content):
        """Convert Markdown content to HTML."""
        return markdown(content)

    # Register all application routes
    register_routes(app)

    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()

    # Configure Flask-Login user loader to load a user by ID
    @login_manager.user_loader
    def load_user(user_id):
        from app.authentication.database.models import User

        return User.query.get(int(user_id))  # Fetch the user from the database by ID

    # Inject the current user into templates for use in Jinja2
    @app.context_processor
    def inject_user():
        return dict(current_user=current_user)

    # Inject admin utility into templates for role-based logic
    @app.context_processor
    def inject_user_utils():
        return dict(is_admin=is_admin)

    return app  # Return the configured application instance
