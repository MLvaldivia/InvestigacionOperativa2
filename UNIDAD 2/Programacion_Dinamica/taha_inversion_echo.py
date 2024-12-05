import tkinter as tk
from tkinter import messagebox

def calcular_acumulacion():
    try:
        inversion_inicial = float(entry_inversion_inicial.get())  
        aporte = float(entry_aporte.get())  

        tasas = [
            float(entry_tasa_ano1.get()) / 100,  
            float(entry_tasa_ano2.get()) / 100,  
            float(entry_tasa_ano3.get()) / 100, 
            float(entry_tasa_ano4.get()) / 100,  
        ]

        acumulacion = inversion_inicial
        acumulaciones = []  
        for i in range(4):
            if i > 0:  
                acumulacion += aporte
            acumulacion *= (1 + tasas[i])  
            acumulaciones.append(acumulacion)

        f1_x1 = 7157.7 + 1.38349 * inversion_inicial

        resultados = (
            f"Acumulación por año:\n"
            f"Año 1: ${acumulaciones[0]:.2f}\n"
            f"Año 2: ${acumulaciones[1]:.2f}\n"
            f"Año 3: ${acumulaciones[2]:.2f}\n"
            f"Año 4: ${acumulaciones[3]:.2f}\n\n"
            f"Acumulación total calculada: ${acumulaciones[-1]:.2f}\n"
            f"f1(x1) = 7157.7 + 1.38349(4000) = ${f1_x1:.2f}"
        )
        messagebox.showinfo("Resultado", resultados)

    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores válidos.")

ventana = tk.Tk()
ventana.title("Cálculo de Acumulación Total")

label_inversion_inicial = tk.Label(ventana, text="Inversión inicial ($4000):")
label_inversion_inicial.pack()
entry_inversion_inicial = tk.Entry(ventana)
entry_inversion_inicial.insert(tk.END, "4000")
entry_inversion_inicial.pack()

label_aporte = tk.Label(ventana, text="Aporte adicional ($2000):")
label_aporte.pack()
entry_aporte = tk.Entry(ventana)
entry_aporte.insert(tk.END, "2000")
entry_aporte.pack()

label_tasa_ano1 = tk.Label(ventana, text="Tasa de interés Año 1 (%):")
label_tasa_ano1.pack()
entry_tasa_ano1 = tk.Entry(ventana)
entry_tasa_ano1.insert(tk.END, "9.8")  # Tasa por defecto (8% + 1.8%)
entry_tasa_ano1.pack()

label_tasa_ano2 = tk.Label(ventana, text="Tasa de interés Año 2 (%):")
label_tasa_ano2.pack()
entry_tasa_ano2 = tk.Entry(ventana)
entry_tasa_ano2.insert(tk.END, "9.7") 
entry_tasa_ano2.pack()

label_tasa_ano3 = tk.Label(ventana, text="Tasa de interés Año 3 (%):")
label_tasa_ano3.pack()
entry_tasa_ano3 = tk.Entry(ventana)
entry_tasa_ano3.insert(tk.END, "10.1")  
entry_tasa_ano3.pack()

label_tasa_ano4 = tk.Label(ventana, text="Tasa de interés Año 4 (%):")
label_tasa_ano4.pack()
entry_tasa_ano4 = tk.Entry(ventana)
entry_tasa_ano4.insert(tk.END, "10.5")  
entry_tasa_ano4.pack()


boton_calcular = tk.Button(ventana, text="Calcular", command=calcular_acumulacion)
boton_calcular.pack()


ventana.mainloop()
