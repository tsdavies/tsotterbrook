from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, URLField
from wtforms.fields.numeric import IntegerField
from wtforms.validators import DataRequired, NumberRange, Optional, URL


class BlogPostForm(FlaskForm):
    """
    Form for creating or editing a blog post.
    - Captures essential details such as title, summary, content, and optional URLs.
    - Includes validation rules to ensure the data is accurate and complete.
    """

    title = StringField(
        "Title", validators=[DataRequired()]  # Ensures the title is not left empty
    )
    summary = TextAreaField(
        "Summary",
        validators=[
            DataRequired(
                message="Please provide a summary for the post."
            )  # Requires a non-empty summary
        ],
    )
    content = TextAreaField(
        "Content",
        validators=[
            DataRequired(
                message="Content cannot be empty."
            )  # Requires the content to be filled
        ],
    )
    repository_url = URLField(
        "Repository URL",
        validators=[
            Optional(),  # This field is optional
            URL(
                message="Enter a valid URL"
            ),  # Validates that the input is a properly formatted URL
        ],
    )
    live_demo_url = URLField(
        "Live Demo URL",
        validators=[
            Optional(),  # This field is optional
            URL(
                message="Enter a valid URL"
            ),  # Validates that the input is a properly formatted URL
        ],
    )
    priority = IntegerField(
        "Priority",
        validators=[
            DataRequired(
                message="Please specify a priority."
            ),  # Ensures priority is provided
            NumberRange(
                min=0, message="Priority must be 0 or higher."
            ),  # Validates priority is non-negative
        ],
    )
    submit = SubmitField("Submit")  # Button to submit the form
