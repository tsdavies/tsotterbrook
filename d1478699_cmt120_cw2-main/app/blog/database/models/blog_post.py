from datetime import datetime

from app.extensions import db


class BlogPost(db.Model):
    """
    Represents a blog post in the database.
    - Stores metadata, content, and related information for a blog post.
    - Includes a relationship to comments associated with the post.
    """

    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for the blog post
    title = db.Column(
        db.String(100), nullable=False
    )  # Title of the blog post (max 100 characters)
    content = db.Column(db.Text, nullable=False)  # Main content of the blog post
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow
    )  # Creation timestamp (default: current time)
    priority = db.Column(
        db.Integer, default=0
    )  # Optional priority level for ordering or categorisation
    author = db.Column(
        db.String(50), nullable=False
    )  # Author's name (max 50 characters)
    summary = db.Column(
        db.String(255), nullable=True
    )  # Short summary or description of the post
    repository_url = db.Column(
        db.String(255), nullable=True
    )  # URL to a related code repository (optional)
    live_demo_url = db.Column(
        db.String(255), nullable=True
    )  # URL to a live demo related to the post (optional)

    # Relationship to comments associated with this blog post
    comments = db.relationship(
        "Comment",  # Name of the related model
        backref="post",  # Back-reference to the blog post from the comment
        cascade="all, delete-orphan",  # Automatically delete comments when the post is deleted
        lazy=True,  # Load comments lazily to improve performance
    )
