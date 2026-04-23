import tkinter as tk
from tkinter import messagebox, ttk
import random
import json
import os

class TaskGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Task Generator")
        self.tasks = {
            "учёба": ["Прочитать статью", "Решить задачу", "Посмотреть лекцию"],
            "спорт": ["Сделать зарядку", "Пробежать 1 км", "Отжаться 20 раз"],
            "работа": ["Написать отчёт", "Провести созвон", "Оптимизировать код"]
        }
        self.history = []
        self.load_history()
        self.create_widgets()

def create_widgets(self):
        # ... (реализация интерфейса: кнопки, выпадающий список для фильтра, текстовые поля и т.д.)
def generate_task(self):
        category = self.category_var.get()
        if category == "Все":
            all_tasks = [task for sublist in self.tasks.values() for task in sublist]
            task = random.choice(all_tasks)
        else:
            task = random.choice(self.tasks.get(category, []))
        self.history.append(task)
        self.update_history_display()
        self.save_history()

def add_task(self):
        category = self.new_category_var.get()
        task = self.new_task_entry.get().strip()
        if not task:
            messagebox.showerror("Ошибка", "Задача не может быть пустой!")
            return
        self.tasks.setdefault(category, []).append(task)
        self.new_task_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskGeneratorApp(root)
    root.mainloop()
