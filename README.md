# Personal Blog Backend with Django Rest Framework

## Overview

This application serves as the backend for a personal blog application, providing REST API endpoints for managing blog posts and user authentication. It is designed to integrate seamlessly with a frontend client, particularly a Flutter application, to enable full CRUD (Create, Read, Update, Delete) functionality for blog posts and user authentication using JWT (JSON Web Token).

## Use Case

The primary use case of this application is to facilitate the following functionalities:

- **CRUD Operations on Blog Posts**: Users can create, read, update, and delete blog posts through API endpoints provided by Django Rest Framework (DRF). Each blog post consists of a title, content, and other relevant metadata.

- **User Authentication with JWT**: The application supports user authentication and authorization using JSON Web Tokens (JWT). Users can log in securely using their credentials, and upon successful authentication, they receive a JWT token that grants access to protected API endpoints.

- **Integration with Flutter Client**: This backend is designed to seamlessly integrate with a Flutter client application, serving as the data management and authentication layer. The Flutter client can consume the API endpoints to fetch blog posts, create new posts, update existing ones, and manage user sessions securely.

## Technologies Used

- **Django**: The backend framework used to develop the REST API endpoints and manage database operations.
- **Django Rest Framework (DRF)**: Provides powerful tools for building web APIs, including serializers, views, and authentication mechanisms.
- **DRF-YASG**: Used for auto-generating Swagger documentation, ensuring clear API documentation and easy integration with frontend teams.
- **django-rest-framework-simplejwt**: Handles JWT-based authentication and token management within the Django Rest Framework ecosystem.
- **django-cors-headers**: Allows cross-origin resource sharing, enabling the frontend client (Flutter app) to communicate with the backend API securely.

## Installation and Setup

To set up this application locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/DevprojectEkla/DjangoApi
   cd DjangoApi
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Apply migrations to set up the database:

   ```bash
   python manage.py migrate
   ```

4. Run the development server:

   ```bash
   python manage.py runserver
   ```

5. Ensure the frontend Flutter client is configured to communicate with the backend API endpoints as defined in the Swagger documentation or directly through URL routes.

## API Endpoints

### Blog Posts

- **GET /posts/**: Retrieves a list of all blog posts.
- **GET /posts/{id}/**: Retrieves a specific blog post by its ID.
- **POST /posts/create/**: Creates a new blog post with provided data.
- **PUT /posts/{id}/update/**: Updates an existing blog post identified by its ID.
- **DELETE /posts/{id}/delete/**: Deletes a blog post identified by its ID.

### Authentication

- **POST /login/**: Authenticates a user with provided credentials and returns a JWT token for accessing protected endpoints.
- **POST /subscribe/**: Registers a new user with provided signup data and automatically logs them in, returning a JWT token for authentication.

### Swagger Documentation

The API is documented using Swagger UI, which provides detailed information about each endpoint, including request methods, expected parameters, and responses. This documentation facilitates easy integration with frontend clients like Flutter, ensuring seamless communication and consistent data management.

## Conclusion

This backend application, built with Django Rest Framework, offers robust functionality for managing blog posts and user authentication. It is optimized for integration with a Flutter client, enabling efficient development of a personalized blogging platform with secure user management and responsive API interactions.

For any questions or further details, please refer to the documentation or contact the development team.
