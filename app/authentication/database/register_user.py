from werkzeug.security import generate_password_hash

from app.extensions import db
from app.authentication.database.models import User


def register_user(username, email, password):
    """
    Register a new user in the system.
    - Checks if the email is already registered.
    - Hashes the user's password for secure storage.
    - Adds the new user to the database and commits the changes.

    Args:
        username (str): The username of the new user.
        email (str): The email address of the new user.
        password (str): The plain text password of the new user.

    Returns:
        tuple: (bool, str)
            - A boolean indicating if the registration was successful.
            - A message describing the result of the registration.
    """
    # Check if the email is already registered in the database
    if User.query.filter_by(email=email).first():
        return False, "Email already registered"

    # Hash the password securely using PBKDF2 with SHA-256
    hashed_password = generate_password_hash(password, method="pbkdf2:sha256")

    # Create a new User object with the provided details
    new_user = User(username=username, email=email, password=hashed_password)

    # Add the new user to the database session and commit the changes
    db.session.add(new_user)
    db.session.commit()

    # Return success message
    return True, "Registration successful! You can now log in."
