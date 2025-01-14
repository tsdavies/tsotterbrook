from flask import Blueprint, render_template
from flask_login import login_required

from .routes import (
    blog,
    post_detail,
    markdown_preview,
    new_post,
    edit_post,
    delete_post,
    delete_comment,
)
from app.extensions import login_manager

# Define the Blueprint
blog_bp = Blueprint("blog", __name__, template_folder="templates")


# Handle unauthenticated access for login-required routes
@login_manager.unauthorized_handler
def unauthorized():
    # Render an unauthorised template if the user is not logged in
    return render_template("forbidden.html"), 403


# Register routes with the Blueprint
blog_bp.add_url_rule("/", view_func=blog, endpoint="blog")
blog_bp.add_url_rule(
    "/<int:post_id>",
    view_func=post_detail,
    methods=["GET", "POST"],
)
blog_bp.add_url_rule(
    "/markdown_preview",
    view_func=markdown_preview,
    methods=["POST"],
)
blog_bp.add_url_rule("/new", view_func=new_post, methods=["GET", "POST"])
blog_bp.add_url_rule(
    "/<int:post_id>/edit", view_func=edit_post, methods=["GET", "POST"]
)
blog_bp.add_url_rule(
    "/<int:post_id>/delete",
    view_func=delete_post,
    methods=["POST", "GET"],
)
blog_bp.add_url_rule(
    "/comment/<int:comment_id>/delete",
    view_func=delete_comment,
    methods=["POST", "GET"],
)

__all__ = ["blog_bp"]
