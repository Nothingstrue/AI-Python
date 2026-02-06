import tkinter as tk
from tkinter import messagebox
users = []
money = []
"""def submit_data():
    usr_input = entry_box.get()
    print(f"You wrote {usr_input}")
    entry_box.delete(0, tk.END)"""
def SubmitButton():
    users.append(userbox.get())
    money.append(moneybox.get())
    userbox.delete(0, tk.END)
    moneybox.delete(0, tk.END)
def Exit_action():
    root.destroy()
def show_page_2():
    home.pack_forget()
    newuser.pack(fill="both", expand=True)
def show_page_1():
    newuser.pack_forget()
    home.pack(fill="both", expand=True)
root = tk.Tk()
root.title("Try")
root.geometry("300x200")
"""entry_box = tk.Entry(root, width=25, bg="white", fg="black")
entry_box.pack(pady=5)
submit_btn = tk.Button(root, text="Submit", command=submit_data)
submit_btn.pack(pady=10)"""
home = tk.Frame(root, bg="lightblue")
tk.Label(home, text="Resort 'La Sfera'\nWelcome", bg="lightblue", font=("Arial", 16)).pack(pady=20)
tk.Button(home, text="Insert a new user in the travel plan", command=show_page_2).pack()
tk.Button(home, text="Exit", command=Exit_action).pack()
newuser = tk.Frame(root, bg="lightgreen")
tk.Label(newuser, text="This is Page 2", bg="lightgreen", font=("Arial", 16)).pack(pady=20)
userbox = tk.Entry(newuser, width=25, bg="white")
userbox.pack(pady=5)
moneybox = tk.Entry(newuser, width=25, bg="white")
moneybox.pack(pady=5)
submitbutton = tk.Button(newuser, text="Submit new user", command=SubmitButton)
submitbutton.pack(pady=10)
tk.Button(newuser, text="Back to Main Page", command=show_page_1).pack()
home.pack(fill="both", expand=True)
root.mainloop()

print(f"""{users[0]}
{money[0]}""")