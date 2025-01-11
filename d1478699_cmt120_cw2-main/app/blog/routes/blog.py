from flask import render_template

from ..database.models import BlogPost


def blog():
    """
    Render the blog page with a list of all blog posts.
    - Fetches all blog posts from the database.
    - Orders posts by priority (descending) and timestamp (descending).
    - Passes the ordered list of posts to the template for rendering.

    Returns:
        Response: Rendered HTML template for the blog page.
    """
    # Query all blog posts, ordered by priority (highest first) and timestamp (most recent first)
    posts = BlogPost.query.order_by(
        BlogPost.priority.desc(),  # Sort by priority in descending order
        BlogPost.timestamp.desc(),  # Sort by timestamp in descending order (secondary sort)
    ).all()

    # Render the 'blogs.html' template with the list of posts
    return render_template("blogs.html", posts=posts)
