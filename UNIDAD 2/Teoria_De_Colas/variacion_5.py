import math
import tkinter as tk
from tkinter import ttk

def calcular_Pj(lmbda, mu, k, j):
    numerador = (lmbda / mu)**j / math.factorial(j)
    denominador = sum((lmbda / mu)**i / math.factorial(i) for i in range(k + 1))
    return numerador / denominador

def calcular_L(lmbda, mu, k):
    Pk = calcular_Pj(lmbda, mu, k, k)
    L = (lmbda / mu) * (1 - Pk)
    return L

def calcular_resultados():
    try:
        lmbda = float(entry_lambda.get())
        mu = float(entry_mu.get())
        k = int(entry_k.get())

        resultados = []
        for j in range(k + 1):
            Pj = calcular_Pj(lmbda, mu, k, j)
            resultados.append(f"P({j}) = {Pj:.4f}")
        
        L = calcular_L(lmbda, mu, k)
        resultados.append(f"L = {L:.4f}")

        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "\n".join(resultados))
    except Exception as e:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, f"Error: {str(e)}")

root = tk.Tk()
root.title("Modelo M/G/k")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E))

ttk.Label(frame, text="λ (Tasa de llegada):").grid(row=0, column=0, sticky=tk.W)
entry_lambda = ttk.Entry(frame, width=10)
entry_lambda.grid(row=0, column=1)

ttk.Label(frame, text="μ (Tasa de servicio):").grid(row=1, column=0, sticky=tk.W)
entry_mu = ttk.Entry(frame, width=10)
entry_mu.grid(row=1, column=1)

ttk.Label(frame, text="k (Número de canales):").grid(row=2, column=0, sticky=tk.W)
entry_k = ttk.Entry(frame, width=10)
entry_k.grid(row=2, column=1)

btn_calcular = ttk.Button(frame, text="Calcular", command=calcular_resultados)
btn_calcular.grid(row=3, column=0, columnspan=2)

output_text = tk.Text(root, width=50, height=15, wrap="word", state="normal")
output_text.grid(row=1, column=0, padx=10, pady=10)

root.mainloop()
