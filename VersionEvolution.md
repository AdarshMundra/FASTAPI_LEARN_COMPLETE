# FastAPI Project Version Evolution

This document provides a detailed explanation of how the FastAPI Blog project evolved through each version.

## Version 0 (v0): Basic API Structure

In this initial version, the project implemented a simple FastAPI application with basic routing and Pydantic models.

### Key Features:
- **Basic FastAPI Setup**: Simple application initialization with `app = FastAPI()`
- **Pydantic Model**: Created a `Blog` model with title, body, and published fields
- **Basic Routing**: Implemented simple GET and POST routes
- **Query Parameters**: Used query parameters for filtering (limit, published, sort)
- **Path Parameters**: Used path parameters to fetch specific blogs by ID
- **No Database**: All responses were hardcoded without actual data storage
- **No Authentication**: No user management or authentication

### Endpoints:
- `GET /`: Root endpoint returning a simple message
- `GET /blog`: List blogs with optional query parameters
- `GET /blog/unpublished`: Get unpublished blogs
- `GET /blog/{id}`: Get a specific blog by ID
- `GET /blog/{id}/comments`: Get comments for a specific blog
- `POST /blog`: Create a new blog (without actual storage)

### Code Structure:
- Single `main.py` file containing all code
- No separation of concerns
- No actual data persistence

## Version 1 (v1): Database Integration

Version 1 introduced SQLAlchemy ORM integration with SQLite database, enabling actual data persistence.

### Key Features:
- **SQLAlchemy Integration**: Added database connection and session management
- **Database Models**: Created SQLAlchemy models for the Blog entity
- **CRUD Operations**: Implemented Create, Read, Update, Delete operations with database
- **Dependency Injection**: Used FastAPI's dependency injection for database sessions
- **Error Handling**: Added basic HTTP exception handling
- **Response Status Codes**: Proper HTTP status codes for different operations

### Database Structure:
- **Blog Table**: Created with id, title, body, and published fields
- **SQLite Database**: Used SQLite as the database engine

### Code Organization:
- **Database Setup**: Added database.py for connection and session management
- **Models**: Added models.py for SQLAlchemy models
- **Schemas**: Added schemas.py for Pydantic models (request/response validation)
- **Main Application**: Enhanced main.py with database operations

### Endpoints:
- `GET /`: Root endpoint
- `GET /blog`: Get all blogs from database
- `GET /blog/unpublished`: Get unpublished blogs
- `GET /blog/{id}`: Get blog by ID with database lookup
- `PUT /blog/{id}`: Update blog in database
- `DELETE /blog/{id}`: Delete blog from database
- `POST /blog`: Create blog with database persistence

## Version 2 (v2): User Management

Version 2 added user management, password hashing, and relationships between users and blogs.

### Key Features:
- **User Model**: Added User entity with name, email, and password
- **Password Hashing**: Implemented bcrypt password hashing for security
- **Relationships**: Created relationship between User and Blog models
- **Response Models**: Enhanced Pydantic schemas with response_model for API documentation
- **API Documentation**: Added tags for better Swagger UI organization
- **Status Codes**: Proper HTTP status codes for different operations

### Database Enhancements:
- **User Table**: Added users table with id, name, email, and password fields
- **Foreign Keys**: Added user_id foreign key in blogs table
- **Relationships**: Configured SQLAlchemy relationships between models

### New Components:
- **Hashing Module**: Added hashing.py for password encryption
- **Enhanced Schemas**: Updated schemas.py with User and ShowUser models
- **Enhanced Models**: Updated models.py with User model and relationships

### Endpoints:
- **User Management**:
  - `POST /create`: Create a new user with hashed password
  - `GET /user/`: Get all users
  - `GET /user/{id}`: Get user by ID
- **Blog Management**: Same as v1 but with user relationship

## Version 3 (v3): Modular Architecture & Authentication

Version 3 completely restructured the application with a modular approach, added JWT authentication, and implemented proper separation of concerns.

