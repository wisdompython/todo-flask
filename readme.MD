Here’s the complete README file content formatted for you:

---

# Task Management API

## Overview
This is a Flask-based REST API for managing users and tasks. It includes CRUD operations for both users and tasks, with MongoDB as the backend database. User and task data are validated using JSON schema validators, and each collection is indexed to ensure unique `id` fields. The application is intended to run within a Docker environment, with Flask handling HTTP requests and MongoDB managing data persistence.

## Setup and Installation

### Requirements
- Docker
- Docker Compose
- Python 3.8 or above (if running locally)

### Installation
1. Clone this repository:
    ```bash
    git clone https://github.com/wisdompython/todo-flask.git
    ```

2. Start the application with Docker Compose:
    ```bash
    docker-compose up --build
    ```

   This will:
   - Build the Flask application.
   - Start MongoDB as the database.
   - Expose the API on `http://localhost:8000`.

3. If you prefer running the Flask application locally without Docker, set up a virtual environment and install dependencies:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

4. Configure MongoDB (if running locally):
    - Modify the MongoDB connection URI in `app.py` to point to your local MongoDB instance.
    - Start the application:
      ```bash
      python app.py
      ```

## API Endpoints

### Users

#### Create a User
- **URL:** `/users`
- **Method:** `POST`
- **Body Parameters:**
  ```json
  {
      "id": <integer>,          // Unique identifier for the user
      "username": <string>,      // Username
      "email": <string>          // Email address
  }
  ```
- **Response:**
  - `200 OK` on success
  - `400 Bad Request` if validation fails



### Tasks

#### Create a Task
- **URL:** `/task`
- **Method:** `POST`
- **Body Parameters:**
  ```json
  {
      "id": <integer>,           // Unique identifier for the task
      "title": <string>,         // Title of the task
      "description": <string>,   // Task description
      "completed": <string>,     // Task completion status ("true" or "false")
      "user_id": <integer>       // ID of the user who owns the task
  }
  ```
- **Response:**
  - `200 OK` on success
  - `400 Bad Request` if validation fails



#### Retrieve All Tasks
- **URL:** `/task`
- **Method:** `GET`
- **Response:** List of all tasks with their details.

#### Retrieve a Task by ID
- **URL:** `/task/<int:id>`
- **Method:** `GET`
- **Response:** Details of the specific task with the provided `id`.

#### Update a Task
- **URL:** `/task/<int:id>/`
- **Method:** `PATCH`
- **Body Parameters:**
  ```json
  {
      // Fields you want to update. Example:
      "title": <string>,
      "description": <string>
  }
  ```
- **Response:** `200 OK` with updated task details, or `404 Not Found` if no match is found.

### MongoDB Collection and Validation

MongoDB collections for `users` and `tasks` are created with JSON schema validators to ensure data integrity. The following validators are applied to each collection:

- **Users**
  - Required fields: `id`, `username`, `email`
  - Data types: `id` (integer), `username` (string), `email` (string)

- **Tasks**
  - Required fields: `id`, `title`, `description`, `completed`, `user_id`
  - Data types: `id` (integer), `title` (string), `description` (string), `completed` (string), `user_id` (integer)

### Database Configuration and Indexing
The application checks if collections exist in MongoDB:
- If a collection is missing, it creates it with the above validators.
- Each collection is indexed on the `id` field to ensure unique values.



## Error Handling
- If validation fails, a `400 Bad Request` error is returned with the details of the validation error.
- For update operations, if no matching task is found, a `404 Not Found` error is returned.



