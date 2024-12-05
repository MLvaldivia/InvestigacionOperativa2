import tkinter as tk
from tkinter import ttk
import math

def calcular():
    try:
        lambda_val = float(entry_lambda.get())
        mu_val = float(entry_mu.get())
        N = int(entry_N.get())
        n_consultar = int(entry_n.get())
        
        if n_consultar > N:
            resultado_label.config(text="Error: n debe ser menor o igual a N.")
            return
        
        sumatoria = 0
        for n in range(0, N + 1):
            factorial_term = math.factorial(N) / math.factorial(N - n)
            sumatoria += factorial_term * (lambda_val / mu_val) ** n
        P0 = 1 / sumatoria

        Lq = N - ((lambda_val + mu_val) / lambda_val) * (1 - P0)

        L = Lq + (1 - P0)

        lambda_efectiva = (N - L) * lambda_val  # Tasa de llegada efectiva
        Wq = Lq / lambda_efectiva

        W = Wq + (1 / mu_val)

        Pw = 1 - P0

        factorial_term = math.factorial(N) / math.factorial(N - n_consultar)
        Pn = factorial_term * (lambda_val / mu_val) ** n_consultar * P0

        resultado_label.config(text=(
            f"P0: {P0:.4f}\n"
            f"Lq: {Lq:.4f}\n"
            f"L: {L:.4f}\n"
            f"Wq: {Wq:.4f}\n"
            f"W: {W:.4f}\n"
            f"Pw: {Pw:.4f}\n"
            f"P{n_consultar}: {Pn:.4f}"
        ))
    except Exception as e:
        resultado_label.config(text=f"Error: {e}")

root = tk.Tk()
root.title("Modelo de Fuentes Finitas")

ttk.Label(root, text="Tasa de llegada (λ):").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_lambda = ttk.Entry(root)
entry_lambda.grid(row=0, column=1, padx=10, pady=5)

ttk.Label(root, text="Tasa de servicio (μ):").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_mu = ttk.Entry(root)
entry_mu.grid(row=1, column=1, padx=10, pady=5)

ttk.Label(root, text="Tamaño de la población (N):").grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_N = ttk.Entry(root)
entry_N.grid(row=2, column=1, padx=10, pady=5)

ttk.Label(root, text="Estado (n):").grid(row=3, column=0, padx=10, pady=5, sticky="e")
entry_n = ttk.Entry(root)
entry_n.grid(row=3, column=1, padx=10, pady=5)

btn_calcular = ttk.Button(root, text="Calcular", command=calcular)
btn_calcular.grid(row=4, column=0, columnspan=2, pady=10)

resultado_label = ttk.Label(root, text="", justify="left", foreground="blue")
resultado_label.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
