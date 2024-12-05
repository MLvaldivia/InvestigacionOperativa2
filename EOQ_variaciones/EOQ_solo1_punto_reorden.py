import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox
from scipy.stats import norm

# Función para calcular el tamaño óptimo del pedido usando EOQ
def calcular_tamano_pedido(demanda_anual, costo_emision, costo_retencion):
    Q_star = np.sqrt((2 * demanda_anual * costo_emision) / costo_retencion)
    return Q_star

# Función que se ejecuta al presionar el botón
def calcular_y_mostrar():
    try:
        # Obtener datos de la interfaz gráfica
        costo_emision = float(entry_costo_emision.get())  # Costo de emitir un pedido
        costo_casco = float(entry_costo_casco.get())      # Costo por casco
        costo_retencion = float(entry_costo_retencion.get())  # Costo de retención
        demanda_media = float(entry_media_demanda.get())  # Demanda media durante el tiempo de entrega
        desviacion_estandar = float(entry_desviacion_estandar.get())  # Desviación estándar
        dias_laborables = int(entry_dias_laborables.get())  # Días laborables al año
        tiempo_entrega = int(entry_tiempo_entrega.get())  # Tiempo de entrega

        # Calcular demanda anual (multiplicando por 52)
        demanda_anual = demanda_media * 52  # Demanda anual estimada
        label_demanda_anual.config(text=f"Demanda Anual: {demanda_anual:.2f}")

        # Calcular el costo de retención
        costo_retencion = 0.18 * costo_casco  # Cálculo del costo de retención anual

        # Calcular el tamaño óptimo de pedido usando EOQ
        Q_star = calcular_tamano_pedido(demanda_anual, costo_emision, costo_retencion)
        label_tamano_pedido.config(text=f"Tamaño Óptimo de Pedido (Q*): {Q_star:.2f}")

        # Calcular la cantidad de pedidos anuales
        cantidad_pedidos_anuales = demanda_anual / Q_star
        label_cantidad_pedidos.config(text=f"Cantidad de Pedidos Anuales: {cantidad_pedidos_anuales:.2f}")

        # Calcular los días hábiles entre pedidos
        dias_entre_pedidos = dias_laborables / cantidad_pedidos_anuales
        label_dias_entre_pedidos.config(text=f"Días Hábiles entre Pedidos: {dias_entre_pedidos:.2f}")

        # Cálculo de la probabilidad acumulada de Z para obtener el valor de r
        probabilidad = 0.9550  # Probabilidad acumulada correspondiente a 95.5%
        r = norm.ppf(probabilidad)  # Buscar el valor de Z (r) correspondiente a esta probabilidad
        label_z_r.config(text=f"Valor de Z (r) para P = 0.9550: {r:.4f}")

        # Cálculo del punto de reorden (momento en el que se debe ordenar)
        punto_reorden = demanda_media + (r * desviacion_estandar)
        label_punto_reorden.config(text=f"Punto de Reorden: {punto_reorden:.2f}")

        # **Nuevo Cálculo de la Existencia de Seguridad**
        existencia_seguridad = dias_laborables - demanda_media
        label_existencia_seguridad.config(text=f"Existencia de Seguridad: {existencia_seguridad:.2f}")

        # **Costo de Retención, Inventario Normal**
        costo_retencion_inventario_normal = (Q_star / 2) * costo_retencion
        label_costo_retencion_inventario_normal.config(text=f"Costo Retención Inventario Normal: {costo_retencion_inventario_normal:.2f}")

        # **Costo de Retención, Existencia de Seguridad**
        costo_retencion_existencia_seguridad = existencia_seguridad * costo_retencion
        label_costo_retencion_existencia_seguridad.config(text=f"Costo Retención Existencia de Seguridad: {costo_retencion_existencia_seguridad:.2f}")

        # **Costo de Ordenar**
        costo_ordenar = (demanda_media / Q_star) * costo_emision
        label_costo_ordenar.config(text=f"Costo de Ordenar: {costo_ordenar:.2f}")

        # **Costo Total**
        costo_total = costo_retencion_inventario_normal + costo_retencion_existencia_seguridad + costo_ordenar
        label_costo_total.config(text=f"Costo Total: {costo_total:.2f}")

        # Mostrar resultados en un cuadro de mensaje
        messagebox.showinfo("Resultados",
            f"La cantidad óptima de cascos a tener disponibles es: {Q_star:.2f}\n"
            f"Cantidad de pedidos anuales: {cantidad_pedidos_anuales:.2f}\n"
            f"Días hábiles entre pedidos: {dias_entre_pedidos:.2f}\n"
            f"Valor de Z (r) para P = 0.9550: {r:.4f}\n"
            f"Punto de Reorden: {punto_reorden:.2f}\n"
            f"Existencia de Seguridad: {existencia_seguridad:.2f}\n"
            f"Costo Retención Inventario Normal: {costo_retencion_inventario_normal:.2f}\n"
            f"Costo Retención Existencia de Seguridad: {costo_retencion_existencia_seguridad:.2f}\n"
            f"Costo de Ordenar: {costo_ordenar:.2f}\n"
            f"Costo Total: {costo_total:.2f}"
        )

        # Graficar la distribución de la demanda
        x = np.linspace(100, 300, 100)
        y = np.random.normal(demanda_media, desviacion_estandar, size=1000)
        
        plt.hist(y, bins=30, density=True, alpha=0.5, color='blue')
        plt.axvline(x=Q_star, color='r', linestyle='--', label='Q*')
        plt.title('Distribución de la Demanda de Cascos')
        plt.xlabel('Cantidad de Cascos')
        plt.ylabel('Densidad de Probabilidad')
        plt.legend()
        plt.grid()
        plt.show()

    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

