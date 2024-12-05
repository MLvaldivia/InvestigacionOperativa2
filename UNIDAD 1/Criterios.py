import numpy as np
import tkinter as tk
from tkinter import simpledialog, messagebox

def ingresar_matriz():
    n = int(simpledialog.askstring("Input", "Ingrese el número de alternativas:"))
    m = int(simpledialog.askstring("Input", "Ingrese el número de estados de la naturaleza:"))
    
    matriz_pagos = np.zeros((n, m))
    for i in range(n):
        for j in range(m):
            matriz_pagos[i][j] = float(simpledialog.askstring("Input", f"Pago de la alternativa {i+1}, estado {j+1}:"))
    
    return matriz_pagos

def criterio_pesimista(matriz):
    return np.min(matriz, axis=1).max()

def criterio_optmista(matriz):
    return np.max(matriz, axis=1).max()

def criterio_laplace(matriz):
    return np.mean(matriz, axis=1).max()

def criterio_hurwicz(matriz, alpha):
    return (alpha * np.max(matriz, axis=1) + (1 - alpha) * np.min(matriz, axis=1)).max()

def criterio_savage(matriz):
    max_por_columna = np.max(matriz, axis=0)
    regret = max_por_columna - matriz
    # Seleccionar el mínimo de los máximos de arrepentimiento
    return np.min(np.max(regret, axis=1))

def main():
    # Crear la ventana principal
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal
    
    # Ingresar la matriz de pagos
    matriz = ingresar_matriz()
    
    # Calcular los resultados
    resultados = (
        f"Criterio PESIMISTA (Maximin): {criterio_pesimista(matriz)}\n"
        f"Criterio OPTIMISTA (Maximax): {criterio_optmista(matriz)}\n"
        f"Criterio LAPLACE: {criterio_laplace(matriz)}\n"
    )
    
    alpha = float(simpledialog.askstring("Input", "Ingrese el valor de alpha para el criterio de Hurwicz (entre 0 y 1): "))
    resultados += f"Criterio HURWICZ: {criterio_hurwicz(matriz, alpha)}\n"
    
    resultados += f"Criterio SAVAGE (Regret): {criterio_savage(matriz)}"
    
    messagebox.showinfo("Resultados de los criterios", resultados)

if __name__ == "__main__":
    main()
