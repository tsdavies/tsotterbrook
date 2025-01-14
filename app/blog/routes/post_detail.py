import bleach
import markdown
from flask import flash, redirect, url_for, render_template
from flask_login import current_user
from markupsafe import Markup

from app import db
from app.blog.database.models import BlogPost, Comment
from app.blog.forms.comment_form import CommentForm


def post_detail(post_id):
    """
    Display the details of a blog post, including its comments.
    - Handles the submission of new comments.
    - Sanitises user input to ensure security.
    - Renders the blog post content and associated comments safely.

    Args:
        post_id (int): The ID of the blog post.

    Returns:
        Response: Rendered HTML template displaying the post and its comments.
    """
    # Retrieve the blog post by ID or return a 404 if not found
    post = BlogPost.query.get_or_404(post_id)
    form = CommentForm()

    if form.validate_on_submit():
        try:
            # Sanitise the comment content submitted by the user
            sanitized_content = bleach.clean(form.content.data)

            # Create and save the new comment
            comment = Comment(
                content=sanitized_content,
                author=current_user.username,
                post_id=post.id,
            )
            db.session.add(comment)
            db.session.commit()

            # Flash success message and reload the page
            flash("Comment added!", "success")
            return redirect(url_for("blog.post_detail", post_id=post_id))
        except Exception as e:
            # Roll back the transaction in case of an error
            db.session.rollback()
            flash("An error occurred while adding your comment.", "danger")

    # Retrieve all comments for the blog post, ordered by timestamp (most recent first)
    comments = (
        Comment.query.filter_by(post_id=post.id)
        .order_by(Comment.timestamp.desc())
        .all()
    )

    # Render and sanitise the blog post content
    raw_content = markdown.markdown(
        post.content, extensions=["fenced_code", "codehilite"]
    )
    safe_content = bleach.clean(
        raw_content,
        tags=bleach.sanitizer.ALLOWED_TAGS,  # Allow only safe HTML tags
        attributes=bleach.sanitizer.ALLOWED_ATTRIBUTES,  # Allow only safe attributes
    )

    # Mark the safe content as safe for rendering in templates
    rendered_content = Markup(safe_content)

    # Render the blog post detail template
    return render_template(
        "blog_post_detail.html",
        post=post,  # Pass the blog post to the template
        content=rendered_content,  # Sanitised blog post content
        form=form,  # Comment form
        comments=comments,  # List of comments
    )
