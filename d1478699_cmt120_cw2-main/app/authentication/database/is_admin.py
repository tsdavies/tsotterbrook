from flask_login import current_user


def is_admin():
    """
    Check if the current user has administrator privileges.
    - Verifies if the user is authenticated.
    - Checks if the user's email matches the designated admin email.

    Returns:
        bool: True if the user is authenticated and their email is the admin email, otherwise False.
    """
    # Ensure the user is authenticated and their email matches the admin email
    return current_user.is_authenticated and current_user.email == "tammy@tsdavies.com"
