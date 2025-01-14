from flask import render_template


def about():
    """
    Render the 'About Me' page.
    - Provides information about the individual or application.
    - Passes a title to the template for consistent page rendering.

    Returns:
        Response: Rendered HTML template for the About page.
    """
    return render_template("about.html", title="About Me")
