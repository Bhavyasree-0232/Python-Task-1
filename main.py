import tkinter as tk
from tkinter import messagebox, simpledialog

# --- Functions ---
def add_task():
    task = entry_task.get().strip()
    if task == "":
        messagebox.showwarning("Warning", "Enter a task!")
        return
    tasks_listbox.insert(tk.END, task)
    entry_task.delete(0, tk.END)

def delete_task():
    try:
        index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(index)
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to delete!")

def edit_task():
    try:
        index = tasks_listbox.curselection()[0]
        current_task = tasks_listbox.get(index)
        new_task = simpledialog.askstring("Edit Task", "Modify your task:", initialvalue=current_task)
        if new_task:
            tasks_listbox.delete(index)
            tasks_listbox.insert(index, new_task)
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to edit!")

def mark_done():
    try:
        index = tasks_listbox.curselection()[0]
        task = tasks_listbox.get(index)
        if not task.startswith("✔ "):
            tasks_listbox.delete(index)
            tasks_listbox.insert(index, f"✔ {task}")
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to mark as done!")

def clear_all():
    if messagebox.askyesno("Clear All", "Delete all tasks?"):
        tasks_listbox.delete(0, tk.END)

def search_task():
    query = entry_search.get().strip().lower()
    for i in range(tasks_listbox.size()):
        task = tasks_listbox.get(i).lower()
        if query in task:
            tasks_listbox.selection_clear(0, tk.END)
            tasks_listbox.selection_set(i)
            tasks_listbox.see(i)
            return
    messagebox.showinfo("Not Found", "No matching task found.")

# --- GUI Setup ---
root = tk.Tk()
root.title("To-Do List")
root.geometry("550x600")
root.config(bg="#F7F9FC")

# Make a frame to hold all widgets and center it
main_frame = tk.Frame(root, bg="#F7F9FC")
main_frame.place(relx=0.5, rely=0.5, anchor="center")

title_label = tk.Label(main_frame, text="📝 To-Do List ", font=("Arial", 18, "bold"), bg="#F7F9FC", fg="#333")
title_label.pack(pady=10)

# --- Task Entry and Buttons ---
frame_top = tk.Frame(main_frame, bg="#F7F9FC")
frame_top.pack(pady=5)

entry_task = tk.Entry(frame_top, width=30, font=("Arial", 12), bd=2, relief="solid")
entry_task.grid(row=0, column=0, padx=5, pady=5)

btn_add = tk.Button(frame_top, text="Add Task", width=12, command=add_task, bg="#90B9EE")
btn_add.grid(row=0, column=1, padx=5)

entry_search = tk.Entry(frame_top, width=30, font=("Arial", 12), bd=2, relief="solid")
entry_search.grid(row=1, column=0, padx=5, pady=5)

btn_search = tk.Button(frame_top, text="Search Task", width=12, command=search_task, bg="#90B9EE")
btn_search.grid(row=1, column=1, padx=5)

# --- Task List Box ---
frame_list = tk.Frame(main_frame, bg="#F7F9FC")
frame_list.pack(pady=10)

scrollbar = tk.Scrollbar(frame_list)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

tasks_listbox = tk.Listbox(
    frame_list,
    width=45,
    height=10,
    font=("Arial", 12),
    selectbackground="#D3D3D3",
    activestyle="none",
    relief="solid",
    bd=2,
    yscrollcommand=scrollbar.set
)
tasks_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar.config(command=tasks_listbox.yview)

# --- Bottom Buttons ---
frame_bottom = tk.Frame(main_frame, bg="#F7F9FC")
frame_bottom.pack(pady=10)

btn_edit = tk.Button(frame_bottom, text="Edit Task", width=12, command=edit_task, bg="#98FB98")
btn_edit.grid(row=0, column=0, padx=5, pady=5)

btn_done = tk.Button(frame_bottom, text="Mark Done", width=12, command=mark_done, bg="#98FB98")
btn_done.grid(row=0, column=2, padx=5, pady=5)


btn_delete = tk.Button(frame_bottom, text="Delete Task", width=12, command=delete_task, bg="#FF7F7F")
btn_delete.grid(row=0, column=1, padx=5, pady=5)

btn_clear = tk.Button(frame_bottom, text="Clear All", width=12, command=clear_all, bg="#FF7F7F")
btn_clear.grid(row=0, column=3, padx=5, pady=5)

root.mainloop()
