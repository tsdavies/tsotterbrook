import bleach
import markdown
from flask import render_template, request, jsonify
from flask_login import login_required

from app.authentication.database import is_admin


@login_required
def markdown_preview():
    """
    Preview rendered and sanitised HTML from markdown input (admin only).
    - Checks admin privileges before processing.
    - Converts raw markdown into HTML using the markdown library.
    - Sanitises the HTML to allow only safe tags and attributes.
    - Returns the cleaned HTML as a JSON response.

    Returns:
        Response: JSON object containing the sanitised HTML or a forbidden page if not authorised.
    """
    # Verify that the current user is an admin
    if not is_admin():
        return render_template("forbidden.html")

    # Retrieve the raw markdown content from the JSON request
    raw_markdown = request.json.get("markdown", "")

    # Convert markdown to HTML using the markdown library
    html_content = markdown.markdown(
        raw_markdown, extensions=["fenced_code", "codehilite"]
    )

    # Define allowed HTML tags and attributes for sanitisation
    allowed_tags = [
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
    ]
    allowed_attributes = {
        "a": ["href", "title"],  # Allow links with href and title
        "img": ["src", "alt", "title"],  # Allow images with src, alt, and title
        "code": ["class"],  # Allow class for code syntax highlighting
    }

    # Sanitise the rendered HTML to allow only safe tags and attributes
    sanitized_html = bleach.clean(
        html_content,
        tags=allowed_tags,
        attributes=allowed_attributes,
        strip=True,  # Strip disallowed tags and attributes
    )

    # Return the sanitised HTML as a JSON response
    return jsonify({"html": sanitized_html})
