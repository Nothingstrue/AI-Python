import tkinter as tk
from tkinter import messagebox

# The data source
my_tasks = ["Update System", "Clean Cache", "Check Logs", "Backup Data"]

def start_task(task_name):
    print(f"Starting process for: {task_name}")

def delete_task(task_name, widget_frame):
    # This function takes the task name AND the frame widget itself
    print(f"Deleting: {task_name}")
    
    # Destroy the visual frame (removes the row from screen)
    widget_frame.destroy()

root = tk.Tk()
root.geometry("400x300")
root.title("Dynamic List Generator")

# 1. Create a container for the list items
# We use a Frame so we can easily pack rows inside it
list_container = tk.Frame(root)
list_container.pack(fill="both", expand=True, padx=10, pady=10)

# 2. The Loop to create widgets
for task in my_tasks:
    # A. Create a row frame (holds the label + 2 buttons)
    row_frame = tk.Frame(list_container, pady=5)
    row_frame.pack(fill="x") # Make it stretch across

    # B. Create the Label
    lbl = tk.Label(row_frame, text=task, width=20, anchor="w")
    lbl.pack(side=tk.LEFT)

    # C. Create Button 1 (Start)
    # CRITICAL: We use 't=task' to bind the CURRENT task string to this lambda
    btn1 = tk.Button(row_frame, text="Start", 
                     command=lambda t=task: start_task(t))
    btn1.pack(side=tk.LEFT, padx=5)

    # D. Create Button 2 (Delete)
    # We pass 'row_frame' so the button knows which row to destroy
    btn2 = tk.Button(row_frame, text="Delete", bg="#ffcccc",
                     command=lambda t=task, f=row_frame: delete_task(t, f))
    btn2.pack(side=tk.LEFT, padx=5)

root.mainloop()