from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# Initialise Flask extensions

# Flask-Mail: Handles email functionality
mail = Mail()

# Flask-Login: Manages user session and authentication
login_manager = LoginManager()

# Flask-Migrate: Manages database migrations
migrate = Migrate()

# SQLAlchemy: Handles database interactions
db = SQLAlchemy()
