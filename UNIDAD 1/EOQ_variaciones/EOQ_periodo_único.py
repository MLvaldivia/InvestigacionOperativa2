import tkinter as tk
from tkinter import messagebox

# Función para calcular el número óptimo de unidades a ordenar, beneficios y costos adicionales
def calcular_optimo():
    try:
        # Obtener los valores ingresados por el usuario
        costo_por_par = float(entry_costo_por_par.get())
        precio_venta = float(entry_precio_venta.get())
        precio_liquidacion = float(entry_precio_liquidacion.get())
        
        # Parámetros de la demanda uniforme
        demanda_min = int(entry_demanda_min.get())
        demanda_max = int(entry_demanda_max.get())
        
        # Demanda promedio (usada directamente)
        demanda_promedio = 500
        
        # Calcular los costos adicionales
        costo_sobreestimar = costo_por_par - precio_liquidacion  # Costo a sobreestimar
        costo_subestimar = precio_venta - costo_por_par  # Costo a subestimar
        
        # Calcular la probabilidad de que la demanda sea menor o igual a la cantidad óptima
        probabilidad_demanda = costo_subestimar / (costo_subestimar + costo_sobreestimar)
        
        # Paso 1: Resta entre demanda máxima y demanda mínima
        resta_demanda = demanda_max - demanda_min
        
        # Paso 2: Multiplicación de la probabilidad de demanda por el resultado de la resta
        resultado_multiplicacion = probabilidad_demanda * resta_demanda
        
        # Paso 3: Sumar la demanda mínima al resultado anterior
        distribucion_uniforme = demanda_min + resultado_multiplicacion
        
        # Mostrar los resultados
        resultado_label.config(text=(
            f"Número óptimo de unidades a ordenar: {demanda_promedio:.0f}\n"
            f"Costo a sobreestimar (Co): ${costo_sobreestimar:.2f}\n"
            f"Costo a subestimar (Cu): ${costo_subestimar:.2f}\n"
            f"Probabilidad de que la demanda sea <= Q*: {probabilidad_demanda:.2f}\n"
            f"Resta entre demanda máxima y mínima: {resta_demanda:.2f}\n"
            f"Multiplicación de probabilidad y resta: {resultado_multiplicacion:.2f}\n"
            f"Distribución uniforme de la demanda: {distribucion_uniforme:.2f}"
        ))
    
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos.")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Modelo de Inventario - Johnson Shoe Company")

# Etiquetas y campos de entrada
label_costo_por_par = tk.Label(ventana, text="Costo por par de zapatos ($):")
label_costo_por_par.grid(row=0, column=0)
entry_costo_por_par = tk.Entry(ventana)
entry_costo_por_par.insert(0, "40")  # Valor por defecto
entry_costo_por_par.grid(row=0, column=1)

label_precio_venta = tk.Label(ventana, text="Precio de venta al público ($):")
label_precio_venta.grid(row=1, column=0)
entry_precio_venta = tk.Entry(ventana)
entry_precio_venta.insert(0, "60")  # Valor por defecto
entry_precio_venta.grid(row=1, column=1)

label_precio_liquidacion = tk.Label(ventana, text="Precio de liquidación ($):")
label_precio_liquidacion.grid(row=2, column=0)
entry_precio_liquidacion = tk.Entry(ventana)
entry_precio_liquidacion.insert(0, "30")  # Valor por defecto
entry_precio_liquidacion.grid(row=2, column=1)

label_demanda_min = tk.Label(ventana, text="Demanda mínima (D_min):")
label_demanda_min.grid(row=3, column=0)
entry_demanda_min = tk.Entry(ventana)
entry_demanda_min.insert(0, "350")  # Valor por defecto
entry_demanda_min.grid(row=3, column=1)

label_demanda_max = tk.Label(ventana, text="Demanda máxima (D_max):")
label_demanda_max.grid(row=4, column=0)
entry_demanda_max = tk.Entry(ventana)
entry_demanda_max.insert(0, "650")  # Valor por defecto
entry_demanda_max.grid(row=4, column=1)

# Botón para calcular el número óptimo y el beneficio
boton_calcular = tk.Button(ventana, text="Calcular Óptimo", command=calcular_optimo)
boton_calcular.grid(row=5, column=0, columnspan=2)

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(ventana, text="", font=("Arial", 12))
resultado_label.grid(row=6, column=0, columnspan=2)

# Ejecutar la interfaz
ventana.mainloop()
