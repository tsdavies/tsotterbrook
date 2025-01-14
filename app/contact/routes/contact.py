import os

import bleach  # Used for sanitising user inputs to prevent injection attacks
from flask import render_template, redirect, url_for, flash
from flask_mail import Message

from app.contact.forms.contact_form import ContactForm
from app.extensions import mail


def contact():
    """
    Handle the contact form submission process.
    - Validates the form input.
    - Sanitises the user-provided data to ensure security.
    - Sends an email to the site owner with the submitted information.

    Returns:
        - On successful submission: Redirects to the contact page and displays a success message.
        - On failure or initial load: Renders the contact form template.
    """
    form = ContactForm()
    if form.validate_on_submit():
        # Sanitise inputs using bleach to remove any malicious code
        sanitised_name = bleach.clean(form.name.data)
        sanitised_email = bleach.clean(form.email.data)
        sanitised_message = bleach.clean(form.message.data)

        # Create an email message to send to the site owner
        msg = Message(
            subject=f"New Contact Form Submission from {sanitised_name} ({sanitised_email})",
            sender=sanitised_email
            or [
                os.environ.get("MAIL_USERNAME")
            ],  # Fallback to environment variable if sender is empty
            recipients=[
                os.environ.get("MAIL_USERNAME")
            ],  # Site owner's email address from environment
            body=sanitised_message,  # The message content
        )

        # Send the email using Flask-Mail
        mail.send(msg)

        # Flash a success message to the user
        flash("Your message has been sent successfully.", "success")

        # Redirect back to the contact page
        return redirect(url_for("contact.contact"))

    # Render the contact form page if not submitted or validation fails
    return render_template("contact.html", form=form)
