import math
import tkinter as tk
from tkinter import messagebox, StringVar

def calcular():
    try:
        demanda_input = float(entry_demanda.get())
        desviacion_input = float(entry_desviacion.get())
        costo_pedido = float(entry_costo_pedido.get())
        costo_mantenimiento_input = float(entry_costo_mantenimiento.get())
        costo_por_venta_perdida_input = float(entry_costo_venta_perdida.get())
        plazo_entrega_input = float(entry_plazo_entrega.get())

        if var_demanda.get() == "semanal":
            demanda_anual = demanda_input * 52  # Convertir a anual
        else:
            demanda_anual = demanda_input  # Ya es anual

        if var_desviacion.get() == "semanal":
            desviacion_estandar_anual = desviacion_input * math.sqrt(52)  # Convertir a anual
        else:
            desviacion_estandar_anual = desviacion_input  # Ya es anual

        if var_costo_mantenimiento.get() == "semanal":
            costo_mantenimiento = costo_mantenimiento_input * 52  # Convertir a anual
        else:
            costo_mantenimiento = costo_mantenimiento_input  # Ya es anual

        if var_costo_venta_perdida.get() == "semanal":
            costo_por_venta_perdida = costo_por_venta_perdida_input * 52  # Convertir a anual
        else:
            costo_por_venta_perdida = costo_por_venta_perdida_input  # Ya es anual

        demanda_plazo_entrega = demanda_anual / plazo_entrega_input  # Modificación aquí
        
        Q_star = math.sqrt((2 * costo_pedido * demanda_anual) / costo_mantenimiento)
        
        desviacion_estandar_plazo_entrega = desviacion_estandar_anual / math.sqrt(plazo_entrega_input)

        r_star = demanda_plazo_entrega + (1.97 * desviacion_estandar_plazo_entrega)
        
        nivel_existencias_seguridad = r_star - demanda_plazo_entrega
        
        numerador = costo_mantenimiento * Q_star
        denominador = costo_mantenimiento * Q_star + (costo_por_venta_perdida * demanda_anual)
        probabilidad_agotamiento = numerador / denominador
        
        valor_z = 1 - probabilidad_agotamiento
        
        resultado_text = (f"Cantidad económica a pedir (Q*): {Q_star:.2f} cajas\n"
                          f"Demanda durante el plazo de entrega: {demanda_plazo_entrega:.2f} cajas\n"
                          f"Desviación estándar de la demanda durante el plazo de entrega: {desviacion_estandar_plazo_entrega:.2f} cajas\n"
                          f"Punto de reabastecimiento (r*): {r_star:.2f} cajas\n"
                          f"Nivel de existencias de seguridad: {nivel_existencias_seguridad:.2f} cajas\n"
                          f"Probabilidad de que se agoten las existencias durante el plazo de entrega (P(x ≥ r)): {probabilidad_agotamiento:.5f}\n"
                          f"Valor de Z: {valor_z:.5f}")
        
        messagebox.showinfo("Resultados", resultado_text)
    
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos.")
root = tk.Tk()
root.title("Modelo de Inventario")

tk.Label(root, text="Demanda (cajas):").grid(row=0, column=0, padx=10, pady=5)
entry_demanda = tk.Entry(root)
entry_demanda.grid(row=0, column=1)

var_demanda = StringVar(value="anual")
tk.Radiobutton(root, text="Anual", variable=var_demanda, value="anual").grid(row=0, column=2, padx=5, pady=5)
tk.Radiobutton(root, text="Semanal", variable=var_demanda, value="semanal").grid(row=0, column=3, padx=5, pady=5)

tk.Label(root, text="Desviación Estándar (cajas):").grid(row=1, column=0, padx=10, pady=5)
entry_desviacion = tk.Entry(root)
entry_desviacion.grid(row=1, column=1)

var_desviacion = StringVar(value="anual")
tk.Radiobutton(root, text="Anual", variable=var_desviacion, value="anual").grid(row=1, column=2, padx=5, pady=5)
tk.Radiobutton(root, text="Semanal", variable=var_desviacion, value="semanal").grid(row=1, column=3, padx=5, pady=5)

tk.Label(root, text="Costo de Hacer un Pedido ($):").grid(row=2, column=0, padx=10, pady=5)
entry_costo_pedido = tk.Entry(root)
entry_costo_pedido.grid(row=2, column=1)

tk.Label(root, text="Costo de Mantener en Inventario ($):").grid(row=3, column=0, padx=10, pady=5)
entry_costo_mantenimiento = tk.Entry(root)
entry_costo_mantenimiento.grid(row=3, column=1)

var_costo_mantenimiento = StringVar(value="anual")
tk.Radiobutton(root, text="Anual", variable=var_costo_mantenimiento, value="anual").grid(row=3, column=2, padx=5, pady=5)
tk.Radiobutton(root, text="Semanal", variable=var_costo_mantenimiento, value="semanal").grid(row=3, column=3, padx=5, pady=5)

tk.Label(root, text="Costo por Ventas Perdidas ($):").grid(row=4, column=0, padx=10, pady=5)
entry_costo_venta_perdida = tk.Entry(root)
entry_costo_venta_perdida.grid(row=4, column=1)

var_costo_venta_perdida = StringVar(value="anual")
tk.Radiobutton(root, text="Anual", variable=var_costo_venta_perdida, value="anual").grid(row=4, column=2, padx=5, pady=5)
tk.Radiobutton(root, text="Semanal", variable=var_costo_venta_perdida, value="semanal").grid(row=4, column=3, padx=5, pady=5)

tk.Label(root, text="Plazo de Entrega:").grid(row=5, column=0, padx=10, pady=5)
entry_plazo_entrega = tk.Entry(root)
entry_plazo_entrega.grid(row=5, column=1)

var_plazo_entrega = StringVar(value="semanas")
tk.Radiobutton(root, text="Semanas", variable=var_plazo_entrega, value="semanas").grid(row=5, column=2, padx=5, pady=5)
tk.Radiobutton(root, text="Días", variable=var_plazo_entrega, value="días").grid(row=5, column=3, padx=5, pady=5)

btn_calcular = tk.Button(root, text="Calcular", command=calcular)
btn_calcular.grid(row=6, columnspan=4, pady=10)

root.mainloop()
