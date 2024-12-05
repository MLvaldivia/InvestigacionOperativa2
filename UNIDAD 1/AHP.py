import numpy as np
from fractions import Fraction

def normalizar_matriz(matriz):
    suma_columnas = np.sum(matriz, axis=0)
    matriz_normalizada = matriz / suma_columnas
    return matriz_normalizada

def calcular_vector_propio(matriz_normalizada):
    return np.mean(matriz_normalizada, axis=1)

def ahp_criterios(matriz_comparacion):
    matriz_normalizada = normalizar_matriz(matriz_comparacion)
    
    vector_propio = calcular_vector_propio(matriz_normalizada)
    
    return vector_propio

def ahp_alternativas(matriz_comparacion):
    matriz_normalizada = normalizar_matriz(matriz_comparacion)
    
    vector_propio = calcular_vector_propio(matriz_normalizada)
    
    return vector_propio

def ingresar_matriz(tamano):
    matriz = np.zeros((tamano, tamano))
    for i in range(tamano):
        fila = input(f"Ingrese los valores de la fila {i + 1} separados por comas (puede usar fracciones, ej. 1/2): ")
        valores = [float(Fraction(x.strip())) for x in fila.split(',')]
        matriz[i, :] = valores  # Asignar la fila ingresada a la matriz
    return matriz

n_criterios = int(input("Ingrese el número de criterios: "))
print("Ingrese los valores de comparación para la matriz de criterios:")
matriz_criterios = ingresar_matriz(n_criterios)

ponderaciones_criterios = ahp_criterios(matriz_criterios)
print("\nPonderaciones de los Criterios:")
for i, peso in enumerate(ponderaciones_criterios):
    print(f"Criterio {i + 1}: {peso:.4f}")

n_alternativas = int(input("\nIngrese el número de alternativas: "))
print("Ingrese los valores de comparación para la matriz de alternativas:")
matriz_alternativas = ingresar_matriz(n_alternativas)

ponderaciones_alternativas = ahp_alternativas(matriz_alternativas)
print("\nPonderaciones de las Alternativas:")
for i, peso in enumerate(ponderaciones_alternativas):
    print(f"Alternativa {i + 1}: {peso:.4f}")


