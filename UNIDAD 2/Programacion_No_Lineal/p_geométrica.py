import numpy as np
import tkinter as tk
from tkinter import messagebox
from scipy.optimize import minimize

def objetivo(x):
    return -(3*x[0] + 4*x[1])  

def restriccion1(x):
    return 10 - (2*x[0] + x[1]) 

def restriccion2(x):
    return 12 - (x[0] + 3*x[1])  
    
def restriccion_no_neg(x):
    return [x[0], x[1]]  

def resolver():
    try:
        x1_inicial = float(entry_x1_inicial.get())
        x2_inicial = float(entry_x2_inicial.get())

        x_inicial = [x1_inicial, x2_inicial]

        restricciones = [{'type': 'ineq', 'fun': restriccion1}, 
                        {'type': 'ineq', 'fun': restriccion2},
                        {'type': 'ineq', 'fun': restriccion_no_neg}]

        resultado = minimize(objetivo, x_inicial, constraints=restricciones)

        if resultado.success:
            label_resultado.config(text=f"Óptimo alcanzado en: {resultado.x}")
            label_valor.config(text=f"Valor óptimo de la función objetivo: {-resultado.fun}")
        else:
            messagebox.showerror("Error", "No se pudo encontrar una solución óptima.")
    
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores válidos.")

root = tk.Tk()
root.title("Optimización con Programación Geométrica")

label_x1_inicial = tk.Label(root, text="Valor inicial de x1:")
label_x1_inicial.grid(row=0, column=0, padx=10, pady=10)

entry_x1_inicial = tk.Entry(root)
entry_x1_inicial.grid(row=0, column=1, padx=10, pady=10)

label_x2_inicial = tk.Label(root, text="Valor inicial de x2:")
label_x2_inicial.grid(row=1, column=0, padx=10, pady=10)

entry_x2_inicial = tk.Entry(root)
entry_x2_inicial.grid(row=1, column=1, padx=10, pady=10)

boton_resolver = tk.Button(root, text="Resolver", command=resolver)
boton_resolver.grid(row=2, column=0, columnspan=2, pady=20)

label_resultado = tk.Label(root, text="Resultado:")
label_resultado.grid(row=3, column=0, columnspan=2, pady=5)

label_valor = tk.Label(root, text="Valor de la función objetivo:")
label_valor.grid(row=4, column=0, columnspan=2, pady=5)

root.mainloop()
