from bleach import clean  # Importing bleach for input sanitisation
from flask import flash, redirect, url_for, render_template

from app.authentication.database import authenticate_user
from app.authentication.forms.login_form import LoginForm


def login():
    """
    Handle user login process with input sanitisation.
    - Validates the login form.
    - Uses `bleach` to clean user inputs for security.
    - Attempts to authenticate the user and provides feedback.
    """
    form = LoginForm()
    if form.validate_on_submit():
        # Sanitise user inputs before processing
        email = clean(form.email.data)
        password = clean(form.password.data)

        # Attempt to authenticate the user
        success, message = authenticate_user(email, password)

        # Flash a success or failure message
        flash(message, "success" if success else "danger")

        if success:
            # Redirect to the 'About' page upon successful login
            return redirect(url_for("about.about"))

    # Render the login page with the form
    return render_template("login.html", form=form, title="Login")
