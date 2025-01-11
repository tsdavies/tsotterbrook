# Personal Digital Portfolio, Tammy Davies

## Student Number:  **D1478699**

## Openshift URL and User Information

### [https://d1478699-cmt-120-cw-2-d1478699-cmt120-cw2.apps.containers.cs.cf.ac.uk/](https://d1478699-cmt-120-cw-2-d1478699-cmt120-cw2.apps.containers.cs.cf.ac.uk/)

- **Register**: You can register with your own email to create a simple user account to comment with.
- **Administrator Login**:
    - **Email**: `tammy@tsdavies.com`
    - **Password**: `test123`

# Table of Contents

1. [Advanced Functionality](#advanced-functionality)
    - [General Architecture and Organisation](#general-architecture-and-organisation)
    - [Authentication and Authorisation](#authentication-and-authorisation)
    - [Validation and Sanitisation](#validation-and-sanitisation)
    - [Markdown and Content Handling](#markdown-and-content-handling)
    - [Flask Extensions and ORM Usage](#flask-extensions-and-orm-usage)
    - [API Integration](#api-integration)
    - [Deployment and DevOps](#deployment-and-devops)
2. [Overview](#overview)
    - [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Installed Packages and Their Purpose](#installed-packages-and-their-purpose)
    - [Core Packages](#core-packages)
    - [Development and Utilities](#development-and-utilities)
    - [Security and Validation](#security-and-validation)
    - [Frontend and Formatting](#frontend-and-formatting)
    - [API and Networking](#api-and-networking)
    - [Other Dependencies](#other-dependencies)
5. [Deployment Instructions](#deployment-instructions)
6. [References](#references)

---

## Advanced Functionality

### General Architecture and Organisation

- **Blueprint Architecture**:
    - Modularisation with Flask's Blueprint architecture for clean separation of concerns and scalability.
    - Templates, views, and static files were co-located for specific functionalities.

- **Custom Template Filters**:
    - Developed filters for rendering Markdown and formatting dates to improve content presentation and reusability.

---

### Authentication and Authorisation

- **Role-Based Access Control (RBAC)**:
    - Implemented three user tiers: anonymous users, registered users, and administrators.
    - Used Flask-Login's `@login_required` decorator to secure sensitive routes like `/blog/new` and `/blog/edit`,
      restricting access to authenticated users.
    - Administrators manage posts and comments, while registered users manage their own comments.
    - Attempts to access restricted areas without authentication display a "Forbidden" page.

- **Session Management**:
    - Used Flask sessions with HttpOnly and Secure cookies to protect against XSS and cookie theft.
    - Managed state for Pokémon API searches via session variables.

---

### Validation and Sanitisation

- **Input Validation**:
    - Robust server-side validation using Flask-WTF with CSRF tokens to prevent cross-site request forgery.
    - Complemented this with JavaScript-based client-side validation for immediate user feedback.

- **Data Sanitisation**:
    - Used the `bleach` library to sanitise user-generated content, allowing safe HTML while mitigating XSS risks.

---

### Markdown and Content Handling

- **Markdown Parsing and Preview**:
    - Integrated Markdown preview functionality using JavaScript to interact with a Flask endpoint.
    - Real-time rendering of parsed Markdown into HTML with sanitised supported HTML tags using `bleach`.

---

### Flask Extensions and ORM Usage

- **Flask-Login**:
    - Simplified authentication and session management, securing routes with decorators like `@login_required`.

- **Flask-WTF**:
    - Streamlined form validation and CSRF protection.

- **SQLAlchemy ORM**:
    - Used for database operations, handling dynamic content such as storing and retrieving blog posts and comments.
    - Abstracted raw SQL into Python objects for improved maintainability and scalability.

---

### API Integration

- **Pokémon API**:
    - Dynamically fetched Pokémon data from PokéAPI to display in a custom "Pokémon card" view.
    - Supported session-based searches and URL parameter handling for direct links to specific Pokémon (e.g.,
      `/pokemon/pikachu`).

---

### Deployment and DevOps

- **OpenShift Deployment**:
    - Deployed using OpenShift with Gunicorn as the WSGI server.
    - Secured credentials (e.g., Gmail for the contact form) using OpenShift's environment variable management.

- **Environment Variable Management**:
    - Used `.env` files and OpenShift for secure handling of sensitive data.

- **Version Control**:
    - Managed the codebase with Git, employing multiple branches for versioning and integration.

---

## Overview

This dynamic web application serves as a personal portfolio showcasing various functionalities:

### Features

1. **Blog**:
    - Dynamic blog page allowing for content updates via a database.
    - User-friendly interface for displaying blog posts chronologically.

2. **Pokémon API Integration**:
    - Fetches and displays Pokémon details using the Pokémon API.
    - Interactive elements to search for specific Pokémon or view their stats and abilities.

3. **About and Contact Pages**:
    - Informative About page highlighting personal achievements and skills.
    - Functional Contact page with a secure form for user messages sent via Gmail.

---

## Technologies Used

- **Backend**: Python with Flask framework
- **Frontend**: HTML5, CSS3, Bootstrap for responsiveness and usability
- **Database**: SQLite for dynamic content storage
- **API Integration**: Pokémon API for real-time Pokémon data
- **Deployment**: OpenShift using Gunicorn for robust hosting and scalability
- **Development**: Initially VSCode, but PyCharm was so much better

---

## Installed Packages and their Purpose

### Core Packages

- **Flask**: Web framework to build and manage the application.
- **Flask-WTF**: Simplifies form handling and validation with built-in CSRF protection.
- **Flask-Login**: Manages user authentication and session handling.
- **Flask-Mail**: Adds email support for user notifications.
- **Flask-Migrate**: Facilitates database migrations using Alembic.
- **Flask-SQLAlchemy**: ORM for handling database interactions dynamically and efficiently.

### Development and Utilities

- **Gunicorn**: WSGI server for deploying the Flask application on OpenShift.
- **python-dotenv**: Manages environment variables securely.
- **black**: A code formatter for consistent Python code styling.
- **alembic**: Database migration tool integrated with Flask-Migrate.

### Security and Validation

- **bleach**: Sanitises HTML input to mitigate XSS vulnerabilities.
- **email_validator**: Validates email inputs for user registrations or forms.

### Frontend and Formatting

- **Markdown**: Parses and converts Markdown to HTML.
- **Jinja2**: Template engine for rendering dynamic HTML content.

### API and Networking

- **Requests**: Handles API calls to the Pokémon API.

### Other Dependencies

- **SQLAlchemy**: Core database interaction package used with Flask-SQLAlchemy.
- **WTForms**: Flexible forms library used with Flask-WTF.

---

## Deployment Instructions

1. Install project dependencies:

    ```bash
    pip install -r requirements.txt
    ```

2. Activate the virtual environment

    ```bash
    . venv/bin/activate # Mac/Linux
    . venv\Scripts\activate # Windows
    ```
3. To enable the gmail functionality locally you need to configure a MAIL_SERVER, note you will need an access key for
   your gmail account, the deployed version has this configured in the OpenShift environment variables for security.

    ```bash
    # Flask Secret Key
    SECRET_KEY=your-very-secret-key
    # Email Configuration
    MAIL_SERVER=smtp.gmail.com
    MAIL_PORT=587
    MAIL_USE_TLS=True
    MAIL_USE_SSL=False
    MAIL_USERNAME=yourgmail@gmail.com
    MAIL_PASSWORD=<access key>
    
    # Flask Environment
    FLASK_ENV=development
    ````

--- 

## References:

### Use of ChatGPT in Development - ChatGPT 4o, 2024

During the development process, I used ChatGPT to assist with converting my JavaScript oriented ideas into Flask/Python
functionality. As someone who naturally thinks in JavaScript first, I found generative AI particularly helpful in
bridging the gap between my learning from the module and my prior experience.
The project’s overall ideas and structure were entirely my own. ChatGPT served as a valuable tool to streamline
implementation, ensuring my work was both meaningful and well-structured.


