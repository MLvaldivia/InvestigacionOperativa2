import tkinter as tk
from tkinter import messagebox


def calcular_mm1():
    try:
        lambda_rate = float(entry_lambda.get())
        mu_rate = float(entry_mu.get())
        
        if lambda_rate >= mu_rate:
            messagebox.showerror("Error", "El sistema no es estable: λ debe ser menor que μ.")
            return
        
        P0 = 1 - lambda_rate / mu_rate
        L = lambda_rate / (mu_rate - lambda_rate)
        Lq = (lambda_rate**2) / (mu_rate * (mu_rate - lambda_rate))
        W = 1 / (mu_rate - lambda_rate)
        Wq = lambda_rate / (mu_rate * (mu_rate - lambda_rate))
        
        result_text.set(
            f"Probabilidad de vacío (P0): {P0:.4f}\n"
            f"Número promedio en el sistema (L): {L:.4f}\n"
            f"Número promedio en la cola (Lq): {Lq:.4f}\n"
            f"Tiempo promedio en el sistema (W): {W:.4f} unidades de tiempo\n"
            f"Tiempo promedio en la cola (Wq): {Wq:.4f} unidades de tiempo"
        )
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")


root = tk.Tk()
root.title("Modelo de Línea de Espera M/M/1")

tk.Label(root, text="Tasa de llegada (λ):").pack()
entry_lambda = tk.Entry(root)
entry_lambda.pack()

tk.Label(root, text="Tasa de servicio (μ):").pack()
entry_mu = tk.Entry(root)
entry_mu.pack()

tk.Button(root, text="Calcular", command=calcular_mm1).pack()

result_text = tk.StringVar()
tk.Label(root, textvariable=result_text, justify="left", padx=10, pady=10).pack()

# Ejecutar la aplicación
root.mainloop()
