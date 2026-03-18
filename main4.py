import tkinter as tk
from tkinter import messagebox as mb
from tkinter import *
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

x = True

# Dataset
ore_studio = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(-1, 1)
voti = np.array([4, 5, 5.5, 6, 6.5, 7.5, 8, 9])

# Suddivisione in training e test
X_train, X_test, y_train, y_test = train_test_split(
    ore_studio, voti, test_size=0.25, random_state=42
)

# Creazione e training del modello
model = LinearRegression()
model.fit(X_train, y_train)

def Predict(hour):
    global x
    # Predizione su nuovi dati
    nuove_ore = np.array([int(hour)]).reshape(-1, 1)
    predizioni_nuove = model.predict(nuove_ore)
    
    if predizioni_nuove>10:
        risultato = 10
    else:
        risultato = predizioni_nuove

    # Mostro le predizioni sul terminale
    for ore, voto in zip(nuove_ore, predizioni_nuove):
        print(f"Ore: {ore[0]} -> Voto previsto: {voto:.2f}")

    votopredict = 2 # Predizioni per disegnare la retta
    ore_plot = np.linspace(0, 9, 100).reshape(-1, 1)
    voti_predetti = model.predict(ore_plot)

    # Grafico completo
    plt.scatter(X_train, y_train, color='blue', label='Train')
    plt.scatter(X_test, y_test, color='green', label='Test')
    plt.scatter(nuove_ore, risultato, color='red', label='Nuovi dati')
    plt.plot(ore_plot, voti_predetti, color='black', label='Retta regressione')
    
    if x:
        plt.xlabel("Ore di studio")
        plt.ylabel("Voto")
        plt.title("Regressione Lineare con nuovi dati")
        plt.legend()
        x = False
    
    canvas.draw()
    
    mb.showinfo("Result", f"Your grade will be {risultato}")

def Click(*args):
    entry.delete(0, "end")

def Action():
    hours = entry.get()
    if not hours:
        mb.showwarning("Error", "Please fill the field")
    elif hours.isdigit():
        entry.delete(0, tk.END)
        entry.insert(0, "Insert hour")
        Predict(hours)
    else:
        mb.showerror("Error", "Please do not insert letters in the hour-box")

root = tk.Tk()
root.geometry("600x400")
root.title("AI")

entry_Frame = tk.Frame(root, bg="gray")
entry_Frame.pack(pady=15)

entry = tk.Entry(root, width=25, bg="white")
entry.insert(0, "Insert hour")
entry.pack()
entry.bind("<Button-1>", Click)
button = tk.Button(root, text="Predict", command=Action)
button.pack()

# Matplotlib Figure Setup
fig, ax = plt.subplots(figsize=(10, 10), dpi=100)
fig.tight_layout(pad=2)

# Embed the figure inside Tkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(fill=tk.BOTH, expand=True)

root.mainloop()
"""
Ashley  Morari
Debora Jovanchev
"""