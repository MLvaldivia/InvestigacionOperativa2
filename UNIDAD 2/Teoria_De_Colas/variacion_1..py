import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        lambda_val = float(entry_lambda.get())
        mu_val = float(entry_mu.get())
        
        if lambda_val >= mu_val:
            messagebox.showerror("Error", "La tasa de llegada debe ser menor que la tasa de servicio.")
            return
        
        P0 = 1 - (lambda_val / mu_val)
        L = lambda_val / (mu_val - lambda_val)
        Lq = (lambda_val ** 2) / (mu_val * (mu_val - lambda_val))
        W = 1 / (mu_val - lambda_val)
        Wq = lambda_val / (mu_val * (mu_val - lambda_val))
        P_w = lambda_val / mu_val
        
        result_var.set(f"Probabilidad de vacío (P0): {P0:.4f}\n"
                       f"Número promedio de unidades en el sistema (L): {L:.4f}\n"
                       f"Número promedio de unidades en la cola (Lq): {Lq:.4f}\n"
                       f"Tiempo promedio en el sistema (W): {W:.4f}\n"
                       f"Tiempo promedio en la cola (Wq): {Wq:.4f}\n"
                       f"Probabilidad de no esperar (P_w): {P_w:.4f}")
    
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

root = tk.Tk()
root.title("Modelo M/M/1")

label_lambda = tk.Label(root, text="Tasa de llegada (λ):")
label_lambda.pack()

entry_lambda = tk.Entry(root)
entry_lambda.pack()

label_mu = tk.Label(root, text="Tasa de servicio (μ):")
label_mu.pack()

entry_mu = tk.Entry(root)
entry_mu.pack()

calcular_button = tk.Button(root, text="Calcular", command=calcular)
calcular_button.pack()

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var)
result_label.pack()

root.mainloop()
