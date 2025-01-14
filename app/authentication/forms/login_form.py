from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(FlaskForm):
    """
    Form for user login.
    - This form handles the input fields and validations for user login.
    """

    email = StringField(
        "Email",
        validators=[
            DataRequired(),  # Ensures the field is not left empty
            Email(),  # Validates the input as a properly formatted email address
        ],
    )
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),  # Ensures the field is not left empty
            Length(min=6),  # Enforces a minimum password length of 6 characters
        ],
    )
    submit = SubmitField("Login")  # Button to submit the form
