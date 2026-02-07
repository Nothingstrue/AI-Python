import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
users = ["Gabriele"]
money = [12]

def Submit_Button():
    name = user_box.get()
    money1 = money_box.get()
    if not name or not money1:
        messagebox.showwarning("Error", "Please fill in both fields.")
    elif money1.isdigit():
        users.append(name)
        money.append(int(money1))
        user_box.delete(0, tk.END)
        money_box.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Please do not insert letters in the budget box")

def Exit_Action():
    root.destroy()

def New_User_Page():
    home.pack_forget()
    new_user.pack(fill="both", expand=True)

def Back_Home():
    new_user.pack_forget()
    modify_user.pack_forget()
    for widget in modify_user.winfo_children():
        widget.destroy()
    home.pack(fill="both", expand=True)

def Reload_Dynamic_List():
    for widget in modify_user.winfo_children():
        widget.destroy()
    
    for i in range(len(users)):
        dynamic_list = tk.Frame(modify_user, bg="orange", pady=5)
        dynamic_list.pack(fill="x")
        user_label = tk.Label(dynamic_list, text=f"Name:{users[i]}   Budget:{money[i]}", bg="orange", font=("Arial", 12), anchor="w")
        user_label.pack(side=tk.LEFT, padx=20) 
        delete_button = tk.Button(dynamic_list, text="Delete", command=lambda x=i : Delete_User(x))
        delete_button.pack(side=tk.RIGHT, padx=10)
        modify_money_button = tk.Button(dynamic_list, text="Modify Money", command=lambda x=i : Modify_Money(x))
        modify_username_button = tk.Button(dynamic_list, text="Modify User", command=lambda x=i : Modify_Username(x))
        modify_username_button.pack(side=tk.RIGHT)
    
    tk.Label(modify_user, text=f"Total Budget:\n{sum(money)}", bg="orange", font=("Arial", 12)).pack(padx=10)
    
    tk.Button(modify_user, text="Back Home", command=Back_Home).pack(pady=10)

def Modify_Username(x):
    users[x] = simpledialog.askstring("Modify", "Modify the name", parent=root)
    Reload_Dynamic_List()
    
def Modify_Money(x):
    money[x] = simpledialog.askstring("Modify", "Modify the budget", parent=root)
    Reload_Dynamic_List()

def Delete_User(x):
    del users[x]
    del money[x]
    Reload_Dynamic_List()

def Modify_Users_Page():
    home.pack_forget()
    Reload_Dynamic_List()
    modify_user.pack(fill="both", expand=True)

root = tk.Tk()
root.title("Try")
root.geometry("600x400")

home = tk.Frame(root, bg="lightblue")
tk.Label(home, text="Resort 'La sfera'\nWelcome", bg="lightblue", font=("Arial", 16)).pack(pady=20)
tk.Button(home, text="Insert a new user in the travel plan", command=New_User_Page).pack(pady=5)
tk.Button(home, text="Check your budget and your friends", command=Modify_Users_Page).pack(pady=5)
tk.Button(home, text="Exit", command=Exit_Action).pack(pady=5)

new_user = tk.Frame(root, bg="lightgreen")
tk.Label(new_user, text="Insert the name of the guest", bg="lightgreen", font=("Arial", 12)).pack()
user_box = tk.Entry(new_user, width=25, bg="white")
user_box.pack(pady=5)
tk.Label(new_user, text="Insert the budget of the guest", bg="lightgreen", font=("Arial", 12)).pack()
money_box = tk.Entry(new_user, width=25, bg="white")
money_box.pack(pady=5)
submit_button = tk.Button(new_user, text="Submit new user", command=Submit_Button).pack(pady=10)
tk.Button(new_user, text="Back to Main Page", command=Back_Home).pack()

modify_user = tk.Frame(root, bg="orange")

home.pack(fill="both", expand=True)
root.mainloop()