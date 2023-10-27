import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a Task.")

def delete_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "Please select the task to be deleted.")

def edit_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        selected_task = listbox.get(selected_task_index)
        new_task = entry.get()
        if new_task:
            listbox.delete(selected_task_index)
            listbox.insert(selected_task_index, new_task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def mark_completed():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        task = listbox.get(selected_task_index)
        task += " (Completed)"
        listbox.delete(selected_task_index)
        listbox.insert(tk.END, task)
    else:
        messagebox.showwarning("Warning", "Select Task")

# Create the main window
root = tk.Tk()
root.title("To-Do List Application")

# Set the initial size of the window (width x height)
root.geometry("500x300")

# Create an entry widget for task input
entry = tk.Entry(root, width=35, justify='center')
entry.pack(pady=10)

# Create buttons for various actions
add_button = tk.Button(root, text="Add new Task", command=add_task)
delete_button = tk.Button(root, text="Delete existing Task", command=delete_task)
edit_button = tk.Button(root, text="Edit Current Task", command=edit_task)
mark_completed_button = tk.Button(root, text="Mark Task as Completed", command=mark_completed)
add_button.pack()
delete_button.pack()
edit_button.pack()
mark_completed_button.pack()

# Create a listbox to display tasks
listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=45)
listbox.pack(pady=15, expand=True)

# Start the main event loop
root.mainloop()
