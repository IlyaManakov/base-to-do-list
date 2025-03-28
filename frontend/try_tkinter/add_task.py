from tkinter import Tk, ttk, scrolledtext
from backend.main import TaskCreate
import requests

def post_task(root, name, comment):
    task_data = TaskCreate(name=name, comment=comment)
    requests.post('http://127.0.0.1:8000/tasks/', json=task_data.dict())
    root.destroy()

def add_task1():
    root = Tk()
    root.title('Добавить задачу')

    # размер окна, расположение по центру, минимальный размер
    w, h = 200, 300
    w_min, h_min = 300, 200
    x = root.winfo_screenwidth() // 2 - w // 2
    y = root.winfo_screenheight() // 2 - h // 2

    #размещение окна с указанными свойствами
    root.geometry(f'{w}x{h}+{x}+{y}')
    root.minsize(w_min, h_min)

    #заголовок приложения
    ttk.Label(root, text='Создание задачи:').pack()

    #название задачи
    ttk.Label(root, text='Название задачи:').pack()
    entry_name = ttk.Entry(root)
    entry_name.pack()

    #описание задачи
    ttk.Label(root, text='Описание задачи:').pack()
    entry_text = scrolledtext.ScrolledText(root, width = 180, height = 10)
    entry_text.pack()

    #кнопка добавления задачи
    btn_add = ttk.Button(root, text='Создать', command=lambda: post_task(root, entry_name.get(), entry_text.get("1.0", "end-1c")))
    btn_add.pack()

    root.mainloop()