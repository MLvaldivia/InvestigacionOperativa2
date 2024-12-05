import tkinter as tk
from tkinter import messagebox
import math

def calculate_total_cost(demand, cost_of_ordering, carrying_cost_percentage, ranges):
    """
    Calcular el costo total anual para diferentes tamaños de pedido basados en los rangos de descuento.
    """
    best_quantity = None
    best_cost = float('inf')

    ranges.sort(key=lambda x: x['min_quantity'])

    for discount_range in ranges:
        min_quantity = discount_range['min_quantity']
        max_quantity = discount_range['max_quantity']
        price_per_unit = discount_range['price_per_unit']
        carrying_cost = carrying_cost_percentage * price_per_unit

        eoq = math.sqrt((2 * demand * cost_of_ordering) / carrying_cost)
        if eoq < min_quantity:
            order_quantity = min_quantity
        elif max_quantity != -1 and eoq > max_quantity:
            order_quantity = max_quantity
        else:
            order_quantity = eoq

        num_orders_per_year = demand / order_quantity
        average_inventory = order_quantity / 2
        total_cost = (num_orders_per_year * cost_of_ordering) + (average_inventory * carrying_cost) + (demand * price_per_unit)

        if total_cost < best_cost:
            best_cost = total_cost
            best_quantity = order_quantity
            best_range = discount_range

    return best_quantity, best_cost, best_range

def generate_range_inputs():
    try:
        num_ranges = int(num_ranges_entry.get())
        if num_ranges <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error de Entrada", "Por favor, ingrese un número válido de rangos.")
        return

    for widget in range_frame.winfo_children():
        widget.destroy()

    range_inputs.clear()

    for i in range(num_ranges):
        tk.Label(range_frame, text=f"Rango {i+1} - Cantidad Mínima:").grid(row=i*3, column=0, padx=5, pady=5)
        min_qty_entry = tk.Entry(range_frame)
        min_qty_entry.grid(row=i*3, column=1, padx=5, pady=5)

        tk.Label(range_frame, text=f"Rango {i+1} - Cantidad Máxima (-1 para infinito):").grid(row=i*3+1, column=0, padx=5, pady=5)
        max_qty_entry = tk.Entry(range_frame)
        max_qty_entry.grid(row=i*3+1, column=1, padx=5, pady=5)

        tk.Label(range_frame, text=f"Rango {i+1} - Precio por Unidad ($):").grid(row=i*3+2, column=0, padx=5, pady=5)
        price_entry = tk.Entry(range_frame)
        price_entry.grid(row=i*3+2, column=1, padx=5, pady=5)

        range_inputs.append({
            'min_qty_entry': min_qty_entry,
            'max_qty_entry': max_qty_entry,
            'price_entry': price_entry
        })

def on_calculate_button_click():
    try:
        demand = int(demanda_entry.get())
        ordering_cost = float(costo_pedido_entry.get())
        carrying_percentage = float(costo_almacenamiento_entry.get()) / 100

        ranges = []
        for inputs in range_inputs:
            min_quantity = int(inputs['min_qty_entry'].get())
            max_quantity = inputs['max_qty_entry'].get()
            max_quantity = int(max_quantity) if max_quantity != '-1' else -1
            price_per_unit = float(inputs['price_entry'].get())

            ranges.append({
                'min_quantity': min_quantity,
                'max_quantity': max_quantity,
                'price_per_unit': price_per_unit
            })

        best_quantity, best_cost, best_range = calculate_total_cost(demand, ordering_cost, carrying_percentage, ranges)

        resultado_label.config(text=f"Mejor cantidad de pedido: {best_quantity:.2f} unidades\n"
                                    f"Costo total mínimo: ${best_cost:.2f}\n"
                                    f"Rango óptimo: Cantidad Mínima {best_range['min_quantity']}, "
                                    f"Cantidad Máxima {'Infinito' if best_range['max_quantity'] == -1 else best_range['max_quantity']}, "
                                    f"Precio por Unidad ${best_range['price_per_unit']:.2f}")
    except ValueError:
        messagebox.showerror("Error de Entrada", "Por favor, ingrese números válidos en todos los campos.")

range_inputs = []

root = tk.Tk()
root.title("Calculadora de Descuentos en Pedido")

general_frame = tk.Frame(root)
general_frame.pack(pady=10)

tk.Label(general_frame, text="Demanda Anual (unidades):").grid(row=0, column=0, padx=5, pady=5)
demanda_entry = tk.Entry(general_frame)
demanda_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(general_frame, text="Costo de Pedido ($):").grid(row=1, column=0, padx=5, pady=5)
costo_pedido_entry = tk.Entry(general_frame)
costo_pedido_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(general_frame, text="Costo de Almacenamiento (%):").grid(row=2, column=0, padx=5, pady=5)
costo_almacenamiento_entry = tk.Entry(general_frame)
costo_almacenamiento_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(general_frame, text="Número de Rangos de Descuento:").grid(row=3, column=0, padx=5, pady=5)
num_ranges_entry = tk.Entry(general_frame)
num_ranges_entry.grid(row=3, column=1, padx=5, pady=5)

generar_button = tk.Button(general_frame, text="Generar Rangos", command=generate_range_inputs)
generar_button.grid(row=4, column=0, columnspan=2, pady=10)

range_frame = tk.Frame(root)
range_frame.pack(pady=10)

calcular_button = tk.Button(root, text="Calcular Mejor Cantidad", command=on_calculate_button_click)
calcular_button.pack(pady=10)

resultado_label = tk.Label(root, text="Mejor cantidad de pedido:")
resultado_label.pack(pady=10)

root.mainloop()
