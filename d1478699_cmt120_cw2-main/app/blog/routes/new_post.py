import bleach
import markdown
from flask import render_template, flash, redirect, url_for
from flask_login import login_required, current_user

from app import db
from app.authentication.database import is_admin
from app.blog.database.models import BlogPost
from app.blog.forms.blog_post_form import BlogPostForm


@login_required
def new_post():
    """
    Create a new blog post (admin only).
    - Validates and sanitises user input.
    - Converts markdown to HTML while ensuring security.
    - Saves the new post to the database and redirects to the blog page.

    Returns:
        Response: Rendered form for creating a post or redirect upon success.
    """
    if not is_admin():
        return render_template(
            "forbidden.html"
        )  # Render forbidden page for non-admin users

    form = BlogPostForm()
    if form.validate_on_submit():
        # Step 1: Sanitise raw markdown input to prevent malicious content
        sanitized_markdown = bleach.clean(
            form.content.data, tags=[], attributes={}, strip=True
        )

        # Step 2: Convert markdown to HTML and sanitise rendered HTML for safe display
        rendered_html = bleach.clean(
            markdown.markdown(
                sanitized_markdown, extensions=["fenced_code", "codehilite"]
            ),
            tags=[
                "p",
                "b",
                "i",
                "u",
                "em",
                "strong",
                "a",
                "ul",
                "ol",
                "li",
                "code",
                "pre",
                "blockquote",
                "h1",
                "h2",
                "h3",
                "h4",
                "h5",
                "h6",
                "img",
                "br",
                "hr",
            ],
            attributes={
                "a": ["href", "title"],
                "img": ["src", "alt", "title"],
                "code": ["class"],
            },
            strip=True,
        )

        # Step 3: Create a new blog post object with sanitised data
        post = BlogPost(
            title=bleach.clean(form.title.data),
            content=sanitized_markdown,  # Store the sanitised markdown
            author=current_user.username,
            summary=bleach.clean(form.summary.data),
            repository_url=bleach.clean(form.repository_url.data),
            live_demo_url=bleach.clean(form.live_demo_url.data),
            priority=form.priority.data,  # Priority assumed to be numeric and valid
        )

        # Save the new post to the database
        db.session.add(post)
        db.session.commit()

        # Flash a success message and redirect to the blog page
        flash("Post created!", "success")
        return redirect(url_for("blog.blog"))

    # Render the form for creating a new post
    return render_template(
        "blog_post.html",
        form=form,
        preview_endpoint=url_for("blog.markdown_preview"),
    )
