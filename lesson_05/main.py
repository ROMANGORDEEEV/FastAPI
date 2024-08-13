from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from fastapi.responses import HTMLResponse

app = FastAPI()


class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False


class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False


tasks = []
current_id = 1


@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <html>
        <head>
            <title>Task Management API</title>
        </head>
        <body>
            <h1>Добро пожаловать в Task Management API</h1>
            <p>Available commands:</p>
            <ul>
                <li>
                    <a href="/tasks">GET /tasks</a> - Get list of all tasks<br>
                    <code>curl -X 'GET' 'http://127.0.0.1:8000/tasks' -H 'accept: application/json'</code>
                </li>
                <li>
                    <a href="/tasks/1">GET /tasks/{id}</a> - Get a task by ID<br>
                    <code>curl -X 'GET' 'http://127.0.0.1:8000/tasks/1' -H 'accept: application/json'</code>
                </li>
                <li>
                    <a href="https://www.postman.com/">POST /tasks</a> - Add a new task (use Postman)<br>
                    <code>curl -X 'POST' 'http://127.0.0.1:8000/tasks' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"title": "Sample Task", "description": "This is a sample task.", "completed": false}'</code>
                </li>
                <li>
                    <a href="https://www.postman.com/">PUT /tasks/{id}</a> - Update a task by ID (use Postman)<br>
                    <code>curl -X 'PUT' 'http://127.0.0.1:8000/tasks/1' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"title": "Updated Task", "description": "This task has been updated.", "completed": true}'</code>
                </li>
                <li>
                    <a href="https://www.postman.com/">DELETE /tasks/{id}</a> - Delete a task by ID (use Postman)<br>
                    <code>curl -X 'DELETE' 'http://127.0.0.1:8000/tasks/1' -H 'accept: application/json'</code>
                </li>
            </ul>
            <p>For more details, visit the <a href="/docs">API Documentation</a>.</p>
        </body>
    </html>
    """


@app.get("/tasks", response_model=List[Task])
def read_tasks():
    return tasks


@app.get("/tasks/{id}", response_model=Task)
def read_task(id: int):
    task = next((task for task in tasks if task["id"] == id), None)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.post("/tasks", response_model=Task)
def create_task(task: TaskCreate):
    global current_id
    new_task = {"id": current_id, **task.dict()}
    tasks.append(new_task)
    current_id += 1
    return new_task


@app.put("/tasks/{id}", response_model=Task)
def update_task(id: int, updated_task: TaskCreate):
    task = next((task for task in tasks if task["id"] == id), None)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    task.update(updated_task.dict())
    return task


@app.delete("/tasks/{id}", response_model=Task)
def delete_task(id: int):
    global tasks
    task = next((task for task in tasks if task["id"] == id), None)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    tasks = [task for task in tasks if task["id"] != id]
    return task


# Для запуска сервера выполните команду: uvicorn main:app --reload
