import numpy as np
from scipy.optimize import linprog
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox

# Función para resolver la optimización con linprog
def resolver_optimización():
    try:
        # Obtener los valores de entrada desde la interfaz de usuario
        f1_values_input = [float(val) for val in entry_f1_values.get().split(',')]
        A_input = [list(map(float, row.split(','))) for row in entry_A.get().split(';')]
        b_input = [float(val) for val in entry_b.get().split(',')]
        Aeq_input = [float(val) for val in entry_Aeq.get().split(',')]
        beq_input = [float(val) for val in entry_beq.get().split(',')]

        # Asegurarse de que las entradas sean válidas
        if len(f1_values_input) != 9 or len(A_input) != 4 or len(A_input[0]) != 10:
            messagebox.showerror("Error", "Verifique las dimensiones de las matrices de entrada.")
            return

        # Concatenar los valores de la función objetivo
        f = np.concatenate([f1_values_input, [-1]])

        # Resolver el problema de optimización
        result = linprog(c=f, A_ub=np.array(A_input), b_ub=np.array(b_input), A_eq=np.array([Aeq_input]), b_eq=np.array(beq_input), bounds=[(0, 8)] * 9 + [(0, 4)], method='highs')

        # Calcular x1 y x2 óptimos
        x1_optimal = sum(i * result.x[i] for i in range(9))  # x1 se calcula como combinación lineal
        x2_optimal = result.x[9]  # x2 es el último valor en result.x
        optimal_value = result.fun  # Valor de la función objetivo óptimo

        # Mostrar los resultados en la interfaz
        result_label.config(text=f"Valor calculado de x1: {x1_optimal:.4f}\nValor calculado de x2: {x2_optimal:.4f}\nValor óptimo de la función objetivo: {optimal_value:.4f}")

        # Graficar la región factible
        x1_range = np.linspace(0, 8, 100)
        x2_range_1 = (24 - 2 * x1_range) / 3
        x2_range_2 = (15 - x1_range) / 2
        x2_range_3 = (24 - 3 * x1_range) / 2

        plt.plot(x1_range, x2_range_1, label=r'$2x_1 + 3x_2 \leq 24$')
        plt.plot(x1_range, x2_range_2, label=r'$x_1 + 2x_2 \leq 15$')
        plt.plot(x1_range, x2_range_3, label=r'$3x_1 + 2x_2 \leq 24$')

        plt.fill_between(x1_range, 0, np.minimum(np.minimum(x2_range_1, x2_range_2), x2_range_3), color='gray', alpha=0.5)
        plt.xlim(0, 8)
        plt.ylim(0, 4)
        plt.xlabel('$x_1$')
        plt.ylabel('$x_2$')
        plt.legend()
        plt.title('Región factible')
        plt.grid(True)
        plt.show()

    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese valores válidos.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Optimización con linprog")

# Etiquetas y campos de entrada para la suposición inicial
tk.Label(ventana, text="Valores de f1(x1): (Separados por comas)").grid(row=0, column=0, columnspan=2)
entry_f1_values = tk.Entry(ventana)
entry_f1_values.grid(row=0, column=2)

tk.Label(ventana, text="Matriz A (filas separadas por ; y columnas por ,)").grid(row=1, column=0, columnspan=2)
entry_A = tk.Entry(ventana)
entry_A.grid(row=1, column=2)

tk.Label(ventana, text="Lados derechos b (separados por comas)").grid(row=2, column=0, columnspan=2)
entry_b = tk.Entry(ventana)
entry_b.grid(row=2, column=2)

tk.Label(ventana, text="Restricción de igualdad Aeq (separados por comas)").grid(row=3, column=0, columnspan=2)
entry_Aeq = tk.Entry(ventana)
entry_Aeq.grid(row=3, column=2)

tk.Label(ventana, text="Lado derecho de Aeq (beq, separados por comas)").grid(row=4, column=0, columnspan=2)
entry_beq = tk.Entry(ventana)
entry_beq.grid(row=4, column=2)

# Botón para resolver el problema
resolver_btn = tk.Button(ventana, text="Resolver", command=resolver_optimización)
resolver_btn.grid(row=5, column=0, columnspan=2)

# Etiqueta para mostrar los resultados
result_label = tk.Label(ventana, text="Resultados aparecerán aquí.")
result_label.grid(row=6, column=0, columnspan=3)

# Ejecutar la interfaz gráfica
ventana.mainloop()
