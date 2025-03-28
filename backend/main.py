from fastapi import FastAPI
from pydantic import BaseModel
from pathlib import Path
import databases.try_sqlite3 as db
import sqlite3

db.start()

# Путь к БД (в той же директории, что и main.py)
DATABASE_URL = Path(__file__).parent / "sqlite3database.db"

app = FastAPI()

# Модель для создания задачи
class TaskCreate(BaseModel):
    name: str
    comment: str

#подключение к бд
def get_db():
    conn = sqlite3.connect(str(DATABASE_URL))
    conn.row_factory = sqlite3.Row
    return conn


# Роуты API
@app.get('/tasks/',
         summary='Получение всех данных',
         tags=['Основные команды'])
def read_tasks():
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM tasks')
    return [dict(row) for row in cursor.fetchall()]


@app.post("/tasks/",
          summary='Добавление новой задачи',
          tags=['Основные команды']
          )
def create_task(task: TaskCreate):
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tasks (name, comment) VALUES (?, ?)",
            (task.name, task.comment)
        )
        conn.commit()
        task_id = cursor.lastrowid
        return {**task.dict(), "task_id": task_id}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", reload=True)