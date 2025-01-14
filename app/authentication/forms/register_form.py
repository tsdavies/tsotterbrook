from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegisterForm(FlaskForm):
    """
    Form for user registration.
    - Captures the user's username, email, password, and password confirmation.
    - Includes validation to ensure the inputs are valid and secure.
    """

    username = StringField(
        "Username",
        validators=[
            DataRequired(),  # Ensures the username field is not left empty
            Length(
                min=3, max=25
            ),  # Limits the username length to between 3 and 25 characters
        ],
    )
    email = StringField(
        "Email",
        validators=[
            DataRequired(),  # Ensures the email field is not left empty
            Email(),  # Validates the input as a properly formatted email address
        ],
    )
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),  # Ensures the password field is not left empty
            Length(min=6),  # Enforces a minimum password length of 6 characters
        ],
    )
    confirm_password = PasswordField(
        "Confirm Password",
        validators=[
            DataRequired(),  # Ensures the confirm password field is not left empty
            EqualTo(
                "password", message="Passwords must match"
            ),  # Ensures the confirmation matches the password
        ],
    )
    submit = SubmitField("Register")  # Button to submit the registration form
