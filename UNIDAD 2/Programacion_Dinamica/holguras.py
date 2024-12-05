import numpy as np

costo_fijo = 300  
costo_unitario = 100  
costo_perdida = 1600  
probabilidad_aceptable = 0.5 
max_etapas = 3 
max_lote = 10  

def K(x):
    return costo_fijo + x * costo_unitario if x > 0 else 0

def calcular_programacion_dinamica(max_etapas, max_lote):
    costos_optimos = np.full((max_etapas + 1, 2), float('inf'))  
    politicas_optimas = np.zeros((max_etapas + 1, 2), dtype=int)

    costos_optimos[max_etapas, 0] = costo_perdida  
    costos_optimos[max_etapas, 1] = 0 

    for n in range(max_etapas - 1, -1, -1):
        for s in [0, 1]:
            mejor_costo = float('inf')
            mejor_x = 0
            for x in range(1, max_lote + 1): 
                prob_aceptable = 1 - (1 - probabilidad_aceptable) ** x

                costo_actual = (
                    K(x)
                    + prob_aceptable * costos_optimos[n + 1, 1]
                    + (1 - prob_aceptable) * costos_optimos[n + 1, 0]
                )

                if costo_actual < mejor_costo:
                    mejor_costo = costo_actual
                    mejor_x = x

            costos_optimos[n, s] = mejor_costo
            politicas_optimas[n, s] = mejor_x

    return costos_optimos, politicas_optimas

costos, politicas = calcular_programacion_dinamica(max_etapas, max_lote)

costo_esperado = costos[0, 0]  
lote_optimo = politicas[0, 0] 

print("Costo total esperado:", costo_esperado)
print("Política óptima: Producir", lote_optimo, "artículos en la primera corrida.")
