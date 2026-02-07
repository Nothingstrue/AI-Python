import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog  # <--- YOU MUST IMPORT THIS

def ask_name():
    # This pops up a box asking for a string
    # parent=root keeps the popup on top of your main window
    name = simpledialog.askstring("Input", "What is your name?", parent=root)
    
    if name is not None and name != "":
        messagebox.showinfo("Hello", f"Welcome, {name}!")
    else:
        messagebox.showwarning("Warning", "You didn't type a name!")

def ask_budget():
    # This ensures the user only types a number
    amount = simpledialog.askfloat("Budget", "What is your budget?", parent=root)
    
    if amount is not None:
        messagebox.showinfo("Budget Set", f"Your budget is ${amount}")
    else:
        # This happens if they click Cancel
        print("User cancelled")

root = tk.Tk()
root.title("Input Boxes")
root.geometry("300x200")

tk.Button(root, text="Ask Name", command=ask_name).pack(pady=20)
tk.Button(root, text="Ask Budget", command=ask_budget).pack(pady=20)

root.mainloop()