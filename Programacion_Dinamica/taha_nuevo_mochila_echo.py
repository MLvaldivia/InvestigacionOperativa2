import tkinter as tk
from tkinter import messagebox

def knapsack_repeated(weights, values, capacity):
    n = len(weights)
    dp = [0] * (capacity + 1)
    items_count = [0] * n  # Para almacenar la cantidad de veces seleccionados

    # Llenar la tabla dp con la versión de mochila con repetición
    for w in range(1, capacity + 1):
        for i in range(n):
            if weights[i] <= w:
                # Solo actualizamos si obtenemos un valor mayor
                if dp[w] < dp[w - weights[i]] + values[i]:
                    dp[w] = dp[w - weights[i]] + values[i]

    # Recuperamos la cantidad de cada artículo seleccionado
    remaining_capacity = capacity
    while remaining_capacity > 0:
        for i in range(n):
            if weights[i] <= remaining_capacity and dp[remaining_capacity] == dp[remaining_capacity - weights[i]] + values[i]:
                items_count[i] += 1  # Incrementamos la cantidad de este artículo
                remaining_capacity -= weights[i]  # Reducimos la capacidad

    return dp[capacity], items_count

def calculate_knapsack():
    try:
        # Obtener los pesos, valores y capacidad
        weights = []
        values = []

        for i in range(len(entry_weights)):
            weight = int(entry_weights[i].get())
            value = int(entry_values[i].get())
            weights.append(weight)
            values.append(value)

        capacity = int(entry_capacity.get())

        # Verificar que haya al menos un artículo
        if len(weights) == 0:
            raise ValueError("Debe ingresar al menos un artículo.")
        
        # Calcular el resultado
        max_value, selected_items = knapsack_repeated(weights, values, capacity)
        result_label.config(text=f"El valor máximo es: {max_value}")
        
        # Mostrar los artículos seleccionados
        selected_items_text = []
        for i, count in enumerate(selected_items):
            selected_items_text.append(f"x{i+1} = {count}")
        
        selected_items_label.config(text="Cantidad seleccionada para cada artículo: " + ", ".join(selected_items_text))
        
    except ValueError as ve:
        messagebox.showerror("Error", f"Entrada no válida: {ve}")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")

def create_items():
    try:
        # Obtener el número de artículos
        num_items = int(entry_num_items.get())
        
        # Verificar que haya al menos un artículo
        if num_items <= 0:
            raise ValueError("El número de artículos debe ser mayor que cero.")
        
        # Limpiar entradas previas
        for widget in frame_entries.winfo_children():
            widget.destroy()

        # Crear nuevas entradas para pesos y valores
        global entry_weights, entry_values
        entry_weights = []
        entry_values = []

        for i in range(num_items):
            tk.Label(frame_entries, text=f"Artículo {i + 1} - Peso:").grid(row=i, column=0)
            weight_entry = tk.Entry(frame_entries)
            weight_entry.grid(row=i, column=1)
            entry_weights.append(weight_entry)

            tk.Label(frame_entries, text=f"Artículo {i + 1} - Valor:").grid(row=i, column=2)
            value_entry = tk.Entry(frame_entries)
            value_entry.grid(row=i, column=3)
            entry_values.append(value_entry)

    except ValueError as ve:
        messagebox.showerror("Error", f"Entrada no válida: {ve}")

# Crear la ventana principal
root = tk.Tk()
root.title("Problema de la Mochila con Repetición")

# Etiqueta para número de artículos
tk.Label(root, text="Número de artículos:").pack()

entry_num_items = tk.Entry(root)
entry_num_items.pack()

# Botón para crear los artículos
create_button = tk.Button(root, text="Crear Artículos", command=create_items)
create_button.pack(pady=10)

# Frame para ingresar peso y valor de cada artículo
frame_entries = tk.Frame(root)
frame_entries.pack()

# Etiqueta y campo para la capacidad de la mochila
tk.Label(root, text="Capacidad de la mochila:").pack()
entry_capacity = tk.Entry(root)
entry_capacity.pack()

# Botón para calcular el resultado
calculate_button = tk.Button(root, text="Calcular", command=calculate_knapsack)
calculate_button.pack(pady=10)

# Etiqueta para mostrar el resultado
result_label = tk.Label(root, text="El valor máximo es: ", font=("Arial", 14))
result_label.pack()

# Etiqueta para mostrar los artículos seleccionados
selected_items_label = tk.Label(root, text="Cantidad seleccionada para cada artículo: ", font=("Arial", 12))
selected_items_label.pack()

# Iniciar la aplicación
root.mainloop()
