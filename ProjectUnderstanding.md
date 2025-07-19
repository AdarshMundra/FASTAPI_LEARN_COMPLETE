# FastAPI Blog Project Understanding

This document provides an overview of the FastAPI Blog project structure, functionality, and evolution through different versions.

## Project Overview

This is a RESTful API project built with FastAPI for managing blogs and users. The project demonstrates progressive development from a simple API to a more complex application with authentication, database integration, and proper code organization.

## Project Structure

The project is organized into three versions (v0, v1, v2, v3), each representing a different stage of development:

```
FASTAPI_LEARN_COMPLETE/
|-- v0/                 # Basic FastAPI implementation
|-- v1/                 # Database integration
|-- v2/                 # User management added
|-- v3/                 # Modular structure with authentication
|-- requirements.txt    # Project dependencies
|-- README.md           # Basic setup instructions
```

## Technology Stack

- **FastAPI**: Modern, fast web framework for building APIs
- **SQLAlchemy**: SQL toolkit and ORM
- **Pydantic**: Data validation and settings management
- **SQLite**: Database engine
- **JWT**: Authentication using JSON Web Tokens
- **Uvicorn**: ASGI server for running the application

## Version Evolution

### v0: Basic API Structure

- Simple FastAPI implementation with basic routes
- In-memory data storage (no database)
- Basic CRUD operations for blogs
- Pydantic models for request/response validation

### v1: Database Integration

- SQLAlchemy ORM integration with SQLite
- Database models for blogs
- CRUD operations connected to database
- Dependency injection for database sessions

### v2: User Management

- Added user model and authentication
- Password hashing with bcrypt
- Relationship between users and blogs
- API documentation with tags

### v3: Modular Architecture

- Code organized into modules (routers, models, schemas)
- Separation of concerns with business logic in code_repo
- JWT authentication with OAuth2
- Protected routes requiring authentication
- Improved error handling

## Key Components

### Models (Database Schema)

- **Blog**: Represents blog posts with title, body, and user relationship
- **User**: Represents users with name, email, password, and blog relationship

### Schemas (Pydantic Models)

- **BlogBase/Blog**: Request/response models for blog operations
- **User**: Request model for user creation
- **ShowUser/ShowBlog**: Response models with relationship data
- **Login/Token/TokenData**: Authentication-related models

### Routers

- **blog.py**: Endpoints for blog CRUD operations
- **user.py**: Endpoints for user management
- **authentication.py**: Login and token generation

### Authentication

- JWT token-based authentication
- Password hashing with bcrypt
- Token verification middleware

## API Endpoints

### Authentication
- `POST /login`: Authenticate user and get access token

### Users
- `POST /users/create`: Create a new user
- `GET /users/`: Get all users
- `GET /users/{id}`: Get user by ID

### Blogs
- `GET /blogs`: Get all blogs (requires authentication)
- `GET /blogs/{id}`: Get blog by ID (requires authentication)
- `POST /blogs`: Create a new blog (requires authentication)
- `PUT /blogs/{id}`: Update a blog (requires authentication)
- `DELETE /blogs/{id}`: Delete a blog (requires authentication)

## Running the Application

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the application:
   ```
   uvicorn main:app --reload
   ```

3. Access the API documentation:
   - Swagger UI: http://127.0.0.1:8000/docs
   - ReDoc: http://127.0.0.1:8000/redoc

## Development Patterns

1. **Dependency Injection**: Used for database sessions and authentication
2. **Repository Pattern**: Business logic separated in code_repo
3. **Model-View-Controller**: Separation of data models, business logic, and API endpoints
4. **Data Transfer Objects**: Pydantic schemas for request/response validation

## Security Features

1. Password hashing with bcrypt
2. JWT token authentication
3. Protected routes with OAuth2
4. Token expiration and validation