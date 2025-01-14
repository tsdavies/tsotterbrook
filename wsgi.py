import logging
import sys

# Configure logging to output to stderr (required for OpenShift logs)
logging.basicConfig(stream=sys.stderr)

# Ensure the correct app path is added to the system path
# Replace with the absolute path to your project if necessary
sys.path.insert(
    0, "/root/customer-account-automation/"  # Update to your app's root directory
)

# Import the application factory
from app import create_app

# Create the app instance
app = create_app()

# Alias `app` as `application` for WSGI compatibility (used by Gunicorn)
application = app

if __name__ == "__main__":
    """
    Entry point for local development.
    - Prints all registered routes for debugging.
    - Starts the Flask development server.
    Note: Production deployments should use a WSGI server like Gunicorn.
    """
    print("Registered routes:")
    print(app.url_map)  # Prints all routes for inspection
    app.run()  # Start the Flask app (debug=True is omitted for production)
