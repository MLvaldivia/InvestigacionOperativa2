import numpy as np
from scipy.optimize import minimize
import tkinter as tk
from tkinter import messagebox

# Función objetivo
def objective_function(x):
    return -(10 * x[0] + 25 * x[1] - 10 * x[0]**2 - x[1]**2 - 4 * x[0] * x[1])

# Funciones de las restricciones
def constraint1(x):
    return 10 - (x[0] + 2 * x[1])

def constraint2(x):
    return 9 - (x[0] + x[1])

# Función para resolver el problema de optimización
def resolver_optimización():
    try:
        # Obtener los datos de entrada desde la interfaz de usuario
        x1_init = float(entry_x1_init.get())  # Obtener valor de x1 inicial
        x2_init = float(entry_x2_init.get())  # Obtener valor de x2 inicial

        # Definir las restricciones
        constraints = [{'type': 'ineq', 'fun': constraint1},
                       {'type': 'ineq', 'fun': constraint2}]

        # Definir los límites para las variables
        bounds = [(0, None), (0, None)]  # No se permiten valores negativos

        # Definir la suposición inicial
        initial_guess = [x1_init, x2_init]

        # Resolver el problema de optimización
        result = minimize(objective_function, initial_guess, method='SLSQP', bounds=bounds, constraints=constraints)

        # Mostrar los resultados en la interfaz
        if result.success:
            result_label.config(text=f"Valor óptimo para x1: {result.x[0]:.4f}\nValor óptimo para x2: {result.x[1]:.4f}\nValor objetivo óptimo: {-result.fun:.4f}")
        else:
            messagebox.showerror("Error", "La optimización no fue exitosa.")
    
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese valores válidos.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Optimización con Scipy")

# Etiquetas y campos de entrada para la suposición inicial
tk.Label(ventana, text="Suposición inicial de las variables:").grid(row=0, column=0, columnspan=2)

tk.Label(ventana, text="x1 inicial:").grid(row=1, column=0)
entry_x1_init = tk.Entry(ventana)
entry_x1_init.grid(row=1, column=1)

tk.Label(ventana, text="x2 inicial:").grid(row=2, column=0)
entry_x2_init = tk.Entry(ventana)
entry_x2_init.grid(row=2, column=1)

# Botón para resolver el problema
resolver_btn = tk.Button(ventana, text="Resolver", command=resolver_optimización)
resolver_btn.grid(row=3, column=0, columnspan=2)

# Etiqueta para mostrar los resultados
result_label = tk.Label(ventana, text="Resultados aparecerán aquí.")
result_label.grid(row=4, column=0, columnspan=2)

# Ejecutar la interfaz gráfica
ventana.mainloop()
