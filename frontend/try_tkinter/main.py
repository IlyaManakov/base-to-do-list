from tkinter import Tk, ttk, PhotoImage
from .add_task import add_task1
import requests


def display_tasks(task_frame, tasks):
    # Очищаем предыдущие данные (если нужно)
    for widget in task_frame.winfo_children():
        widget.destroy()
    print(tasks)
    # Выводим каждую задачу
    for task in tasks:
        task_text = f"{task['task_id']}. {task['name']}"
        if task['comment']:
            task_text += f" ({task['comment']})"
        ttk.Label(task_frame, text=task_text).pack(anchor='w')


def fetch_tasks(task_frame):
    response = requests.get("http://127.0.0.1:8000/tasks/")
    response.raise_for_status()  # Проверяем на ошибки HTTP
    tasks = response.json()  # Получаем данные JSON
    display_tasks(task_frame, tasks)


#получение информации о всех виджетах в окне
def print_info(widget, depth=0):
    widget_class=widget.winfo_class()
    widget_width = widget.winfo_width()
    widget_height = widget.winfo_height()
    widget_x = widget.winfo_x()
    widget_y = widget.winfo_y()
    print("   "*depth + f"{widget_class} width={widget_width} height={widget_height}  x={widget_x} y={widget_y}")
    for child in widget.winfo_children():
        print_info(child, depth+1)

def statistic_obj(root):
    '''получение информации о всех виджетах в окне'''
    root.update()
    print_info(root)

def window_start():
    #инициализация окна
    root = Tk()
    root.title('To-Do-list')

    #установка иконки приложения
    icon = PhotoImage(file='frontend/sources/to-do-list.png')
    root.iconphoto(False, icon)

    #размер окна, расположение по центру, минимальный размер
    w, h = 300, 600
    w_min, h_min = 300, 200
    x = root.winfo_screenwidth()//2 - w//2
    y = root.winfo_screenheight()//2 - h//2

    #размещение окна с указанными свойствами
    root.geometry(f'{w}x{h}+{x}+{y}')
    root.minsize(w_min, h_min)

    #заголовок приложения
    ttk.Label(root, text='Список задач:').pack()

    #кнопка добавления задачи
    btn_add = ttk.Button(root, text='Добавить задачу', command=add_task1)
    btn_add.pack()

    #кнопка статистики
    ttk.Button(root, text='Статистика', command=lambda: statistic_obj(root)).pack()

    #кнопка обновления
    ttk.Button(root, text="Обновить список", command=lambda: fetch_tasks(task_frame)).pack(pady=10)

    task_frame = ttk.Frame(root)
    task_frame.pack(fill='both', expand=True)

    root.mainloop()

