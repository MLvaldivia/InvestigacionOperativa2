import cvxopt
import tkinter as tk
from tkinter import messagebox

# Función para resolver el problema de programación lineal
def resolver_optimización():
    try:
        # Obtener los datos de entrada
        c1 = float(entry_c1.get())
        c2 = float(entry_c2.get())
        g11 = float(entry_g11.get())
        g12 = float(entry_g12.get())
        g21 = float(entry_g21.get())
        g22 = float(entry_g22.get())
        h1 = float(entry_h1.get())
        h2 = float(entry_h2.get())

        # Coeficientes de la función objetivo (4x1 + 3x2)
        c = cvxopt.matrix([-c1, -c2])  # Negamos los coeficientes porque cvxopt minimiza, no maximiza.

        # Matrices de las restricciones
        G = cvxopt.matrix([[g11, g12],  # 2x1 + x2 <= 10
                           [g21, g22]])  # x1 + 3x2 <= 15

        h = cvxopt.matrix([h1, h2])  # Lado derecho de las restricciones

        # Resolución del problema
        sol = cvxopt.solvers.lp(c, G, h)

        # Mostrar la solución en la interfaz
        result_label.config(text=f"Solución óptima:\nx1 (Producto A): {sol['x'][0]}\nx2 (Producto B): {sol['x'][1]}")
    
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese todos los valores correctamente.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Optimización Lineal")

# Etiquetas y campos de entrada para los coeficientes de la función objetivo
tk.Label(ventana, text="Coeficientes de la función objetivo:").grid(row=0, column=0, columnspan=2)

tk.Label(ventana, text="c1:").grid(row=1, column=0)
entry_c1 = tk.Entry(ventana)
entry_c1.grid(row=1, column=1)

tk.Label(ventana, text="c2:").grid(row=2, column=0)
entry_c2 = tk.Entry(ventana)
entry_c2.grid(row=2, column=1)

# Etiquetas y campos de entrada para las matrices de restricciones
tk.Label(ventana, text="Restricciones:").grid(row=3, column=0, columnspan=2)

tk.Label(ventana, text="g11:").grid(row=4, column=0)
entry_g11 = tk.Entry(ventana)
entry_g11.grid(row=4, column=1)

tk.Label(ventana, text="g12:").grid(row=5, column=0)
entry_g12 = tk.Entry(ventana)
entry_g12.grid(row=5, column=1)

tk.Label(ventana, text="g21:").grid(row=6, column=0)
entry_g21 = tk.Entry(ventana)
entry_g21.grid(row=6, column=1)

tk.Label(ventana, text="g22:").grid(row=7, column=0)
entry_g22 = tk.Entry(ventana)
entry_g22.grid(row=7, column=1)

tk.Label(ventana, text="h1:").grid(row=8, column=0)
entry_h1 = tk.Entry(ventana)
entry_h1.grid(row=8, column=1)

tk.Label(ventana, text="h2:").grid(row=9, column=0)
entry_h2 = tk.Entry(ventana)
entry_h2.grid(row=9, column=1)

# Botón para resolver el problema
resolver_btn = tk.Button(ventana, text="Resolver", command=resolver_optimización)
resolver_btn.grid(row=10, column=0, columnspan=2)

# Etiqueta para mostrar los resultados
result_label = tk.Label(ventana, text="Solución óptima: ")
result_label.grid(row=11, column=0, columnspan=2)

# Ejecutar la interfaz gráfica
ventana.mainloop()
