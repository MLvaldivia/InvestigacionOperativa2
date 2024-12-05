import tkinter as tk
import math

def calcular_cantidad_economica_pedido(demanda_promedio, costo_pedido, costo_mantenimiento):
    Q_star = math.sqrt((2 * demanda_promedio * costo_pedido) / costo_mantenimiento)
    return Q_star

def calcular_probabilidad_agotamiento(costo_mantenimiento, Q_star, costo_agotamiento, demanda_promedio):
    probabilidad_agotamiento = (costo_mantenimiento * Q_star) / (costo_agotamiento * demanda_promedio)
    return probabilidad_agotamiento

def calcular_datos_demanda_plazo(demanda_promedio, desviacion_demanda, tiempo_entrega):
    mu_x = tiempo_entrega * demanda_promedio
    sigma_x = desviacion_demanda * math.sqrt(tiempo_entrega)
    return mu_x, sigma_x

def calcular():
    # Leer los valores de los inputs
    demanda_promedio = float(entry_demanda_media.get())
    desviacion_demanda = float(entry_desviacion_estandar.get())
    costo_pedido = float(entry_costo_pedido.get())
    costo_mantenimiento = float(entry_costo_mantenimiento.get())
    costo_agotamiento = float(entry_costo_venta_perdida.get())
    tiempo_entrega = float(entry_plazo_entrega.get())

    # Cálculo de Q*
    Q_star = calcular_cantidad_economica_pedido(demanda_promedio, costo_pedido, costo_mantenimiento)
    label_resultado_Q_star.config(text=f"Cantidad económica a pedir (Q*): {Q_star:.2f} ≈ {round(Q_star)} cartuchos")

    # Cálculo de P(X >= r*)
    probabilidad_agotamiento = calcular_probabilidad_agotamiento(costo_mantenimiento, Q_star, costo_agotamiento, demanda_promedio)
    label_resultado_probabilidad.config(text=f"Probabilidad de agotamiento (P(X >= r*)): {probabilidad_agotamiento:.2f}")

    # Cálculo de μX y σX
    mu_x, sigma_x = calcular_datos_demanda_plazo(demanda_promedio, desviacion_demanda, tiempo_entrega)
    label_resultado_mu_x.config(text=f"Demanda promedio durante el plazo de entrega (μX): {mu_x}")
    label_resultado_sigma_x.config(text=f"Desviación estándar durante el plazo de entrega (σX): {sigma_x:.2f}")

# Crear la ventana de la aplicación
ventana = tk.Tk()
ventana.title("Cálculos de Inventario")

# Crear los widgets (entradas, etiquetas y botones)
label_demanda_media = tk.Label(ventana, text="Demanda promedio (cartuchos):")
label_demanda_media.grid(row=0, column=0)
entry_demanda_media = tk.Entry(ventana)
entry_demanda_media.grid(row=0, column=1)

label_desviacion_estandar = tk.Label(ventana, text="Desviación estándar de la demanda:")
label_desviacion_estandar.grid(row=1, column=0)
entry_desviacion_estandar = tk.Entry(ventana)
entry_desviacion_estandar.grid(row=1, column=1)

label_costo_pedido = tk.Label(ventana, text="Costo de hacer un pedido ($):")
label_costo_pedido.grid(row=2, column=0)
entry_costo_pedido = tk.Entry(ventana)
entry_costo_pedido.grid(row=2, column=1)

label_costo_mantenimiento = tk.Label(ventana, text="Costo semanal de mantenimiento ($):")
label_costo_mantenimiento.grid(row=3, column=0)
entry_costo_mantenimiento = tk.Entry(ventana)
entry_costo_mantenimiento.grid(row=3, column=1)

label_costo_venta_perdida = tk.Label(ventana, text="Costo de agotamiento de existencias ($):")
label_costo_venta_perdida.grid(row=4, column=0)
entry_costo_venta_perdida = tk.Entry(ventana)
entry_costo_venta_perdida.grid(row=4, column=1)

label_plazo_entrega = tk.Label(ventana, text="Tiempo de entrega (semanas):")
label_plazo_entrega.grid(row=5, column=0)
entry_plazo_entrega = tk.Entry(ventana)
entry_plazo_entrega.grid(row=5, column=1)

# Crear un botón para ejecutar los cálculos
boton_calcular = tk.Button(ventana, text="Calcular", command=calcular)
boton_calcular.grid(row=6, column=0, columnspan=2)

# Crear etiquetas para mostrar los resultados
label_resultado_Q_star = tk.Label(ventana, text="Cantidad económica a pedir (Q*):")
label_resultado_Q_star.grid(row=7, column=0, columnspan=2)

label_resultado_probabilidad = tk.Label(ventana, text="Probabilidad de agotamiento (P(X >= r*)): ")
label_resultado_probabilidad.grid(row=8, column=0, columnspan=2)

label_resultado_mu_x = tk.Label(ventana, text="Demanda promedio durante el plazo de entrega (μX): ")
label_resultado_mu_x.grid(row=9, column=0, columnspan=2)

label_resultado_sigma_x = tk.Label(ventana, text="Desviación estándar durante el plazo de entrega (σX): ")
label_resultado_sigma_x.grid(row=10, column=0, columnspan=2)

# Ejecutar la ventana
ventana.mainloop()
