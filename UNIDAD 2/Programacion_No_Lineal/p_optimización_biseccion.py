import tkinter as tk
from tkinter import messagebox

def f(x):
    """Función a maximizar."""
    return 12 * x - 3 * x**4 - 2 * x**6

def df(x):
    """Primera derivada de la función."""
    return 12 * (1 - x**3 - x**5)

def bisection_method(f, df, x_lower, x_upper, epsilon=0.01):
    """Implementación del método de bisección para maximización."""
    iterations = []
    while (x_upper - x_lower) > 2 * epsilon:
        x_mid = (x_lower + x_upper) / 2
        df_mid = df(x_mid)

        # Almacenar información de la iteración actual
        iterations.append((x_lower, x_upper, x_mid, df_mid, f(x_mid)))

        if df_mid > 0:  # Óptimo está a la derecha
            x_lower = x_mid
        elif df_mid < 0:  # Óptimo está a la izquierda
            x_upper = x_mid
        else:  # Derivada es cero, se encontró el óptimo
            break

    x_opt = (x_lower + x_upper) / 2
    f_opt = f(x_opt)
    return x_opt, f_opt, iterations

def calculate():
    try:
        # Obtener valores ingresados
        x_lower = float(entry_x_lower.get())
        x_upper = float(entry_x_upper.get())
        epsilon = float(entry_epsilon.get())

        # Validaciones
        if x_lower >= x_upper:
            raise ValueError("El límite inferior debe ser menor al límite superior.")
        if epsilon <= 0:
            raise ValueError("El error permisible debe ser mayor que 0.")

        # Ejecutar método de bisección
        x_opt, f_opt, iterations = bisection_method(f, df, x_lower, x_upper, epsilon)

        # Mostrar resultados en una nueva ventana
        result_window = tk.Toplevel(root)
        result_window.title("Resultados")

        result_label = tk.Label(result_window, text=f"Óptimo aproximado x*: {x_opt:.5f}\nValor máximo f(x*): {f_opt:.5f}")
        result_label.pack(pady=10)

        iteration_label = tk.Label(result_window, text="Iteraciones:")
        iteration_label.pack()

        # Mostrar iteraciones en una lista
        iteration_text = tk.Text(result_window, height=15, width=80)
        iteration_text.pack()
        iteration_text.insert(tk.END, "Iteración\t x_lower\t x_upper\t x_mid\t\t df(x_mid)\t f(x_mid)\n")
        for i, (xl, xu, xm, dfm, fm) in enumerate(iterations):
            iteration_text.insert(tk.END, f"{i+1}\t\t {xl:.5f}\t {xu:.5f}\t {xm:.5f}\t {dfm:.5f}\t {fm:.5f}\n")
        iteration_text.config(state=tk.DISABLED)

    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Crear ventana principal
root = tk.Tk()
root.title("Método de Bisección")

# Etiquetas y entradas para parámetros
label_x_lower = tk.Label(root, text="Límite inferior (x_lower):")
label_x_lower.grid(row=0, column=0, padx=10, pady=5)
entry_x_lower = tk.Entry(root)
entry_x_lower.grid(row=0, column=1, padx=10, pady=5)
entry_x_lower.insert(0, "0")  # Valor predeterminado

label_x_upper = tk.Label(root, text="Límite superior (x_upper):")
label_x_upper.grid(row=1, column=0, padx=10, pady=5)
entry_x_upper = tk.Entry(root)
entry_x_upper.grid(row=1, column=1, padx=10, pady=5)
entry_x_upper.insert(0, "2")  # Valor predeterminado

label_epsilon = tk.Label(root, text="Error permisible (epsilon):")
label_epsilon.grid(row=2, column=0, padx=10, pady=5)
entry_epsilon = tk.Entry(root)
entry_epsilon.grid(row=2, column=1, padx=10, pady=5)
entry_epsilon.insert(0, "0.01")  # Valor predeterminado

# Botón para ejecutar el cálculo
calculate_button = tk.Button(root, text="Calcular", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

# Iniciar la interfaz gráfica
root.mainloop()
