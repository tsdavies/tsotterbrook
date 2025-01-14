from flask_login import login_user
from werkzeug.security import check_password_hash

from app.authentication.database.models import User


def authenticate_user(email, password):
    """
    Authenticate a user based on email and password.
    - Retrieves the user from the database using the provided email.
    - Verifies the password using a secure hash comparison.
    - Logs the user in if authentication is successful.

    Args:
        email (str): The user's email address.
        password (str): The user's plain text password.

    Returns:
        tuple: (bool, str)
            - A boolean indicating if the authentication was successful.
            - A message describing the result of the authentication.
    """
    # Query the database for a user with the given email
    user = User.query.filter_by(email=email).first()

    # If a user is found and the password hash matches the provided password
    if user and check_password_hash(user.password, password):
        login_user(user)  # Log the user in
        return True, "Login successful!"  # Return success message

    # Return failure message if authentication fails
    return False, "Invalid email or password"
