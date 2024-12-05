import tkinter as tk
from tkinter import messagebox

def knapsack_repeated(weights, values, capacity):
    n = len(weights)
    dp = [0] * (capacity + 1)
    items_count = [0] * n  

    for w in range(1, capacity + 1):
        for i in range(n):
            if weights[i] <= w:
                if dp[w] < dp[w - weights[i]] + values[i]:
                    dp[w] = dp[w - weights[i]] + values[i]

    remaining_capacity = capacity
    while remaining_capacity > 0:
        for i in range(n):
            if weights[i] <= remaining_capacity and dp[remaining_capacity] == dp[remaining_capacity - weights[i]] + values[i]:
                items_count[i] += 1  
                remaining_capacity -= weights[i]  

    return dp[capacity], items_count

def calculate_knapsack():
    try:
        weights = []
        values = []

        for i in range(len(entry_weights)):
            weight = int(entry_weights[i].get())
            value = int(entry_values[i].get())
            weights.append(weight)
            values.append(value)

        capacity = int(entry_capacity.get())

        if len(weights) == 0:
            raise ValueError("Debe ingresar al menos un artículo.")
        
        max_value, selected_items = knapsack_repeated(weights, values, capacity)
        result_label.config(text=f"El valor máximo es: {max_value}")
        
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
        num_items = int(entry_num_items.get())
        
        if num_items <= 0:
            raise ValueError("El número de artículos debe ser mayor que cero.")
        
        for widget in frame_entries.winfo_children():
            widget.destroy()

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

root = tk.Tk()
root.title("Problema de la Mochila con Repetición")

tk.Label(root, text="Número de artículos:").pack()

entry_num_items = tk.Entry(root)
entry_num_items.pack()

create_button = tk.Button(root, text="Crear Artículos", command=create_items)
create_button.pack(pady=10)

frame_entries = tk.Frame(root)
frame_entries.pack()

tk.Label(root, text="Capacidad de la mochila:").pack()
entry_capacity = tk.Entry(root)
entry_capacity.pack()

calculate_button = tk.Button(root, text="Calcular", command=calculate_knapsack)
calculate_button.pack(pady=10)

result_label = tk.Label(root, text="El valor máximo es: ", font=("Arial", 14))
result_label.pack()

selected_items_label = tk.Label(root, text="Cantidad seleccionada para cada artículo: ", font=("Arial", 12))
selected_items_label.pack()

root.mainloop()
