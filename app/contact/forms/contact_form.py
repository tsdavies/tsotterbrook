from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class ContactForm(FlaskForm):
    """
    Form for handling contact submissions.
    - Captures the user's name, email, and message.
    - Includes validation rules to ensure valid input.
    """

    name = StringField(
        "Name",
        validators=[
            DataRequired(),  # Ensures the name field is not empty
            Length(min=2, max=50),  # Restricts the name to between 2 and 50 characters
        ],
    )
    email = StringField(
        "Email",
        validators=[
            DataRequired(),  # Ensures the email field is not empty
            Email(),  # Validates the input as a properly formatted email address
        ],
    )
    message = TextAreaField(
        "Message",
        validators=[
            DataRequired(),  # Ensures the message field is not empty
            Length(
                min=10, max=1000
            ),  # Restricts the message to between 10 and 1000 characters
        ],
    )
    submit = SubmitField("Send")  # Button to submit the contact form
