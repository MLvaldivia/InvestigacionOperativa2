import numpy as np
from scipy.optimize import minimize
import tkinter as tk
from tkinter import messagebox

def objective_function(x):
    numerator = -2 * x[0] + x[1] + 2  
    denominator = x[0] + 3 * x[1] + 4  
    if denominator == 0:  
        return np.inf
    return numerator / denominator

def constraint1(x):
    return 4 - (-x[0] + x[1])  

def constraint2(x):
    return 14 - (2 * x[0] + 2 * x[1]) 

def constraint3(x):
    return 6 - x[1]  

def resolver_optimización():
    try:
        x1_init = float(entry_x1_init.get())  
        x2_init = float(entry_x2_init.get())  

        constraints = [
            {'type': 'ineq', 'fun': constraint1},
            {'type': 'ineq', 'fun': constraint2},
            {'type': 'ineq', 'fun': constraint3},
        ]
        
        bounds = [(0, None), (0, None)]
        
        initial_guess = [x1_init, x2_init]
        
        result = minimize(objective_function, initial_guess, method='SLSQP', bounds=bounds, constraints=constraints)
        
        if result.success:
            x1_opt, x2_opt = result.x
            
            epsilon = 1e-8
            x1_opt = 0 if abs(x1_opt) < epsilon else x1_opt
            x2_opt = 0 if abs(x2_opt) < epsilon else x2_opt

            result_label.config(text=f"Valor óptimo para x1: {x1_opt:.4f}\nValor óptimo para x2: {x2_opt:.4f}\nValor objetivo óptimo (z): {result.fun:.4f}")
            
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

ventana = tk.Tk()
ventana.title("Optimización de Costo")

tk.Label(ventana, text="Suposición inicial de las variables:").grid(row=0, column=0, columnspan=2)

tk.Label(ventana, text="x1 inicial:").grid(row=1, column=0)
entry_x1_init = tk.Entry(ventana)
entry_x1_init.grid(row=1, column=1)

tk.Label(ventana, text="x2 inicial:").grid(row=2, column=0)
entry_x2_init = tk.Entry(ventana)
entry_x2_init.grid(row=2, column=1)

resolver_btn = tk.Button(ventana, text="Resolver", command=resolver_optimización)
resolver_btn.grid(row=3, column=0, columnspan=2)

result_label = tk.Label(ventana, text="Resultados aparecerán aquí.")
result_label.grid(row=4, column=0, columnspan=2)

ventana.mainloop()
