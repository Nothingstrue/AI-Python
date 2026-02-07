import tkinter as tk

# --- Global Data ---
# This is the "State" of your application
my_data = ["Server 1", "Server 2"]

# --- Page Logic ---

def show_main_menu():
    """Hides the list frame and shows the main menu"""
    list_frame.pack_forget()
    main_menu_frame.pack(fill="both", expand=True)

def show_list_page():
    """Refreshes the data, hides main menu, shows list frame"""
    
    # 1. CLEAN THE SLATE
    # Destroy every widget currently inside list_frame
    for widget in list_frame.winfo_children():
        widget.destroy()

    # 2. REBUILD THE UI FROM DATA
    # Add a title
    title_lbl = tk.Label(list_frame, text="Active Servers List", font=("Arial", 14, "bold"), pady=10)
    title_lbl.pack()

    # Loop through the global data and create rows
    for item in my_data:
        # --- FIXED SECTION START ---
        # Create the row frame inside 'list_frame' (the correct parent)
        row_frame = tk.Frame(list_frame, bd=1, relief="solid", pady=5)
        row_frame.pack(fill="x", padx=10, pady=2)
        # --- FIXED SECTION END ---
        
        lbl = tk.Label(row_frame, text=item, width=20, anchor="w")
        lbl.pack(side=tk.LEFT, padx=5)
        
        # Dynamic Button 1
        btn1 = tk.Button(row_frame, text="Ping", 
                         command=lambda x=item: print(f"Pinging {x}"))
        btn1.pack(side=tk.LEFT)
        
        # Dynamic Button 2
        btn2 = tk.Button(row_frame, text="Kill", bg="#ffcccc",
                         command=lambda x=item: print(f"Killing {x}"))
        btn2.pack(side=tk.LEFT, padx=5)

    # 3. Add the Back Button
    back_btn = tk.Button(list_frame, text="<< Back to Main Menu", command=show_main_menu)
    back_btn.pack(pady=20)

    # 4. SWITCH FRAMES
    main_menu_frame.pack_forget()
    list_frame.pack(fill="both", expand=True)

def add_dummy_data():
    """Adds an item to the list so you can see the change"""
    my_data.append(f"Server {len(my_data) + 1}")
    print(f"Data Added. List is now: {my_data}")

# --- Setup Main Window ---
root = tk.Tk()
root.geometry("400x500")
root.title("Auto-Refresh Frame")

# --- Create the Two Main Frames ---
main_menu_frame = tk.Frame(root, bg="lightblue")
list_frame = tk.Frame(root) # This stays empty until we "show" it

# --- Setup Main Menu Content (Static) ---
tk.Label(main_menu_frame, text="Main Menu", font=("Arial", 20)).pack(pady=50)

# Button to modify data (to prove the refresh works)
tk.Button(main_menu_frame, text="Add New Server (Simulate Data)", 
          command=add_dummy_data, height=2, bg="white").pack(pady=10)

# Button to navigate
tk.Button(main_menu_frame, text="Go to List View >", 
          command=show_list_page, height=2, bg="lightgreen").pack(pady=10)

# Start logic
main_menu_frame.pack(fill="both", expand=True)
root.mainloop()