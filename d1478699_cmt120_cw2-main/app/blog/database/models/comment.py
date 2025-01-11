from datetime import datetime

from app.extensions import db


class Comment(db.Model):
    """
    Represents a comment on a blog post in the database.
    - Stores content, metadata, and the relationship to the associated blog post.
    """

    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for the comment
    content = db.Column(db.Text, nullable=False)  # Content of the comment
    author = db.Column(
        db.String(50), nullable=False
    )  # Author's name (max 50 characters)
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow
    )  # Timestamp of when the comment was created
    post_id = db.Column(db.Integer, db.ForeignKey("blog_post.id"), nullable=False)
    # Foreign key linking the comment to the associated blog post
