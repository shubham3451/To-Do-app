
---

# To-Do List API

This is a simple **To-Do List** REST API built with **FastAPI** and **SQLite**. The API allows you to create, fetch, update, and delete tasks.

## Features

The API supports the following endpoints:

- **POST /tasks**: Create a new task with title, description, and status.
- **GET /tasks**: Fetch all tasks.
- **GET /tasks/{id}**: Fetch a task by its ID.
- **PUT /tasks/{id}**: Update a task's status.
- **DELETE /tasks/{id}**: Delete a task by its ID.

## Requirements

- Python 3.7 or higher
- FastAPI
- SQLite

### Install Dependencies

You can install the required dependencies using `pip`:

```bash
pip install fastapi uvicorn sqlite3
```

## How to Run

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/todo-api.git
cd todo-api
```

### 2. Run the FastAPI Application

To start the application, run:

```bash
uvicorn main:app --reload
```

This will start the FastAPI app at `http://127.0.0.1:8000`.

### 3. Access Swagger UI

Once the application is running, you can access the interactive Swagger UI to test the API at:

```
http://127.0.0.1:8000/docs
```

You can use the Swagger UI to interact with the API endpoints and test each functionality by clicking **"Try it out"** and **"Execute"**.

### 4. Access Redoc Documentation

Alternatively, you can view the Redoc API documentation at:

```
http://127.0.0.1:8000/redoc
```

## API Endpoints

### 1. **POST /tasks**

- **Description**: Create a new task.
- **Request Body**:  
  - `title`: Task title (required, string)
  - `description`: Task description (optional, string)
  - `status`: Task status (optional, default: "pending", string; valid values: `pending`, `in-progress`, `completed`)
  
- **Response**:
  - Returns a message confirming the task was created.

#### Example Request

```json
{
  "title": "Buy groceries",
  "description": "Milk, eggs, bread",
  "status": "pending"
}
```

#### Example Response

```json
{
  "message": "Task created successfully"
}
```

### 2. **GET /tasks**

- **Description**: Fetch all tasks.
- **Response**:  
  - Returns a list of all tasks, including their `id`, `title`, `description`, and `status`.

#### Example Response

```json
[
  {
    "id": 1,
    "title": "Buy groceries",
    "description": "Milk, eggs, bread",
    "status": "pending"
  },
  {
    "id": 2,
    "title": "Complete homework",
    "description": "Math and science assignments",
    "status": "in-progress"
  }
]
```

### 3. **GET /tasks/{id}**

- **Description**: Fetch a task by its ID.
- **Path Parameter**:  
  - `id`: Task ID (required, integer)
- **Response**:  
  - Returns a task with the specified `id`.

#### Example Response

```json
{
  "id": 1,
  "title": "Buy groceries",
  "description": "Milk, eggs, bread",
  "status": "pending"
}
```

### 4. **PUT /tasks/{id}**

- **Description**: Update the status of a task.
- **Path Parameter**:  
  - `id`: Task ID (required, integer)
- **Request Body**:  
  - `status`: Task status (required, string; valid values: `pending`, `in-progress`, `completed`)

- **Response**:  
  - Returns a message confirming the task status was updated.

#### Example Request

```json
{
  "status": "completed"
}
```

#### Example Response

```json
{
  "message": "Task status updated successfully",
  "task": {
    "id": 1,
    "title": "Buy groceries",
    "description": "Milk, eggs, bread",
    "status": "completed"
  }
}
```

### 5. **DELETE /tasks/{id}**

- **Description**: Delete a task by its ID.
- **Path Parameter**:  
  - `id`: Task ID (required, integer)
- **Response**:  
  - Returns a message confirming the task was deleted.

#### Example Response

```json
{
  "message": "Task deleted successfully"
}
```

## Database

The application uses an **SQLite database** (stored in a file named `tasks.db`) to persist the data. This database will be automatically created when you run the application, and the `tasks` table will be created if it doesn't exist.

---

### Notes:

- **Persistent Database**: The SQLite database is file-based (`tasks.db`), meaning the tasks will persist across app restarts.
- **Swagger UI**: FastAPI provides a built-in interactive interface (`/docs`) to test the API easily.
  
Make sure to follow the steps above to get started with the API and test it using Swagger UI.
