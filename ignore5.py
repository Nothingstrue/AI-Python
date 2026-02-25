import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def plot_function(event=None):
    """Evaluates the user's input and updates the plot."""
    func_str = entry.get()
    
    # Replace common math notation '^' with Python's power operator '**'
    func_str = func_str.replace('^', '**')
    
    # Generate X values from -10 to 10
    x = np.linspace(-10, 10, 1000)
    
    # A safe dictionary of mathematical functions so we don't need "np." prefixes
    safe_dict = {
        'x': x,
        'sin': np.sin, 'cos': np.cos, 'tan': np.tan,
        'arcsin': np.arcsin, 'arccos': np.arccos, 'arctan': np.arctan,
        'exp': np.exp, 'log': np.log, 'log10': np.log10,
        'sqrt': np.sqrt, 'abs': np.abs,
        'pi': np.pi, 'e': np.e
    }
    
    try:
        # Evaluate the string using only our safe dictionary
        y = eval(func_str, {"__builtins__": None}, safe_dict)
        
        # Handle cases where the function is a constant (e.g., user inputs "5")
        if isinstance(y, (int, float)):
            y = np.full_like(x, y)
            
        # Clear the old plot and draw the new one
        ax.clear()
        ax.plot(x, y, label=f'y = {func_str.replace("**", "^")}', color='#1f77b4')
        
        # Format the graph
        ax.axhline(0, color='black', linewidth=1)
        ax.axvline(0, color='black', linewidth=1)
        ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
        ax.set_title("Function Graph", pad=10)
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.legend()
        
        # Set dynamic Y limits to prevent extreme asymptotes (like tan(x)) from ruining the view
        y_min, y_max = np.nanmin(y), np.nanmax(y)
        if y_max - y_min > 100:
            ax.set_ylim(-20, 20)
            
        canvas.draw()
        
    except Exception as e:
        messagebox.showerror("Invalid Input", f"Could not plot the function.\n\nError: {e}\n\nMake sure to use proper syntax, like '2*x' instead of '2x'.")

# --- UI Setup ---
root = tk.Tk()
root.title("Math Function Plotter")
root.geometry("650x550")

# Input Frame
input_frame = tk.Frame(root)
input_frame.pack(pady=15)

tk.Label(input_frame, text="f(x) = ", font=("Arial", 14)).pack(side=tk.LEFT)

entry = tk.Entry(input_frame, width=30, font=("Arial", 14))
entry.pack(side=tk.LEFT, padx=5)
entry.insert(0, "sin(x) + x^2/10")
entry.bind("<Return>", plot_function) # Allow plotting by pressing Enter

btn = tk.Button(input_frame, text="Plot", font=("Arial", 12), command=plot_function, bg="#4CAF50", fg="white")
btn.pack(side=tk.LEFT, padx=5)

# Matplotlib Figure Setup
fig, ax = plt.subplots(figsize=(6, 4), dpi=100)
fig.tight_layout(pad=2)

# Embed the figure inside Tkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(fill=tk.BOTH, expand=True)

# Generate the initial plot
plot_function()

# Start the application
root.mainloop()