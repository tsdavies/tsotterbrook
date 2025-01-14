import bleach
import markdown
from flask import render_template, flash, redirect, url_for
from flask_login import login_required

from app import db
from app.authentication.database import is_admin
from app.blog.forms.blog_post_form import BlogPostForm
from ..database.models import BlogPost


@login_required
def edit_post(post_id):
    """
    Edit an existing blog post (admin only).
    - Retrieves the post by ID or shows a forbidden page if the user is not an admin.
    - Sanitises user input to ensure security.
    - Updates the post's title, content, summary, repository URL, live demo URL, and priority.
    - Saves the updated post to the database and redirects to the post detail page.
    """
    if not is_admin():
        # Render a forbidden page if the user lacks admin privileges
        return render_template("forbidden.html")

    # Fetch the blog post by ID or return a 404 if not found
    post = BlogPost.query.get_or_404(post_id)
    form = BlogPostForm(obj=post)  # Populate the form with the existing post data

    if form.validate_on_submit():
        # Sanitise the post's title
        post.title = bleach.clean(form.title.data)

        # Sanitise and process the markdown content
        raw_markdown = bleach.clean(
            form.content.data, tags=[], attributes={}, strip=True
        )
        rendered_html = markdown.markdown(
            raw_markdown, extensions=["fenced_code", "codehilite"]
        )
        post.content = bleach.clean(
            rendered_html,
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

        # Sanitise other fields
        post.summary = bleach.clean(form.summary.data)
        post.repository_url = bleach.clean(form.repository_url.data)
        post.live_demo_url = bleach.clean(form.live_demo_url.data)
        post.priority = form.priority.data  # Priority is assumed numeric and safe

        # Save changes to the database
        db.session.commit()
        flash("Post updated successfully!", "success")

        # Redirect to the post detail page
        return redirect(url_for("blog.post_detail", post_id=post.id))

    # Render the blog post edit page
    return render_template(
        "blog_post.html",
        form=form,
        post=post,
        edit=True,
        preview_endpoint=url_for("blog.markdown_preview"),
    )
