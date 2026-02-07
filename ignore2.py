import tkinter as tk

# --- The Logic Functions ---

def add_new_row():
    """Gets text from input and calls the create function"""
    task_text = entry_box.get()
    
    if task_text != "":
        create_task_row(task_text)  # Call the builder function
        entry_box.delete(0, tk.END) # Clear the input box
    else:
        print("Input is empty!")

def create_task_row(task_name):
    """
    Creates the visual row: [ Label | Button | Delete ]
    This works for both initial items AND new items.
    """
    # 1. Create the row container
    row_frame = tk.Frame(list_container, pady=5, bd=1, relief="solid")
    row_frame.pack(fill="x", pady=2)

    # 2. The Label
    lbl = tk.Label(row_frame, text=task_name, width=20, anchor="w")
    lbl.pack(side=tk.LEFT, padx=5)

    # 3. The Action Button
    # Note: We use `t=task_name` to snapshot the text
    btn_action = tk.Button(row_frame, text="Process", 
                           command=lambda t=task_name: print(f"Processing: {t}"))
    btn_action.pack(side=tk.LEFT, padx=5)

    # 4. The Delete Button
    # Note: We use `f=row_frame` to snapshot the specific frame widget
    # This allows the button to destroy ONLY its own row.
    btn_del = tk.Button(row_frame, text="X", bg="red", fg="white",
                        command=lambda f=row_frame: f.destroy())
    btn_del.pack(side=tk.RIGHT, padx=5)

# --- GUI Setup ---
root = tk.Tk()
root.geometry("400x400")
root.title("Dynamic Row Adder")

# 1. Input Area (Top)
input_frame = tk.Frame(root, pady=10)
input_frame.pack(fill="x")

entry_box = tk.Entry(input_frame, width=30)
entry_box.pack(side=tk.LEFT, padx=10)

add_btn = tk.Button(input_frame, text="Add Task", command=add_new_row)
add_btn.pack(side=tk.LEFT)

# 2. List Container (Bottom - Scrollable area usually, but Frame for now)
list_container = tk.Frame(root)
list_container.pack(fill="both", expand=True, padx=10)

# --- Load Initial Data ---
# We just reuse the exact same function!
initial_data = ["System Update", "Firewall Check"]
for item in initial_data:
    create_task_row(item)

root.mainloop()