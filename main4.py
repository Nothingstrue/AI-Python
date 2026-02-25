import tkinter as tk
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np

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

# Predizione su nuovi dati
nuove_ore = np.array([2.5, 5.5, 9]).reshape(-1, 1)
predizioni_nuove = model.predict(nuove_ore)

# Mostro le predizioni sul terminale
for ore, voto in zip(nuove_ore, predizioni_nuove):
    print(f"Ore: {ore[0]} -> Voto previsto: {voto:.2f}")

votopredict = # Predizioni per disegnare la retta
ore_plot = np.linspace(0, 9, 100).reshape(-1, 1)
voti_predetti = model.predict(ore_plot)

# Grafico completo
plt.scatter(X_train, y_train, color='blue', label='Train')
plt.scatter(X_test, y_test, color='green', label='Test')
plt.scatter(nuove_ore, predizioni_nuove, color='red', label='Nuovi dati')
plt.plot(ore_plot, voti_predetti, color='black', label='Retta regressione')

plt.xlabel("Ore di studio")
plt.ylabel("Voto")
plt.title("Regressione Lineare con nuovi dati")
plt.legend()
plt.show()

def Action():
    name = button.get()
    if not name:
        mb.showwarning("Error", "Please fill the field")
    elif name.isdigit():
        entry.delete(0, tk.END)
    else:
        mb.showerror("Error", "Please do not insert letters in the budget box")

root = tk.Tk()
root.geometry("600x400")
root.title("AI")

entry = tk.Entry(root, width=25, bg="white")
button = tk.Button(root, text="Predict", command=Action).pack()

root.mainloop()

"""
Ashley  Morari
Debora Jovanchev
"""