### Key Features:
- **Modular Structure**: Code organized into separate modules and packages
- **JWT Authentication**: Implemented OAuth2 with JWT tokens
- **Protected Routes**: Secured endpoints requiring authentication
- **Router Separation**: Split routes into separate router files
- **Business Logic Separation**: Moved business logic to dedicated code repository
- **Token Management**: Added token generation and validation

### Code Organization:
- **Routers Package**: Separated routes into authentication.py, blog.py, and user.py
- **Code Repository**: Created code_repo package with blog_code.py and user_code.py
- **Authentication**: Added oauth2.py and token_data.py for JWT handling
- **Main Application**: Simplified main.py to include routers

### Authentication Flow:
1. User logs in with username/password
2. System validates credentials against database
3. System generates JWT token with expiration
4. Client uses token in Authorization header for protected routes
5. System validates token for each protected request

### Security Enhancements:
- **Password Hashing**: Secure password storage with bcrypt
- **JWT Tokens**: Secure authentication with expiring tokens
- **Protected Routes**: All blog operations require authentication
- **Token Verification**: Middleware for validating tokens

### Endpoints:
- **Authentication**:
  - `POST /login`: Authenticate and get access token
- **Users** (prefix: /users):
  - `POST /create`: Create user
  - `GET /`: Get all users
  - `GET /{id}`: Get user by ID
- **Blogs** (prefix: /blogs):
  - `GET /`: Get all blogs (authenticated)
  - `GET /{id}`: Get blog by ID (authenticated)
  - `PUT /{id}`: Update blog (authenticated)
  - `DELETE /{id}`: Delete blog (authenticated)
  - `POST /`: Create blog (authenticated)

### Architecture Patterns:
- **Repository Pattern**: Business logic in separate modules
- **Dependency Injection**: For database and authentication
- **Router Pattern**: Routes organized by resource type
- **Service Layer**: Authentication services separated from routes

## Summary of Evolution

1. **v0**: Basic FastAPI setup with hardcoded responses
2. **v1**: Added database integration with SQLAlchemy
3. **v2**: Added user management and relationships
4. **v3**: Restructured with modular architecture and added JWT authentication

The project evolved from a simple API to a well-structured application following best practices for API development, security, and code organization.

## Migration Considerations

### Migrating from v0 to v1

1. **Database Setup**:
   - Install SQLAlchemy and database drivers
   - Create database connection and session management
   - Define SQLAlchemy models for existing entities

2. **Code Restructuring**:
   - Split code into multiple files (database.py, models.py, schemas.py)
   - Move Pydantic models to schemas.py
   - Create proper dependency injection for database sessions

3. **Endpoint Updates**:
   - Replace hardcoded responses with database queries
   - Add error handling for database operations
   - Implement proper CRUD operations with database persistence

4. **Testing**:
   - Test database connection and migrations
   - Verify all CRUD operations work with the database
   - Ensure proper error handling for invalid operations

### Migrating from v1 to v2

1. **User Management**:
   - Add User model to models.py
   - Create user-related Pydantic schemas
   - Implement password hashing functionality

2. **Relationship Setup**:
   - Add foreign keys between Blog and User models
   - Configure SQLAlchemy relationships
   - Update database schema with migrations

3. **API Enhancements**:
   - Add user management endpoints
   - Update response models to include relationships
   - Add API documentation tags

4. **Security Considerations**:
   - Implement password hashing for user creation
   - Ensure sensitive user data is not exposed in responses
   - Add validation for user operations

### Migrating from v2 to v3

1. **Code Reorganization**:
   - Create routers package and split routes by resource
   - Create code_repo package for business logic
   - Move endpoint handlers to appropriate router files

2. **Authentication Implementation**:
   - Add JWT token generation and validation
   - Create OAuth2 authentication scheme
   - Implement login endpoint
   - Add token verification middleware

3. **Route Protection**:
   - Add authentication dependency to protected routes
   - Update all endpoints to use the new router structure
   - Ensure proper error handling for authentication failures

4. **Testing and Validation**:
   - Test authentication flow
   - Verify protected routes reject unauthenticated requests
   - Ensure all functionality works with the new modular structure