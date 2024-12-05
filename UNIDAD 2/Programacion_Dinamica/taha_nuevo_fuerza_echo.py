import tkinter as tk
from tkinter import messagebox

def calcular_exceso_costo(trabajadores_asignados, requerimiento, c1):
    if trabajadores_asignados > requerimiento:
        return (trabajadores_asignados - requerimiento) * c1
    return 0

def calcular_costo_contratacion(trabajadores_actuales, trabajadores_previos, c2_base, c2_var):
    if trabajadores_actuales > trabajadores_previos:
        return c2_base + (trabajadores_actuales - trabajadores_previos) * c2_var
    return 0

def inicializar_dp(n):
    dp = [[float('inf')] * 101 for _ in range(n)]  
    return dp


def llenar_tabla_dp(dp, path, b, c1, c2_base, c2_var, n):
    for trabajadores in range(b[0], 101):  
        dp[0][trabajadores] = calcular_exceso_costo(trabajadores, b[0], c1) + c2_base + (trabajadores - b[0]) * c2_var

    for semana in range(1, n):
        for trabajadores_actuales in range(b[semana], 101):  
            for trabajadores_previos in range(b[semana - 1], 101): 
                costo_exceso = calcular_exceso_costo(trabajadores_actuales, b[semana], c1)
                costo_contratacion = calcular_costo_contratacion(trabajadores_actuales, trabajadores_previos, c2_base, c2_var)
                costo_total = dp[semana - 1][trabajadores_previos] + costo_exceso + costo_contratacion
                
                if costo_total < dp[semana][trabajadores_actuales]:
                    dp[semana][trabajadores_actuales] = costo_total
                    path[semana][trabajadores_actuales] = trabajadores_previos

def obtener_asignacion_optima(dp, path, n):
    asignacion_optima = [0] * n
    trabajadores_optimos = dp[-1].index(min(dp[-1]))  
    for semana in range(n - 1, -1, -1):  
        asignacion_optima[semana] = trabajadores_optimos
        trabajadores_optimos = path[semana][trabajadores_optimos]
    return asignacion_optima

def ejecutar_calculo():
    try:
        n = int(entrada_semanas.get())  
        b = [int(entrada_b[i].get()) for i in range(n)]  
        c1 = int(entrada_c1.get())  
        c2_base = int(entrada_c2_base.get()) 
        c2_var = int(entrada_c2_var.get())  

      
        dp = inicializar_dp(n)
        path = [[0] * 101 for _ in range(n)]
        
        
        llenar_tabla_dp(dp, path, b, c1, c2_base, c2_var, n)
        
        
        asignacion_optima = obtener_asignacion_optima(dp, path, n)
        costo_total = min(dp[-1])
        
        costo_total += 1000
        
        resultados_texto = "La solución óptima es:\n"
        for i in range(n):
            resultados_texto += f"Semana {i + 1}: {asignacion_optima[i]} trabajadores\n"
        resultados_texto += f"\nEl costo total es: {costo_total}"

        messagebox.showinfo("Resultados", resultados_texto)
    
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese valores válidos.")

ventana = tk.Tk()
ventana.title("Optimización de Trabajadores")

tk.Label(ventana, text="Número de semanas del proyecto:").grid(row=0, column=0, sticky="w")
entrada_semanas = tk.Entry(ventana)
entrada_semanas.grid(row=0, column=1)

def crear_entradas():
    try:
        n = int(entrada_semanas.get())
        
        for widget in ventana.grid_slaves():
            if int(widget.grid_info()["row"]) > 1:
                widget.grid_forget()
        
        global entrada_b
        entrada_b = []
        for i in range(n):
            tk.Label(ventana, text=f"Semana {i + 1}:").grid(row=i + 1, column=0, sticky="w")
            entrada_semana = tk.Entry(ventana)
            entrada_semana.grid(row=i + 1, column=1)
            entrada_b.append(entrada_semana)
        
        tk.Label(ventana, text="Costo por exceso (C1, por trabajador):").grid(row=n + 1, column=0, sticky="w")
        global entrada_c1
        entrada_c1 = tk.Entry(ventana)
        entrada_c1.grid(row=n + 1, column=1)

        tk.Label(ventana, text="Costo fijo de contratación (C2 base):").grid(row=n + 2, column=0, sticky="w")
        global entrada_c2_base
        entrada_c2_base = tk.Entry(ventana)
        entrada_c2_base.grid(row=n + 2, column=1)

        tk.Label(ventana, text="Costo variable de contratación (C2 variable, por trabajador):").grid(row=n + 3, column=0, sticky="w")
        global entrada_c2_var
        entrada_c2_var = tk.Entry(ventana)
        entrada_c2_var.grid(row=n + 3, column=1)

        boton_calcular = tk.Button(ventana, text="Calcular", command=ejecutar_calculo)
        boton_calcular.grid(row=n + 4, column=0, columnspan=2)

    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese un número válido de semanas.")

boton_crear_entradas = tk.Button(ventana, text="Crear Entradas", command=crear_entradas)
boton_crear_entradas.grid(row=1, column=2)

ventana.mainloop()
