import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
users = ["Gabriele"]
money = [12]
vacation = ["Cheap", "Standard", "Premium", "VIP"]
cost = [300, 500, 2000, 2000000]

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
    travel_selection.pack_forget()
    for widget in modify_user.winfo_children():
        widget.destroy()
    home.pack(fill="both", expand=True)

def Reload_Dynamic_List():
    for widget in modify_user.winfo_children():
        widget.destroy()
    if len(users)>0:
        for i in range(len(users)):
            dynamic_list = tk.Frame(modify_user, bg="orange", pady=5)
            dynamic_list.pack(fill="x")
            user_label = tk.Label(dynamic_list, text=f"Name:{users[i]}   Budget:{money[i]}", bg="orange", font=("Arial", 12), anchor="w")
            user_label.pack(side=tk.LEFT, padx=20) 
            delete_button = tk.Button(dynamic_list, text="Delete", command=lambda temp=i : Delete_User(temp))
            delete_button.pack(side=tk.RIGHT, padx=10)
            modify_money_button = tk.Button(dynamic_list, text="Modify Money", command=lambda temp=i : Modify_Money(temp))
            modify_money_button.pack(side=tk.RIGHT)
            modify_username_button = tk.Button(dynamic_list, text="Modify User", command=lambda temp=i : Modify_Username(temp))
            modify_username_button.pack(side=tk.RIGHT, padx=10)
        
        tk.Label(modify_user, text=f"Total Budget:\n{sum(money)}", bg="orange", font=("Arial", 12)).pack(padx=10)
    else:
        tk.Label(modify_user, text="There are no user registrated yet", bg="orange", font=("Arial", 12)).pack(pady=10)
    
    tk.Button(modify_user, text="Back Home", command=Back_Home).pack(pady=10)

def Modify_Username(x):
    temp = None
    i = 0
    while not temp:
        if i>0:
            messagebox.showwarning("Error", "Please fill the box")
        temp = simpledialog.askstring("Modify", "Modify the name", parent=root)
        i = i + 1
    users[x] = temp
    Reload_Dynamic_List()
    
def Modify_Money(x):
    temp = "hell"
    i = 0
    while not temp or not temp.isdigit():
        if i>0 and not temp:
            messagebox.showwarning("Error", "Please fill the box")
        elif i>0 and not temp.isdigit():
            messagebox.showerror("Error", "Please do not insert letters in the budget box")
        temp = simpledialog.askstring("Modify", "Modify the budget", parent=root)
        i = i+1
    money[x] = int(temp)
    Reload_Dynamic_List()

def Delete_User(x):
    del users[x]
    del money[x]
    Reload_Dynamic_List()

def Modify_Users_Page():
    home.pack_forget()
    Reload_Dynamic_List()
    modify_user.pack(fill="both", expand=True)
    
def Finish_Page():
    home.pack_forget()
    travel_selection.pack(fill="both", expand=True)
    
def Select_Vacation(x):
    if sum(money) >= cost[x]:
        temp = messagebox.askyesno("Selection", f"Are you sure you want to select the {vacation[x]} package?", parent=root)
        if temp:
            messagebox.showinfo("Confirmation", f"Your vacation has been successfuly selected\nSelected package: {vacation[x]} Cost: {cost[x]}", parent=root)
    else:
        messagebox.showwarning("Cost", f"You don't have enough budget for this package\nCurrent budget: {sum(money)}\nCost of the package: {cost[x]}", parent=root)

root = tk.Tk()
root.title("Try")
root.geometry("600x400")

home = tk.Frame(root, bg="lightblue")
tk.Label(home, text="Resort 'La sfera'\nWelcome", bg="lightblue", font=("Arial", 16)).pack(pady=20)
tk.Button(home, text="Insert a new user in the travel plan", command=New_User_Page).pack(pady=5)
tk.Button(home, text="Check your budget and your friends", command=Modify_Users_Page).pack(pady=5)
tk.Button(home, text="Finalize your vacation", command=Finish_Page).pack(pady=5)
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

travel_selection = tk.Frame(root, bg="#EE3F3F")
for i in range(len(vacation)):
    delete_button = tk.Button(travel_selection, text=vacation[i], command=lambda temp=i : Select_Vacation(temp))
    delete_button.pack(side=tk.LEFT, padx=10, expand=True)
tk.Button(travel_selection, text="Return Home", command=Back_Home).pack(pady=20, side=tk.BOTTOM, anchor="center")

home.pack(fill="both", expand=True)
root.mainloop()