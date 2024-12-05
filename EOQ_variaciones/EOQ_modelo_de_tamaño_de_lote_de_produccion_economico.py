import tkinter as tk
from tkinter import messagebox
import math

def calcular():
    try:
        demanda = float(entry_demanda.get())
        produccion = float(entry_produccion.get())
        dias_habiles = int(entry_dias_habiles.get())
        costo_preparacion = float(entry_costo_preparacion.get())

        unidad_demanda = var_unidad_demanda.get()
        unidad_produccion = var_unidad_produccion.get()
        unidad_dias_habiles = var_unidad_dias_habiles.get()
        unidad_retencion = var_unidad_retencion.get()

        if unidad_demanda == 'Mensual':
            D = demanda * 12  
        elif unidad_demanda == 'Diaria':
            D = demanda * 240  
        else:
            D = demanda  

        if unidad_produccion == 'Mensual':
            P = produccion * 12  
        elif unidad_produccion == 'Diaria':
            P = produccion * 240  
        else:
            P = produccion  

        if unidad_dias_habiles == 'Mensual':
            dias_habiles_anuales = dias_habiles * 12  
        else:
            dias_habiles_anuales = dias_habiles 

        
        if unidad_retencion == 'Porcentaje':
            tasa_retencion = float(entry_tasa_retencion.get()) / 100  
           
            if entry_costo_produccion.get():  
                costo_produccion = float(entry_costo_produccion.get())
                Ch = tasa_retencion * costo_produccion  
            else:  
                Ch = tasa_retencion  
        else:
            Ch = float(entry_tasa_retencion.get())  

        p = P / dias_habiles_anuales  
        d = D / dias_habiles_anuales  

        if p <= d:
            messagebox.showerror("Error", "La tasa de producción debe ser mayor que la tasa de demanda.")
            return

        Q = math.sqrt((2 * D * costo_preparacion) / (Ch * (1 - d / p)))

        TC = (D / Q) * costo_preparacion + (Q / 2) * Ch * (1 - d / p)

        messagebox.showinfo("Resultados",
                            f"Demanda anual (D): {D:.2f} unidades\n"
                            f"Producción anual (P): {P:.2f} unidades\n"
                            f"Días hábiles anuales: {dias_habiles_anuales} días\n"
                            f"Costo anual de retención por unidad (Ch): S/. {Ch:.2f}\n"
                            f"Tasa de producción diaria (p): {p:.2f} unidades/día\n"
                            f"Tasa de demanda diaria (d): {d:.2f} unidades/día\n"
                            f"Tamaño óptimo del lote de producción (Q): {Q:.2f} unidades\n"
                            f"Costo anual total (TC): S/. {TC:.2f}")

    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores válidos.")

ventana = tk.Tk()
ventana.title("Modelo de Tamaño de Lote de Producción Económico")

var_unidad_demanda = tk.StringVar(value='Mensual')
var_unidad_produccion = tk.StringVar(value='Mensual')
var_unidad_dias_habiles = tk.StringVar(value='Mensual')
var_unidad_retencion = tk.StringVar(value='Porcentaje')

tk.Label(ventana, text="Demanda:").grid(row=0, column=0)
entry_demanda = tk.Entry(ventana)
entry_demanda.grid(row=0, column=1)

tk.Radiobutton(ventana, text="Mensual", variable=var_unidad_demanda, value='Mensual').grid(row=0, column=2)
tk.Radiobutton(ventana, text="Anual", variable=var_unidad_demanda, value='Anual').grid(row=0, column=3)
tk.Radiobutton(ventana, text="Diaria", variable=var_unidad_demanda, value='Diaria').grid(row=0, column=4)

tk.Label(ventana, text="Producción:").grid(row=1, column=0)
entry_produccion = tk.Entry(ventana)
entry_produccion.grid(row=1, column=1)

tk.Radiobutton(ventana, text="Mensual", variable=var_unidad_produccion, value='Mensual').grid(row=1, column=2)
tk.Radiobutton(ventana, text="Anual", variable=var_unidad_produccion, value='Anual').grid(row=1, column=3)
tk.Radiobutton(ventana, text="Diaria", variable=var_unidad_produccion, value='Diaria').grid(row=1, column=4)

tk.Label(ventana, text="Días hábiles:").grid(row=2, column=0)
entry_dias_habiles = tk.Entry(ventana)
entry_dias_habiles.grid(row=2, column=1)

tk.Radiobutton(ventana, text="Mensual", variable=var_unidad_dias_habiles, value='Mensual').grid(row=2, column=2)
tk.Radiobutton(ventana, text="Anual", variable=var_unidad_dias_habiles, value='Anual').grid(row=2, column=3)
tk.Radiobutton(ventana, text="Diaria", variable=var_unidad_dias_habiles, value='Diaria').grid(row=2, column=4)

tk.Label(ventana, text="Costo de preparación (S/.):").grid(row=3, column=0)
entry_costo_preparacion = tk.Entry(ventana)
entry_costo_preparacion.grid(row=3, column=1)

tk.Label(ventana, text="Tasa de costos de retención:").grid(row=4, column=0)
entry_tasa_retencion = tk.Entry(ventana)
entry_tasa_retencion.grid(row=4, column=1)

tk.Radiobutton(ventana, text="Porcentaje (%)", variable=var_unidad_retencion, value='Porcentaje').grid(row=4, column=2)
tk.Radiobutton(ventana, text="Valor fijo", variable=var_unidad_retencion, value='Fijo').grid(row=4, column=3)

tk.Label(ventana, text="Costo de producción (opcional) (S/.):").grid(row=5, column=0)
entry_costo_produccion = tk.Entry(ventana)
entry_costo_produccion.grid(row=5, column=1)

boton_calcular = tk.Button(ventana, text="Calcular", command=calcular)
boton_calcular.grid(row=6, columnspan=5)

ventana.mainloop()
