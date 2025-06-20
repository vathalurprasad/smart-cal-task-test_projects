import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = task_input.get()
    if task:
        tasks.append(task)
        update_tasks()
        task_input.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task can't be empty!")

def update_tasks():
    task_list.delete(0, tk.END)
    for task in tasks:
        task_list.insert(tk.END, task)

def delete_task():
    selected = task_list.curselection()
    if selected:
        tasks.pop(selected[0])
        update_tasks()

app = tk.Tk()
app.title("To-Do List")
app.geometry("300x400")

task_input = tk.Entry(app, width=25)
task_input.pack(pady=10)

add_btn = tk.Button(app, text="Add Task", command=add_task)
add_btn.pack()

task_list = tk.Listbox(app, width=40, height=15)
task_list.pack(pady=10)

del_btn = tk.Button(app, text="Delete Task", command=delete_task)
del_btn.pack()

app.mainloop()
