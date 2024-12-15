from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
from typing import List, Optional

# FastAPI app initialization
app = FastAPI()

# SQLite database setup (file-based)
DATABASE = "tasks.db"  # Use file-based database to persist data

# Create the tasks table if it doesn't exist
def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            status TEXT DEFAULT 'pending'
        )
    ''')
    conn.commit()
    conn.close()

# Ensure the table is created when the app starts
@app.on_event("startup")
def startup():
    init_db()

# Task model for input data validation
class Task(BaseModel):
    title: str
    description: Optional[str] = None
    status: Optional[str] = 'pending'

# Helper function to get a task by its ID
def get_task_by_id(task_id: int):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE id=?", (task_id,))
    task = cursor.fetchone()
    conn.close()
    return task

# Endpoints

# 1. POST /tasks: Create a new task
@app.post("/tasks/")
async def create_task(task: Task):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (title, description, status) VALUES (?, ?, ?)",
                   (task.title, task.description, task.status))
    conn.commit()
    conn.close()
    return {"message": "Task created successfully"}

# 2. GET /tasks: Fetch all tasks
@app.get("/tasks/", response_model=List[Task])
async def get_tasks():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return [{"id": task[0], "title": task[1], "description": task[2], "status": task[3]} for task in tasks]

# 3. GET /tasks/{id}: Fetch a task by ID
@app.get("/tasks/{task_id}/")
async def get_task(task_id: int):
    task = get_task_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"id": task[0], "title": task[1], "description": task[2], "status": task[3]}

# 4. PUT /tasks/{id}: Update task status
@app.put("/tasks/{task_id}/")
async def update_task(task_id: int, status: str):
    if status not in ["pending", "in-progress", "completed"]:
        raise HTTPException(status_code=400, detail="Invalid status value")
    
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET status=? WHERE id=?", (status, task_id))
    conn.commit()
    conn.close()
    
    task = get_task_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    return {"message": "Task status updated successfully", "task": {"id": task[0], "title": task[1], "description": task[2], "status": task[3]}}

# 5. DELETE /tasks/{id}: Delete a task by ID
@app.delete("/tasks/{task_id}/")
async def delete_task(task_id: int):
    task = get_task_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    conn.close()
    
    return {"message": "Task deleted successfully"}

