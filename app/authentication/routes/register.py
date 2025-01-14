from flask import flash, redirect, url_for, render_template
from bleach import clean  # Importing bleach for input sanitisation

from app.authentication.database import register_user
from app.authentication.forms.register_form import RegisterForm


def register():
    """
    Handle user registration process with input sanitisation.
    - Validates the form data.
    - Uses `bleach` to clean the inputs for additional security.
    - Attempts to register the user and provides feedback.
    """
    form = RegisterForm()
    if form.validate_on_submit():
        # Sanitise user inputs before processing
        username = clean(form.username.data)
        email = clean(form.email.data)
        password = clean(form.password.data)

        # Attempt to register the user
        success, message = register_user(username, email, password)

        # Flash a success or failure message
        flash(message, "success" if success else "danger")

        if success:
            # Redirect to the login page upon successful registration
            return redirect(url_for("authentication.login"))

    # Render the registration page with the form
    return render_template("register.html", form=form, title="Register")
