import tkinter as tk
from tkinter import messagebox

def calcular_mg1():
    try:
        lambd = float(entry_lambda.get())
        mu = float(entry_mu.get())
        sigma = float(entry_sigma.get())

        if lambd <= 0 or mu <= 0 or sigma < 0:
            raise ValueError("Valores no válidos. λ y μ deben ser positivos, σ debe ser no negativo.")
        if lambd >= mu:
            raise ValueError("El sistema no es estable: λ debe ser menor que μ.")

        rho = lambd / mu
        P0 = 1 - rho
        Lq = (lambd**2 * sigma**2 + rho**2) / (2 * (1 - rho))
        L = Lq + rho
        Wq = Lq / lambd
        W = Wq + 1 / mu
        Pw = rho

        label_resultado.config(text=(
            f"P0 (Sistema vacío): {P0:.4f}\n"
            f"Lq (Unidades en la línea): {Lq:.4f}\n"
            f"L (Unidades en el sistema): {L:.4f}\n"
            f"Wq (Tiempo en la línea): {Wq:.4f}\n"
            f"W (Tiempo en el sistema): {W:.4f}\n"
            f"Pw (Prob. de esperar): {Pw:.4f}"
        ))
    except ValueError as e:
        messagebox.showerror("Error", str(e))

ventana = tk.Tk()
ventana.title("Modelo M/G/1")

tk.Label(ventana, text="λ (Tasa de llegada):").grid(row=0, column=0, padx=10, pady=5)
entry_lambda = tk.Entry(ventana)
entry_lambda.grid(row=0, column=1, padx=10, pady=5)

tk.Label(ventana, text="μ (Tasa de servicio):").grid(row=1, column=0, padx=10, pady=5)
entry_mu = tk.Entry(ventana)
entry_mu.grid(row=1, column=1, padx=10, pady=5)

tk.Label(ventana, text="σ (Desviación estándar):").grid(row=2, column=0, padx=10, pady=5)
entry_sigma = tk.Entry(ventana)
entry_sigma.grid(row=2, column=1, padx=10, pady=5)

btn_calcular = tk.Button(ventana, text="Calcular", command=calcular_mg1)
btn_calcular.grid(row=3, column=0, columnspan=2, pady=10)

label_resultado = tk.Label(ventana, text="", justify="left")
label_resultado.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

ventana.mainloop()
