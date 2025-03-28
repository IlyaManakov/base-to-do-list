import sqlite3

def start():
    conn = sqlite3.connect('sqlite3database.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            task_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            comment TEXT
        )
    ''')
    conn.commit()