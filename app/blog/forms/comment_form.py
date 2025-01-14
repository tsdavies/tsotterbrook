from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired


class CommentForm(FlaskForm):
    """
    Form for submitting a comment on a blog post.
    - Captures the comment content.
    - Includes validation to ensure the comment is not empty.
    """

    content = TextAreaField(
        "Comment",
        validators=[DataRequired()],  # Ensures the comment content is not left empty
    )
    submit = SubmitField("Submit")  # Button to submit the comment form
