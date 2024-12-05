import numpy as np
from scipy.optimize import minimize
import tkinter as tk
from tkinter import messagebox

# Función objetivo fraccionaria
def objective_function(x):
    numerator = -2 * x[0] + x[1] + 2  # Numerador
    denominator = x[0] + 3 * x[1] + 4  # Denominador
    if denominator == 0:  # Evitar división por cero
        return np.inf
    return numerator / denominator

# Definir las restricciones
def constraint1(x):
    return 4 - (-x[0] + x[1])  # Restricción 1: -x1 + x2 <= 4

def constraint2(x):
    return 14 - (2 * x[0] + 2 * x[1])  # Restricción 2: 2*x1 + 2*x2 <= 14

def constraint3(x):
    return 6 - x[1]  # Restricción 3: x2 <= 6

# Función para resolver el problema de optimización
def resolver_optimización():
    try:
        # Obtener los valores de entrada desde la interfaz de usuario
        x1_init = float(entry_x1_init.get())  # Obtener valor de x1 inicial
        x2_init = float(entry_x2_init.get())  # Obtener valor de x2 inicial

        # Definir las restricciones
        constraints = [
            {'type': 'ineq', 'fun': constraint1},
            {'type': 'ineq', 'fun': constraint2},
            {'type': 'ineq', 'fun': constraint3},
        ]
        
        # Límites para las variables (x1 >= 0, x2 >= 0)
        bounds = [(0, None), (0, None)]
        
        # Suposición inicial
        initial_guess = [x1_init, x2_init]
        
        # Resolver el problema de optimización
        result = minimize(objective_function, initial_guess, method='SLSQP', bounds=bounds, constraints=constraints)
        
        # Mostrar los resultados en la interfaz
        if result.success:
            x1_opt, x2_opt = result.x
            
            # Establecer un umbral para valores cercanos a 0
            epsilon = 1e-8
            x1_opt = 0 if abs(x1_opt) < epsilon else x1_opt
            x2_opt = 0 if abs(x2_opt) < epsilon else x2_opt

            # Mostrar resultados
            result_label.config(text=f"Valor óptimo para x1: {x1_opt:.4f}\nValor óptimo para x2: {x2_opt:.4f}\nValor objetivo óptimo (z): {result.fun:.4f}")
            
            # Interpretación del resultado
            if x1_opt > 0 and x2_opt == 0:
                result_label.config(text=result_label.cget("text") + "\nRecomendación: Para optimizar su eficiencia operativa minimizando el costo por unidad transportada, se debe optar por el vehículo de tipo 1.")
            elif x2_opt > 0 and x1_opt == 0:
                result_label.config(text=result_label.cget("text") + "\nRecomendación: Para optimizar su eficiencia operativa, se debe optar por el vehículo de tipo 2.")
            else:
                result_label.config(text=result_label.cget("text") + "\nRecomendación: Usar una combinación de ambos vehículos para optimizar el costo.")
        else:
            messagebox.showerror("Error", "No se encontró una solución óptima.")
    
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese valores válidos.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Optimización de Costo")

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
