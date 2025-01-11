from flask import flash, redirect, request, url_for
from flask_login import login_required, current_user

from app import db
from app.authentication.database import is_admin
from ..database.models import Comment


@login_required
def delete_comment(comment_id):
    """
    Delete a comment from the blog.
    - Ensures the user is logged in.
    - Checks if the current user is the comment author or an admin.
    - Deletes the comment if the user has the necessary permissions.
    - Redirects to the referring page or the blog page.

    Args:
        comment_id (int): The ID of the comment to delete.

    Returns:
        Response: Redirects to the previous page or the blog page.
    """
    # Retrieve the comment by ID or return a 404 error if not found
    comment = Comment.query.get_or_404(comment_id)

    # Check if the current user is the comment's author or an admin
    if comment.author != current_user.username and not is_admin():
        # Display an error message if the user lacks permission
        flash("You do not have permission to delete this comment.", "danger")
        return redirect(request.referrer or url_for("blog.blog"))

    # Delete the comment from the database
    db.session.delete(comment)
    db.session.commit()

    # Display a success message
    flash("Comment deleted successfully!", "success")

    # Redirect to the referring page or the blog page
    return redirect(request.referrer or url_for("blog.blog"))
