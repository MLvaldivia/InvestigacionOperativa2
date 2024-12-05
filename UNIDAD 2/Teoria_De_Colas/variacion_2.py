import tkinter as tk
from tkinter import messagebox
from math import factorial

def calcular():
    try:
        lambda_val = float(entry_lambda.get())
        mu_val = float(entry_mu.get())
        c_val = int(entry_c.get())
        
        if lambda_val / (c_val * mu_val) >= 1:
            messagebox.showerror("Error", "El sistema no es estable (ρ >= 1).")
            return
        
        rho = lambda_val / (c_val * mu_val)
        
        sumatoria = sum((lambda_val / mu_val) ** n / factorial(n) for n in range(c_val))
        P0 = 1 / (sumatoria + ((lambda_val / mu_val) ** c_val / factorial(c_val)) * (1 / (1 - rho)))
        
        Lq = P0 * ((lambda_val / mu_val) ** c_val) * rho / (factorial(c_val) * (1 - rho) ** 2)
        
        L = Lq + lambda_val / mu_val
        
        Wq = Lq / lambda_val
        
        W = Wq + 1 / mu_val
        
        Pw = (P0 * ((lambda_val / mu_val) ** c_val) / factorial(c_val)) * (1 / (1 - rho))
        
        label_resultado.config(
            text=f"Resultados:\n"
                 f"Lq (Clientes en la fila): {Lq:.2f}\n"
                 f"L (Clientes en el sistema): {L:.2f}\n"
                 f"Wq (Tiempo en la fila): {Wq:.2f}\n"
                 f"W (Tiempo en el sistema): {W:.2f}\n"
                 f"P0 (Sistema vacío): {P0:.4f}\n"
                 f"Pw (Todos los servidores ocupados): {Pw:.4f}"
        )
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa valores válidos.")

root = tk.Tk()
root.title("Modelo M/M/c")
root.geometry("500x400")

label_lambda = tk.Label(root, text="Tasa de llegada (λ):")
label_lambda.pack(pady=5)

entry_lambda = tk.Entry(root)
entry_lambda.pack(pady=5)

label_mu = tk.Label(root, text="Tasa de servicio (μ):")
label_mu.pack(pady=5)

entry_mu = tk.Entry(root)
entry_mu.pack(pady=5)

label_c = tk.Label(root, text="Número de servidores (c):")
label_c.pack(pady=5)

entry_c = tk.Entry(root)
entry_c.pack(pady=5)

button_calcular = tk.Button(root, text="Calcular", command=calcular)
button_calcular.pack(pady=10)

label_resultado = tk.Label(root, text="Resultados:")
label_resultado.pack(pady=20)

root.mainloop()
