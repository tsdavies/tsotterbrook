from flask import render_template


def hello():
    """
    Render the 'Hello World' page.
    - Provides a short 'hello world' message
    - Passes a title to the template for consistent page rendering.

    Returns:
        Response: Rendered HTML template for the About page.
    """
    return render_template("hello.html", title="Hello World")