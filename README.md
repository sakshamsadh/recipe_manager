# Recipe Manager API

The Recipe Manager API is a RESTful web service built with Flask, allowing users to manage and organize their recipes. This documentation provides an overview of the project, installation instructions, usage guidelines, and other relevant information.

## Table of Contents
- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [API Endpoints](#api-endpoints)
- [Usage](#usage)
- [Authentication](#authentication)
- [Contributing](#contributing)
- [License](#license)

---

## Features
- User registration and authentication
- Create, read, update, and delete recipes
- Secure JWT-based authentication
- SQLite database for data storage
- User-friendly API endpoints for recipe management

## Technologies
- [Flask](https://flask.palletsprojects.com/): A lightweight Python web framework for building web applications.
- [Flask-JWT](https://pythonhosted.org/Flask-JWT/): A Flask extension for JSON Web Token (JWT) authentication.
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/): An extension for Flask to interact with databases using SQLAlchemy.
- [SQLite](https://www.sqlite.org/): A lightweight, serverless database engine.
- [Postman](https://www.postman.com/): A popular API testing tool for testing API endpoints.

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/recipe-manager-api.git
   cd recipe-manager-api

    Create a virtual environment and activate it:

    bash

python -m venv venv
source venv/bin/activate   # On Windows, use: venv\Scripts\activate

Install project dependencies:

bash

pip install -r requirements.txt

Set up the database:

bash

    flask db init
    flask db migrate
    flask db upgrade

API Endpoints

    POST /register: Register a new user account.
    POST /login: Authenticate and receive a JWT token.
    POST /recipes: Create a new recipe.
    GET /recipes: Retrieve a list of all recipes.
    GET /recipes/<recipe_id>: Retrieve details of a specific recipe.
    PUT /recipes/<recipe_id>: Update a specific recipe.
    DELETE /recipes/<recipe_id>: Delete a specific recipe.

Usage

    Start the development server:

    bash

    flask run

    Use a tool like Postman to interact with the API. Refer to the API Endpoints section for details on each endpoint.

Authentication

    To access protected routes (e.g., creating or updating recipes), include the JWT token in the Authorization header of your request using the Bearer scheme.

Contributing

Contributions are welcome! If you want to contribute to this project, please fork the repository, create a new branch, make your changes, and submit a pull request.