# Interfaz gráfica con Tkinter
ventana = tk.Tk()
ventana.title("Modelo de Inventario de Período Único - EOQ")

# Etiquetas y campos de entrada
tk.Label(ventana, text="Costo de Emitir un Pedido:").grid(row=0, column=0)
entry_costo_emision = tk.Entry(ventana)
entry_costo_emision.grid(row=0, column=1)

tk.Label(ventana, text="Costo por Casco:").grid(row=1, column=0)
entry_costo_casco = tk.Entry(ventana)
entry_costo_casco.grid(row=1, column=1)

tk.Label(ventana, text="Costo de Retención (anual):").grid(row=2, column=0)
entry_costo_retencion = tk.Entry(ventana)
entry_costo_retencion.grid(row=2, column=1)

tk.Label(ventana, text="Demanda Media (10 días):").grid(row=3, column=0)
entry_media_demanda = tk.Entry(ventana)
entry_media_demanda.grid(row=3, column=1)

tk.Label(ventana, text="Desviación Estándar (10 días):").grid(row=4, column=0)
entry_desviacion_estandar = tk.Entry(ventana)
entry_desviacion_estandar.grid(row=4, column=1)

tk.Label(ventana, text="Días Laborables:").grid(row=5, column=0)
entry_dias_laborables = tk.Entry(ventana)
entry_dias_laborables.grid(row=5, column=1)

tk.Label(ventana, text="Tiempo de Entrega (días):").grid(row=6, column=0)
entry_tiempo_entrega = tk.Entry(ventana)
entry_tiempo_entrega.grid(row=6, column=1)

# Botón para ejecutar los cálculos
boton_calcular = tk.Button(ventana, text="Calcular", command=calcular_y_mostrar)
boton_calcular.grid(row=7, columnspan=2)

# Etiquetas para mostrar resultados
label_demanda_anual = tk.Label(ventana, text="Demanda Anual: --")
label_demanda_anual.grid(row=8, columnspan=2)

label_tamano_pedido = tk.Label(ventana, text="Tamaño Óptimo de Pedido (Q*): --")
label_tamano_pedido.grid(row=9, columnspan=2)

label_cantidad_pedidos = tk.Label(ventana, text="Cantidad de Pedidos Anuales: --")
label_cantidad_pedidos.grid(row=10, columnspan=2)

label_dias_entre_pedidos = tk.Label(ventana, text="Días Hábiles entre Pedidos: --")
label_dias_entre_pedidos.grid(row=11, columnspan=2)

label_z_r = tk.Label(ventana, text="Valor de Z (r): --")
label_z_r.grid(row=12, columnspan=2)

label_punto_reorden = tk.Label(ventana, text="Punto de Reorden: --")
label_punto_reorden.grid(row=13, columnspan=2)

label_existencia_seguridad = tk.Label(ventana, text="Existencia de Seguridad: --")
label_existencia_seguridad.grid(row=14, columnspan=2)

label_costo_retencion_inventario_normal = tk.Label(ventana, text="Costo Retención Inventario Normal: --")
label_costo_retencion_inventario_normal.grid(row=15, columnspan=2)

label_costo_retencion_existencia_seguridad = tk.Label(ventana, text="Costo Retención Existencia de Seguridad: --")
label_costo_retencion_existencia_seguridad.grid(row=16, columnspan=2)

label_costo_ordenar = tk.Label(ventana, text="Costo de Ordenar: --")
label_costo_ordenar.grid(row=17, columnspan=2)

label_costo_total = tk.Label(ventana, text="Costo Total: --")
label_costo_total.grid(row=18, columnspan=2)

# Ejecutar la interfaz
ventana.mainloop()
