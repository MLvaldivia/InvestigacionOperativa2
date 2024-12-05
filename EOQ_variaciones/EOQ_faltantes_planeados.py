import tkinter as tk
from tkinter import messagebox
import math

def calcular_modelo():
    try:
        D = float(entry_demand.get()) 
        Co = float(entry_order_cost.get())  
        Cw = float(entry_wait_cost.get()) 

        if entry_storage_cost.get():
            Ch = float(entry_storage_cost.get())  
        else:
            I = float(entry_interest.get()) if entry_interest.get() else 0  
            C = float(entry_cost.get()) if entry_cost.get() else 0  
            Ch = I * C 

        if Ch == 0:
            messagebox.showerror("Error", "Debe ingresar un valor para Ch o proporcionar I y C válidos.")
            return

        Q_star = math.sqrt((2 * D * Co * (Ch + Cw)) / (Ch * Cw))
        S_star = Q_star * Ch / (Ch + Cw)

        inventario_maximo = Q_star - S_star
        TQ = Q_star / D * 250 

        # Costos
        costo_retencion = (inventario_maximo ** 2) / (2 * Q_star) * Ch
        costo_ordenar = D / Q_star * Co
        costo_pedido_espera = (S_star ** 2) / (2 * Q_star) * Cw
        costo_total = costo_retencion + costo_ordenar + costo_pedido_espera

        # Mostrar resultados
        result_text = (
            f"Costo de almacenamiento por unidad (Ch): ${Ch:.2f}\n"
            f"Q* (Cantidad óptima de pedido): {Q_star:.2f} unidades\n"
            f"S* (Stock de seguridad): {S_star:.2f} unidades\n"
            f"Inventario máximo: {inventario_maximo:.2f} unidades\n"
            f"Tiempo de ciclo (días hábiles): {TQ:.2f} días\n"
            f"Costo de retención: ${costo_retencion:.2f}\n"
            f"Costo de ordenar: ${costo_ordenar:.2f}\n"
            f"Costo de pedido en espera: ${costo_pedido_espera:.2f}\n"
            f"Costo total: ${costo_total:.2f}\n"
        )

        # Calculo del ahorro en costos comparado con el modelo EOQ regular
        Q_EOQ = math.sqrt(2 * D * Co / Ch)
        costo_retencion_EOQ = (Q_EOQ / 2) * Ch
        costo_ordenar_EOQ = D / Q_EOQ * Co
        costo_total_EOQ = costo_retencion_EOQ + costo_ordenar_EOQ

        ahorro_costos = costo_total_EOQ - costo_total
        porcentaje_ahorro = (ahorro_costos / costo_total_EOQ) * 100

        result_text += (
            f"\nModelo EOQ regular: Q*: {Q_EOQ:.2f} unidades\n"
            f"Costo total EOQ: ${costo_total_EOQ:.2f}\n"
            f"Ahorro en costos al usar pedidos en espera: ${ahorro_costos:.2f}\n"
            f"Porcentaje de ahorro: {porcentaje_ahorro:.2f}%"
        )

        # Mostrar los resultados en el cuadro de texto
        result_label.config(text=result_text)

    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos.")

# Crear la ventana principal
window = tk.Tk()
window.title("Modelo de Inventario con Faltantes Planeados")

# Crear y colocar las etiquetas y entradas
tk.Label(window, text="Demanda anual (D):").grid(row=0, column=0, padx=10, pady=10)
entry_demand = tk.Entry(window)
entry_demand.grid(row=0, column=1)

tk.Label(window, text="Tasa de interés (I) (Opcional):").grid(row=1, column=0, padx=10, pady=10)
entry_interest = tk.Entry(window)
entry_interest.grid(row=1, column=1)

tk.Label(window, text="Costo por unidad (C) (Opcional):").grid(row=2, column=0, padx=10, pady=10)
entry_cost = tk.Entry(window)
entry_cost.grid(row=2, column=1)

tk.Label(window, text="Costo de almacenamiento por unidad (Ch):").grid(row=3, column=0, padx=10, pady=10)
entry_storage_cost = tk.Entry(window)
entry_storage_cost.grid(row=3, column=1)

tk.Label(window, text="Costo por pedido (Co):").grid(row=4, column=0, padx=10, pady=10)
entry_order_cost = tk.Entry(window)
entry_order_cost.grid(row=4, column=1)

tk.Label(window, text="Costo pedido en espera (Cw):").grid(row=5, column=0, padx=10, pady=10)
entry_wait_cost = tk.Entry(window)
entry_wait_cost.grid(row=5, column=1)

# Botón para calcular
calculate_button = tk.Button(window, text="Calcular", command=calcular_modelo)
calculate_button.grid(row=6, column=0, columnspan=2, pady=10)

# Etiqueta para mostrar los resultados
result_label = tk.Label(window, text="", justify=tk.LEFT)
result_label.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

# Ejecutar la aplicación
window.mainloop()
