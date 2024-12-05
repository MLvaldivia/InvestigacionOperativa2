import tkinter as tk
from tkinter import messagebox

def calculate_queue():
    try:
        lambda_ = float(entry_lambda.get())
        mu = float(entry_mu.get())
        
        if lambda_ <= 0 or mu <= 0 or lambda_ >= mu:
            messagebox.showerror("Error", "Por favor, asegúrate de que λ > 0, μ > 0, y μ > λ.")
            return

        p0 = 1 - (lambda_ / mu)
        lq = (lambda_ ** 2) / (mu * (mu - lambda_))
        l = lq + (lambda_ / mu)
        wq = lq / lambda_
        w = wq + (1 / mu)
        pw = lambda_ / mu

        wq_minutes = int(wq * 60)
        wq_seconds = int((wq * 60 - wq_minutes) * 60)
        w_minutes = int(w * 60)
        w_seconds = int((w * 60 - w_minutes) * 60)

        label_p0_result.config(text=f"{p0:.4f}")
        label_lq_result.config(text=f"{lq:.4f}")
        label_l_result.config(text=f"{l:.4f}")
        label_wq_result.config(text=f"{wq:.4f} ({wq_minutes} min {wq_seconds} s)")
        label_w_result.config(text=f"{w:.4f} ({w_minutes} min {w_seconds} s)")
        label_pw_result.config(text=f"{pw:.4f}")

        if var_calc_pn.get():
            try:
                n = int(entry_n.get())
                if n >= 0:
                    pn = ((lambda_ / mu) ** n) * p0
                    label_pn_result.config(text=f"{pn:.4f}")
                else:
                    messagebox.showerror("Error", "Por favor, ingresa un valor de n válido (n >= 0).")
            except ValueError:
                messagebox.showerror("Error", "Por favor, ingresa un valor de n válido.")
        else:
            label_pn_result.config(text="No calculado")

    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos para λ y μ.")

def toggle_n_input():
    if var_calc_pn.get():
        entry_n.config(state="normal")
    else:
        entry_n.config(state="disabled")

root = tk.Tk()
root.title("Calculadora de Teoría de Colas (Modelo M/M/1)")

tk.Label(root, text="Tasa de Llegadas (λ):").grid(row=0, column=0, sticky="e")
entry_lambda = tk.Entry(root)
entry_lambda.grid(row=0, column=1)

tk.Label(root, text="Tasa de Servicio (μ):").grid(row=1, column=0, sticky="e")
entry_mu = tk.Entry(root)
entry_mu.grid(row=1, column=1)

var_calc_pn = tk.BooleanVar()
chk_calc_pn = tk.Checkbutton(root, text="Calcular Pₙ (probabilidad de que haya n unidades en el sistema)", variable=var_calc_pn, command=toggle_n_input)
chk_calc_pn.grid(row=2, column=0, columnspan=2, sticky="w")

tk.Label(root, text="Número de unidades en el sistema (n):").grid(row=3, column=0, sticky="e")
entry_n = tk.Entry(root, state="disabled")
entry_n.grid(row=3, column=1)

btn_calculate = tk.Button(root, text="Calcular", command=calculate_queue)
btn_calculate.grid(row=4, column=0, columnspan=2)

tk.Label(root, text="Resultados:").grid(row=5, column=0, columnspan=2)

tk.Label(root, text="Probabilidad de que no haya unidades en el sistema (P₀):").grid(row=6, column=0, sticky="e")
label_p0_result = tk.Label(root, text="")
label_p0_result.grid(row=6, column=1)

tk.Label(root, text="Número promedio de unidades en la línea de espera (Lq):").grid(row=7, column=0, sticky="e")
label_lq_result = tk.Label(root, text="")
label_lq_result.grid(row=7, column=1)

tk.Label(root, text="Número promedio de unidades en el sistema (L):").grid(row=8, column=0, sticky="e")
label_l_result = tk.Label(root, text="")
label_l_result.grid(row=8, column=1)

tk.Label(root, text="Tiempo promedio en la línea de espera (Wq):").grid(row=9, column=0, sticky="e")
label_wq_result = tk.Label(root, text="")
label_wq_result.grid(row=9, column=1)

tk.Label(root, text="Tiempo promedio en el sistema (W):").grid(row=10, column=0, sticky="e")
label_w_result = tk.Label(root, text="")
label_w_result.grid(row=10, column=1)

tk.Label(root, text="Probabilidad de que una unidad no tenga que esperar (Pw):").grid(row=11, column=0, sticky="e")
label_pw_result = tk.Label(root, text="")
label_pw_result.grid(row=11, column=1)

tk.Label(root, text="Probabilidad de que haya n unidades en el sistema (Pn):").grid(row=12, column=0, sticky="e")
label_pn_result = tk.Label(root, text="No calculado")
label_pn_result.grid(row=12, column=1)

root.mainloop()


