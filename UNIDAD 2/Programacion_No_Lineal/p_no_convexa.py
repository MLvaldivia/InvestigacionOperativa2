import tkinter as tk
from tkinter import messagebox
import sympy as sp
from scipy.optimize import minimize

x = sp.symbols('x')
objective_function = (x - 1) * (x - 2) * (x - 3) * (x - 4) * (x - 5)
objective_func = sp.lambdify(x, objective_function, 'numpy')

def optimizar():
    try:
        a = float(entry_a.get())  
        b = float(entry_b.get())  
        initial_guess = float(entry_initial_guess.get()) 
        
        bounds = [(a, b)]
        
        result = minimize(objective_func, [initial_guess], bounds=bounds)
        
        if result.success:
            label_result.config(text=f"Valor óptimo para x: {result.x[0]:.4f}\nValor objetivo óptimo: {result.fun:.4f}")
        else:
            label_result.config(text="No se pudo encontrar el mínimo.")
    except ValueError as e:
        messagebox.showerror("Error", f"Entrada inválida: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")

ventana = tk.Tk()
ventana.title("Optimización - Función de Costo")

label_a = tk.Label(ventana, text="Valor de a (extremo inferior):")
label_a.pack()

entry_a = tk.Entry(ventana, width=20)
entry_a.insert(0, "1")  # Valor por defecto
entry_a.pack()

label_b = tk.Label(ventana, text="Valor de b (extremo superior):")
label_b.pack()

entry_b = tk.Entry(ventana, width=20)
entry_b.insert(0, "5")  
entry_b.pack()

label_initial_guess = tk.Label(ventana, text="Valor inicial (x):")
label_initial_guess.pack()

entry_initial_guess = tk.Entry(ventana, width=20)
entry_initial_guess.insert(0, "3") 
entry_initial_guess.pack()

boton_optimizar = tk.Button(ventana, text="Optimizar", command=optimizar)
boton_optimizar.pack()

label_result = tk.Label(ventana, text="Resultado:")
label_result.pack()

ventana.mainloop()
