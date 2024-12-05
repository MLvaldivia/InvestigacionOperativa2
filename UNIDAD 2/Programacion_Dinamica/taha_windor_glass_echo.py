import tkinter as tk
from tkinter import messagebox
from scipy.optimize import linprog

def solve_optimization():
    try:
        c1 = float(entry_c1.get())
        c2 = float(entry_c2.get())
        b1 = float(entry_b1.get())
        b2 = float(entry_b2.get())
        b3 = float(entry_b3.get())
        
        c = [-c1, -c2] 

        A = [[1, 0],   
             [0, 2],   
             [3, 2]]    

        b = [b1, b2, b3]  

        x_bounds = (0, None) 
        y_bounds = (0, None)  

        result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

        if result.success:
            result_text = f"El valor máximo de la función objetivo es: {-result.fun}\n"
            result_text += f"Los valores óptimos de las variables son: x1 = {result.x[0]}, x2 = {result.x[1]}"
        else:
            result_text = "No se pudo encontrar una solución óptima."

        messagebox.showinfo("Resultado de Optimización", result_text)
        
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores válidos.")

root = tk.Tk()
root.title("Optimización Lineal")

label_c1 = tk.Label(root, text="Coeficiente c1 (para x1):")
label_c1.grid(row=0, column=0, padx=10, pady=5)
entry_c1 = tk.Entry(root)
entry_c1.grid(row=0, column=1, padx=10, pady=5)

label_c2 = tk.Label(root, text="Coeficiente c2 (para x2):")
label_c2.grid(row=1, column=0, padx=10, pady=5)
entry_c2 = tk.Entry(root)
entry_c2.grid(row=1, column=1, padx=10, pady=5)

label_b1 = tk.Label(root, text="Lado derecho b1 (para x1 <= b1):")
label_b1.grid(row=2, column=0, padx=10, pady=5)
entry_b1 = tk.Entry(root)
entry_b1.grid(row=2, column=1, padx=10, pady=5)

label_b2 = tk.Label(root, text="Lado derecho b2 (para 2x2 <= b2):")
label_b2.grid(row=3, column=0, padx=10, pady=5)
entry_b2 = tk.Entry(root)
entry_b2.grid(row=3, column=1, padx=10, pady=5)

label_b3 = tk.Label(root, text="Lado derecho b3 (para 3x1 + 2x2 <= b3):")
label_b3.grid(row=4, column=0, padx=10, pady=5)
entry_b3 = tk.Entry(root)
entry_b3.grid(row=4, column=1, padx=10, pady=5)

solve_button = tk.Button(root, text="Resolver Optimización", command=solve_optimization)
solve_button.grid(row=5, column=0, columnspan=2, pady=20)

root.mainloop()
