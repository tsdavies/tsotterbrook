from flask import redirect, url_for, flash
from flask_login import logout_user, login_required


@login_required
def logout():
    """
    Log out the currently logged-in user.
    - Ensures the user is authenticated before logging out.
    - Logs out the user and provides a confirmation message.
    """
    logout_user()
    flash("You have been logged out.", "success")
    return redirect(url_for("authentication.login"))
