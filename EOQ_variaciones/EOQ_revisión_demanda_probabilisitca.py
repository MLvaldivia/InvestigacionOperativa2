import numpy as np
import tkinter as tk
from tkinter import messagebox
from scipy.stats import norm

def calcular_inventario():
    try:
        demanda_diaria_media = float(entry_demanda.get())
        desviacion_estandar_diaria = float(entry_desviacion.get())
        tiempo_revision = int(entry_revision.get())
        tiempo_entrega = int(entry_entrega.get())
        inventario_actual = float(entry_inventario.get())
        nivel_servicio_porcentaje = float(entry_nivel_servicio.get()) / 100.0  # Convertir porcentaje a decimal

        z = norm.ppf(nivel_servicio_porcentaje)  # Valor Z de la tabla

        demanda_total = demanda_diaria_media * (tiempo_revision + tiempo_entrega)

        desviacion_total = desviacion_estandar_diaria * np.sqrt(tiempo_revision + tiempo_entrega)

        seguridad = z * desviacion_total

        M = demanda_total + seguridad

        Q = M - inventario_actual

        resultados = (
            f"Nivel de servicio deseado: {nivel_servicio_porcentaje*100:.2f}%\n"
            f"Valor Z (tabla): {z:.4f}\n"
            f"Demanda total durante {tiempo_revision + tiempo_entrega} días: {demanda_total:.2f} unidades\n"
            f"Desviación estándar durante {tiempo_revision + tiempo_entrega} días: {desviacion_total:.2f} unidades\n"
            f"Stock de seguridad (SS): {seguridad:.2f} unidades\n"
            f"Nivel de reposición (M): {M:.2f} unidades\n"
            f"Cantidad de pedido (Q): {Q:.2f} unidades"
        )

        messagebox.showinfo("Resultados del Inventario", resultados)
    
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores válidos.")

ventana = tk.Tk()
ventana.title("Cálculo de Inventario")

tk.Label(ventana, text="Demanda diaria promedio:").grid(row=0, column=0, padx=10, pady=5)
entry_demanda = tk.Entry(ventana)
entry_demanda.grid(row=0, column=1, padx=10, pady=5)

tk.Label(ventana, text="Desviación estándar diaria:").grid(row=1, column=0, padx=10, pady=5)
entry_desviacion = tk.Entry(ventana)
entry_desviacion.grid(row=1, column=1, padx=10, pady=5)

tk.Label(ventana, text="Días de revisión:").grid(row=2, column=0, padx=10, pady=5)
entry_revision = tk.Entry(ventana)
entry_revision.grid(row=2, column=1, padx=10, pady=5)

tk.Label(ventana, text="Días de tiempo de entrega:").grid(row=3, column=0, padx=10, pady=5)
entry_entrega = tk.Entry(ventana)
entry_entrega.grid(row=3, column=1, padx=10, pady=5)

tk.Label(ventana, text="Inventario disponible actual:").grid(row=4, column=0, padx=10, pady=5)
entry_inventario = tk.Entry(ventana)
entry_inventario.grid(row=4, column=1, padx=10, pady=5)

tk.Label(ventana, text="Nivel de servicio deseado (%):").grid(row=5, column=0, padx=10, pady=5)
entry_nivel_servicio = tk.Entry(ventana)
entry_nivel_servicio.grid(row=5, column=1, padx=10, pady=5)

boton_calcular = tk.Button(ventana, text="Calcular", command=calcular_inventario)
boton_calcular.grid(row=6, columnspan=2, pady=10)

ventana.mainloop()
