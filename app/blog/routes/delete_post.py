from flask import render_template, flash, redirect, url_for
from flask_login import login_required

from app import db
from app.authentication.database import is_admin
from ..database.models import BlogPost


@login_required
def delete_post(post_id):
    """
    Delete a blog post.
    - Ensures the user is logged in and is an admin.
    - Retrieves the post by its ID or returns a 404 error if not found.
    - Deletes the post from the database.
    - Displays a success message and redirects to the blog page.

    Args:
        post_id (int): The ID of the post to delete.

    Returns:
        Response: Redirects to the blog page or renders a forbidden page if the user lacks permissions.
    """
    # Check if the current user has admin privileges
    if not is_admin():
        # Render a forbidden page if the user is not an admin
        return render_template("forbidden.html")

    # Retrieve the blog post by ID or return a 404 error if not found
    post = BlogPost.query.get_or_404(post_id)

    # Delete the blog post from the database
    db.session.delete(post)
    db.session.commit()

    # Display a success message
    flash("Post deleted successfully!", "success")

    # Redirect to the blog page
    return redirect(url_for("blog.blog"))
