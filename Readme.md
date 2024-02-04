## User Registration, Login, and Logout API

This Django app provides a RESTful API for user registration, login, and logout functionalities. Users can register with their username, email, and password, authenticate themselves by logging in, and logout when they are done using the application.

### Features

- User registration with username, email, and password.
- User login authentication.
- User logout functionality.

### API Endpoints

#### User Registration

- **Endpoint**: `/user/register/`
- **Method**: POST
- **Request Body**:
  - `username`: Username of the user (required).
  - `email`: Email address of the user (required).
  - `password`: Password for the user account (required).
- **Response**:
  - `201 CREATED` if the user is successfully registered.
  - `400 BAD REQUEST` if username, email, or password is missing.

#### User Login

- **Endpoint**: `/user/login/`
- **Method**: POST
- **Request Body**:
  - `username`: Username of the user (required).
  - `password`: Password for the user account (required).
- **Response**:
  - `200 OK` if the user is successfully logged in.
  - `400 BAD REQUEST` if username or password is missing.
  - `400 BAD REQUEST` if the user does not exist with the given username.
  - `401 UNAUTHORIZED` if the password is incorrect.

#### User Logout

- **Endpoint**: `/user/logout/<user_id>/`
- **Method**: POST
- **URL Parameter**:
  - `user_id`: The unique identifier of the user (required).
- **Response**:
  - `200 OK` if the user is successfully logged out.
  - `400 BAD REQUEST` if the user ID is incorrect.

### How to Use

1. **User Registration**:

   - Send a POST request to `/user/register/` with the required parameters (`username`, `email`, `password`).
   - Upon successful registration, the server will respond with a status code `201 CREATED`.

2. **User Login**:

   - Send a POST request to `/user/login/` with the required parameters (`username`, `password`).
   - Upon successful login, the server will respond with a status code `200 OK`.

3. **User Logout**:
   - Send a POST request to `/user/logout/<user_id>/` with the user ID as a URL parameter.
   - Upon successful logout, the server will respond with a status code `200 OK`.

### Security Considerations

- Passwords are encrypted before storage using a secure encryption method.
- Authentication tokens or sessions are not used in this API; instead, users are logged in and out based on their active status in the database.

### Dependencies

- Django
- Django REST Framework

### Note

- Ensure that proper error handling is implemented on the client-side to handle different response statuses and scenarios.

This readme provides an overview of the API functionalities and usage. It's essential to test the API thoroughly and consider additional security measures for production deployment.
